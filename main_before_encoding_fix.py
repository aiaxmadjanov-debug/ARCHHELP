import asyncio
import os
import json
import math

from aiogram import Bot, Dispatcher, F, BaseMiddleware
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

from dotenv import load_dotenv
from telegram_model_search import search_3d_models, format_results

# =========================================================
# ADMIN
# =========================================================

ADMIN_ID = 8050206263
# =========================================================
# USERLAR BAZASI
# =========================================================

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    try:
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"вќЊ USERS.JSON OвЂQISH XATOSI: {e}")
        return {}


def save_users(users):
    try:
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(
                users,
                f,
                ensure_ascii=False,
                indent=4
            )
    except Exception as e:
        print(f"вќЊ USERS.JSON SAQLASH XATOSI: {e}")


def register_user(user):
    if not user:
        return

    users = load_users()

    user_id = str(user.id)

    users[user_id] = {
        "id": user.id,
        "username": user.username,
        "first_name": user.first_name or ""
    }

    save_users(users)


from knowledge.revit_errors import REVIT_ERRORS
from knowledge.revit_installation import REVIT_INSTALLATION
from knowledge.revit_tips import REVIT_TIPS
from knowledge.revit_tools import REVIT_TOOLS
from knowledge.revit_families import REVIT_FAMILIES
from knowledge.revit_dimensions import REVIT_DIMENSIONS

from knowledge.autocad_commands import AUTOCAD_COMMANDS
from knowledge.autocad_errors import AUTOCAD_ERRORS

from knowledge.calculator import calculator_menu
from knowledge.ai_helper import AIHelper, ask_ai

# =========================================================
# ENV
# =========================================================

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN .env faylda topilmadi")


# =========================================================
# BOT
# =========================================================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
# =========================================================
# MAJBURIY KANAL OBUNASI
# =========================================================

CHANNEL_ID = "@autocadrvt"
CHANNEL_URL = "https://t.me/autocadrvt"


def subscription_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="рџ“ў Kanalga a'zo boвЂlish",
                    url=CHANNEL_URL
                )
            ],
            [
                InlineKeyboardButton(
                    text="вњ… Tekshirish",
                    callback_data="check_subscription"
                )
            ]
        ]
    )


async def check_subscription(user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(
            chat_id=CHANNEL_ID,
            user_id=user_id
        )

        if member.status in (
            "creator",
            "administrator",
            "member"
        ):
            return True

        if (
            member.status == "restricted"
            and getattr(member, "is_member", False)
        ):
            return True

        return False

    except Exception as e:
        print(f"вќЊ KANAL TEKSHIRISH XATOSI: {e}")
        return False


class SubscriptionMiddleware(BaseMiddleware):

    async def __call__(self, handler, event, data):

        # -----------------------------------------------------
        # MESSAGE
        # -----------------------------------------------------

        if isinstance(event, Message):

            # /start har doim ishlaydi
            if event.text and event.text.startswith("/start"):
                return await handler(event, data)

            if not event.from_user:
                return await handler(event, data)

            subscribed = await check_subscription(
                event.from_user.id
            )

            if not subscribed:
                await event.answer(
                    "рџ”’ ARCHHELP BOT\n\n"
                    "Botdan foydalanish uchun avval "
                    "kanalimizga aвЂ™zo boвЂling.\n\n"
                    "рџ“ў Kanal: @autocadrvt\n\n"
                    "1пёЏвѓЈ Kanalga aвЂ™zo boвЂling\n"
                    "2пёЏвѓЈ В«вњ… TekshirishВ» tugmasini bosing.",
                    reply_markup=subscription_keyboard()
                )
                return

            register_user(event.from_user)

            return await handler(event, data)
        # -----------------------------------------------------
        # CALLBACK
        # -----------------------------------------------------

        if isinstance(event, CallbackQuery):

            # Obunani tekshirish tugmasi doim ishlaydi
            if event.data == "check_subscription":
                return await handler(event, data)

            if not event.from_user:
                return await handler(event, data)

            subscribed = await check_subscription(
                event.from_user.id
            )

            if not subscribed:

                await event.answer(
                    "рџ”’ Avval kanalga a'zo boвЂling!",
                    show_alert=True
                )

                return

            return await handler(event, data)

        return await handler(event, data)


# Middleware ulash
dp.message.outer_middleware(
    SubscriptionMiddleware()
)

dp.callback_query.outer_middleware(
    SubscriptionMiddleware()
)


# =========================================================
# AUTOCAD MASLAHATLARI
# =========================================================

AUTOCAD_TIPS = {

    "AutoCADni tezlashtirish": {
        "tushuntirish":
            "Katta DWG fayllarda AutoCAD sekinlashishi mumkin.",
        "qadamlar": [
            "PURGE buyrugвЂi bilan keraksiz elementlarni oвЂchiring.",
            "AUDIT orqali chizmani tekshiring.",
            "OVERKILL orqali takroriy chiziqlarni tozalang.",
            "Keraksiz XREF va ogвЂir bloklarni kamaytiring."
        ],
        "misol":
            "500 MB DWG faylni PURGE va OVERKILL orqali yengillashtirish mumkin.",
        "maslahat":
            "Katta loyihalarni muntazam tozalab turing."
    },

    "Layerlarni toвЂgвЂri tashkil qilish": {
        "tushuntirish":
            "Har bir chizma elementi alohida va mantiqiy Layerda boвЂlishi kerak.",
        "qadamlar": [
            "Devorlar uchun alohida Layer yarating.",
            "Eshik va derazalarni alohida Layerga ajrating.",
            "OвЂlcham va matnlar uchun alohida Layer ishlating.",
            "Keraksiz Layerlarni Freeze yoki Off qiling."
        ],
        "misol":
            "A-WALL, A-DOOR, A-WINDOW, A-DIMS kabi tizim.",
        "maslahat":
            "Layer nomlarini loyiha boshida standartlashtiring."
    },

    "Layer 0 dan toвЂgвЂri foydalanish": {
        "tushuntirish":
            "Block yaratishda Layer 0 maxsus ahamiyatga ega.",
        "qadamlar": [
            "Block geometriyasini Layer 0 da yarating.",
            "Properties uchun ByLayer va ByBlock ishlating.",
            "Blockni kerakli Layerga joylashtiring."
        ],
        "misol":
            "Eshik Blockini Layer 0 da yaratib, A-DOOR Layeriga qoвЂyish.",
        "maslahat":
            "Blocklarni tartibli yaratish keyinchalik boshqarishni osonlashtiradi."
    },

    "Model Space va Layoutni toвЂgвЂri ishlatish": {
        "tushuntirish":
            "Model Space loyiha geometriyasi uchun, Layout esa chop etish uchun ishlatiladi.",
        "qadamlar": [
            "Modelni 1:1 masshtabda chizing.",
            "Layout yarating.",
            "Viewport oching.",
            "Kerakli scale ni belgilang.",
            "Viewportni Lock qiling."
        ],
        "misol":
            "Model 1:1, Layout viewport 1:100.",
        "maslahat":
            "Modelni 1:100 qilib chizmang."
    },

    "Object Snapni toвЂgвЂri ishlatish": {
        "tushuntirish":
            "Object Snap obyektlarning aniq nuqtalariga ulanish imkonini beradi.",
        "qadamlar": [
            "F3 orqali Object Snapni yoqing.",
            "Endpointni belgilang.",
            "Midpointni belgilang.",
            "Center va Intersection kerak boвЂlsa yoqing."
        ],
        "misol":
            "Devorni boshqa devorning Endpoint nuqtasiga aniq ulash.",
        "maslahat":
            "Aniq arxitektura chizmalarida OSNAP juda muhim."
    },

    "Unitsni toвЂgвЂri sozlash": {
        "tushuntirish":
            "Chizma boshida birliklarni toвЂgвЂri oвЂrnatish kerak.",
        "qadamlar": [
            "UNITS buyrugвЂini yozing.",
            "Type ni Decimal qiling.",
            "Insertion Scale ni Millimeters qiling.",
            "OK bosing."
        ],
        "misol":
            "Arxitektura loyihasida millimetrdan foydalanish.",
        "maslahat":
            "Har bir yangi loyiha boshida UNITSni tekshiring."
    },

    "PURGE bilan tozalash": {
        "tushuntirish":
            "PURGE ishlatilmayotgan Layer, Block, Linetype va boshqa maвЂ™lumotlarni tozalaydi.",
        "qadamlar": [
            "PURGE buyrugвЂini yozing.",
            "Purge All ni tanlang.",
            "Keraksiz elementlarni tozalang.",
            "Zarur boвЂlsa jarayonni qaytaring."
        ],
        "misol":
            "Eski Block va Layerlarni olib tashlash.",
        "maslahat":
            "Loyihani topshirishdan oldin PURGE qilish foydali."
    },

    "AUDIT bilan DWGni tekshirish": {
        "tushuntirish":
            "AUDIT DWG ichidagi xatolarni aniqlash va tuzatishga yordam beradi.",
        "qadamlar": [
            "AUDIT buyrugвЂini yozing.",
            "Yes tanlang.",
            "AutoCAD faylni tekshiradi.",
            "Topilgan muammolarni tuzatadi."
        ],
        "misol":
            "DWG ochilganda xatolar chiqsa AUDIT ishlatish.",
        "maslahat":
            "AUDITdan keyin faylni qayta saqlang."
    },

    "OVERKILL bilan takroriy chiziqlarni tozalash": {
        "tushuntirish":
            "OVERKILL bir-birining ustiga tushgan yoki takrorlangan geometriyani tozalaydi.",
        "qadamlar": [
            "OVERKILL buyrugвЂini yozing.",
            "Kerakli obyektlarni tanlang.",
            "Enter bosing.",
            "Sozlamalarni tekshiring."
        ],
        "misol":
            "Bir devor chizigвЂi tasodifan bir necha marta chizilgan boвЂlsa.",
        "maslahat":
            "Katta DWGlarni yengillashtirishda foydali."
    },

    "PDFga sifatli chiqarish": {
        "tushuntirish":
            "PDF sifati Plot sozlamalariga bogвЂliq.",
        "qadamlar": [
            "PLOT buyrugвЂini oching.",
            "DWG To PDF.pc3 ni tanlang.",
            "Paper Size ni tanlang.",
            "Plot Area ni belgilang.",
            "Scale va Lineweightlarni tekshiring.",
            "Preview orqali tekshiring."
        ],
        "misol":
            "A3 formatda 1:100 plan chiqarish.",
        "maslahat":
            "PDF chiqarishdan oldin Previewni tekshiring."
    },

    "Viewportni qulflash": {
        "tushuntirish":
            "Viewport Lock scale tasodifan oвЂzgarib ketishining oldini oladi.",
        "qadamlar": [
            "Layoutga oвЂting.",
            "Viewportni tanlang.",
            "Display Locked qiymatini Yes qiling."
        ],
        "misol":
            "1:100 viewportni Lock qilish.",
        "maslahat":
            "Tayyor Layoutdagi viewportlarni Lock qiling."
    },

    "Template DWT yaratish": {
        "tushuntirish":
            "DWT loyiha standartlarini oldindan tayyorlab qoвЂyish imkonini beradi.",
        "qadamlar": [
            "Layerlarni yarating.",
            "Text Style sozlang.",
            "Dimension Style yarating.",
            "Layoutlarni tayyorlang.",
            "Faylni DWT sifatida saqlang."
        ],
        "misol":
            "Arxitektura loyihalari uchun standart A3 yoki A1 template.",
        "maslahat":
            "Bir xil turdagi loyihalarda vaqtni tejaydi."
    },

    "Chizmani 1:1 chizish": {
        "tushuntirish":
            "AutoCAD Model Space'da geometriya real oвЂlchamda chiziladi.",
        "qadamlar": [
            "UNITSni tekshiring.",
            "Haqiqiy oвЂlchamni kiriting.",
            "Modelda scale ishlatmang.",
            "Scale ni Layoutda boshqaring."
        ],
        "misol":
            "5000 mm devor Model Space'da 5000 mm boвЂladi.",
        "maslahat":
            "Model oвЂlchami bilan chop etish masshtabini aralashtirmang."
    },

    "REGEN va REGENALL": {
        "tushuntirish":
            "REGEN chizma koвЂrinishini qayta hisoblaydi.",
        "qadamlar": [
            "REGEN yozing.",
            "Muammo qolsa REGENALL yozing."
        ],
        "misol":
            "Circle yoki Hatch notoвЂgвЂri koвЂringanda.",
        "maslahat":
            "KoвЂrinishdagi gвЂalati muammolarda sinab koвЂring."
    },

    "AutoSave va Recovery": {
        "tushuntirish":
            "AutoSave va Recovery maвЂ™lumot yoвЂqolishining oldini olishga yordam beradi.",
        "qadamlar": [
            "OPTIONS ni oching.",
            "Open and Save boвЂlimiga kiring.",
            "Automatic Save ni yoqing.",
            "Backup nusxalarni saqlashni yoqing."
        ],
        "misol":
            "Har 10 daqiqada avtomatik saqlash.",
        "maslahat":
            "Muhim loyihalarda AutoSave yoqilgan boвЂlsin."
    }
}


# =========================================================
# AUTOCAD SOZLAMALARI
# =========================================================

AUTOCAD_SETTINGS = {

    "UNITS": {
        "vazifasi": "Chizma birliklarini sozlash.",
        "buyruq": "UNITS",
        "tavsiya":
            "Arxitektura loyihalarida odatda Decimal va millimetr ishlatiladi.",
        "qadamlar": [
            "UNITS yozing.",
            "Type в†’ Decimal.",
            "Insertion Scale в†’ Millimeters.",
            "OK bosing."
        ]
    },

    "OPTIONS": {
        "vazifasi": "AutoCADning umumiy sozlamalarini boshqarish.",
        "buyruq": "OPTIONS",
        "tavsiya":
            "Display, Open and Save, System va boshqa sozlamalar shu yerda.",
        "qadamlar": [
            "OPTIONS yozing.",
            "Open and Save boвЂlimini tekshiring.",
            "Display boвЂlimini tekshiring.",
            "Files boвЂlimidagi pathlarni tekshiring."
        ]
    },

    "Object Snap": {
        "vazifasi": "Obyektlarning aniq nuqtalariga ulanish.",
        "buyruq": "OSNAP yoki F3",
        "tavsiya":
            "Endpoint, Midpoint, Center va Intersection eng koвЂp ishlatiladi.",
        "qadamlar": [
            "F3 bosing.",
            "Object Snap Settingsni oching.",
            "Kerakli Snaplarni belgilang."
        ]
    },

    "Ortho": {
        "vazifasi": "Chiziqlarni gorizontal yoki vertikal chizish.",
        "buyruq": "F8",
        "tavsiya":
            "ToвЂgвЂri devorlar va oвЂqlar chizishda foydali.",
        "qadamlar": [
            "F8 bosing.",
            "Ortho yoqiladi.",
            "LINE yoki boshqa chizish buyrugвЂini ishlating."
        ]
    },

    "Polar Tracking": {
        "vazifasi":
            "Belgilangan burchaklar boвЂyicha aniq chizish.",
        "buyruq": "F10",
        "tavsiya":
            "90В°, 45В°, 30В° kabi burchaklarda ishlash uchun qulay.",
        "qadamlar": [
            "F10 bosing.",
            "Drafting Settings orqali burchaklarni sozlang."
        ]
    },

    "Dynamic Input": {
        "vazifasi":
            "Kursor yonida masofa va burchak qiymatlarini kiritish.",
        "buyruq": "F12",
        "tavsiya":
            "Tezkor chizishda foydali.",
        "qadamlar": [
            "F12 bosing.",
            "Dynamic Input yoqiladi yoki oвЂchiriladi."
        ]
    },

    "Selection Settings": {
        "vazifasi":
            "Obyektlarni tanlash xatti-harakatlarini boshqarish.",
        "buyruq": "OPTIONS",
        "tavsiya":
            "Selection boвЂlimida tanlash parametrlarini sozlang.",
        "qadamlar": [
            "OPTIONS yozing.",
            "Selection boвЂlimiga oвЂting.",
            "Kerakli parametrlarni sozlang."
        ]
    },

    "Lineweight": {
        "vazifasi":
            "Chiziqlarning qalinligini boshqarish.",
        "buyruq": "LWEIGHT",
        "tavsiya":
            "Arxitektura chizmalarida chiziq ierarxiyasini koвЂrsatishda muhim.",
        "qadamlar": [
            "Layer Properties Manager oching.",
            "Layerlarga Lineweight belgilang.",
            "LWT orqali koвЂrinishni yoqing."
        ]
    },

    "Linetype Scale": {
        "vazifasi":
            "Dash, Center va boshqa chiziq turlarining koвЂrinishini boshqarish.",
        "buyruq": "LTSCALE",
        "tavsiya":
            "Layoutda chiziqlar notoвЂgвЂri koвЂrinsa LTSCALE va PSLTSCALEni tekshiring.",
        "qadamlar": [
            "LTSCALE yozing.",
            "Kerakli qiymatni kiriting.",
            "REGENALL bajaring."
        ]
    },

    "Autosave": {
        "vazifasi": "Loyihani avtomatik saqlash.",
        "buyruq": "OPTIONS",
        "tavsiya":
            "Muhim loyihalarda AutoSave yoqilgan boвЂlishi kerak.",
        "qadamlar": [
            "OPTIONS yozing.",
            "Open and Save boвЂlimiga kiring.",
            "Automatic Save ni yoqing.",
            "Kerakli intervalni belgilang."
        ]
    }
}


# =========================================================
# MENYULAR
# =========================================================

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏗 Revit"),
            KeyboardButton(text="🔧 AutoCAD"),
        ],
        [
            KeyboardButton(text="📐 Hisoblagich"),
            KeyboardButton(text="🤖 AI yordamchi"),
        ],
        [
            KeyboardButton(text="📚 Videodarsliklar"),
        ],
        [
            KeyboardButton(text="🔎 3D MODEL TOPISH"),
        ],
        [
            KeyboardButton(text="📞 Admin bilan bog‘lanish"),
        ],
    ],
    resize_keyboard=True
)


