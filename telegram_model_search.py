import asyncio
import os
import sqlite3
import tempfile
from pathlib import Path

import imagehash
from PIL import Image
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import FloodWaitError


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
        "TELEGRAM_API_ID yoki TELEGRAM_API_HASH topilmadi."
    )


# =========================================================
# 7 TA KANAL
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
# PATHS
# =========================================================

SESSION_DIR = BASE_DIR / "bot" / "model_search"
SESSION_DIR.mkdir(parents=True, exist_ok=True)

SESSION_FILE = SESSION_DIR / "archhelp_search"

DB_FILE = SESSION_DIR / "model_index.db"


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
    conn = sqlite3.connect(
        DB_FILE,
        timeout=30,
    )

    conn.execute("""
        PRAGMA journal_mode=WAL
    """)

    conn.execute("""
        PRAGMA synchronous=NORMAL
    """)

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
        CREATE INDEX IF NOT EXISTS idx_channel_message
        ON models(channel, message_id)
    """)

    conn.commit()

    return conn


# =========================================================
# START TELEGRAM
# =========================================================

async def start_client():

    global _client_started

    if _client_started:
        return

    await client.connect()

    if not await client.is_user_authorized():

        raise RuntimeError(
            "Telegram akkaunt ulanmagan.\n"
            "Avval telegram_model_login.py ni ishga tushiring."
        )

    _client_started = True


# =========================================================
# HELPERS
# =========================================================

def make_post_link(
    channel_username,
    message_id,
):
    return (
        f"https://t.me/"
        f"{channel_username}/"
        f"{message_id}"
    )


def get_model_files(message):

    result = []

    if not message:
        return result

    media = getattr(
        message,
        "media",
        None,
    )

    if not media:
        return result

    document = getattr(
        media,
        "document",
        None,
    )

    if not document:
        return result

    for attribute in getattr(
        document,
        "attributes",
        [],
    ):

        filename = getattr(
            attribute,
            "file_name",
            None,
        )

        if filename:
            result.append(filename)

    return result


def get_message_title(message):

    text = (
        message.message or ""
    ).strip()

    if text:

        first_line = (
            text.splitlines()[0]
            .strip()
        )

        if len(first_line) > 150:

            first_line = (
                first_line[:150]
                + "..."
            )

        return first_line

    files = get_model_files(
        message
    )

    if files:
        return files[0]

    return "3D Model"


# =========================================================
# PHASH
# =========================================================

def calculate_hash(
    image_path,
):

    try:

        with Image.open(
            image_path
        ) as image:

            image = image.convert(
                "RGB"
            )

            image.thumbnail(
                (500, 500)
            )

            return imagehash.phash(
                image
            )

    except Exception as e:

        print(
            f"[HASH ERROR] {e}"
        )

        return None


def hash_to_string(
    phash,
):

    return str(phash)


def string_to_hash(
    value,
):

    try:

        return imagehash.hex_to_hash(
            value
        )

    except Exception:

        return None


def calculate_similarity(
    hash1,
    hash2,
):

    if hash1 is None or hash2 is None:
        return 0.0

    distance = hash1 - hash2

    max_distance = (
        len(hash1.hash) ** 2
    )

    if max_distance <= 0:
        return 0.0

    similarity = (
        100
        * (
            1
            - (
                distance
                / max_distance
            )
        )
    )

    return max(
        0.0,
        min(
            100.0,
            similarity,
        ),
    )


# =========================================================
# DB COUNT
# =========================================================

def index_count():

    conn = get_db()

    try:

        result = conn.execute(
            "SELECT COUNT(*) FROM models"
        ).fetchone()

        return result[0]

    finally:

        conn.close()


def channel_index_count(
    channel,
):

    conn = get_db()

    try:

        result = conn.execute(
            """
            SELECT COUNT(*)
            FROM models
            WHERE channel = ?
            """,
            (channel,),
        ).fetchone()

        return result[0]

    finally:

        conn.close()


# =========================================================
# CHECK MESSAGE
# =========================================================

def message_exists(
    channel,
    message_id,
):

    conn = get_db()

    try:

        result = conn.execute(
            """
            SELECT id
            FROM models
            WHERE channel = ?
            AND message_id = ?
            LIMIT 1
            """,
            (
                channel,
                message_id,
            ),
        ).fetchone()

        return result is not None

    finally:

        conn.close()


# =========================================================
# SAVE MODEL
# =========================================================

def save_model(
    channel,
    message,
    phash,
    model_files,
):

    conn = get_db()

    try:

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
                channel,
                message.id,
                get_message_title(
                    message
                ),
                hash_to_string(
                    phash
                ),
                "|||".join(
                    model_files
                ),
                (
                    message.date.isoformat()
                    if message.date
                    else None
                ),
            ),
        )

        conn.commit()

    finally:

        conn.close()


# =========================================================
# THUMBNAIL DOWNLOAD
# =========================================================

async def download_small_thumbnail(
    message,
    temp_dir,
):

    try:

        # 0 = eng kichik photo preview
        image_path = (
            await client.download_media(
                message,
                file=temp_dir,
                thumb=0,
            )
        )

        if image_path:
            return Path(
                image_path
            )

    except Exception as e:

        print(
            f"[THUMB ERROR] "
            f"message={message.id}: {e}"
        )

    return None


# =========================================================
# INDEX ONE CHANNEL
# =========================================================

async def index_channel(
    channel,
):

    try:

        entity = await client.get_entity(
            channel
        )

    except Exception as e:

        print(
            f"[CHANNEL ERROR] "
            f"@{channel}: {e}"
        )

        return

    existing_count = (
        channel_index_count(
            channel
        )
    )

    print()
    print("=" * 60)
    print(
        f"[INDEX] @{channel}"
    )
    print(
        f"Oldindan indekslangan: "
        f"{existing_count}"
    )
    print("=" * 60)

    scanned = 0
    added = 0

    try:

        async for message in client.iter_messages(
            entity
        ):

            scanned += 1

            # Faqat rasmli postlar
            if not message.photo:
                continue

            # Oldin indekslangan bo'lsa o'tkazib yuboramiz
            if message_exists(
                channel,
                message.id,
            ):
                continue

            temp_dir = tempfile.mkdtemp(
                prefix="archhelp_thumb_"
            )

            image_path = None

            try:

                image_path = (
                    await download_small_thumbnail(
                        message,
                        temp_dir,
                    )
                )

                if not image_path:
                    continue

                phash = calculate_hash(
                    image_path
                )

                if phash is None:
                    continue

                model_files = (
                    get_model_files(
                        message
                    )
                )

                save_model(
                    channel,
                    message,
                    phash,
                    model_files,
                )

                added += 1

            except FloodWaitError as e:

                print(
                    f"[FLOOD WAIT] "
                    f"@{channel}: "
                    f"{e.seconds} sekund"
                )

                await asyncio.sleep(
                    e.seconds
                )

            except Exception as e:

                print(
                    f"[POST ERROR] "
                    f"@{channel} "
                    f"{message.id}: {e}"
                )

            finally:

                if image_path:

                    try:
                        image_path.unlink(
                            missing_ok=True
                        )
                    except Exception:
                        pass

                try:
                    Path(
                        temp_dir
                    ).rmdir()

                except Exception:
                    pass

            # Har 250 postda progress
            if scanned % 250 == 0:

                current = (
                    channel_index_count(
                        channel
                    )
                )

                print(
                    f"    @{channel}: "
                    f"{scanned} post ko'rildi | "
                    f"{current} ta indekslangan"
                )

    except FloodWaitError as e:

        print(
            f"[FLOOD WAIT] "
            f"@{channel}: "
            f"{e.seconds} sekund"
        )

        await asyncio.sleep(
            e.seconds
        )

    except Exception as e:

        print(
            f"[CHANNEL SEARCH ERROR] "
            f"@{channel}: {e}"
        )

    final_count = (
        channel_index_count(
            channel
        )
    )

    print()
    print(
        f"[INDEX DONE] @{channel}"
    )

    print(
        f"Ko'rilgan post: {scanned}"
    )

    print(
        f"Yangi indeks: {added}"
    )

    print(
        f"Jami kanal indeksi: "
        f"{final_count}"
    )


# =========================================================
# PARALLEL INDEX
# =========================================================

async def build_index():

    await start_client()

    print()
    print("=" * 70)
    print(
        "🚀 ARCHHELP 3D FAST INDEX"
    )
    print("=" * 70)

    print(
        "Kanallar:",
        len(CHANNELS)
    )

    print(
        "Mavjud indeks:",
        index_count()
    )

    print("=" * 70)

    # Bir vaqtning o'zida 2 ta kanal
    # Telegram flood limitini haddan tashqari oshirmaslik uchun.
    semaphore = asyncio.Semaphore(2)

    async def worker(channel):

        async with semaphore:

            await index_channel(
                channel
            )

    await asyncio.gather(
        *[
            worker(channel)
            for channel in CHANNELS
        ]
    )

    print()
    print("=" * 70)
    print(
        f"✅ INDEKS TAYYOR: "
        f"{index_count()} TA MODEL"
    )
    print("=" * 70)


# =========================================================
# USER IMAGE
# =========================================================

async def save_user_image(
    image_bytes,
):

    fd, path = tempfile.mkstemp(
        suffix=".jpg",
        prefix="archhelp_user_",
    )

    os.close(fd)

    with open(
        path,
        "wb",
    ) as file:

        file.write(
            image_bytes
        )

    return Path(path)


# =========================================================
# LOAD INDEX TO MEMORY
# =========================================================

def load_index():

    conn = get_db()

    try:

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

        return rows

    finally:

        conn.close()


# =========================================================
# FAST SEARCH
# =========================================================

async def search_3d_models(
    image_bytes,
    max_results_per_channel=5,
    final_results=5,
):

    await start_client()

    # Agar indeks hali mavjud bo'lmasa
    if index_count() == 0:

        print(
            "[INDEX] Indeks bo'sh."
        )

        print(
            "[INDEX] Birinchi indekslash boshlanmoqda..."
        )

        await build_index()

    user_image = None

    try:

        user_image = (
            await save_user_image(
                image_bytes
            )
        )

        target_hash = calculate_hash(
            user_image
        )

        if target_hash is None:
            return []

        rows = load_index()

        print(
            f"[FAST SEARCH] "
            f"{len(rows)} ta model tekshirilmoqda..."
        )

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

            similarity = (
                calculate_similarity(
                    target_hash,
                    candidate_hash,
                )
            )

            model_files = []

            if model_files_text:

                model_files = [
                    item
                    for item in
                    model_files_text.split(
                        "|||"
                    )
                    if item
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

                    "model_files":
                        model_files,

                    "date": date,
                }
            )

        # Eng yuqori o'xshashlik
        results.sort(
            key=lambda item:
                item["similarity"],
            reverse=True,
        )

        # Bir kanalning natijalari
        # haddan tashqari ko'payib ketmasin
        channel_counts = {}

        final = []

        for result in results:

            channel = result[
                "channel"
            ]

            current = (
                channel_counts.get(
                    channel,
                    0,
                )
            )

            if (
                current
                >= max_results_per_channel
            ):
                continue

            channel_counts[channel] = (
                current + 1
            )

            final.append(
                result
            )

            if len(final) >= final_results:
                break

        print(
            "[FAST SEARCH] "
            f"TOP {len(final)} natija tayyor."
        )

        return final

    finally:

        if user_image:

            try:

                user_image.unlink(
                    missing_ok=True
                )

            except Exception:
                pass


# =========================================================
# FORMAT RESULTS
# =========================================================

def format_results(
    results,
):

    if not results:

        return (
            "❌ **Mos 3D model topilmadi.**\n\n"
            "7 ta Telegram kanalidagi "
            "indeks bo'yicha mos model aniqlanmadi."
        )

    text = (
        "🔎 **ARCHHELP 3D MODEL TOPISH**\n\n"
        "⚡️ Tezkor lokal indeks orqali topildi.\n\n"
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
            f"📊 O'xshashlik: "
            f"**{similarity}%**\n"
            f"📢 Kanal: @{channel}\n"
            f"🔗 [Postni ochish]({link})\n"
        )

        if result[
            "model_files"
        ]:

            text += (
                "📦 Model fayli: "
                "**MAVJUD**\n"
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
# DIRECT INDEX TEST
# =========================================================

if __name__ == "__main__":

    async def main():

        await build_index()

        await client.disconnect()

    asyncio.run(main())