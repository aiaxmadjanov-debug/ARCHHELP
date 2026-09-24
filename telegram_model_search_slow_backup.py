import asyncio
import os
import re
import tempfile
from pathlib import Path

import imagehash
from PIL import Image
from dotenv import load_dotenv
from telethon import TelegramClient


# ============================================================
# ARCHHELP — TELEGRAM 3D MODEL SEARCH
# ============================================================

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


# ============================================================
# FAQAT SHU 7 TA KANAL
# ============================================================

CHANNELS = [
    "promodel_3dsky",
    "my_3dsky",
    "red_models",
    "Exterior_3dmax_modellar",
    "Free3dmodels",
    "blocks_01",
    "Uzbekcha_3d_modellar",
]


# ============================================================
# TELEGRAM SESSION
# ============================================================

SESSION_DIR = BASE_DIR / "bot" / "model_search"
SESSION_DIR.mkdir(parents=True, exist_ok=True)

SESSION_FILE = SESSION_DIR / "archhelp_search"


# ============================================================
# MODEL FILE FORMATLARI
# ============================================================

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


# ============================================================
# TELEGRAM CLIENT
# ============================================================

client = TelegramClient(
    str(SESSION_FILE),
    API_ID,
    API_HASH,
)


_client_started = False


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


# ============================================================
# LINK
# ============================================================

def make_post_link(channel_username, message_id):
    return f"https://t.me/{channel_username}/{message_id}"


# ============================================================
# MODEL FAYLNI ANIQLASH
# ============================================================

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


# ============================================================
# POST NOMINI ANIQLASH
# ============================================================

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


# ============================================================
# IMAGE HASH
# ============================================================

def calculate_hash(image_path):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")
            img.thumbnail((1200, 1200))

            return imagehash.phash(img)

    except Exception:
        return None


def calculate_similarity(hash1, hash2):
    if hash1 is None or hash2 is None:
        return 0.0

    distance = hash1 - hash2

    max_distance = len(hash1.hash) ** 2

    if max_distance <= 0:
        return 0.0

    similarity = 100 * (1 - (distance / max_distance))

    return max(0.0, min(100.0, similarity))


# ============================================================
# FOYDALANUVCHI RASMINI VAQTINCHA SAQLASH
# ============================================================

async def save_temp_user_image(image_bytes):
    fd, path = tempfile.mkstemp(
        suffix=".jpg",
        prefix="archhelp_user_"
    )

    os.close(fd)

    with open(path, "wb") as f:
        f.write(image_bytes)

    return Path(path)


# ============================================================
# KANALDAGI RASMLARNI TEKSHIRISH
# ============================================================

async def search_channel(
    channel_username,
    target_hash,
    max_results=5,
):
    results = []

    try:
        entity = await client.get_entity(channel_username)

    except Exception as e:
        print(
            f"[CHANNEL ERROR] @{channel_username}: {e}"
        )
        return results

    print(
        f"[SEARCH] @{channel_username}"
    )

    message_count = 0

    try:
        async for message in client.iter_messages(entity):

            message_count += 1

            # ------------------------------------------------
            # RASM BO'LMAGAN POSTLARNI O'TKAZIB YUBORAMIZ
            # ------------------------------------------------

            if not message.photo:
                continue

            try:
                # --------------------------------------------
                # RASMNI VAQTINCHA YUKLAB OLISH
                # --------------------------------------------

                temp_dir = tempfile.mkdtemp(
                    prefix="archhelp_model_"
                )

                image_path = await client.download_media(
                    message,
                    file=temp_dir,
                )

                if not image_path:
                    continue

                image_path = Path(image_path)

                # --------------------------------------------
                # HASH
                # --------------------------------------------

                candidate_hash = calculate_hash(
                    image_path
                )

                similarity = calculate_similarity(
                    target_hash,
                    candidate_hash
                )

                # --------------------------------------------
                # MODEL FAYL
                # --------------------------------------------

                model_files = get_model_files(
                    message
                )

                title = get_message_title(
                    message
                )

                result = {
                    "similarity": round(
                        similarity,
                        2
                    ),
                    "channel": channel_username,
                    "message_id": message.id,
                    "title": title,
                    "link": make_post_link(
                        channel_username,
                        message.id
                    ),
                    "model_files": model_files,
                    "date": (
                        message.date.isoformat()
                        if message.date
                        else None
                    ),
                }

                results.append(result)

                # --------------------------------------------
                # VAQTINCHA RASMNI O'CHIRISH
                # --------------------------------------------

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

            except Exception as e:
                print(
                    f"[IMAGE ERROR] "
                    f"@{channel_username} "
                    f"message={message.id}: {e}"
                )

            # Konsolga progress
            if message_count % 100 == 0:
                print(
                    f"    @{channel_username}: "
                    f"{message_count} ta post ko'rildi..."
                )

    except Exception as e:
        print(
            f"[SEARCH ERROR] @{channel_username}: {e}"
        )

    results.sort(
        key=lambda x: x["similarity"],
        reverse=True
    )

    return results[:max_results]


# ============================================================
# 7 TA KANALDAN QIDIRISH
# ============================================================

async def search_3d_models(
    image_bytes,
    max_results_per_channel=5,
    final_results=5,
):
    """
    Foydalanuvchi yuborgan rasmni
    faqat 7 ta Telegram kanalidan qidiradi.

    7000+ model oldindan saqlanmaydi.
    Rasmlar qidiruv vaqtida vaqtincha yuklanadi.
    """

    await start_client()

    user_image_path = None

    try:
        # ----------------------------------------------------
        # USER IMAGE
        # ----------------------------------------------------

        user_image_path = await save_temp_user_image(
            image_bytes
        )

        target_hash = calculate_hash(
            user_image_path
        )

        if target_hash is None:
            return []

        all_results = []

        # ----------------------------------------------------
        # 7 TA KANAL
        # ----------------------------------------------------

        for channel in CHANNELS:

            channel_results = await search_channel(
                channel_username=channel,
                target_hash=target_hash,
                max_results=max_results_per_channel,
            )

            all_results.extend(
                channel_results
            )

        # ----------------------------------------------------
        # UMUMIY SARALASH
        # ----------------------------------------------------

        all_results.sort(
            key=lambda x: x["similarity"],
            reverse=True
        )

        # Bir xil post takrorlanmasin
        unique = []
        seen = set()

        for result in all_results:

            key = (
                result["channel"],
                result["message_id"],
            )

            if key in seen:
                continue

            seen.add(key)
            unique.append(result)

        return unique[:final_results]

    finally:

        # ----------------------------------------------------
        # USER RASMINI O'CHIRISH
        # ----------------------------------------------------

        if user_image_path:

            try:
                user_image_path.unlink(
                    missing_ok=True
                )
            except Exception:
                pass


# ============================================================
# FORMAT
# ============================================================

def format_results(results):

    if not results:
        return (
            "❌ Mos 3D model topilmadi.\n\n"
            "7 ta Telegram kanalida mos rasm "
            "aniqlanmadi."
        )

    text = "🔎 **ARCHHELP 3D MODEL TOPISH**\n\n"

    for index, result in enumerate(
        results,
        start=1
    ):

        similarity = result["similarity"]
        title = result["title"]
        channel = result["channel"]
        link = result["link"]

        text += (
            f"🏆 **{index}. {title}**\n"
            f"📊 O‘xshashlik: **{similarity}%**\n"
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


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    async def main():
        await start_client()

        print(
            "ARCHHELP 3D SEARCH CLIENT IS READY"
        )

        await client.disconnect()

    asyncio.run(main())