revit_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Revit xatolari"),
            KeyboardButton(text="⚙️ Revit o‘rnatish"),
        ],
        [
            KeyboardButton(text="💡 Revit maslahatlari"),
            KeyboardButton(text="🔧 Revit Tools"),
        ],
        [
            KeyboardButton(text="🧩 Revit Families"),
            KeyboardButton(text="📏 Revit o‘lchamlar"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
        ],
    ],
    resize_keyboard=True
)


autocad_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛠️ AutoCAD buyruqlari"),
        ],
        [
            KeyboardButton(text="❌ AutoCAD xatolari"),
            KeyboardButton(text="💡 AutoCAD maslahatlari"),
        ],
        [
            KeyboardButton(text="📐 AutoCAD sozlamalari"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
        ],
    ],
    resize_keyboard=True
)


autocad_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛠️ AutoCAD buyruqlari"),
        ],
        [
            KeyboardButton(text="❌ AutoCAD xatolari"),
            KeyboardButton(text="💡 AutoCAD maslahatlari"),
        ],
        [
            KeyboardButton(text="📐 AutoCAD sozlamalari"),
        ],
        [
            KeyboardButton(text="⬅️ Orqaga"),
        ],
    ],
    resize_keyboard=True
)

# =========================================================
# VIDEODARSLIKLAR MENYUSI
# =========================================================

video_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="рџ’» AutoCAD oвЂrnatish",
                url="https://t.me/autocadrvt/204"
            )
        ],
        [
            InlineKeyboardButton(
                text="рџЏ— Revit oвЂrnatish",
                url="https://t.me/autocadrvt/3"
            )
        ],
        [
            InlineKeyboardButton(
                text="в¬…пёЏ Orqaga",
                callback_data="video_back"
            )
        ],
    ]
)


# =========================================================
# VIDEODARSLIKLAR
# =========================================================

@dp.message(F.text == "рџ“љ Videodarsliklar")
async def video_lessons_handler(message: Message):

    await message.answer(
        "рџ“љ VIDEODARSLIKLAR\n\n"
        "Kerakli dastur boвЂyicha oвЂrnatish "
        "videodarsligini tanlang:",
        reply_markup=video_menu
    )

# =========================================================
# VIDEODARSLIKLARDAN ORQAGA
# =========================================================

@dp.callback_query(F.data == "video_back")
async def video_back_handler(callback: CallbackQuery):

    await callback.message.delete()

    await callback.message.answer(
        "рџЏ  Asosiy menyu:",
        reply_markup=main_menu
    )

    await callback.answer()

# =========================================================
# START
# =========================================================

@dp.message(CommandStart())
async def start_handler(
    message: Message,
    state: FSMContext
):

    await state.clear()

    subscribed = await check_subscription(
        message.from_user.id
    )

    if not subscribed:
        await message.answer(
            "рџ”’ ARCHHELP BOT\n\n"
            "рџЏ— ARCHHELP'dan foydalanish uchun "
            "kanalimizga a'zo boвЂlishingiz kerak.\n\n"
            "рџ“ў Kanal: @autocadrvt\n\n"
            "1пёЏвѓЈ Kanalga aвЂ™zo boвЂling\n"
            "2пёЏвѓЈ В«вњ… TekshirishВ» tugmasini bosing.",
            reply_markup=subscription_keyboard()
        )
        return

    register_user(message.from_user)

    await message.answer(
        "рџЏ— ARCHHELP ga xush kelibsiz!\n\n"
        "Arxitektura, Revit va AutoCAD boвЂyicha "
        "amaliy yordam olishingiz mumkin.",
        reply_markup=main_menu
    )
# =========================================================
# ADMIN вЂ” STATISTIKA
# =========================================================

@dp.message(Command("stats"))
async def admin_stats(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    users = load_users()

    await message.answer(
        "рџ“Љ ARCHHELP STATISTIKA\n\n"
        f"рџ‘Ґ Jami foydalanuvchilar: {len(users)} ta"
    )


# =========================================================
# OBUNANI TEKSHIRISH
# =========================================================

@dp.callback_query(F.data == "check_subscription")
async def check_subscription_callback(
    callback: CallbackQuery
):

    subscribed = await check_subscription(
        callback.from_user.id
    )

    if not subscribed:

        await callback.answer(
            "вќЊ Siz hali kanalga a'zo boвЂlmagansiz!",
            show_alert=True
        )

        return

    await callback.answer(
        "вњ… Obuna tasdiqlandi!"
    )

    if callback.message:

        try:
            await callback.message.edit_text(
                "вњ… Kanalga a'zoligingiz tasdiqlandi!\n\n"
                "рџЋ‰ Endi ARCHHELP botidan foydalanishingiz mumkin."
            )
        except Exception:
            pass

        await callback.message.answer(
            "рџЏ  ARCHHELP\n\n"
            "Kerakli boвЂlimni tanlang:",
            reply_markup=main_menu
        )


# =========================================================
# ORQAGA
# =========================================================

@dp.message(F.text == "в¬…пёЏ Orqaga")
async def back_handler(
    message: Message,
    state: FSMContext
):

    await state.clear()

    await message.answer(
        "рџЏ  Asosiy menyu",
        reply_markup=main_menu
    )


# =========================================================
# REVIT
# =========================================================

@dp.message(F.text == "рџЏ— Revit")
async def revit_handler(message: Message):

    await message.answer(
        "рџЏ— Revit boвЂlimi\n\n"
        "Kerakli boвЂlimni tanlang:",
        reply_markup=revit_menu
    )


# =========================================================
# REVIT XATOLARI
# =========================================================

@dp.message(F.text == "вќЊ Revit xatolari")
async def revit_errors_handler(message: Message):

    buttons = [
        [KeyboardButton(text=f"вќЊ {name}")]
        for name in REVIT_ERRORS.keys()
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"вќЊ Revit xatolari\n\n"
        f"Jami: {len(REVIT_ERRORS)} ta\n\n"
        f"Muammoni tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("вќЊ ")
        and message.text[2:] in REVIT_ERRORS
)
async def revit_error_detail(message: Message):

    name = message.text[2:]
    data = REVIT_ERRORS[name]

    text = (
        f"вќЊ {name}\n\n"
        f"рџ”ґ Sabab:\n{data.get('sabab', '-')}\n\n"
        f"рџ›  Yechim:\n{data.get('yechim', '-')}\n\n"
        f"рџ“Њ Misol:\n{data.get('misol', '-')}\n\n"
        f"рџ’Ў Maslahat:\n{data.get('maslahat', '-')}"
    )

    await message.answer(text)


# =========================================================
# REVIT INSTALLATION
# =========================================================

@dp.message(F.text == "вљ™пёЏ Revit oвЂrnatish")
async def revit_installation_handler(message: Message):

    buttons = [
        [KeyboardButton(text=f"вљ™пёЏ {name}")]
        for name in REVIT_INSTALLATION.keys()
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"вљ™пёЏ Revit oвЂrnatish va sozlash\n\n"
        f"Jami: {len(REVIT_INSTALLATION)} ta muammo\n\n"
        f"Muammoni tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("вљ™пёЏ ")
        and message.text[3:] in REVIT_INSTALLATION
)
async def revit_installation_detail(message: Message):

    name = message.text[3:]
    data = REVIT_INSTALLATION[name]

    text = (
        f"вљ™пёЏ {name}\n\n"
        f"рџ”ґ Sabab:\n{data.get('sabab', '-')}\n\n"
        f"рџ›  Yechim:\n{data.get('yechim', '-')}\n\n"
        f"рџ“Њ Misol:\n{data.get('misol', '-')}\n\n"
        f"рџ’Ў Maslahat:\n{data.get('maslahat', '-')}"
    )

    await message.answer(text)


# =========================================================
# REVIT TIPS
# =========================================================

@dp.message(F.text == "рџ’Ў Revit maslahatlari")
async def revit_tips_handler(message: Message):

    buttons = [
        [KeyboardButton(text=f"рџ’Ў {name}")]
        for name in REVIT_TIPS.keys()
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"рџ’Ў Revit maslahatlari\n\n"
        f"Jami: {len(REVIT_TIPS)} ta\n\n"
        f"Maslahatni tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("рџ’Ў ")
        and message.text[2:] in REVIT_TIPS
)
async def revit_tip_detail(message: Message):

    name = message.text[2:]
    data = REVIT_TIPS[name]

    text = (
        f"рџ’Ў {name}\n\n"
        f"рџ“– Tushuntirish:\n"
        f"{data.get('tushuntirish', data.get('yechim', '-'))}\n\n"
        f"рџ“Њ Misol:\n"
        f"{data.get('misol', '-')}\n\n"
        f"рџ’Ў Maslahat:\n"
        f"{data.get('maslahat', '-')}"
    )

    if data.get("qadamlar"):

        text += "\n\nрџЄњ Qadamlar:\n"

        for i, step in enumerate(data["qadamlar"], 1):
            text += f"{i}. {step}\n"

    await message.answer(text)


# =========================================================
# REVIT TOOLS
# =========================================================

@dp.message(F.text == "рџ”§ Revit Tools")
async def revit_tools_handler(message: Message):

    buttons = [
        [KeyboardButton(text=f"рџ”§ {name}")]
        for name in REVIT_TOOLS.keys()
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"рџ”§ Revit Tools\n\n"
        f"Jami: {len(REVIT_TOOLS)} ta tool\n\n"
        f"Toolni tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("рџ”§ ")
        and message.text[2:] in REVIT_TOOLS
)
async def revit_tool_detail(message: Message):

    name = message.text[2:]
    data = REVIT_TOOLS[name]

    text = (
        f"рџ”§ {name}\n\n"
        f"рџ“‚ Kategoriya:\n{data.get('kategoriya', '-')}\n\n"
        f"рџ“– Vazifasi:\n{data.get('vazifasi', '-')}\n\n"
        f"вЊЁпёЏ Ishlatish:\n{data.get('ishlatish', '-')}\n\n"
        f"рџ“Њ Misol:\n{data.get('misol', '-')}\n\n"
        f"рџ’Ў Maslahat:\n{data.get('maslahat', '-')}"
    )

    if data.get("qadamlar"):

        text += "\n\nрџЄњ Qadamlar:\n"

        for i, step in enumerate(data["qadamlar"], 1):
            text += f"{i}. {step}\n"

    await message.answer(text)


# =========================================================
# REVIT FAMILIES
# =========================================================

@dp.message(F.text == "рџ§© Revit Families")
async def revit_families_handler(message: Message):

    buttons = [
        [KeyboardButton(text=f"рџ§© {name}")]
        for name in REVIT_FAMILIES.keys()
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"рџ§© Revit Families\n\n"
        f"Jami: {len(REVIT_FAMILIES)} ta\n\n"
        f"Kerakli mavzuni tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("рџ§© ")
        and message.text[2:] in REVIT_FAMILIES
)
async def revit_family_detail(message: Message):

    name = message.text[2:]
    data = REVIT_FAMILIES[name]

    text = (
        f"рџ§© {name}\n\n"
        f"рџ“‚ Kategoriya:\n{data.get('kategoriya', '-')}\n\n"
        f"рџ“– Vazifasi:\n{data.get('vazifasi', '-')}\n\n"
        f"рџ“љ Tushuntirish:\n{data.get('tushuntirish', '-')}\n\n"
        f"рџ“Њ Misol:\n{data.get('misol', '-')}\n\n"
        f"рџ’Ў Maslahat:\n{data.get('maslahat', '-')}"
    )

    if data.get("qadamlar"):

        text += "\n\nрџЄњ Qadamlar:\n"

        for i, step in enumerate(data["qadamlar"], 1):
            text += f"{i}. {step}\n"

    await message.answer(text)


# =========================================================
# REVIT DIMENSIONS
# =========================================================

def revit_dimensions_categories():

    categories = set()

    for data in REVIT_DIMENSIONS.values():

        category = data.get("kategoriya")

        if category:
            categories.add(category)

    return sorted(categories)


@dp.message(F.text == "рџ“Џ Revit oвЂlchamlar")
async def revit_dimensions_handler(message: Message):

    categories = revit_dimensions_categories()

    buttons = [
        [KeyboardButton(text=f"рџ“ђ {category}")]
        for category in categories
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"рџ“Џ Revit normativ oвЂlchamlar\n\n"
        f"Jami: {len(REVIT_DIMENSIONS)} ta parametr\n\n"
        f"Kategoriya tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("рџ“ђ ")
        and message.text[2:] in revit_dimensions_categories()
)
async def revit_dimensions_category_handler(message: Message):

    category = message.text[2:]

    buttons = []

    for name, data in REVIT_DIMENSIONS.items():

        if data.get("kategoriya") == category:

            buttons.append(
                [KeyboardButton(text=f"рџ“Џ {name}")]
            )

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"рџ“ђ {category}\n\n"
        f"Parametrni tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("рџ“Џ ")
        and message.text[2:] in REVIT_DIMENSIONS
)
async def revit_dimension_detail(message: Message):

    name = message.text[2:]
    data = REVIT_DIMENSIONS[name]

    text = (
        f"рџ“Џ {name}\n\n"
        f"рџ“ђ Qiymat:\n{data.get('qiymat', '-')}\n\n"
        f"рџ“љ Manba:\n{data.get('manba', '-')}\n\n"
        f"рџ“Њ Band:\n{data.get('band', '-')}\n\n"
        f"рџ’Ў Izoh:\n"
        f"{data.get('izoh', data.get('maslahat', '-'))}"
    )

    await message.answer(text)


# =========================================================
# AUTOCAD
# =========================================================

@dp.message(F.text == "рџ”§ AutoCAD")
async def autocad_handler(message: Message):

    await message.answer(
        "рџ”§ AutoCAD boвЂlimi\n\n"
        "Kerakli boвЂlimni tanlang:",
        reply_markup=autocad_menu
    )


# =========================================================
# AUTOCAD BUYRUQLARI
# =========================================================

@dp.message(F.text == "вЊЁпёЏ AutoCAD buyruqlari")
async def autocad_commands_handler(message: Message):

    buttons = [
        [KeyboardButton(text=f"рџ”№ {name}")]
        for name in AUTOCAD_COMMANDS.keys()
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"вЊЁпёЏ AutoCAD buyruqlari\n\n"
        f"Jami: {len(AUTOCAD_COMMANDS)} ta\n\n"
        f"Buyruqni tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("рџ”№ ")
        and message.text[2:] in AUTOCAD_COMMANDS
)
async def autocad_command_detail(message: Message):

    name = message.text[2:]
    data = AUTOCAD_COMMANDS[name]

    text = (
        f"рџ”№ {name}\n\n"
        f"рџ“– Vazifasi:\n{data.get('vazifasi', '-')}\n\n"
        f"вЊЁпёЏ Ishlatish:\n{data.get('ishlatish', '-')}\n\n"
        f"рџ“Њ Misol:\n{data.get('misol', '-')}\n\n"
        f"рџЏ— Arxitekturada:\n"
        f"{data.get('arxitektura', '-')}\n\n"
        f"рџ’Ў Maslahat:\n{data.get('maslahat', '-')}"
    )

    await message.answer(text)


# =========================================================
# AUTOCAD XATOLARI
# =========================================================

@dp.message(F.text == "вќЊ AutoCAD xatolari")
async def autocad_errors_handler(message: Message):

    buttons = [
        [KeyboardButton(text=f"вќЊ {name}")]
        for name in AUTOCAD_ERRORS.keys()
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"вќЊ AutoCAD xatolari\n\n"
        f"Jami: {len(AUTOCAD_ERRORS)} ta\n\n"
        f"Muammoni tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("вќЊ ")
        and message.text[2:] in AUTOCAD_ERRORS
)
async def autocad_error_detail(message: Message):

    name = message.text[2:]
    data = AUTOCAD_ERRORS[name]

    text = (
        f"вќЊ {name}\n\n"
        f"рџ”ґ Sabab:\n{data.get('sabab', '-')}\n\n"
        f"рџ›  Yechim:\n{data.get('yechim', '-')}\n\n"
        f"рџ’Ў Maslahat:\n{data.get('maslahat', '-')}"
    )

    await message.answer(text)


# =========================================================
# AUTOCAD MASLAHATLARI
# =========================================================

@dp.message(F.text == "рџ’Ў AutoCAD maslahatlari")
async def autocad_tips_handler(message: Message):

    buttons = [
        [KeyboardButton(text=f"рџ’Ў {name}")]
        for name in AUTOCAD_TIPS.keys()
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"рџ’Ў AutoCAD maslahatlari\n\n"
        f"Jami: {len(AUTOCAD_TIPS)} ta\n\n"
        f"Maslahatni tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("рџ’Ў ")
        and message.text[2:] in AUTOCAD_TIPS
)
async def autocad_tip_detail(message: Message):

    name = message.text[2:]
    data = AUTOCAD_TIPS[name]

    text = (
        f"рџ’Ў {name}\n\n"
        f"рџ“– Tushuntirish:\n"
        f"{data.get('tushuntirish', '-')}\n\n"
        f"рџ“Њ Misol:\n"
        f"{data.get('misol', '-')}\n\n"
        f"рџ’Ў Maslahat:\n"
        f"{data.get('maslahat', '-')}"
    )

    if data.get("qadamlar"):

        text += "\n\nрџЄњ Qadamlar:\n"

        for i, step in enumerate(data["qadamlar"], 1):
            text += f"{i}. {step}\n"

    await message.answer(text)


