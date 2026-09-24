from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def calculator_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🧱 G‘isht"),
                KeyboardButton(text="🟫 Gazoblok"),
            ],
            [
                KeyboardButton(text="🟨 Penoblok"),
                KeyboardButton(text="🧱 Keramoblok"),
            ],
            [
                KeyboardButton(text="🟪 Shlakoblok"),
                KeyboardButton(text="📐 Maydon"),
            ],
            [
                KeyboardButton(text="📦 Hajm"),
                KeyboardButton(text="🧱 Beton"),
            ],
            [
                KeyboardButton(text="🎨 Bo‘yoq"),
                KeyboardButton(text="🪜 Zina"),
            ],
            [
                KeyboardButton(text="📏 Masshtab"),
            ],
            [
                KeyboardButton(text="⬅️ Orqaga"),
            ],
        ],
        resize_keyboard=True
    )

    return keyboard