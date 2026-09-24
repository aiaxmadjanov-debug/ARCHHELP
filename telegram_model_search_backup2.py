import asyncio
import os
import sqlite3
import tempfile
from pathlib import Path

import imagehash
from PIL import Image
from dotenv import load_dotenv
from telethon import TelegramClient


# =========================================================
# PATH / ENV
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)

API_ID = int(os.getenv("TELEGRAM_API_ID", "0"))
API_HASH = os.getenv("TELEGRAM_API_HASH", "")

if not API_ID or not API_HASH:
    raise RuntimeError(
        f"TELEGRAM_API_ID yoki TELEGRAM_API_HASH topilmadi.\n"
        f".env: {ENV_FILE}"
    )


# =========================================================
# 7 TA TELEGRAM KANAL
# =========================================================

CHANNELS = [
    "promodel_3dsky",
    "my_3dsky",
    "red_models",
    "Exterior_3dmax_modellar",
    "Free3dmodels",
    "blocks_01",
    "Uzbekcha_3d_modellar",
]


# =========================================================
# FILES
# =========================================================

SESSION_DIR = BASE_DIR / "bot" / "model_search"
SESSION_DIR.mkdir(parents=True, exist_ok=True)

SESSION_FILE = SESSION_DIR / "archhelp_search"

DB_FILE = SESSION_DIR / "model_index.db"


# =========================================================
# MODEL FORMATLARI
# =========================================================

MODEL_EXTENSIONS = {
    ".max",
    ".fbx",
    ".obj",
    ".blend",
    ".3ds",
    ".skp",
    ".c4d",
    ".glb",
    ".gltf",
    ".dae",
    ".stl",
    ".abc",
    ".ply",
    ".zip",
    ".rar",
    ".7z",
}


# =========================================================
# TELEGRAM CLIENT
# =========================================================

client = TelegramClient(
    str(SESSION_FILE),
    API_ID,
    API_HASH,
)

_client_started = False


# =========================================================
# DATABASE
# =========================================================

def get_db():
    conn = sqlite3.connect(DB_FILE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS models (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            channel TEXT NOT NULL,
            message_id INTEGER NOT NULL,
            title TEXT,
            phash TEXT NOT NULL,
            model_files TEXT,
            date TEXT,
            UNIQUE(channel, message_id)
        )
    """)

    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_phash
        ON models(phash)
    """)

    conn.commit()

    return conn


# =========================================================
# TELEGRAM START
# =========================================================

async def start_client():
    global _client_started

    if _client_started:
        return

    await client.connect()

    if not await client.is_user_authorized():
        raise RuntimeError(
            "Telegram akkaunt ulanmagan.\n"
            "Avval telegram_model_login.py orqali login qiling."
        )

    _client_started = True


# =========================================================
# HELPERS
# =========================================================

def make_post_link(channel_username, message_id):
    return f"https://t.me/{channel_username}/{message_id}"


def get_model_files(message):
    result = []

    if not message or not message.media:
        return result

    document = getattr(message.media, "document", None)

    if not document:
        return result

    for attribute in getattr(document, "attributes", []):
        filename = getattr(attribute, "file_name", None)

        if not filename:
            continue

        ext = Path(filename).suffix.lower()

        if ext in MODEL_EXTENSIONS:
            result.append(filename)

    return result


def get_message_title(message):
    text = (message.message or "").strip()

    if text:
        first_line = text.splitlines()[0].strip()

        if len(first_line) > 150:
            first_line = first_line[:150] + "..."

        return first_line

    files = get_model_files(message)

    if files:
        return files[0]

    return "3D Model"


def calculate_hash(image_path):
    try:
        with Image.open(image_path) as img:

            img = img.convert("RGB")

            img.thumbnail((800, 800))

            return imagehash.phash(img)

    except Exception as e:
        print(f"[HASH ERROR] {e}")
        return None


def hash_to_string(phash):
    return str(phash)


def string_to_hash(value):
    try:
        return imagehash.hex_to_hash(value)
    except Exception:
        return None