# =========================================================
# AUTOCAD SOZLAMALARI
# =========================================================

@dp.message(F.text == "рџ“ђ AutoCAD sozlamalari")
async def autocad_settings_handler(message: Message):

    buttons = [
        [KeyboardButton(text=f"вљ™пёЏ {name}")]
        for name in AUTOCAD_SETTINGS.keys()
    ]

    buttons.append(
        [KeyboardButton(text="в¬…пёЏ Orqaga")]
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )

    await message.answer(
        f"рџ“ђ AutoCAD sozlamalari\n\n"
        f"Jami: {len(AUTOCAD_SETTINGS)} ta\n\n"
        f"Sozlamani tanlang:",
        reply_markup=keyboard
    )


@dp.message(
    lambda message:
        message.text
        and message.text.startswith("вљ™пёЏ ")
        and message.text[3:] in AUTOCAD_SETTINGS
)
async def autocad_settings_detail(message: Message):

    name = message.text[3:]
    data = AUTOCAD_SETTINGS[name]

    text = (
        f"вљ™пёЏ {name}\n\n"
        f"рџ“– Vazifasi:\n{data.get('vazifasi', '-')}\n\n"
        f"вЊЁпёЏ Buyruq:\n{data.get('buyruq', '-')}\n\n"
        f"рџ’Ў Tavsiya:\n{data.get('tavsiya', '-')}"
    )

    if data.get("qadamlar"):

        text += "\n\nрџЄњ Qadamlar:\n"

        for i, step in enumerate(data["qadamlar"], 1):
            text += f"{i}. {step}\n"

    await message.answer(text)

# =========================================================
# HISOBLAGICH вЂ” ASOSIY MENYU
# =========================================================

@dp.message(F.text == "рџ“ђ Hisoblagich")
async def calculator_handler(
    message: Message,
    state: FSMContext
):

    await state.clear()

    await message.answer(
        "рџ§® ARCHHELP KALKULYATOR\n\n"
        "Kerakli kalkulyatorni tanlang:",
        reply_markup=calculator_menu()
    )
# =========================================================
# HISOBLAGICH вЂ” ORTGA
# =========================================================

@dp.message(F.text == "в¬…пёЏ Ortga")
async def calculator_back_handler(
    message: Message,
    state: FSMContext
):
    await state.clear()

    await message.answer(
        "рџЏ  Bosh menyu:",
        reply_markup=main_menu
    )

# =========================================================
# HISOBLAGICH вЂ” GвЂISHT FSM
# =========================================================

class BrickCalculator(StatesGroup):

    # Devor
    length = State()
    height = State()

    # Eshik/deraza tanlovi
    openings = State()

    # Eshik
    door_count = State()
    door_length = State()
    door_height = State()

    # Deraza
    window_count = State()
    window_length = State()
    window_height = State()

    # GвЂisht
    brick_size = State()
    thickness = State()


# =========================================================
# GвЂISHT вЂ” BOSHLASH
# =========================================================

@dp.message(F.text == "рџ§± GвЂisht")
async def brick_calculator_handler(
    message: Message,
    state: FSMContext
):

    await state.clear()

    await state.set_state(
        BrickCalculator.length
    )

    await message.answer(
        "рџ§± GвЂISHT KALKULYATORI\n\n"
        "1пёЏвѓЈ Devor uzunligini kiriting.\n\n"
        "Masalan:\n"
        "10 m\n"
        "yoki\n"
        "10000 mm\n\n"
        "рџ“Њ m, cm yoki mm ishlatishingiz mumkin."
    )


# =========================================================
# OвЂLCHOVNI METRGA OвЂTKAZISH
# =========================================================

def parse_measurement(value: str):

    if not value:
        return None

    text = (
        value
        .strip()
        .lower()
        .replace(",", ".")
        .replace(" ", "")
    )

    try:

        # millimetr
        if text.endswith("mm"):

            number = float(
                text[:-2]
            )

            return number / 1000

        # santimetr
        if text.endswith("cm"):

            number = float(
                text[:-2]
            )

            return number / 100

        # metr
        if text.endswith("m"):

            number = float(
                text[:-1]
            )

            return number

        # Birlik yozilmasa metr deb olinadi
        return float(text)

    except ValueError:

        return None


# =========================================================
# 1-QADAM вЂ” DEVOR UZUNLIGI
# =========================================================

@dp.message(BrickCalculator.length)
async def brick_length_handler(
    message: Message,
    state: FSMContext
):

    if not message.text:

        await message.answer(
            "вќЊ Iltimos, devor uzunligini kiriting.\n\n"
            "Masalan: 10 m yoki 10000 mm"
        )

        return

    length = parse_measurement(
        message.text
    )

    if length is None:

        await message.answer(
            "вќЊ OвЂlchamni tushunmadim.\n\n"
            "Masalan:\n"
            "10 m\n"
            "10000 mm\n"
            "1000 cm"
        )

        return

    if length <= 0:

        await message.answer(
            "вќЊ Uzunlik 0 dan katta boвЂlishi kerak."
        )

        return

    if length > 10000:

        await message.answer(
            "вќЊ Juda katta qiymat kiritildi.\n\n"
            "Iltimos, devor uzunligini tekshiring."
        )

        return

    await state.update_data(
        wall_length=length
    )

    await state.set_state(
        BrickCalculator.height
    )

    await message.answer(
        f"вњ… Devor uzunligi: {length:g} m\n\n"
        "2пёЏвѓЈ Devor balandligini kiriting.\n\n"
        "Masalan:\n"
        "3 m\n"
        "3000 mm"
    )


# =========================================================
# 2-QADAM вЂ” DEVOR BALANDLIGI
# =========================================================

@dp.message(BrickCalculator.height)
async def brick_height_handler(
    message: Message,
    state: FSMContext
):

    if not message.text:

        await message.answer(
            "вќЊ Iltimos, devor balandligini kiriting."
        )

        return

    height = parse_measurement(
        message.text
    )

    if height is None:

        await message.answer(
            "вќЊ OвЂlchamni tushunmadim.\n\n"
            "Masalan:\n"
            "3 m\n"
            "3000 mm"
        )

        return

    if height <= 0:

        await message.answer(
            "вќЊ Balandlik 0 dan katta boвЂlishi kerak."
        )

        return

    if height > 100:

        await message.answer(
            "вќЊ Juda katta qiymat kiritildi.\n\n"
            "Iltimos, balandlikni tekshiring."
        )

        return

    await state.update_data(
        wall_height=height
    )

    # Eshik/deraza tanlovi
    opening_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="рџљЄ Eshik")
            ],
            [
                KeyboardButton(text="рџЄџ Deraza")
            ],
            [
                KeyboardButton(
                    text="рџљЄрџЄџ Eshik + deraza"
                )
            ],
            [
                KeyboardButton(text="вќЊ YoвЂq")
            ],
            [
                KeyboardButton(text="в¬…пёЏ Orqaga")
            ],
        ],
        resize_keyboard=True
    )

    await state.set_state(
        BrickCalculator.openings
    )

    await message.answer(
        f"вњ… Devor balandligi: {height:g} m\n\n"
        "3пёЏвѓЈ Devorning ichida eshik yoki derazalar bormi?\n\n"
        "рџ“Њ Eshik va derazalar maydoni "
        "keyinchalik umumiy devor maydonidan ayriladi.",
        reply_markup=opening_menu
    )


# =========================================================
# 3-QADAM вЂ” ESHIK / DERAZA
# =========================================================

@dp.message(BrickCalculator.openings)
async def brick_openings_handler(
    message: Message,
    state: FSMContext
):

    if not message.text:

        await message.answer(
            "вќЊ Quyidagi tugmalardan birini tanlang."
        )

        return

    text = message.text.strip()

    # -----------------------------------------------------
    # FAQAT ESHIK
    # -----------------------------------------------------

    if text == "рџљЄ Eshik":

        await state.update_data(
            door_area=0,
            window_area=0
        )

        await state.set_state(
            BrickCalculator.door_count
        )

        await message.answer(
            "рџљЄ ESHIK\n\n"
            "Eshiklar sonini kiriting.\n\n"
            "Masalan: 2"
        )

        return

    # -----------------------------------------------------
    # FAQAT DERAZA
    # -----------------------------------------------------

    if text == "рџЄџ Deraza":

        await state.update_data(
            door_area=0,
            window_area=0
        )

        await state.set_state(
            BrickCalculator.window_count
        )

        await message.answer(
            "рџЄџ DERAZA\n\n"
            "Derazalar sonini kiriting.\n\n"
            "Masalan: 4"
        )

        return

    # -----------------------------------------------------
    # ESHIK + DERAZA
    # -----------------------------------------------------

    if text == "рџљЄрџЄџ Eshik + deraza":

        await state.update_data(
            door_area=0,
            window_area=0
        )

        await state.set_state(
            BrickCalculator.door_count
        )

        await message.answer(
            "рџљЄ ESHIK\n\n"
            "Avval eshiklar sonini kiriting.\n\n"
            "Masalan: 2"
        )

        return

    # -----------------------------------------------------
    # OCHILISH YOвЂQ
    # -----------------------------------------------------

    if text == "вќЊ YoвЂq":

        await state.update_data(
            door_area=0,
            window_area=0
        )

        await state.set_state(
            BrickCalculator.brick_size
        )

        await send_brick_size_menu(
            message
        )

        return

    await message.answer(
        "вќЊ Iltimos, quyidagi tugmalardan birini tanlang."
    )


# =========================================================
# ESHIK SONI
# =========================================================

@dp.message(BrickCalculator.door_count)
async def brick_door_count_handler(
    message: Message,
    state: FSMContext
):

    if not message.text:

        await message.answer(
            "вќЊ Eshik sonini kiriting.\n\n"
            "Masalan: 2"
        )

        return

    try:

        count = int(
            message.text.strip()
        )

    except ValueError:

        await message.answer(
            "вќЊ Faqat butun son kiriting.\n\n"
            "Masalan: 2"
        )

        return

    if count <= 0:

        await message.answer(
            "вќЊ Eshik soni 0 dan katta boвЂlishi kerak."
        )

        return

    if count > 1000:

        await message.answer(
            "вќЊ Juda katta son kiritildi."
        )

        return

    await state.update_data(
        door_count=count
    )

    await state.set_state(
        BrickCalculator.door_length
    )

    await message.answer(
        f"рџљЄ Eshik soni: {count} ta\n\n"
        "Eshik uzunligini kiriting.\n\n"
        "Masalan:\n"
        "900 mm\n"
        "yoki\n"
        "0.9 m"
    )


# =========================================================
# ESHIK UZUNLIGI
# =========================================================

@dp.message(BrickCalculator.door_length)
async def brick_door_length_handler(
    message: Message,
    state: FSMContext
):

    length = parse_measurement(
        message.text or ""
    )

    if length is None or length <= 0:

        await message.answer(
            "вќЊ Eshik uzunligi notoвЂgвЂri.\n\n"
            "Masalan: 900 mm yoki 0.9 m"
        )

        return

    await state.update_data(
        door_length=length
    )

    await state.set_state(
        BrickCalculator.door_height
    )

    await message.answer(
        f"вњ… Eshik uzunligi: {length:g} m\n\n"
        "рџљЄ Endi eshik boвЂyini kiriting.\n\n"
        "Masalan:\n"
        "2100 mm\n"
        "yoki\n"
        "2.1 m"
    )


# =========================================================
# ESHIK BOвЂYI
# =========================================================

@dp.message(BrickCalculator.door_height)
async def brick_door_height_handler(
    message: Message,
    state: FSMContext
):

    height = parse_measurement(
        message.text or ""
    )

    if height is None or height <= 0:

        await message.answer(
            "вќЊ Eshik boвЂyi notoвЂgвЂri.\n\n"
            "Masalan: 2100 mm yoki 2.1 m"
        )

        return

    data = await state.get_data()

    door_count = data["door_count"]
    door_length = data["door_length"]

    door_area = (
        door_count *
        door_length *
        height
    )

    await state.update_data(
        door_height=height,
        door_area=door_area
    )

    # Agar foydalanuvchi Eshik + deraza tanlagan boвЂlsa,
    # keyin derazaga oвЂtamiz.
    await state.set_state(
        BrickCalculator.window_count
    )

    await message.answer(
        f"рџљЄ Eshik maydoni: {door_area:.2f} mВІ\n\n"
        "рџЄџ Endi derazalar sonini kiriting.\n\n"
        "Masalan: 4"
    )


# =========================================================
# DERAZA SONI
# =========================================================

@dp.message(BrickCalculator.window_count)
async def brick_window_count_handler(
    message: Message,
    state: FSMContext
):

    if not message.text:

        await message.answer(
            "вќЊ Deraza sonini kiriting.\n\n"
            "Masalan: 4\n\n"
            "Agar deraza boвЂlmasa, 0 yuboring."
        )

        return

    try:

        count = int(
            message.text.strip()
        )

    except ValueError:

        await message.answer(
            "вќЊ Faqat butun son kiriting.\n\n"
            "Masalan: 4\n\n"
            "Agar deraza boвЂlmasa, 0 yuboring."
        )

        return

    if count < 0:

        await message.answer(
            "вќЊ Deraza soni manfiy boвЂlishi mumkin emas.\n\n"
            "Agar deraza boвЂlmasa, 0 yuboring."
        )

        return

    if count > 1000:

        await message.answer(
            "вќЊ Juda katta son kiritildi."
        )

        return

    # =====================================================
    # DERAZA YOвЂQ
    # =====================================================

    if count == 0:

        await state.update_data(
            window_count=0,
            window_length=0,
            window_height=0,
            window_area=0
        )

        await state.set_state(
            BrickCalculator.brick_size
        )

        await message.answer(
            "рџЄџ Deraza: 0 ta\n"
            "вњ… Deraza maydoni: 0.00 mВІ\n\n"
            "Endi gвЂisht oвЂlchamini tanlang:"
        )

        await send_brick_size_menu(
            message
        )

        return

    # =====================================================
    # DERAZA BOR
    # =====================================================

    await state.update_data(
        window_count=count
    )

    await state.set_state(
        BrickCalculator.window_length
    )

    await message.answer(
        f"рџЄџ Deraza soni: {count} ta\n\n"
        "Deraza uzunligini kiriting.\n\n"
        "Masalan:\n"
        "1500 mm\n"
        "yoki\n"
        "1.5 m"
    )

# =========================================================
# DERAZA UZUNLIGI
# =========================================================

@dp.message(BrickCalculator.window_length)
async def brick_window_length_handler(
    message: Message,
    state: FSMContext
):

    length = parse_measurement(
        message.text or ""
    )

    if length is None or length <= 0:

        await message.answer(
            "вќЊ Deraza uzunligi notoвЂgвЂri.\n\n"
            "Masalan: 1500 mm yoki 1.5 m"
        )

        return

    await state.update_data(
        window_length=length
    )

    await state.set_state(
        BrickCalculator.window_height
    )

    await message.answer(
        f"вњ… Deraza uzunligi: {length:g} m\n\n"
        "рџЄџ Endi deraza boвЂyini kiriting.\n\n"
        "Masalan:\n"
        "1500 mm\n"
        "yoki\n"
        "1.5 m"
    )


# =========================================================
# DERAZA BOвЂYI
# =========================================================

@dp.message(BrickCalculator.window_height)
async def brick_window_height_handler(
    message: Message,
    state: FSMContext
):

    height = parse_measurement(
        message.text or ""
    )

    if height is None or height <= 0:

        await message.answer(
            "вќЊ Deraza boвЂyi notoвЂgвЂri.\n\n"
            "Masalan: 1500 mm yoki 1.5 m"
        )

        return

    data = await state.get_data()

    window_count = data["window_count"]
    window_length = data["window_length"]

    window_area = (
        window_count *
        window_length *
        height
    )

    await state.update_data(
        window_height=height,
        window_area=window_area
    )

    await state.set_state(
        BrickCalculator.brick_size
    )

    await message.answer(
        f"рџЄџ Deraza maydoni: {window_area:.2f} mВІ\n\n"
        "вњ… Eshik va derazalar hisoblandi.\n\n"
        "Endi gвЂisht oвЂlchamini tanlang:"
    )

    await send_brick_size_menu(
        message
    )


# =========================================================
# GвЂISHT OвЂLCHAMI MENYUSI
# =========================================================

async def send_brick_size_menu(
    message: Message
):

    brick_size_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="250Г—120Г—65 mm"
                )
            ],
            [
                KeyboardButton(
                    text="250Г—120Г—88 mm"
                )
            ],
            [
                KeyboardButton(
                    text="250Г—120Г—138 mm"
                )
            ],
            [
                KeyboardButton(
                    text="Boshqa oвЂlcham"
                )
            ],
            [
                KeyboardButton(
                    text="в¬…пёЏ Orqaga"
                )
            ],
        ],
        resize_keyboard=True
    )

    await message.answer(
        "рџ“¦ GвЂisht oвЂlchamini tanlang:",
        reply_markup=brick_size_menu
    )


# =========================================================
# GвЂISHT OвЂLCHAMI
# =========================================================

