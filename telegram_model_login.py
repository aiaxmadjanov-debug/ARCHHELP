import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from telethon import TelegramClient


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


SESSION_DIR = BASE_DIR / "bot" / "model_search"
SESSION_DIR.mkdir(parents=True, exist_ok=True)

SESSION_FILE = SESSION_DIR / "archhelp_search"


async def main():

    client = TelegramClient(
        str(SESSION_FILE),
        API_ID,
        API_HASH
    )

    print("🔐 Telegram akkaunt ulanishi boshlanmoqda...")

    await client.start()

    print()
    print("✅ Telegram akkaunt muvaffaqiyatli ulandi!")
    print()
    print(f"Session fayl:")
    print(SESSION_FILE)

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())