def calculate_similarity(hash1, hash2):

    if hash1 is None or hash2 is None:
        return 0.0

    distance = hash1 - hash2

    max_distance = len(hash1.hash) ** 2

    if max_distance <= 0:
        return 0.0

    similarity = 100 * (
        1 - (distance / max_distance)
    )

    return max(
        0.0,
        min(100.0, similarity)
    )


# =========================================================
# INDEX STATUS
# =========================================================

def index_count():

    conn = get_db()

    try:
        cursor = conn.execute(
            "SELECT COUNT(*) FROM models"
        )

        return cursor.fetchone()[0]

    finally:
        conn.close()


# =========================================================
# INDEX CHANNEL
# =========================================================

async def index_channel(channel_username):

    conn = get_db()

    try:

        entity = await client.get_entity(
            channel_username
        )

    except Exception as e:

        print(
            f"[CHANNEL ERROR] "
            f"@{channel_username}: {e}"
        )

        conn.close()

        return 0

    print(
        f"\n[INDEX] "
        f"@{channel_username}"
    )

    count = 0
    photos = 0

    try:

        async for message in client.iter_messages(
            entity
        ):

            count += 1

            if not message.photo:
                continue

            photos += 1

            # -------------------------------------------------
            # Tekshiramiz: oldin indekslanganmi?
            # -------------------------------------------------

            existing = conn.execute(
                """
                SELECT id
                FROM models
                WHERE channel = ?
                AND message_id = ?
                """,
                (
                    channel_username,
                    message.id,
                ),
            ).fetchone()

            if existing:

                continue

            # -------------------------------------------------
            # TEMP DIRECTORY
            # -------------------------------------------------

            temp_dir = tempfile.mkdtemp(
                prefix="archhelp_index_"
            )

            try:

                image_path = await client.download_media(
                    message,
                    file=temp_dir,
                )

                if not image_path:
                    continue

                image_path = Path(image_path)

                phash = calculate_hash(
                    image_path
                )

                if phash is None:
                    continue

                model_files = get_model_files(
                    message
                )

                title = get_message_title(
                    message
                )

                conn.execute(
                    """
                    INSERT OR IGNORE INTO models
                    (
                        channel,
                        message_id,
                        title,
                        phash,
                        model_files,
                        date
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        channel_username,
                        message.id,
                        title,
                        hash_to_string(phash),
                        "|||".join(model_files),
                        (
                            message.date.isoformat()
                            if message.date
                            else None
                        ),
                    ),
                )

                conn.commit()

            except Exception as e:

                print(
                    f"[IMAGE ERROR] "
                    f"@{channel_username} "
                    f"message={message.id}: {e}"
                )

            finally:

                try:
                    image_path.unlink(
                        missing_ok=True
                    )
                except Exception:
                    pass

                try:
                    Path(temp_dir).rmdir()
                except Exception:
                    pass

            # -------------------------------------------------
            # PROGRESS
            # -------------------------------------------------

            if count % 100 == 0:

                print(
                    f"    @{channel_username}: "
                    f"{count} post | "
                    f"{photos} rasm | "
                    f"indeks: {index_count()}"
                )

    except Exception as e:

        print(
            f"[INDEX ERROR] "
            f"@{channel_username}: {e}"
        )

    finally:

        conn.close()

    print(
        f"[INDEX DONE] "
        f"@{channel_username} | "
        f"post={count} | "
        f"rasm={photos}"
    )

    return photos


# =========================================================
# FULL INDEX
# =========================================================

async def build_index():

    await start_client()

    print("\n" + "=" * 60)

    print(
        "ARCHHELP 3D MODEL INDEXER"
    )

    print("=" * 60)

    print(
        f"Kanallar: {len(CHANNELS)}"
    )

    print(
        f"Eski indeks: {index_count()} ta model"
    )

    print("=" * 60)

    for channel in CHANNELS:

        await index_channel(
            channel
        )

    print("\n" + "=" * 60)

    print(
        f"✅ INDEKS TAYYOR: "
        f"{index_count()} ta model"
    )

    print("=" * 60)


# =========================================================
# USER IMAGE
# =========================================================

async def save_temp_user_image(
    image_bytes
):

    fd, path = tempfile.mkstemp(
        suffix=".jpg",
        prefix="archhelp_user_"
    )

    os.close(fd)

    with open(path, "wb") as f:
        f.write(image_bytes)

    return Path(path)


# =========================================================
# FAST SEARCH
# =========================================================

async def search_3d_models(
    image_bytes,
    max_results_per_channel=5,
    final_results=5,
):

    await start_client()

    # -----------------------------------------------------
    # INDEX BO'SH BO'LSA
    # -----------------------------------------------------

    if index_count() == 0:

        print(
            "[INDEX] Indeks bo'sh. "
            "Birinchi marta indeks yaratiladi..."
        )

        await build_index()

    user_image_path = None

    try:

        user_image_path = (
            await save_temp_user_image(
                image_bytes
            )
        )

        target_hash = calculate_hash(
            user_image_path
        )

        if target_hash is None:
            return []

        conn = get_db()

        rows = conn.execute(
            """
            SELECT
                channel,
                message_id,
                title,
                phash,
                model_files,
                date
            FROM models
            """
        ).fetchall()

        conn.close()

        results = []

        for row in rows:

            (
                channel,
                message_id,
                title,
                phash_text,
                model_files_text,
                date,
            ) = row

            candidate_hash = (
                string_to_hash(
                    phash_text
                )
            )

            similarity = calculate_similarity(
                target_hash,
                candidate_hash
            )

            model_files = []

            if model_files_text:

                model_files = [
                    x
                    for x in model_files_text.split("|||")
                    if x
                ]

            results.append(
                {
                    "similarity": round(
                        similarity,
                        2,
                    ),
                    "channel": channel,
                    "message_id": message_id,
                    "title": title,
                    "link": make_post_link(
                        channel,
                        message_id,
                    ),
                    "model_files": model_files,
                    "date": date,
                }
            )

        results.sort(
            key=lambda x: x["similarity"],
            reverse=True,
        )

        # Har kanal bo'yicha limit

        channel_counts = {}
        filtered = []

        for result in results:

            channel = result["channel"]

            current = channel_counts.get(
                channel,
                0,
            )

            if current >= max_results_per_channel:
                continue

            channel_counts[channel] = (
                current + 1
            )

            filtered.append(result)

            if len(filtered) >= final_results:
                break

        print(
            f"[FAST SEARCH] "
            f"{len(rows)} ta indeks "
            f"ichidan qidirildi."
        )

        return filtered

    finally:

        if user_image_path:

            try:
                user_image_path.unlink(
                    missing_ok=True
                )
            except Exception:
                pass


# =========================================================
# RESULT FORMAT
# =========================================================

def format_results(results):

    if not results:

        return (
            "❌ Mos 3D model topilmadi.\n\n"
            "7 ta Telegram kanalining "
            "indeksida mos model aniqlanmadi."
        )

    text = (
        "🔎 **ARCHHELP 3D MODEL TOPISH**\n\n"
        "⚡️ Tezkor indeks orqali qidirildi.\n\n"
    )

    for index, result in enumerate(
        results,
        start=1,
    ):

        similarity = result[
            "similarity"
        ]

        title = result[
            "title"
        ]

        channel = result[
            "channel"
        ]

        link = result[
            "link"
        ]

        text += (
            f"🏆 **{index}. {title}**\n"
            f"📊 O‘xshashlik: "
            f"**{similarity}%**\n"
            f"📢 Kanal: @{channel}\n"
            f"🔗 [Postni ochish]({link})\n"
        )

        if result["model_files"]:

            text += (
                "📦 Model fayli: **MAVJUD**\n"
            )

            for filename in result[
                "model_files"
            ][:3]:

                text += (
                    f"   • `{filename}`\n"
                )

        else:

            text += (
                "📦 Model fayli: "
                "postda aniqlanmadi\n"
            )

        text += "\n"

    return text


# =========================================================
# DIRECT TEST
# =========================================================

if __name__ == "__main__":

    async def main():

        await build_index()

        await client.disconnect()

    asyncio.run(main())