@dp.message(BrickCalculator.brick_size)
async def brick_size_handler(
    message: Message,
    state: FSMContext
):

    text = (
        message.text or ""
    ).strip()

    brick_sizes = {

        "250Г—120Г—65 mm":
            "250Г—120Г—65 mm",

        "250Г—120Г—88 mm":
            "250Г—120Г—88 mm",

        "250Г—120Г—138 mm":
            "250Г—120Г—138 mm"
    }

    # -----------------------------------------------------
    # STANDART
    # -----------------------------------------------------

    if text in brick_sizes:

        await state.update_data(
            brick_name=brick_sizes[text]
        )

        await state.set_state(
            BrickCalculator.thickness
        )

        await send_thickness_menu(
            message
        )

        return

    # -----------------------------------------------------
    # BOSHQA OвЂLCHAM
    # -----------------------------------------------------

    if text == "Boshqa oвЂlcham":

        await message.answer(
            "рџ“Џ GвЂisht oвЂlchamlarini millimetrda kiriting.\n\n"
            "Format:\n"
            "uzunlik kenglik balandlik\n\n"
            "Masalan:\n"
            "250 120 65"
        )

        return

    # -----------------------------------------------------
    # CUSTOM OвЂLCHAM
    # -----------------------------------------------------

    parts = text.replace(",", ".").split()

    if len(parts) == 3:

        try:

            l = float(parts[0])
            w = float(parts[1])
            h = float(parts[2])

        except ValueError:

            await message.answer(
                "вќЊ OвЂlcham notoвЂgвЂri.\n\n"
                "Masalan:\n"
                "250 120 65"
            )

            return

        if l <= 0 or w <= 0 or h <= 0:

            await message.answer(
                "вќЊ Barcha oвЂlchamlar 0 dan katta boвЂlishi kerak."
            )

            return

        await state.update_data(
            brick_name=(
                f"{l:g}Г—{w:g}Г—{h:g} mm"
            )
        )

        await state.set_state(
            BrickCalculator.thickness
        )

        await send_thickness_menu(
            message
        )

        return

    await message.answer(
        "вќЊ GвЂisht oвЂlchami notoвЂgвЂri.\n\n"
        "Tugmadan tanlang yoki:\n\n"
        "250 120 65"
    )


# =========================================================
# QALINLIK MENYUSI
# =========================================================

async def send_thickness_menu(
    message: Message
):

    thickness_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="0.5 gвЂisht"
                )
            ],
            [
                KeyboardButton(
                    text="1 gвЂisht"
                )
            ],
            [
                KeyboardButton(
                    text="1.5 gвЂisht"
                )
            ],
            [
                KeyboardButton(
                    text="2 gвЂisht"
                )
            ],
            [
                KeyboardButton(
                    text="в¬…пёЏ Orqaga"
                )
            ],
        ],
        resize_keyboard=True
    )

    await message.answer(
        "рџ§± Devor qalinligini tanlang:",
        reply_markup=thickness_menu
    )


# =========================================================
# YAKUNIY HISOBLASH
# =========================================================

@dp.message(BrickCalculator.thickness)
async def brick_thickness_handler(
    message: Message,
    state: FSMContext
):

    text = (
        message.text or ""
    ).strip()

    # =====================================================
    # SEN BELGILAGAN STANDART SARFLAR
    # =====================================================

    brick_rates = {

        "0.5 gвЂisht": {
            "rate": 51,
            "thickness": "125вЂ“130 mm"
        },

        "1 gвЂisht": {
            "rate": 102,
            "thickness": "250 mm"
        },

        "1.5 gвЂisht": {
            "rate": 153,
            "thickness": "380вЂ“400 mm"
        },

        "2 gвЂisht": {
            "rate": 255,
            "thickness": "510вЂ“520 mm"
        }
    }

    if text not in brick_rates:

        await message.answer(
            "вќЊ Devor qalinligini tugmalardan tanlang."
        )

        return

    data = await state.get_data()

    # =====================================================
    # ASOSIY MA'LUMOTLAR
    # =====================================================

    wall_length = data.get(
        "wall_length", 0
    )

    wall_height = data.get(
        "wall_height", 0
    )

    brick_name = data.get(
        "brick_name",
        "250Г—120Г—65 mm"
    )

    # =====================================================
    # DEVOR MAYDONI
    # =====================================================

    wall_area = (
        wall_length *
        wall_height
    )

    # =====================================================
    # ESHIK MAYDONI
    # =====================================================

    door_area = data.get(
        "door_area",
        0
    )

    # =====================================================
    # DERAZA MAYDONI
    # =====================================================

    window_area = data.get(
        "window_area",
        0
    )

    # =====================================================
    # OCHILISHLAR UMUMIY MAYDONI
    # =====================================================

    openings_area = (
        door_area +
        window_area
    )

    # =====================================================
    # SOF DEVOR MAYDONI
    # =====================================================

    net_wall_area = (
        wall_area -
        openings_area
    )

    # Xavfsizlik
    if net_wall_area < 0:

        await state.clear()

        await message.answer(
            "вќЊ Eshik va derazalar maydoni "
            "devor maydonidan katta chiqdi.\n\n"
            "Iltimos, oвЂlchamlarni tekshirib "
            "qaytadan hisoblang.",
            reply_markup=calculator_menu()
        )

        return

    # =====================================================
    # 1 MВІ UCHUN GвЂISHT SARFI
    # =====================================================

    rate = brick_rates[text]["rate"]

    practical_thickness = (
        brick_rates[text]["thickness"]
    )

    # =====================================================
    # ASOSIY GвЂISHT MIQDORI
    # =====================================================

    brick_count = (
        net_wall_area *
        rate
    )

    # =====================================================
    # 5% ZAXIRA
    # =====================================================

    reserve = (
        brick_count *
        0.05
    )

    # =====================================================
    # JAMI
    # =====================================================

    total_bricks = (
        brick_count +
        reserve
    )

    total_bricks_rounded = int(
        total_bricks + 0.999999
    )

    reserve_rounded = int(
        reserve + 0.999999
    )

    # =====================================================
    # NATIJA
    # =====================================================

    result = (
        "рџ§± GвЂISHT KALKULYATORI\n"
        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n\n"

        f"рџ“Џ Devor uzunligi: "
        f"{wall_length:g} m\n"

        f"рџ“ђ Devor balandligi: "
        f"{wall_height:g} m\n"

        f"рџ“ђ Umumiy devor maydoni: "
        f"{wall_area:.2f} mВІ\n\n"

        f"рџљЄ Eshik maydoni: "
        f"{door_area:.2f} mВІ\n"

        f"рџЄџ Deraza maydoni: "
        f"{window_area:.2f} mВІ\n"

        f"вћ– Eshik + deraza: "
        f"{openings_area:.2f} mВІ\n\n"

        f"рџ“ђ SOF DEVOR MAYDONI: "
        f"{net_wall_area:.2f} mВІ\n\n"

        f"рџ“¦ GвЂisht oвЂlchami: "
        f"{brick_name}\n"

        f"рџ§± Devor qalinligi: "
        f"{text}\n"

        f"рџ“Џ Amaliy qalinlik: "
        f"{practical_thickness}\n\n"

        f"рџ§± 1 mВІ ga sarf: "
        f"{rate} dona\n\n"

        f"рџ§± Asosiy gвЂisht: "
        f"{brick_count:,.0f} dona\n"

        f"вћ• 5% zaxira: "
        f"{reserve_rounded:,} dona\n\n"

        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"

        f"вњ… JAMI: "
        f"{total_bricks_rounded:,} dona gвЂisht\n\n"

        "в„№пёЏ Hisoblashda eshik va derazalar "
        "maydoni umumiy devor maydonidan ayrildi.\n"

        "в„№пёЏ GвЂisht sarfi siz belgilagan standart "
        "boвЂyicha hisoblandi.\n"

        "в„№пёЏ 5% zaxira sinish, kesish va "
        "chiqindilar uchun qoвЂshildi."
    )

    await message.answer(
        result,
        reply_markup=calculator_menu()
    )

    await state.clear()

# =========================================================
# 1-QADAM вЂ” DEVOR UZUNLIGI
# =========================================================

@dp.message(BrickCalculator.length)
async def brick_length_handler(
    message: Message,
    state: FSMContext
):

    if not message.text:

        await message.answer(
            "вќЊ Iltimos, uzunlikni son bilan kiriting.\n\n"
            "Masalan: 15"
        )

        return

    text = (
        message.text
        .strip()
        .replace(",", ".")
    )

    try:
        length = float(text)

    except ValueError:

        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n\n"
            "Devor uzunligini metrda son bilan kiriting.\n\n"
            "Masalan:\n"
            "10\n"
            "12.5\n"
            "15"
        )

        return

    if length <= 0:

        await message.answer(
            "вќЊ Devor uzunligi 0 dan katta boвЂlishi kerak.\n\n"
            "Masalan: 10"
        )

        return

    if length > 10000:

        await message.answer(
            "вќЊ Juda katta qiymat kiritildi.\n\n"
            "Iltimos, devor uzunligini tekshiring."
        )

        return

    await state.update_data(
        wall_length=length
    )

    await state.set_state(
        BrickCalculator.height
    )

    await message.answer(
        f"вњ… Devor uzunligi: {length:g} m\n\n"
        "2пёЏвѓЈ Endi devor balandligini metrda kiriting.\n\n"
        "Masalan:\n"
        "3\n\n"
        "рџ“Њ Faqat son kiriting."
    )


# =========================================================
# 2-QADAM вЂ” DEVOR BALANDLIGI
# =========================================================

@dp.message(BrickCalculator.height)
async def brick_height_handler(
    message: Message,
    state: FSMContext
):

    if not message.text:

        await message.answer(
            "вќЊ Iltimos, balandlikni son bilan kiriting.\n\n"
            "Masalan: 3"
        )

        return

    text = (
        message.text
        .strip()
        .replace(",", ".")
    )

    try:
        height = float(text)

    except ValueError:

        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n\n"
            "Devor balandligini metrda kiriting.\n\n"
            "Masalan:\n"
            "3\n"
            "3.2\n"
            "3.5"
        )

        return

    if height <= 0:

        await message.answer(
            "вќЊ Devor balandligi 0 dan katta boвЂlishi kerak.\n\n"
            "Masalan: 3"
        )

        return

    if height > 100:

        await message.answer(
            "вќЊ Juda katta qiymat kiritildi.\n\n"
            "Iltimos, devor balandligini tekshiring."
        )

        return

    await state.update_data(
        wall_height=height
    )

    await state.set_state(
        BrickCalculator.brick_size
    )

    brick_size_menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="250Г—120Г—65 mm"
                )
            ],
            [
                KeyboardButton(
                    text="250Г—120Г—88 mm"
                )
            ],
            [
                KeyboardButton(
                    text="250Г—120Г—138 mm"
                )
            ],
            [
                KeyboardButton(
                    text="Boshqa oвЂlcham"
                )
            ],
            [
                KeyboardButton(
                    text="в¬…пёЏ Orqaga"
                )
            ],
        ],
        resize_keyboard=True
    )

    await message.answer(
        f"вњ… Devor balandligi: {height:g} m\n\n"
        "3пёЏвѓЈ GвЂisht oвЂlchamini tanlang:\n\n"
        "рџ“Њ Kerakli standart oвЂlchamni belgilang.",
        reply_markup=brick_size_menu
    )


# =========================================================
# 3-QADAM вЂ” GвЂISHT OвЂLCHAMI
# =========================================================

@dp.message(BrickCalculator.brick_size)
async def brick_size_handler(
    message: Message,
    state: FSMContext
):

    if not message.text:

        await message.answer(
            "вќЊ GвЂisht oвЂlchamini tanlang."
        )

        return

    text = message.text.strip()

    brick_sizes = {

        "250Г—120Г—65 mm": {
            "length": 0.250,
            "width": 0.120,
            "height": 0.065,
            "name": "250Г—120Г—65 mm"
        },

        "250Г—120Г—88 mm": {
            "length": 0.250,
            "width": 0.120,
            "height": 0.088,
            "name": "250Г—120Г—88 mm"
        },

        "250Г—120Г—138 mm": {
            "length": 0.250,
            "width": 0.120,
            "height": 0.138,
            "name": "250Г—120Г—138 mm"
        }
    }

    # -----------------------------------------------------
    # BOSHQA OвЂLCHAM
    # -----------------------------------------------------

    if text == "Boshqa oвЂlcham":

        await message.answer(
            "рџ“Џ GвЂishtning oвЂlchamlarini millimetrda "
            "ketma-ket kiriting.\n\n"
            "Format:\n"
            "uzunlik kenglik balandlik\n\n"
            "Masalan:\n"
            "250 120 65"
        )

        return

    # -----------------------------------------------------
    # STANDART OвЂLCHAM
    # -----------------------------------------------------

    if text in brick_sizes:

        brick = brick_sizes[text]

        await state.update_data(
            brick_length=brick["length"],
            brick_width=brick["width"],
            brick_height=brick["height"],
            brick_name=brick["name"]
        )

        await state.set_state(
            BrickCalculator.thickness
        )

        thickness_menu = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text="0.5 gвЂisht"
                    )
                ],
                [
                    KeyboardButton(
                        text="1 gвЂisht"
                    )
                ],
                [
                    KeyboardButton(
                        text="1.5 gвЂisht"
                    )
                ],
                [
                    KeyboardButton(
                        text="2 gвЂisht"
                    )
                ],
                [
                    KeyboardButton(
                        text="в¬…пёЏ Orqaga"
                    )
                ],
            ],
            resize_keyboard=True
        )

        await message.answer(
            f"вњ… GвЂisht oвЂlchami: {brick['name']}\n\n"
            "4пёЏвѓЈ Devor qalinligini tanlang:",
            reply_markup=thickness_menu
        )

        return

    # -----------------------------------------------------
    # BOSHQA OвЂLCHAM вЂ” 3 TA SON
    # -----------------------------------------------------

    parts = (
        text
        .replace(",", ".")
        .split()
    )

    if len(parts) == 3:

        try:

            length_mm = float(parts[0])
            width_mm = float(parts[1])
            height_mm = float(parts[2])

        except ValueError:

            await message.answer(
                "вќЊ OвЂlcham notoвЂgвЂri.\n\n"
                "Masalan:\n"
                "250 120 65"
            )

            return

        if (
            length_mm <= 0
            or width_mm <= 0
            or height_mm <= 0
        ):

            await message.answer(
                "вќЊ GвЂisht oвЂlchamlari 0 dan katta "
                "boвЂlishi kerak."
            )

            return

        if (
            length_mm > 2000
            or width_mm > 2000
            or height_mm > 2000
        ):

            await message.answer(
                "вќЊ GвЂisht oвЂlchami juda katta.\n\n"
                "OвЂlchamlarni millimetrda tekshiring."
            )

            return

        await state.update_data(
            brick_length=length_mm / 1000,
            brick_width=width_mm / 1000,
            brick_height=height_mm / 1000,
            brick_name=(
                f"{length_mm:g}Г—"
                f"{width_mm:g}Г—"
                f"{height_mm:g} mm"
            )
        )

        await state.set_state(
            BrickCalculator.thickness
        )

        thickness_menu = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text="0.5 gвЂisht"
                    )
                ],
                [
                    KeyboardButton(
                        text="1 gвЂisht"
                    )
                ],
                [
                    KeyboardButton(
                        text="1.5 gвЂisht"
                    )
                ],
                [
                    KeyboardButton(
                        text="2 gвЂisht"
                    )
                ],
                [
                    KeyboardButton(
                        text="в¬…пёЏ Orqaga"
                    )
                ],
            ],
            resize_keyboard=True
        )

        await message.answer(
            f"вњ… GвЂisht oвЂlchami: "
            f"{length_mm:g}Г—"
            f"{width_mm:g}Г—"
            f"{height_mm:g} mm\n\n"
            "4пёЏвѓЈ Devor qalinligini tanlang:",
            reply_markup=thickness_menu
        )

        return

    await message.answer(
        "вќЊ GвЂisht oвЂlchami topilmadi.\n\n"
        "Standart oвЂlchamlardan birini tanlang yoki "
        "boshqa oвЂlcham uchun quyidagi formatda yozing:\n\n"
        "250 120 65"
    )


# =========================================================
# 4-QADAM вЂ” DEVOR QALINLIGI
# =========================================================

