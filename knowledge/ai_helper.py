from openai import AsyncOpenAI
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = AsyncOpenAI(
    api_key=OPENAI_API_KEY
)


class AIHelper(StatesGroup):
    chat = State()


AI_INSTRUCTIONS = """
Sen ARCHHELP Telegram botining AI yordamchisisan.

Foydalanuvchi bilan doimo O'ZBEK TILIDA gaplash.

Sening asosiy yo'nalishlaring:
- Arxitektura
- Qurilish
- Revit
- AutoCAD
- 3ds Max
- BIM
- Qurilish materiallari
- Qurilish texnologiyalari
- Qurilish hisob-kitoblari
- SHNQ va qurilish me'yorlari
- Chizmalar
- Konstruksiyalar
- Arxitektura bo'yicha amaliy maslahatlar

Qoidalar:
- Savolga to'g'ridan-to'g'ri javob ber.
- Kerak bo'lsa bosqichma-bosqich tushuntir.
- Revit va AutoCAD savollarida aniq buyruq va menyularni ko'rsat.
- Hisob-kitoblarda formulani ko'rsat.
- Noto'g'ri ma'lumotni o'ylab topma.
- Aniq bilmasang, buni ochiq ayt.
- Konstruktiv hisoblar xavfsizlikka ta'sir qilsa, professional konstruktor
  tekshiruvi kerakligini bildir.
- Javoblarni tushunarli va amaliy qil.
- Keraksiz uzun javoblardan qoch.

Sen oddiy savollarga ham javob bera olasan.
Masalan, foydalanuvchi "Salom" desa, salomlashib javob ber.

ARCHHELP — arxitektura va qurilish bo'yicha professional AI yordamchi.
"""


async def ask_ai(
    question: str,
    state: FSMContext
):
    data = await state.get_data()

    history = data.get("ai_history", [])

    history.append({
        "role": "user",
        "content": question
    })

    # Oxirgi suhbatlarni saqlaymiz
    history = history[-10:]

    try:
        response = await client.responses.create(
            model="gpt-5.6-luna",
            instructions=AI_INSTRUCTIONS,
            input=history
        )

        answer = response.output_text

        history.append({
            "role": "assistant",
            "content": answer
        })

        history = history[-10:]

        await state.update_data(
            ai_history=history
        )

        return answer

    except Exception as e:
        print(f"❌ OPENAI XATOLIK: {e}")

        return (
            "❌ AI bilan bog‘lanishda xatolik yuz berdi.\n\n"
            "Iltimos, birozdan keyin qayta urinib ko‘ring."
        )