@dp.message(BrickCalculator.thickness)
async def brick_thickness_handler(
    message: Message,
    state: FSMContext
):

    if not message.text:

        await message.answer(
            "вќЊ Devor qalinligini tugmalardan tanlang."
        )

        return

    text = message.text.strip()

    thickness_values = {
        "0.5 gвЂisht": 0.5,
        "1 gвЂisht": 1.0,
        "1.5 gвЂisht": 1.5,
        "2 gвЂisht": 2.0
    }

    if text not in thickness_values:

        await message.answer(
            "вќЊ Devor qalinligini tugmalardan tanlang."
        )

        return

    wall_thickness = thickness_values[text]

    data = await state.get_data()

    required_keys = [
        "wall_length",
        "wall_height",
        "brick_length",
        "brick_width",
        "brick_height",
        "brick_name"
    ]

    for key in required_keys:

        if key not in data:

            await state.clear()

            await message.answer(
                "вќЊ Hisoblash maвЂ™lumotlarida xatolik yuz berdi.\n\n"
                "Iltimos, kalkulyatorni qaytadan boshlang.",
                reply_markup=calculator_menu()
            )

            return

    wall_length = data["wall_length"]
    wall_height = data["wall_height"]

    brick_length = data["brick_length"]
    brick_width = data["brick_width"]
    brick_height = data["brick_height"]

    brick_name = data["brick_name"]

    # -----------------------------------------------------
    # 10 MM QORISHMA
    # -----------------------------------------------------

    mortar = 0.010

    module_length = brick_length + mortar
    module_height = brick_height + mortar

    # -----------------------------------------------------
    # DEVOR QALINLIGI
    # -----------------------------------------------------

    thickness_map = {
        0.5: brick_width,
        1.0: brick_length,
        1.5: brick_length + brick_width,
        2.0: brick_length * 2
    }

    wall_thickness_m = thickness_map[wall_thickness]

    # -----------------------------------------------------
    # DEVOR MAYDONI
    # -----------------------------------------------------

    wall_area = (
        wall_length *
        wall_height
    )

    # -----------------------------------------------------
    # DEVOR HAJMI
    # -----------------------------------------------------

    wall_volume = (
        wall_area *
        wall_thickness_m
    )

    # -----------------------------------------------------
    # GвЂISHT MODULI HAJMI
    # -----------------------------------------------------

    brick_module_volume = (
        module_length *
        brick_width *
        module_height
    )

    # -----------------------------------------------------
    # GвЂISHT SONI
    # -----------------------------------------------------

    brick_count = (
        wall_volume /
        brick_module_volume
    )

    # -----------------------------------------------------
    # 5% ZAXIRA
    # -----------------------------------------------------

    waste_percent = 5

    reserve = (
        brick_count *
        waste_percent /
        100
    )

    # -----------------------------------------------------
    # JAMI
    # -----------------------------------------------------

    total_bricks = (
        brick_count +
        reserve
    )

    total_bricks_rounded = int(
        total_bricks + 0.999999
    )

    # -----------------------------------------------------
    # NATIJA
    # -----------------------------------------------------

    result = (
        "рџ§± GвЂISHT KALKULYATORI вЂ” NATIJA\n\n"

        f"рџ“Џ Devor uzunligi: "
        f"{wall_length:g} m\n"

        f"рџ“ђ Devor balandligi: "
        f"{wall_height:g} m\n"

        f"рџ“¦ GвЂisht oвЂlchami: "
        f"{brick_name}\n"

        f"рџ§± Devor qalinligi: "
        f"{wall_thickness:g} gвЂisht\n"

        f"рџ§± Hisobiy qalinlik: "
        f"{wall_thickness_m:.3f} m\n\n"

        f"рџ“ђ Devor maydoni: "
        f"{wall_area:.2f} mВІ\n"

        f"рџ“¦ Devor hajmi: "
        f"{wall_volume:.3f} mВі\n\n"

        f"рџ§± Asosiy gвЂisht miqdori: "
        f"{brick_count:,.0f} dona\n"

        f"вћ• 5% zaxira: "
        f"{reserve:,.0f} dona\n\n"

        f"вњ… JAMI: "
        f"{total_bricks_rounded:,} dona gвЂisht\n\n"

        "в„№пёЏ Hisoblashda 10 mm qorishma "
        "choklari hisobga olindi.\n"

        "в„№пёЏ 5% zaxira sinish va chiqindilar "
        "uchun qoвЂshildi."
    )

    await message.answer(
        result,
        reply_markup=calculator_menu()
    )

    await state.clear()

# =========================================================
# GAZOBLOK KALKULYATORI
# GвЂISHT KODIGA TEGILMAYDI
# =========================================================

class GazoblokCalculator(StatesGroup):
    length = State()
    height = State()
    openings = State()

    door_count = State()
    door_width = State()
    door_height = State()

    window_count = State()
    window_width = State()
    window_height = State()

    block_size = State()


# =========================================================
# GAZOBLOK вЂ” BOSHLASH
# =========================================================

@dp.message(F.text == "рџ§± Gazoblok")
async def gazoblok_start(
    message: Message,
    state: FSMContext
):
    await state.clear()
    await state.set_state(GazoblokCalculator.length)

    await message.answer(
        "рџ§± GAZOBLOK KALKULYATORI\n\n"
        "1пёЏвѓЈ Devor uzunligini kiriting.\n\n"
        "Masalan:\n"
        "10\n"
        "10.5 m\n"
        "1050 cm"
    )


# =========================================================
# DEVOR UZUNLIGI
# =========================================================

@dp.message(GazoblokCalculator.length)
async def gazoblok_length(
    message: Message,
    state: FSMContext
):
    try:
        text = message.text.lower().replace(",", ".").strip()

        if text.endswith("cm"):
            length = float(text[:-2].strip()) / 100
        elif text.endswith("mm"):
            length = float(text[:-2].strip()) / 1000
        elif text.endswith("m"):
            length = float(text[:-1].strip())
        else:
            length = float(text)

        if length <= 0:
            raise ValueError

    except ValueError:
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n\n"
            "Masalan: 10 m yoki 1000 cm"
        )
        return

    await state.update_data(length=length)
    await state.set_state(GazoblokCalculator.height)

    await message.answer(
        "рџ“Џ Endi devor balandligini kiriting.\n\n"
        "Masalan: 3 m"
    )


# =========================================================
# DEVOR BALANDLIGI
# =========================================================

@dp.message(GazoblokCalculator.height)
async def gazoblok_height(
    message: Message,
    state: FSMContext
):
    try:
        text = message.text.lower().replace(",", ".").strip()

        if text.endswith("cm"):
            height = float(text[:-2].strip()) / 100
        elif text.endswith("mm"):
            height = float(text[:-2].strip()) / 1000
        elif text.endswith("m"):
            height = float(text[:-1].strip())
        else:
            height = float(text)

        if height <= 0:
            raise ValueError

    except ValueError:
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n\n"
            "Masalan: 3 m"
        )
        return

    await state.update_data(height=height)
    await state.set_state(GazoblokCalculator.openings)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="рџљЄ Eshik/deraza bor"),
                KeyboardButton(text="вќЊ YoвЂq")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "рџЄџ Devorda eshik yoki deraza bormi?",
        reply_markup=keyboard
    )


# =========================================================
# OCHIQ JOYLAR
# =========================================================

@dp.message(GazoblokCalculator.openings, F.text == "вќЊ YoвЂq")
async def gazoblok_no_openings(
    message: Message,
    state: FSMContext
):
    await state.update_data(
        door_area=0,
        window_area=0
    )

    await gazoblok_show_sizes(message, state)


@dp.message(GazoblokCalculator.openings, F.text == "рџљЄ Eshik/deraza bor")
async def gazoblok_has_openings(
    message: Message,
    state: FSMContext
):
    await state.set_state(GazoblokCalculator.door_count)

    await message.answer(
        "рџљЄ Eshiklar sonini kiriting.\n\n"
        "Agar eshik boвЂlmasa: 0"
    )


# =========================================================
# ESHIK SONI
# =========================================================

@dp.message(GazoblokCalculator.door_count)
async def gazoblok_door_count(
    message: Message,
    state: FSMContext
):
    try:
        count = int(message.text.strip())

        if count < 0:
            raise ValueError

    except ValueError:
        await message.answer("вќЊ Butun son kiriting. Masalan: 2")
        return

    await state.update_data(door_count=count)

    if count == 0:
        await state.update_data(door_area=0)
        await state.set_state(GazoblokCalculator.window_count)

        await message.answer(
            "рџЄџ Derazalar sonini kiriting.\n\n"
            "Agar deraza boвЂlmasa: 0"
        )
    else:
        await state.set_state(GazoblokCalculator.door_width)

        await message.answer(
            "рџљЄ Eshik kengligini kiriting.\n\n"
            "Masalan: 0.9 m"
        )


# =========================================================
# ESHIK KENGLIGI
# =========================================================

@dp.message(GazoblokCalculator.door_width)
async def gazoblok_door_width(
    message: Message,
    state: FSMContext
):
    try:
        width = float(
            message.text.replace(",", ".").replace("m", "").strip()
        )

        if width <= 0:
            raise ValueError

    except ValueError:
        await message.answer("вќЊ Masalan: 0.9")
        return

    await state.update_data(door_width=width)
    await state.set_state(GazoblokCalculator.door_height)

    await message.answer(
        "рџљЄ Eshik balandligini kiriting.\n\n"
        "Masalan: 2.1 m"
    )


# =========================================================
# ESHIK BALANDLIGI
# =========================================================

@dp.message(GazoblokCalculator.door_height)
async def gazoblok_door_height(
    message: Message,
    state: FSMContext
):
    try:
        height = float(
            message.text.replace(",", ".").replace("m", "").strip()
        )

        if height <= 0:
            raise ValueError

    except ValueError:
        await message.answer("вќЊ Masalan: 2.1")
        return

    data = await state.get_data()

    door_area = (
        data["door_count"]
        * data["door_width"]
        * height
    )

    await state.update_data(door_area=door_area)
    await state.set_state(GazoblokCalculator.window_count)

    await message.answer(
        "рџЄџ Derazalar sonini kiriting.\n\n"
        "Agar deraza boвЂlmasa: 0"
    )


# =========================================================
# DERAZA SONI
# =========================================================

@dp.message(GazoblokCalculator.window_count)
async def gazoblok_window_count(
    message: Message,
    state: FSMContext
):
    try:
        count = int(message.text.strip())

        if count < 0:
            raise ValueError

    except ValueError:
        await message.answer("вќЊ Butun son kiriting. Masalan: 4")
        return

    await state.update_data(window_count=count)

    if count == 0:
        await state.update_data(window_area=0)
        await gazoblok_show_sizes(message, state)
    else:
        await state.set_state(GazoblokCalculator.window_width)

        await message.answer(
            "рџЄџ Deraza kengligini kiriting.\n\n"
            "Masalan: 1.5 m"
        )


# =========================================================
# DERAZA KENGLIGI
# =========================================================

@dp.message(GazoblokCalculator.window_width)
async def gazoblok_window_width(
    message: Message,
    state: FSMContext
):
    try:
        width = float(
            message.text.replace(",", ".").replace("m", "").strip()
        )

        if width <= 0:
            raise ValueError

    except ValueError:
        await message.answer("вќЊ Masalan: 1.5")
        return

    await state.update_data(window_width=width)
    await state.set_state(GazoblokCalculator.window_height)

    await message.answer(
        "рџЄџ Deraza balandligini kiriting.\n\n"
        "Masalan: 1.5 m"
    )


# =========================================================
# DERAZA BALANDLIGI
# =========================================================

@dp.message(GazoblokCalculator.window_height)
async def gazoblok_window_height(
    message: Message,
    state: FSMContext
):
    try:
        height = float(
            message.text.replace(",", ".").replace("m", "").strip()
        )

        if height <= 0:
            raise ValueError

    except ValueError:
        await message.answer("вќЊ Masalan: 1.5")
        return

    data = await state.get_data()

    window_area = (
        data["window_count"]
        * data["window_width"]
        * height
    )

    await state.update_data(window_area=window_area)

    await gazoblok_show_sizes(message, state)


# =========================================================
# GAZOBLOK OвЂLCHAMLARI
# =========================================================

async def gazoblok_show_sizes(
    message: Message,
    state: FSMContext
):
    await state.set_state(GazoblokCalculator.block_size)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="625Г—250Г—100 mm"),
                KeyboardButton(text="625Г—250Г—125 mm")
            ],
            [
                KeyboardButton(text="625Г—250Г—150 mm"),
                KeyboardButton(text="625Г—250Г—200 mm")
            ],
            [
                KeyboardButton(text="625Г—250Г—250 mm"),
                KeyboardButton(text="625Г—250Г—300 mm")
            ],
            [
                KeyboardButton(text="625Г—250Г—350 mm"),
                KeyboardButton(text="вњЏпёЏ Maxsus oвЂlcham")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "рџ§± Gazoblok oвЂlchamini tanlang:",
        reply_markup=keyboard
    )


# =========================================================
# GAZOBLOK HISOBLASH
# =========================================================

@dp.message(GazoblokCalculator.block_size)
async def gazoblok_calculate(
    message: Message,
    state: FSMContext
):
    text = message.text.strip()

    sizes = {
        "625Г—250Г—100 mm": (625, 250, 100),
        "625Г—250Г—125 mm": (625, 250, 125),
        "625Г—250Г—150 mm": (625, 250, 150),
        "625Г—250Г—200 mm": (625, 250, 200),
        "625Г—250Г—250 mm": (625, 250, 250),
        "625Г—250Г—300 mm": (625, 250, 300),
        "625Г—250Г—350 mm": (625, 250, 350),
    }

    if text == "вњЏпёЏ Maxsus oвЂlcham":
        await message.answer(
            "вњЏпёЏ Maxsus oвЂlchamni quyidagi koвЂrinishda kiriting:\n\n"
            "Masalan:\n"
            "625x250x200"
        )
        return

    if text not in sizes:
        await message.answer(
            "вќЊ Iltimos, roвЂyxatdan gazoblok oвЂlchamini tanlang."
        )
        return

    block_length, block_height, block_width = sizes[text]

    data = await state.get_data()

    wall_area = data["length"] * data["height"]

    opening_area = (
        data.get("door_area", 0)
        + data.get("window_area", 0)
    )

    useful_area = wall_area - opening_area

    if useful_area <= 0:
        await message.answer(
            "вќЊ Eshik va deraza maydoni devor maydonidan katta boвЂlishi mumkin emas."
        )
        await state.clear()
        return

    # Blokning devor yuzasiga tushadigan oвЂlchami:
    block_face_area = (
        (block_length / 1000)
        * (block_height / 1000)
    )

    basic_quantity = useful_area / block_face_area

    reserve = basic_quantity * 0.05
    total_quantity = basic_quantity + reserve

    await message.answer(
        "рџ§± GAZOBLOK HISOB-KITOBI\n\n"
        f"рџ“Џ Devor uzunligi: {data['length']:.2f} m\n"
        f"рџ“ђ Devor balandligi: {data['height']:.2f} m\n"
        f"рџ§± Blok oвЂlchami: {block_length}Г—{block_height}Г—{block_width} mm\n\n"
        f"рџ“ђ Devor maydoni: {wall_area:.2f} mВІ\n"
        f"рџљЄ Eshik/deraza maydoni: {opening_area:.2f} mВІ\n"
        f"рџ“ђ Sof devor maydoni: {useful_area:.2f} mВІ\n\n"
        f"рџ§± Asosiy miqdor: {basic_quantity:.0f} dona\n"
        f"вћ• 5% zaxira: {reserve:.0f} dona\n\n"
        f"вњ… KERAKLI GAZOBLOK: {total_quantity:.0f} DONA",
        reply_markup=calculator_menu()
    )

    await state.clear()

# =========================================================
# SHLAKOBLOK KALKULYATORI
# GвЂISHT VA GAZOBLOK KODIGA TEGILMAYDI
# =========================================================

class ShlakoblokCalculator(StatesGroup):
    length = State()
    height = State()
    openings = State()

    door_count = State()
    door_width = State()
    door_height = State()

    window_count = State()
    window_width = State()
    window_height = State()

    block_size = State()
    custom_size = State()


# =========================================================
# SHLAKOBLOK вЂ” BOSHLASH
# =========================================================

@dp.message(F.text == "рџЄЁ Shlakoblok")
async def shlakoblok_start(
    message: Message,
    state: FSMContext
):
    await state.clear()
    await state.set_state(ShlakoblokCalculator.length)

    await message.answer(
        "рџЄЁ SHLAKOBLOK KALKULYATORI\n\n"
        "рџ“Џ Devor uzunligini kiriting.\n\n"
        "Masalan:\n"
        "10\n"
        "10.5 m\n"
        "1050 cm"
    )


# =========================================================
# OвЂLCHOVNI QABUL QILISH
# =========================================================

def parse_shlak_measurement(text: str):
    text = text.lower().replace(",", ".").strip()

    if text.endswith("mm"):
        return float(text[:-2].strip()) / 1000

    if text.endswith("cm"):
        return float(text[:-2].strip()) / 100

    if text.endswith("m"):
        return float(text[:-1].strip())

    return float(text)


# =========================================================
# DEVOR UZUNLIGI
# =========================================================

@dp.message(ShlakoblokCalculator.length)
async def shlakoblok_length(
    message: Message,
    state: FSMContext
):
    try:
        length = parse_shlak_measurement(message.text)

        if length <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n\n"
            "Masalan: 10 m yoki 1000 cm"
        )
        return

    await state.update_data(length=length)
    await state.set_state(ShlakoblokCalculator.height)

    await message.answer(
        "рџ“ђ Endi devor balandligini kiriting.\n\n"
        "Masalan: 3 m"
    )


# =========================================================
# DEVOR BALANDLIGI
# =========================================================

@dp.message(ShlakoblokCalculator.height)
async def shlakoblok_height(
    message: Message,
    state: FSMContext
):
    try:
        height = parse_shlak_measurement(message.text)

        if height <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n\n"
            "Masalan: 3 m"
        )
        return

    await state.update_data(height=height)
    await state.set_state(ShlakoblokCalculator.openings)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="рџљЄ Eshik/deraza bor"),
                KeyboardButton(text="вќЊ YoвЂq")
            ],
            [
                KeyboardButton(text="в¬…пёЏ Ortga")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "рџЄџ Devorda eshik yoki deraza bormi?",
        reply_markup=keyboard
    )


# =========================================================
# OCHIQ JOYLAR YOвЂQ
# =========================================================

@dp.message(
    ShlakoblokCalculator.openings,
    F.text == "вќЊ YoвЂq"
)
async def shlakoblok_no_openings(
    message: Message,
    state: FSMContext
):
    await state.update_data(
        door_area=0,
        window_area=0
    )

    await shlakoblok_show_sizes(message, state)


# =========================================================
# OCHIQ JOYLAR BOR
# =========================================================

@dp.message(
    ShlakoblokCalculator.openings,
    F.text == "рџљЄ Eshik/deraza bor"
)
async def shlakoblok_has_openings(
    message: Message,
    state: FSMContext
):
    await state.set_state(ShlakoblokCalculator.door_count)

    await message.answer(
        "рџљЄ Eshiklar sonini kiriting.\n\n"
        "Agar eshik boвЂlmasa: 0"
    )


# =========================================================
# ESHIK SONI
# =========================================================

@dp.message(ShlakoblokCalculator.door_count)
async def shlakoblok_door_count(
    message: Message,
    state: FSMContext
):
    try:
        count = int(message.text.strip())

        if count < 0:
            raise ValueError

    except ValueError:
        await message.answer(
            "вќЊ Butun son kiriting.\n"
            "Masalan: 2"
        )
        return

    await state.update_data(door_count=count)

    if count == 0:
        await state.update_data(door_area=0)
        await state.set_state(
            ShlakoblokCalculator.window_count
        )

        await message.answer(
            "рџЄџ Derazalar sonini kiriting.\n\n"
            "Agar deraza boвЂlmasa: 0"
        )
    else:
        await state.set_state(
            ShlakoblokCalculator.door_width
        )

        await message.answer(
            "рџљЄ Eshik kengligini kiriting.\n\n"
            "Masalan: 0.9 m"
        )


# =========================================================
# ESHIK KENGLIGI
# =========================================================

@dp.message(ShlakoblokCalculator.door_width)
async def shlakoblok_door_width(
    message: Message,
    state: FSMContext
):
    try:
        width = parse_shlak_measurement(message.text)

        if width <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ Masalan: 0.9 m"
        )
        return

    await state.update_data(door_width=width)
    await state.set_state(
        ShlakoblokCalculator.door_height
    )

    await message.answer(
        "рџљЄ Eshik balandligini kiriting.\n\n"
        "Masalan: 2.1 m"
    )


# =========================================================
# ESHIK BALANDLIGI
# =========================================================

@dp.message(ShlakoblokCalculator.door_height)
async def shlakoblok_door_height(
    message: Message,
    state: FSMContext
):
    try:
        height = parse_shlak_measurement(message.text)

        if height <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ Masalan: 2.1 m"
        )
        return

    data = await state.get_data()

    door_area = (
        data["door_count"]
        * data["door_width"]
        * height
    )

    await state.update_data(
        door_area=door_area
    )

    await state.set_state(
        ShlakoblokCalculator.window_count
    )

    await message.answer(
        "рџЄџ Derazalar sonini kiriting.\n\n"
        "Agar deraza boвЂlmasa: 0"
    )


# =========================================================
# DERAZA SONI
# =========================================================

@dp.message(ShlakoblokCalculator.window_count)
async def shlakoblok_window_count(
    message: Message,
    state: FSMContext
):
    try:
        count = int(message.text.strip())

        if count < 0:
            raise ValueError

    except ValueError:
        await message.answer(
            "вќЊ Butun son kiriting.\n"
            "Masalan: 4"
        )
        return

    await state.update_data(window_count=count)

    if count == 0:
        await state.update_data(window_area=0)
        await shlakoblok_show_sizes(message, state)
    else:
        await state.set_state(
            ShlakoblokCalculator.window_width
        )

        await message.answer(
            "рџЄџ Deraza kengligini kiriting.\n\n"
            "Masalan: 1.5 m"
        )


# =========================================================
# DERAZA KENGLIGI
# =========================================================

@dp.message(ShlakoblokCalculator.window_width)
async def shlakoblok_window_width(
    message: Message,
    state: FSMContext
):
    try:
        width = parse_shlak_measurement(message.text)

        if width <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ Masalan: 1.5 m"
        )
        return

    await state.update_data(
        window_width=width
    )

    await state.set_state(
        ShlakoblokCalculator.window_height
    )

    await message.answer(
        "рџЄџ Deraza balandligini kiriting.\n\n"
        "Masalan: 1.5 m"
    )


# =========================================================
# DERAZA BALANDLIGI
# =========================================================

@dp.message(ShlakoblokCalculator.window_height)
async def shlakoblok_window_height(
    message: Message,
    state: FSMContext
):
    try:
        height = parse_shlak_measurement(message.text)

        if height <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ Masalan: 1.5 m"
        )
        return

    data = await state.get_data()

    window_area = (
        data["window_count"]
        * data["window_width"]
        * height
    )

    await state.update_data(
        window_area=window_area
    )

    await shlakoblok_show_sizes(message, state)


# =========================================================
# SHLAKOBLOK OвЂLCHAM MENYUSI
# =========================================================

async def shlakoblok_show_sizes(
    message: Message,
    state: FSMContext
):
    await state.set_state(
        ShlakoblokCalculator.block_size
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="390Г—190Г—188 mm"
                ),
                KeyboardButton(
                    text="390Г—190Г—90 mm"
                )
            ],
            [
                KeyboardButton(
                    text="вњЏпёЏ Maxsus oвЂlcham"
                )
            ],
            [
                KeyboardButton(
                    text="в¬…пёЏ Ortga"
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "рџЄЁ SHLAKOBLOK OвЂLCHAMINI TANLANG:\n\n"
        "в„№пёЏ KoвЂrsatilgan oвЂlchamlar amaliy "
        "standart variantlar sifatida berilgan.",
        reply_markup=keyboard
    )


# =========================================================
# SHLAKOBLOK вЂ” STANDART OвЂLCHAM
# =========================================================

@dp.message(
    ShlakoblokCalculator.block_size,
    F.text == "390Г—190Г—188 mm"
)
async def shlakoblok_standard_1(
    message: Message,
    state: FSMContext
):
    await shlakoblok_calculate_result(
        message,
        state,
        390,
        190,
        188
    )


# =========================================================
# SHLAKOBLOK вЂ” YARIM BLOK
# =========================================================

@dp.message(
    ShlakoblokCalculator.block_size,
    F.text == "390Г—190Г—90 mm"
)
async def shlakoblok_standard_2(
    message: Message,
    state: FSMContext
):
    await shlakoblok_calculate_result(
        message,
        state,
        390,
        190,
        90
    )


# =========================================================
# MAXSUS OвЂLCHAM
# =========================================================

@dp.message(
    ShlakoblokCalculator.block_size,
    F.text == "вњЏпёЏ Maxsus oвЂlcham"
)
async def shlakoblok_custom_size(
    message: Message,
    state: FSMContext
):
    await state.set_state(
        ShlakoblokCalculator.custom_size
    )

    await message.answer(
        "вњЏпёЏ Maxsus shlakoblok oвЂlchamini kiriting.\n\n"
        "Format:\n"
        "uzunlik Г— balandlik Г— qalinlik\n\n"
        "Masalan:\n"
        "390x190x188"
    )


# =========================================================
# MAXSUS OвЂLCHAMNI QABUL QILISH
# =========================================================

@dp.message(ShlakoblokCalculator.custom_size)
async def shlakoblok_custom_size_input(
    message: Message,
    state: FSMContext
):
    try:
        text = (
            message.text
            .lower()
            .replace(" ", "")
            .replace("Г—", "x")
        )

        parts = text.split("x")

        if len(parts) != 3:
            raise ValueError

        block_length = float(parts[0])
        block_height = float(parts[1])
        block_width = float(parts[2])

        if (
            block_length <= 0
            or block_height <= 0
            or block_width <= 0
        ):
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ OвЂlcham notoвЂgвЂri.\n\n"
            "Masalan:\n"
            "390x190x188"
        )
        return

    await shlakoblok_calculate_result(
        message,
        state,
        block_length,
        block_height,
        block_width
    )


# =========================================================
# SHLAKOBLOK вЂ” HISOBLASH
# =========================================================

async def shlakoblok_calculate_result(
    message: Message,
    state: FSMContext,
    block_length,
    block_height,
    block_width
):
    data = await state.get_data()

    wall_area = (
        data["length"]
        * data["height"]
    )

    opening_area = (
        data.get("door_area", 0)
        + data.get("window_area", 0)
    )

    useful_area = wall_area - opening_area

    if useful_area <= 0:
        await message.answer(
            "вќЊ Eshik va deraza maydoni "
            "devor maydonidan katta boвЂlishi mumkin emas.",
            reply_markup=calculator_menu()
        )
        await state.clear()
        return

    # Blokning devor yuzasiga tushadigan maydoni
    block_face_area = (
        (block_length / 1000)
        * (block_height / 1000)
    )

    basic_quantity = (
        useful_area / block_face_area
    )

    reserve = basic_quantity * 0.05

    total_quantity = (
        basic_quantity + reserve
    )

    total_quantity_rounded = int(
        total_quantity + 0.999999
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="рџ”„ Qayta hisoblash"
                )
            ],
            [
                KeyboardButton(
                    text="в¬…пёЏ Ortga"
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "рџЄЁ SHLAKOBLOK HISOB-KITOBI\n\n"

        f"рџ“Џ Devor uzunligi: "
        f"{data['length']:.2f} m\n"

        f"рџ“ђ Devor balandligi: "
        f"{data['height']:.2f} m\n"

        f"рџЄЁ Blok oвЂlchami: "
        f"{block_length:g}Г—"
        f"{block_height:g}Г—"
        f"{block_width:g} mm\n\n"

        f"рџ“ђ Umumiy devor maydoni: "
        f"{wall_area:.2f} mВІ\n"

        f"рџљЄ Eshik/deraza maydoni: "
        f"{opening_area:.2f} mВІ\n"

        f"рџ“ђ Sof devor maydoni: "
        f"{useful_area:.2f} mВІ\n\n"

        f"рџЄЁ Asosiy miqdor: "
        f"{basic_quantity:.0f} dona\n"

        f"вћ• 5% zaxira: "
        f"{reserve:.0f} dona\n\n"

        f"вњ… KERAKLI SHLAKOBLOK:\n"
        f"рџЄЁ {total_quantity_rounded} DONA",

        reply_markup=keyboard
    )

    await state.clear()


# =========================================================
# SHLAKOBLOK вЂ” QAYTA HISOBLASH
# =========================================================

@dp.message(F.text == "рџ”„ Qayta hisoblash")
async def shlakoblok_recalculate(
    message: Message,
    state: FSMContext
):
    await shlakoblok_start(message, state)


# =========================================================
# SHLAKOBLOK вЂ” ORTGA
# =========================================================

@dp.message(
    F.text == "в¬…пёЏ Ortga"
)
async def shlakoblok_back(
    message: Message,
    state: FSMContext
):
    await state.clear()

    await message.answer(
        "рџ§® ARCHHELP KALKULYATOR\n\n"
        "Kerakli kalkulyatorni tanlang:",
        reply_markup=calculator_menu()
    )

# =========================================================
# BETON KALKULYATORI
# GвЂISHT / GAZOBLOK / SHLAKOBLOK KODIGA TEGILMAYDI
# =========================================================

class BetonCalculator(StatesGroup):
    length = State()
    width = State()
    height = State()


# =========================================================
# BETON вЂ” BOSHLASH
# =========================================================

@dp.message(F.text == "рџЏ  Beton")
async def beton_start(
    message: Message,
    state: FSMContext
):
    await state.clear()
    await state.set_state(BetonCalculator.length)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="в¬…пёЏ Ortga")
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "рџЏ  BETON KALKULYATORI\n\n"
        "рџ§± Beton qalinligi: 400 mm (40 sm)\n\n"
        "рџ“Џ Xona uzunligini kiriting.\n\n"
        "Masalan: 4 m",
        reply_markup=keyboard
    )


# =========================================================
# XONA UZUNLIGI
# =========================================================

@dp.message(BetonCalculator.length)
async def beton_length(
    message: Message,
    state: FSMContext
):
    try:
        text = (
            message.text
            .lower()
            .replace(",", ".")
            .strip()
        )

        if text.endswith("mm"):
            length = float(text[:-2].strip()) / 1000
        elif text.endswith("cm"):
            length = float(text[:-2].strip()) / 100
        elif text.endswith("m"):
            length = float(text[:-1].strip())
        else:
            length = float(text)

        if length <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n\n"
            "Masalan: 4 m"
        )
        return

    await state.update_data(length=length)
    await state.set_state(BetonCalculator.width)

    await message.answer(
        "рџ“ђ Endi xona enini kiriting.\n\n"
        "Masalan: 3 m"
    )


# =========================================================
# XONA ENI
# =========================================================

@dp.message(BetonCalculator.width)
async def beton_width(
    message: Message,
    state: FSMContext
):
    try:
        text = (
            message.text
            .lower()
            .replace(",", ".")
            .strip()
        )

        if text.endswith("mm"):
            width = float(text[:-2].strip()) / 1000
        elif text.endswith("cm"):
            width = float(text[:-2].strip()) / 100
        elif text.endswith("m"):
            width = float(text[:-1].strip())
        else:
            width = float(text)

        if width <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n\n"
            "Masalan: 3 m"
        )
        return

    await state.update_data(width=width)
    await state.set_state(BetonCalculator.height)

    await message.answer(
        "рџ“Џ Endi beton balandligini kiriting.\n\n"
        "Masalan: 2 m"
    )


# =========================================================
# BETON BALANDLIGI VA HISOBLASH
# =========================================================

@dp.message(BetonCalculator.height)
async def beton_height(
    message: Message,
    state: FSMContext
):
    try:
        text = (
            message.text
            .lower()
            .replace(",", ".")
            .strip()
        )

        if text.endswith("mm"):
            height = float(text[:-2].strip()) / 1000
        elif text.endswith("cm"):
            height = float(text[:-2].strip()) / 100
        elif text.endswith("m"):
            height = float(text[:-1].strip())
        else:
            height = float(text)

        if height <= 0:
            raise ValueError

    except (ValueError, TypeError):
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n\n"
            "Masalan: 2 m"
        )
        return

    data = await state.get_data()

    length = data["length"]
    width = data["width"]

    # =====================================================
    # BETON STANDART QALINLIGI
    # =====================================================

    concrete_thickness = 0.4  # 400 mm = 40 sm

    # =====================================================
    # MUHIM:
    # FAQAT UZUN TOMON IKKI TOMONDAN 40 SM GA UZAYADI
    # ENI ESA OвЂZINING BERILGAN OвЂLCHAMIDA QOLADI
    # =====================================================

    calculated_length = (
        length + concrete_thickness + concrete_thickness
    )

    calculated_width = width

    # Xona maydoni
    room_area = (
        calculated_length * calculated_width
    )

    # Beton hajmi
    concrete_volume = (
        room_area * height
    )

    # 5% zaxira
    reserve = concrete_volume * 0.05

    total_concrete = (
        concrete_volume + reserve
    )

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="рџ”„ Qayta hisoblash"
                )
            ],
            [
                KeyboardButton(
                    text="в¬…пёЏ Ortga"
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "рџЏ  BETON HISOB-KITOBI\n\n"

        f"рџ“Џ Kiritilgan uzunlik: "
        f"{length:.2f} m\n"

        f"рџ“ђ Kiritilgan eni: "
        f"{width:.2f} m\n"

        f"рџ§± Beton qalinligi: "
        f"{concrete_thickness:.2f} m (400 mm)\n\n"

        f"рџ“Џ Hisobiy uzunlik: "
        f"{calculated_length:.2f} m\n"

        f"рџ“ђ Hisobiy eni: "
        f"{calculated_width:.2f} m\n\n"

        f"рџЏ  Xona maydoni: "
        f"{room_area:.2f} mВІ\n"

        f"рџ“Џ Beton balandligi: "
        f"{height:.2f} m\n\n"

        f"рџЏ— Asosiy beton hajmi: "
        f"{concrete_volume:.2f} mВі\n"

        f"вћ• 5% zaxira: "
        f"{reserve:.2f} mВі\n\n"

        f"вњ… KERAKLI BETON:\n"
        f"рџЏ— {total_concrete:.2f} mВі",

        reply_markup=keyboard
    )

    await state.clear()


# =========================================================
# BETON вЂ” QAYTA HISOBLASH
# =========================================================

@dp.message(F.text == "рџ”„ Qayta hisoblash")
async def beton_recalculate(
    message: Message,
    state: FSMContext
):
    await beton_start(message, state)


# =========================================================
# BETON вЂ” ORTGA
# =========================================================

@dp.message(F.text == "в¬…пёЏ Ortga")
async def beton_back(
    message: Message,
    state: FSMContext
):
    await state.clear()

    await message.answer(
        "рџ§® ARCHHELP KALKULYATOR\n\n"
        "Kerakli kalkulyatorni tanlang:",
        reply_markup=calculator_menu()
    )

# ============================================================
# рџ”© ARMATURA KALKULYATORI
# ============================================================

class ArmaturaCalculator(StatesGroup):
    element = State()

    # Plita
    slab_length = State()
    slab_width = State()
    slab_cover = State()
    slab_main_diameter = State()
    slab_main_spacing = State()
    slab_cross_diameter = State()
    slab_cross_spacing = State()

    # Setka
    mesh_length = State()
    mesh_width = State()
    mesh_cover = State()
    mesh_diameter = State()
    mesh_spacing = State()
    foundation_type = State()

    foundation_length = State()
    foundation_width = State()
    foundation_height = State()
    foundation_cover = State()

    foundation_main_diameter = State()
    foundation_main_count = State()

    foundation_cross_diameter = State()
    foundation_cross_spacing = State()

    foundation_quantity = State()

def armatura_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="рџЏ  Plita"),
                KeyboardButton(text="рџЏ— Poydevor")
            ],
            [
                KeyboardButton(text="рџ“ђ ToвЂsin"),
                KeyboardButton(text="рџЏ› Ustun")
            ],
            [
                KeyboardButton(text="рџ§± Devor"),
                KeyboardButton(text="рџ•ё Setka")
            ],
            [
                KeyboardButton(text="в¬…пёЏ Ortga")
            ]
        ],
        resize_keyboard=True
    )


def diameter_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Г8"),
                KeyboardButton(text="Г10"),
                KeyboardButton(text="Г12")
            ],
            [
                KeyboardButton(text="Г14"),
                KeyboardButton(text="Г16"),
                KeyboardButton(text="Г18")
            ],
            [
                KeyboardButton(text="Г20"),
                KeyboardButton(text="Г22"),
                KeyboardButton(text="Г25")
            ],
            [
                KeyboardButton(text="в¬…пёЏ Ortga")
            ]
        ],
        resize_keyboard=True
    )


def spacing_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="100 mm"),
                KeyboardButton(text="150 mm")
            ],
            [
                KeyboardButton(text="200 mm"),
                KeyboardButton(text="250 mm")
            ],
            [
                KeyboardButton(text="300 mm"),
                KeyboardButton(text="Maxsus")
            ],
            [
                KeyboardButton(text="в¬…пёЏ Ortga")
            ]
        ],
        resize_keyboard=True
    )


def parse_number(text: str):
    """
    4
    4.5
    4,5
    """
    try:
        return float(text.replace(",", ".").strip())
    except ValueError:
        return None


def parse_diameter(text: str):
    """
    Г12 -> 12
    """
    text = text.replace("Г", "").replace("Гё", "").strip()

    try:
        return float(text)
    except ValueError:
        return None


def parse_spacing(text: str):
    """
    150 mm -> 150
    200 mm -> 200
    """
    text = text.lower().replace("mm", "").strip()

    try:
        return float(text)
    except ValueError:
        return None


def rebar_weight_per_meter(diameter_mm: float):
    """
    Armatura nazariy massasi:
    dВІ / 162 kg/m
    """
    return (diameter_mm ** 2) / 162


# ------------------------------------------------------------
# ARMATURA ASOSIY MENYU
# ------------------------------------------------------------

@dp.message(F.text == "рџ”© Armatura")
async def armatura_handler(
    message: Message,
    state: FSMContext
):
    await state.clear()

    await message.answer(
        "рџ”© ARMATURA KALKULYATORI\n\n"
        "Konstruksiya turini tanlang:",
        reply_markup=armatura_menu()
    )


# ------------------------------------------------------------
# PLITA
# ------------------------------------------------------------

@dp.message(F.text == "рџЏ  Plita")
async def armatura_slab_start(
    message: Message,
    state: FSMContext
):
    await state.clear()

    await state.set_state(ArmaturaCalculator.slab_length)

    await message.answer(
        "рџЏ  PLITA ARMATURA HISOBI\n\n"
        "1пёЏвѓЈ Plita uzunligini kiriting.\n\n"
        "Masalan: 6 m"
    )


@dp.message(ArmaturaCalculator.slab_length)
async def armatura_slab_length(
    message: Message,
    state: FSMContext
):
    value = parse_number(message.text)

    if value is None or value <= 0:
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n"
            "Masalan: 6 yoki 6.5"
        )
        return

    await state.update_data(slab_length=value)
    await state.set_state(ArmaturaCalculator.slab_width)

    await message.answer(
        "2пёЏвѓЈ Plita kengligini kiriting.\n\n"
        "Masalan: 4 m"
    )


@dp.message(ArmaturaCalculator.slab_width)
async def armatura_slab_width(
    message: Message,
    state: FSMContext
):
    value = parse_number(message.text)

    if value is None or value <= 0:
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n"
            "Masalan: 4 yoki 4.5"
        )
        return

    await state.update_data(slab_width=value)
    await state.set_state(ArmaturaCalculator.slab_cover)

    await message.answer(
        "3пёЏвѓЈ Himoya qatlamini kiriting (mm).\n\n"
        "Masalan: 20"
    )


@dp.message(ArmaturaCalculator.slab_cover)
async def armatura_slab_cover(
    message: Message,
    state: FSMContext
):
    value = parse_number(message.text)

    if value is None or value < 0:
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n"
            "Masalan: 20"
        )
        return

    await state.update_data(slab_cover=value)
    await state.set_state(ArmaturaCalculator.slab_main_diameter)

    await message.answer(
        "4пёЏвѓЈ Asosiy armatura diametrini tanlang:",
        reply_markup=diameter_menu()
    )


@dp.message(ArmaturaCalculator.slab_main_diameter)
async def armatura_slab_main_diameter(
    message: Message,
    state: FSMContext
):
    diameter = parse_diameter(message.text)

    if diameter is None or diameter <= 0:
        await message.answer(
            "вќЊ Diametrni tanlang.",
            reply_markup=diameter_menu()
        )
        return

    await state.update_data(slab_main_diameter=diameter)
    await state.set_state(ArmaturaCalculator.slab_main_spacing)

    await message.answer(
        "5пёЏвѓЈ Asosiy armatura qadamini tanlang:",
        reply_markup=spacing_menu()
    )


@dp.message(ArmaturaCalculator.slab_main_spacing)
async def armatura_slab_main_spacing(
    message: Message,
    state: FSMContext
):
    spacing = parse_spacing(message.text)

    if spacing is None or spacing <= 0:
        await message.answer(
            "вќЊ Qadamni tanlang.",
            reply_markup=spacing_menu()
        )
        return

    await state.update_data(slab_main_spacing=spacing)
    await state.set_state(ArmaturaCalculator.slab_cross_diameter)

    await message.answer(
        "6пёЏвѓЈ KoвЂndalang armatura diametrini tanlang:",
        reply_markup=diameter_menu()
    )


@dp.message(ArmaturaCalculator.slab_cross_diameter)
async def armatura_slab_cross_diameter(
    message: Message,
    state: FSMContext
):
    diameter = parse_diameter(message.text)

    if diameter is None or diameter <= 0:
        await message.answer(
            "вќЊ Diametrni tanlang.",
            reply_markup=diameter_menu()
        )
        return

    await state.update_data(slab_cross_diameter=diameter)
    await state.set_state(ArmaturaCalculator.slab_cross_spacing)

    await message.answer(
        "7пёЏвѓЈ KoвЂndalang armatura qadamini tanlang:",
        reply_markup=spacing_menu()
    )


@dp.message(ArmaturaCalculator.slab_cross_spacing)
async def armatura_slab_cross_spacing(
    message: Message,
    state: FSMContext
):
    spacing = parse_spacing(message.text)

    if spacing is None or spacing <= 0:
        await message.answer(
            "вќЊ Qadamni tanlang.",
            reply_markup=spacing_menu()
        )
        return

    data = await state.get_data()

    length = data["slab_length"]
    width = data["slab_width"]
    cover = data["slab_cover"]

    main_d = data["slab_main_diameter"]
    main_spacing = data["slab_main_spacing"]

    cross_d = data["slab_cross_diameter"]
    cross_spacing = spacing

    # Himoya qatlamidan keyingi ishchi o'lchamlar
    clear_length_mm = (length * 1000) - (2 * cover)
    clear_width_mm = (width * 1000) - (2 * cover)

    if clear_length_mm <= 0 or clear_width_mm <= 0:
        await message.answer(
            "вќЊ Himoya qatlami plita oвЂlchamiga nisbatan juda katta."
        )
        await state.clear()
        return

    # --------------------------------------------------------
    # ASOSIY ARMATURA
    # Sterjenlar plita kengligi bo'ylab joylashadi.
    # Har bir sterjen uzunligi = ishchi uzunlik.
    # --------------------------------------------------------

    main_count = math.ceil(
        clear_width_mm / main_spacing
    ) + 1

    main_length_each_m = clear_length_mm / 1000
    main_total_m = main_count * main_length_each_m

    # --------------------------------------------------------
    # KOвЂNDALANG ARMATURA
    # --------------------------------------------------------

    cross_count = math.ceil(
        clear_length_mm / cross_spacing
    ) + 1

    cross_length_each_m = clear_width_mm / 1000
    cross_total_m = cross_count * cross_length_each_m

    # --------------------------------------------------------
    # KG HISOBI
    # dВІ / 162
    # --------------------------------------------------------

    main_kg_per_m = rebar_weight_per_meter(main_d)
    cross_kg_per_m = rebar_weight_per_meter(cross_d)

    main_weight = main_total_m * main_kg_per_m
    cross_weight = cross_total_m * cross_kg_per_m

    total_m = main_total_m + cross_total_m
    total_weight = main_weight + cross_weight

    # 5% zaxira
    reserve_m = total_m * 0.05
    reserve_kg = total_weight * 0.05

    final_m = total_m + reserve_m
    final_weight = total_weight + reserve_kg

    await message.answer(
        "вњ… PLITA ARMATURA HISOBI\n\n"

        f"рџ“ђ Plita: {length:.2f} Г— {width:.2f} m\n"
        f"рџ›Ў Himoya qatlami: {cover:.0f} mm\n\n"

        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"
        "рџ”№ ASOSIY ARMATURA\n"
        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"

        f"Г{main_d:.0f} вЂ” {main_spacing:.0f} mm qadam\n"
        f"рџ“Њ Sterjenlar soni: {main_count} dona\n"
        f"рџ“Џ Har biri: {main_length_each_m:.2f} m\n"
        f"рџ“ђ Jami: {main_total_m:.2f} m\n"
        f"вљ–пёЏ OgвЂirligi: {main_weight:.2f} kg\n\n"

        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"
        "рџ”№ KOвЂNDALANG ARMATURA\n"
        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"

        f"Г{cross_d:.0f} вЂ” {cross_spacing:.0f} mm qadam\n"
        f"рџ“Њ Sterjenlar soni: {cross_count} dona\n"
        f"рџ“Џ Har biri: {cross_length_each_m:.2f} m\n"
        f"рџ“ђ Jami: {cross_total_m:.2f} m\n"
        f"вљ–пёЏ OgвЂirligi: {cross_weight:.2f} kg\n\n"

        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"
        "рџ“Љ YAKUNIY NATIJA\n"
        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"

        f"рџ“Џ Umumiy armatura: {total_m:.2f} m\n"
        f"вљ–пёЏ Umumiy ogвЂirlik: {total_weight:.2f} kg\n\n"

        f"вћ• 5% zaxira: {reserve_kg:.2f} kg\n\n"

        f"рџџў YAKUNIY: {final_weight:.2f} kg\n"
        f"рџџў Umumiy uzunlik: {final_m:.2f} m\n\n"

        "вљ пёЏ Eslatma:\n"
        "Bu hisob berilgan diametr va qadam boвЂyicha "
        "armatura miqdorini aniqlaydi. Diametr va qadamning "
        "konstruktiv jihatdan tanlanishi yuklar, beton klassi, "
        "konstruksiya turi va loyiha hisobiga bogвЂliq."
    )

    await state.clear()

    await message.answer(
        "рџ”© Yana hisoblash uchun tanlang:",
        reply_markup=armatura_menu()
    )


# ------------------------------------------------------------
# ARMATURA SETKASI
# ------------------------------------------------------------

@dp.message(F.text == "рџ•ё Setka")
async def armatura_mesh_start(
    message: Message,
    state: FSMContext
):
    await state.clear()

    await state.set_state(ArmaturaCalculator.mesh_length)

    await message.answer(
        "рџ•ё ARMATURA SETKASI HISOBI\n\n"
        "1пёЏвѓЈ Setka uzunligini kiriting.\n\n"
        "Masalan: 6 m"
    )


@dp.message(ArmaturaCalculator.mesh_length)
async def mesh_length(
    message: Message,
    state: FSMContext
):
    value = parse_number(message.text)

    if value is None or value <= 0:
        await message.answer("вќЊ Masalan: 6")
        return

    await state.update_data(mesh_length=value)
    await state.set_state(ArmaturaCalculator.mesh_width)

    await message.answer(
        "2пёЏвѓЈ Setka kengligini kiriting.\n\n"
        "Masalan: 4 m"
    )


@dp.message(ArmaturaCalculator.mesh_width)
async def mesh_width(
    message: Message,
    state: FSMContext
):
    value = parse_number(message.text)

    if value is None or value <= 0:
        await message.answer("вќЊ Masalan: 4")
        return

    await state.update_data(mesh_width=value)
    await state.set_state(ArmaturaCalculator.mesh_cover)

    await message.answer(
        "3пёЏвѓЈ Himoya qatlamini kiriting (mm).\n\n"
        "Masalan: 20"
    )


@dp.message(ArmaturaCalculator.mesh_cover)
async def mesh_cover(
    message: Message,
    state: FSMContext
):
    value = parse_number(message.text)

    if value is None or value < 0:
        await message.answer("вќЊ Masalan: 20")
        return

    await state.update_data(mesh_cover=value)
    await state.set_state(ArmaturaCalculator.mesh_diameter)

    await message.answer(
        "4пёЏвѓЈ Armatura diametrini tanlang:",
        reply_markup=diameter_menu()
    )


@dp.message(ArmaturaCalculator.mesh_diameter)
async def mesh_diameter(
    message: Message,
    state: FSMContext
):
    diameter = parse_diameter(message.text)

    if diameter is None or diameter <= 0:
        await message.answer(
            "вќЊ Diametrni tanlang.",
            reply_markup=diameter_menu()
        )
        return

    await state.update_data(mesh_diameter=diameter)
    await state.set_state(ArmaturaCalculator.mesh_spacing)

    await message.answer(
        "5пёЏвѓЈ Setka qadamini tanlang:",
        reply_markup=spacing_menu()
    )


@dp.message(ArmaturaCalculator.mesh_spacing)
async def mesh_spacing(
    message: Message,
    state: FSMContext
):
    spacing = parse_spacing(message.text)

    if spacing is None or spacing <= 0:
        await message.answer(
            "вќЊ Qadamni tanlang.",
            reply_markup=spacing_menu()
        )
        return

    data = await state.get_data()

    length = data["mesh_length"]
    width = data["mesh_width"]
    cover = data["mesh_cover"]
    diameter = data["mesh_diameter"]

    clear_length_mm = (length * 1000) - (2 * cover)
    clear_width_mm = (width * 1000) - (2 * cover)

    # 1-yo'nalish
    count_1 = math.ceil(clear_width_mm / spacing) + 1
    length_1 = clear_length_mm / 1000
    total_1 = count_1 * length_1

    # 2-yo'nalish
    count_2 = math.ceil(clear_length_mm / spacing) + 1
    length_2 = clear_width_mm / 1000
    total_2 = count_2 * length_2

    total_m = total_1 + total_2

    kg_per_m = rebar_weight_per_meter(diameter)
    total_weight = total_m * kg_per_m

    reserve_m = total_m * 0.05
    reserve_kg = total_weight * 0.05

    final_m = total_m + reserve_m
    final_weight = total_weight + reserve_kg

    await message.answer(
        "вњ… ARMATURA SETKASI HISOBI\n\n"

        f"рџ“ђ OвЂlcham: {length:.2f} Г— {width:.2f} m\n"
        f"рџ›Ў Himoya qatlami: {cover:.0f} mm\n"
        f"рџ”© Armatura: Г{diameter:.0f}\n"
        f"рџ“Џ Qadam: {spacing:.0f} mm\n\n"

        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"

        f"в†”пёЏ 1-yoвЂnalish: {count_1} dona Г— "
        f"{length_1:.2f} m = {total_1:.2f} m\n"

        f"в†•пёЏ 2-yoвЂnalish: {count_2} dona Г— "
        f"{length_2:.2f} m = {total_2:.2f} m\n\n"

        f"рџ“Џ Jami: {total_m:.2f} m\n"
        f"вљ–пёЏ OgвЂirligi: {total_weight:.2f} kg\n\n"

        f"вћ• 5% zaxira: {reserve_kg:.2f} kg\n\n"

        f"рџџў YAKUNIY: {final_weight:.2f} kg\n"
        f"рџџў Umumiy uzunlik: {final_m:.2f} m\n\n"

        "вљ пёЏ Eslatma:\n"
        "Hisob tanlangan diametr va qadam boвЂyicha "
        "material miqdorini aniqlaydi. Konstruktiv armatura "
        "diametri va qadami loyiha yuklamalari boвЂyicha "
        "alohida hisoblanadi."
    )

    await state.clear()

    await message.answer(
        "рџ”© Armatura menyusi:",
        reply_markup=armatura_menu()
    )


# ------------------------------------------------------------
# ARMATURA ORTGA
# ------------------------------------------------------------

@dp.message(
    ArmaturaCalculator.element,
    F.text == "в¬…пёЏ Ortga"
)
async def armatura_back(
    message: Message,
    state: FSMContext
):
    await state.clear()

    await message.answer(
        "рџ§® ARCHHELP KALKULYATOR\n\n"
        "Kerakli kalkulyatorni tanlang:",
        reply_markup=calculator_menu()
    )

# ============================================================
# рџЏ— POYDEVOR ARMATURA KALKULYATORI
# ============================================================

def foundation_type_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="рџ§± Lenta poydevor")],
            [KeyboardButton(text="в¬› Plita poydevor")],
            [KeyboardButton(text="рџџ« Alohida poydevor")],
            [KeyboardButton(text="рџЏ— Ustunli poydevor")],
            [KeyboardButton(text="рџЏў Monolit poydevor")],
            [KeyboardButton(text="в¬…пёЏ Ortga")]
        ],
        resize_keyboard=True
    )


def foundation_diameter_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Г8"),
                KeyboardButton(text="Г10"),
                KeyboardButton(text="Г12")
            ],
            [
                KeyboardButton(text="Г14"),
                KeyboardButton(text="Г16"),
                KeyboardButton(text="Г18")
            ],
            [
                KeyboardButton(text="Г20"),
                KeyboardButton(text="Г22"),
                KeyboardButton(text="Г25")
            ],
            [KeyboardButton(text="в¬…пёЏ Ortga")]
        ],
        resize_keyboard=True
    )


def foundation_spacing_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="100 mm"),
                KeyboardButton(text="150 mm")
            ],
            [
                KeyboardButton(text="200 mm"),
                KeyboardButton(text="250 mm")
            ],
            [
                KeyboardButton(text="300 mm"),
                KeyboardButton(text="Maxsus")
            ],
            [KeyboardButton(text="в¬…пёЏ Ortga")]
        ],
        resize_keyboard=True
    )


# ============================================================
# YORDAMCHI FUNKSIYALAR
# ============================================================

def foundation_parse_length(text):
    text = text.lower().strip().replace(",", ".")

    try:
        if text.endswith("mm"):
            return float(text[:-2].strip()) / 1000

        if text.endswith("cm"):
            return float(text[:-2].strip()) / 100

        if text.endswith("m"):
            return float(text[:-1].strip())

        return float(text)

    except ValueError:
        return None


def foundation_parse_diameter(text):
    text = (
        text.lower()
        .replace("Гё", "")
        .replace("Г", "")
        .strip()
    )

    try:
        return float(text)
    except ValueError:
        return None


def foundation_parse_spacing(text):
    text = text.lower().replace("mm", "").strip()

    try:
        return float(text)
    except ValueError:
        return None


def foundation_rebar_weight(diameter):
    return (diameter ** 2) / 162


def foundation_answer_back():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="рџ”„ Qayta hisoblash"),
                KeyboardButton(text="в¬…пёЏ Ortga")
            ]
        ],
        resize_keyboard=True
    )


# ============================================================
# 1. POYDEVOR MENYUSI
# ============================================================

@dp.message(F.text == "рџЏ— Poydevor")
async def foundation_start(
    message: Message,
    state: FSMContext
):
    await state.clear()

    await state.set_state(
        ArmaturaCalculator.foundation_type
    )

    await message.answer(
        "рџЏ— POYDEVOR ARMATURA KALKULYATORI\n\n"
        "Poydevor turini tanlang:",
        reply_markup=foundation_type_menu()
    )


# ============================================================
# 2. POYDEVOR TURI
# ============================================================

@dp.message(ArmaturaCalculator.foundation_type)
async def foundation_choose_type(
    message: Message,
    state: FSMContext
):

    types = {
        "рџ§± Lenta poydevor",
        "в¬› Plita poydevor",
        "рџџ« Alohida poydevor",
        "рџЏ— Ustunli poydevor",
        "рџЏў Monolit poydevor"
    }

    if message.text not in types:
        await message.answer(
            "вќЊ Avval poydevor turini tanlang.",
            reply_markup=foundation_type_menu()
        )
        return

    await state.update_data(
        foundation_type=message.text
    )

    await state.set_state(
        ArmaturaCalculator.foundation_length
    )

    await message.answer(
        f"вњ… {message.text}\n\n"
        "1пёЏвѓЈ Uzunligini kiriting.\n\n"
        "Masalan: 10 m"
    )


# ============================================================
# 3. UZUNLIK
# ============================================================

@dp.message(ArmaturaCalculator.foundation_length)
async def foundation_get_length(
    message: Message,
    state: FSMContext
):

    value = foundation_parse_length(message.text)

    if value is None or value <= 0:
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n"
            "Masalan: 10 m"
        )
        return

    await state.update_data(
        foundation_length=value
    )

    await state.set_state(
        ArmaturaCalculator.foundation_width
    )

    await message.answer(
        "2пёЏвѓЈ Enini kiriting.\n\n"
        "Masalan: 0.5 m"
    )


# ============================================================
# 4. ENI
# ============================================================

@dp.message(ArmaturaCalculator.foundation_width)
async def foundation_get_width(
    message: Message,
    state: FSMContext
):

    value = foundation_parse_length(message.text)

    if value is None or value <= 0:
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n"
            "Masalan: 0.5 m"
        )
        return

    await state.update_data(
        foundation_width=value
    )

    await state.set_state(
        ArmaturaCalculator.foundation_height
    )

    await message.answer(
        "3пёЏвѓЈ Balandligini kiriting.\n\n"
        "Masalan: 0.6 m"
    )


# ============================================================
# 5. BALANDLIK
# ============================================================

@dp.message(ArmaturaCalculator.foundation_height)
async def foundation_get_height(
    message: Message,
    state: FSMContext
):

    value = foundation_parse_length(message.text)

    if value is None or value <= 0:
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n"
            "Masalan: 0.6 m"
        )
        return

    await state.update_data(
        foundation_height=value
    )

    await state.set_state(
        ArmaturaCalculator.foundation_cover
    )

    await message.answer(
        "4пёЏвѓЈ Himoya qatlamini kiriting (mm).\n\n"
        "Masalan: 50"
    )


# ============================================================
# 6. HIMOYA QATLAMI
# ============================================================

@dp.message(ArmaturaCalculator.foundation_cover)
async def foundation_get_cover(
    message: Message,
    state: FSMContext
):

    value = parse_number(message.text)

    if value is None or value < 0:
        await message.answer(
            "вќЊ NotoвЂgвЂri qiymat.\n"
            "Masalan: 50"
        )
        return

    await state.update_data(
        foundation_cover=value
    )

    await state.set_state(
        ArmaturaCalculator.foundation_main_diameter
    )

    await message.answer(
        "5пёЏвѓЈ Asosiy armatura diametrini tanlang:",
        reply_markup=foundation_diameter_menu()
    )


# ============================================================
# 7. ASOSIY DIAMETR
# ============================================================

@dp.message(ArmaturaCalculator.foundation_main_diameter)
async def foundation_get_main_diameter(
    message: Message,
    state: FSMContext
):

    diameter = foundation_parse_diameter(message.text)

    if diameter is None or diameter <= 0:
        await message.answer(
            "вќЊ Diametrni tanlang.",
            reply_markup=foundation_diameter_menu()
        )
        return

    await state.update_data(
        foundation_main_diameter=diameter
    )

    await state.set_state(
        ArmaturaCalculator.foundation_main_count
    )

    await message.answer(
        "6пёЏвѓЈ Asosiy boвЂylama armatura sonini kiriting.\n\n"
        "Masalan: 4\n\n"
        "вљ пёЏ Bu loyiha boвЂyicha qabul qilinadigan "
        "boвЂylama sterjenlar soni."
    )


# ============================================================
# 8. ASOSIY ARMATURA SONI
# ============================================================

@dp.message(ArmaturaCalculator.foundation_main_count)
async def foundation_get_main_count(
    message: Message,
    state: FSMContext
):

    try:
        count = int(message.text.strip())
    except ValueError:
        count = 0

    if count <= 0:
        await message.answer(
            "вќЊ Butun son kiriting.\n"
            "Masalan: 4"
        )
        return

    await state.update_data(
        foundation_main_count=count
    )

    await state.set_state(
        ArmaturaCalculator.foundation_cross_diameter
    )

    await message.answer(
        "7пёЏвѓЈ Xomut / koвЂndalang armatura diametrini tanlang:",
        reply_markup=foundation_diameter_menu()
    )


# ============================================================
# 9. XOMUT DIAMETRI
# ============================================================

@dp.message(ArmaturaCalculator.foundation_cross_diameter)
async def foundation_get_cross_diameter(
    message: Message,
    state: FSMContext
):

    diameter = foundation_parse_diameter(message.text)

    if diameter is None or diameter <= 0:
        await message.answer(
            "вќЊ Diametrni tanlang.",
            reply_markup=foundation_diameter_menu()
        )
        return

    await state.update_data(
        foundation_cross_diameter=diameter
    )

    await state.set_state(
        ArmaturaCalculator.foundation_cross_spacing
    )

    await message.answer(
        "8пёЏвѓЈ Xomut qadamini kiriting (mm).\n\n"
        "Masalan: 200"
    )


# ============================================================
# 10. XOMUT QADAMI
# ============================================================

@dp.message(ArmaturaCalculator.foundation_cross_spacing)
async def foundation_get_cross_spacing(
    message: Message,
    state: FSMContext
):

    spacing = foundation_parse_spacing(message.text)

    if spacing is None or spacing <= 0:
        await message.answer(
            "вќЊ Qadamni mm da kiriting.\n"
            "Masalan: 200"
        )
        return

    await state.update_data(
        foundation_cross_spacing=spacing
    )

    await state.set_state(
        ArmaturaCalculator.foundation_quantity
    )

    await message.answer(
        "9пёЏвѓЈ Nechta bir xil poydevor hisoblanadi?\n\n"
        "Masalan: 4"
    )


# ============================================================
# 11. HISOB
# ============================================================

@dp.message(ArmaturaCalculator.foundation_quantity)
async def foundation_calculate(
    message: Message,
    state: FSMContext
):

    try:
        quantity = int(message.text.strip())
    except ValueError:
        quantity = 0

    if quantity <= 0:
        await message.answer(
            "вќЊ Butun son kiriting.\n"
            "Masalan: 4"
        )
        return

    data = await state.get_data()

    f_type = data["foundation_type"]

    length = data["foundation_length"]
    width = data["foundation_width"]
    height = data["foundation_height"]
    cover = data["foundation_cover"]

    main_d = data["foundation_main_diameter"]
    main_count = data["foundation_main_count"]

    cross_d = data["foundation_cross_diameter"]
    spacing = data["foundation_cross_spacing"]

    length_mm = length * 1000
    width_mm = width * 1000
    height_mm = height * 1000

    # ========================================================
    # ASOSIY BOвЂYLAMA ARMATURA
    # ========================================================

    working_length = max(
        0,
        length_mm - (2 * cover)
    ) / 1000

    main_total_m = (
        working_length
        * main_count
        * quantity
    )

    # ========================================================
    # XOMUT SONI
    # ========================================================

    working_length_mm = max(
        0,
        length_mm - (2 * cover)
    )

    stirrup_count = (
        math.ceil(
            working_length_mm / spacing
        ) + 1
    )

    # ========================================================
    # XOMUT UZUNLIGI
    # ========================================================

    inner_width = max(
        0,
        width_mm - (2 * cover)
    )

    inner_height = max(
        0,
        height_mm - (2 * cover)
    )

    stirrup_each_m = (
        2 * (inner_width + inner_height)
    ) / 1000

    stirrup_total_m = (
        stirrup_count
        * stirrup_each_m
        * quantity
    )

    # ========================================================
    # UMUMIY METR
    # ========================================================

    total_m = (
        main_total_m
        + stirrup_total_m
    )

    reserve_m = total_m * 0.05

    final_m = total_m + reserve_m

    # ========================================================
    # KG
    # ========================================================

    main_kg_m = foundation_rebar_weight(main_d)
    cross_kg_m = foundation_rebar_weight(cross_d)

    main_kg = main_total_m * main_kg_m
    cross_kg = stirrup_total_m * cross_kg_m

    total_kg = main_kg + cross_kg
    final_kg = total_kg * 1.05

    # ========================================================
    # NATIJA
    # ========================================================

    await message.answer(
        "вњ… POYDEVOR ARMATURA HISOBI\n\n"

        f"рџЏ— Poydevor turi:\n"
        f"{f_type}\n\n"

        f"рџ“ђ OвЂlcham:\n"
        f"{length:.2f} Г— "
        f"{width:.2f} Г— "
        f"{height:.2f} m\n\n"

        f"рџ”ў Miqdor: {quantity} dona\n"
        f"рџ›Ў Himoya qatlami: {cover:.0f} mm\n\n"

        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"
        "рџ”© ASOSIY ARMATURA\n"
        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"

        f"Г{main_d:.0f}\n"
        f"Sterjen: {main_count} dona\n"
        f"Har biri: {working_length:.2f} m\n"
        f"Jami: {main_total_m:.2f} m\n"
        f"OgвЂirligi: {main_kg:.2f} kg\n\n"

        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"
        "рџ”— XOMUT\n"
        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"

        f"Г{cross_d:.0f}\n"
        f"Qadam: {spacing:.0f} mm\n"
        f"Xomut: {stirrup_count} dona\n"
        f"Har biri: {stirrup_each_m:.2f} m\n"
        f"Jami: {stirrup_total_m:.2f} m\n"
        f"OgвЂirligi: {cross_kg:.2f} kg\n\n"

        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"
        "рџ“Љ YAKUNIY NATIJA\n"
        "в”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓв”Ѓ\n"

        f"рџ“Џ Asosiy armatura: "
        f"{main_total_m:.2f} m\n"

        f"рџ“Џ Xomut: "
        f"{stirrup_total_m:.2f} m\n"

        f"рџ“Џ Umumiy: "
        f"{total_m:.2f} m\n\n"

        f"вћ• 5% zaxira: "
        f"{reserve_m:.2f} m\n\n"

        f"рџџў KERAKLI ARMATURA:\n"
        f"рџ”Ґ {final_m:.2f} METR\n\n"

        f"вљ–пёЏ Taxminiy ogвЂirlik:\n"
        f"{final_kg:.2f} kg\n\n"

        "вљ пёЏ Eslatma:\n"
        "Bu natija berilgan konstruktiv parametrlar "
        "asosida armatura material miqdorini hisoblaydi. "
        "Diametr, sterjen soni va qadam loyiha hisobiga "
        "muvofiq belgilanadi."
    )

    await state.clear()

    await message.answer(
        "рџЏ— Poydevor boвЂyicha yana hisoblash:",
        reply_markup=armatura_menu()
    )

# =========================================================
# AI
# =========================================================

@dp.message(F.text == "рџ¤– AI yordamchi")
async def ai_handler(
    message: Message,
    state: FSMContext
):
    await state.clear()
    await state.set_state(AIHelper.chat)

    await message.answer(
        "рџ¤– ARCHHELP AI YORDAMCHI\n\n"
        "Savolingizni yozing.\n\n"
        "Men sizga arxitektura, qurilish, "
        "Revit, AutoCAD va boshqa mavzularda yordam beraman.\n\n"
        "Masalan:\n"
        "вЂў Revitda devorni 300 mm qilish\n"
        "вЂў AutoCADda layer yaratish\n"
        "вЂў Beton hisoblash\n"
        "вЂў Qurilish materiallari haqida\n\n"
        "в¬…пёЏ Ortga вЂ” chiqish"
    )


@dp.message(AIHelper.chat, F.text)
async def ai_message_handler(
    message: Message,
    state: FSMContext
):
    question = message.text.strip()

    if question == "в¬…пёЏ Ortga":
        await state.clear()

        await message.answer(
            "рџЏ  Bosh menyu:",
            reply_markup=main_menu
        )
        return

    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action="typing"
    )

    answer = await ask_ai(
        question,
        state
    )

    await message.answer(answer)

# =========================================================
# ADMIN BILAN BOGвЂLANISH
# =========================================================

@dp.message(F.text == "рџ“ћ Admin bilan bogвЂlanish")
async def admin_contact_handler(message: Message):

    admin_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="рџ“© Admin bilan bogвЂlanish",
                    url="https://t.me/ArchHelpBot_support"
                )
            ]
        ]
    )

    await message.answer(
        "рџ‘ЁвЂЌрџ’» ARCHHELP ADMIN\n\n"
        "Savol, taklif, xatolik yoki hamkorlik boвЂyicha "
        "admin bilan bogвЂlanishingiz mumkin.\n\n"
        "рџ“© Murojaat uchun quyidagi tugmani bosing:",
        reply_markup=admin_keyboard
    )

# =========================================================
# =========================================================
# 3D MODEL TOPISH
# =========================================================

@dp.message(F.text == '🔎 3D MODEL TOPISH')
async def model_finder_start_handler(message: Message):
    await message.answer(
        '🔎 3D MODEL TOPISH\n\n'
        'Istalgan 3D model rasmini yuboring.\n'
        '📷 Oddiy rasm, screenshot yoki JPG/PNG fayl yuborishingiz mumkin.\n\n'
        'Men mavjud 3D model indeksidan o‘xshash modellarni qidiraman.'
    )


@dp.message(F.photo)
async def model_finder_photo_handler(message: Message):
    status_message = await message.answer(
        '🔎 Rasm qabul qilindi.\n\n'
        '⏳ 3D modellar bazasidan qidirilmoqda...\n'
        'Bir necha soniya vaqt olishi mumkin.'
    )

    try:
        photo = message.photo[-1]
        file = await bot.get_file(photo.file_id)
        image_bytes = await bot.download_file(file.file_path)
        image_data = image_bytes.read()

        results = await search_3d_models(
            image_bytes=image_data,
            max_results_per_channel=5,
            final_results=5,
        )

        result_text = format_results(results)

        await status_message.edit_text(
            result_text,
            parse_mode='Markdown',
            disable_web_page_preview=True,
        )

    except Exception as e:
        print(f'[3D SEARCH ERROR] {e}')

        await status_message.edit_text(
            '❌ 3D model qidirishda xatolik yuz berdi.\n\n'
            'Iltimos, boshqa rasm bilan qayta urinib ko‘ring.'
        )


@dp.message(F.document)
async def model_finder_document_handler(message: Message):
    document = message.document

    if not document:
        return

    mime_type = document.mime_type or ''

    if not mime_type.startswith('image/'):
        return

    status_message = await message.answer(
        '🔎 Rasm fayli qabul qilindi.\n\n'
        '⏳ 3D modellar bazasidan qidirilmoqda...'
    )

    try:
        file = await bot.get_file(document.file_id)
        image_bytes = await bot.download_file(file.file_path)
        image_data = image_bytes.read()

        results = await search_3d_models(
            image_bytes=image_data,
            max_results_per_channel=5,
            final_results=5,
        )

        result_text = format_results(results)

        await status_message.edit_text(
            result_text,
            parse_mode='Markdown',
            disable_web_page_preview=True,
        )

    except Exception as e:
        print(f'[3D DOCUMENT SEARCH ERROR] {e}')

        await status_message.edit_text(
            '❌ Rasm faylini tahlil qilishda xatolik yuz berdi.'
        )

async def main():

    print("рџљЂ ARCHHELP ISHGA TUSHDI")

    await dp.start_polling(bot)


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    asyncio.run(main())


