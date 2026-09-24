# -*- coding: utf-8 -*-

"""
ARCHHELP — REVIT NORMATIV BAZASI
O'zbekiston SHNQ/QMQ asosida.

STATUS:
    normativ    -> hujjatda aniq talab sifatida berilgan
    hisoblangan -> normativ qiymatdan matematik hisoblangan
    reference   -> normativ hujjat mavjud, lekin bu yozuv raqamli norma emas

MUHIM:
    Normativ bo'lmagan amaliy o'lchamlar "normativ" deb belgilanmaydi.
"""

import math


# ============================================================
# MANBALAR
# ============================================================

SOURCES = {
    "SHNQ_2_08_01_24":
        "https://lex.uz/docs/-7121730",

    "SHNQ_2_08_02_23":
        "https://lex.uz/docs/-6920040",

    "SHNQ_2_09_02_23":
        "https://lex.uz/docs/-7178346",

    "SHNQ_2_09_03_23":
        "https://lex.uz/acts/-6689681",

    "SHNQ_2_05_07_24":
        "https://lex.uz/en/docs/-7396504",

    "SHNQ_2_07_01_23":
        "https://lex.uz/pdffile/7954120",

    "SHNQ_2_07_02_24":
        "https://lex.uz/",

    "SHNQ_2_08_06_23":
        "https://lex.uz/",

    "SHNQ_2_04_01_22":
        "https://lex.uz/",

    "SHNQ_2_04_05_22":
        "https://lex.uz/",

    "SHNQ_2_01_05_24":
        "https://lex.uz/",

    "SHNQ_2_03_10_24":
        "https://lex.uz/",

    "LEX_UZ":
        "https://lex.uz/",
}


# ============================================================
# MATEMATIK FUNKSIYALAR
# ============================================================

def percent_to_degree(percent):
    return math.degrees(math.atan(percent / 100))


def ratio_to_degree(ratio):
    if ratio <= 0:
        raise ValueError("Nisbat 0 dan katta bo'lishi kerak.")

    return math.degrees(math.atan(1 / ratio))


def meter_to_mm(value):
    return round(value * 1000)


def mm_to_meter(value):
    return value / 1000


# ============================================================
# RECORD YARATISH
# ============================================================

def norm(
    kategoriya,
    parametr,
    qiymat,
    birlik,
    chegara,
    qollanish,
    hujjat,
    band,
    manba,
    izoh="",
    status="normativ",
):
    return {
        "kategoriya": kategoriya,
        "parametr": parametr,
        "qiymat": qiymat,
        "birlik": birlik,
        "chegara": chegara,
        "qollanish": qollanish,
        "hujjat": hujjat,
        "band": band,
        "manba": manba,
        "izoh": izoh,
        "status": status,
    }


REVIT_DIMENSIONS = {}


def add(name, data):
    REVIT_DIMENSIONS[name] = data


# ============================================================
# 1. PANDUS
# ============================================================

add(
    "Pandus — maxsus kvartira eni",
    norm(
        "Pandus",
        "Minimal kenglik",
        1.2,
        "m",
        "minimal",
        "Maxsus kvartirali turar joy",
        "SHNQ 2.08.01-24",
        "181-band",
        SOURCES["SHNQ_2_08_01_24"],
        "Pandus eni kamida 1,2 m.",
    ),
)

add(
    "Pandus — maxsus kvartira qiyaligi",
    norm(
        "Pandus",
        "Maksimal qiyalik",
        5,
        "%",
        "maksimal",
        "Maxsus kvartirali turar joy",
        "SHNQ 2.08.01-24",
        "181-band",
        SOURCES["SHNQ_2_08_01_24"],
        "1:20 dan ko'p emas.",
    ),
)

add(
    "Pandus — 1:20 gradus",
    norm(
        "Pandus",
        "Hisoblangan qiyalik",
        round(ratio_to_degree(20), 2),
        "°",
        "hisoblangan",
        "1:20 pandus",
        "SHNQ 2.08.01-24",
        "181-band",
        SOURCES["SHNQ_2_08_01_24"],
        "1:20 dan matematik hisoblangan.",
        "hisoblangan",
    ),
)

add(
    "Ombor ichki pandusi",
    norm(
        "Pandus",
        "Maksimal qiyalik",
        16,
        "%",
        "maksimal",
        "Ombor ichki pandusi",
        "SHNQ 2.09.03-23",
        "27-band",
        SOURCES["SHNQ_2_09_03_23"],
    ),
)

add(
    "Ombor tashqi pandusi",
    norm(
        "Pandus",
        "Maksimal qiyalik",
        10,
        "%",
        "maksimal",
        "Ombor tashqi pandusi",
        "SHNQ 2.09.03-23",
        "27-band",
        SOURCES["SHNQ_2_09_03_23"],
    ),
)

add(
    "Ombor ichki pandusi — gradus",
    norm(
        "Pandus",
        "Hisoblangan qiyalik",
        round(percent_to_degree(16), 2),
        "°",
        "hisoblangan",
        "16%",
        "SHNQ 2.09.03-23",
        "27-band",
        SOURCES["SHNQ_2_09_03_23"],
        "16% dan hisoblangan.",
        "hisoblangan",
    ),
)

add(
    "Ombor tashqi pandusi — gradus",
    norm(
        "Pandus",
        "Hisoblangan qiyalik",
        round(percent_to_degree(10), 2),
        "°",
        "hisoblangan",
        "10%",
        "SHNQ 2.09.03-23",
        "27-band",
        SOURCES["SHNQ_2_09_03_23"],
        "10% dan hisoblangan.",
        "hisoblangan",
    ),
)


# ============================================================
# 2. RAMPA
# ============================================================

add(
    "Avtoyuklagich rampasi eni",
    norm(
        "Rampa",
        "Minimal eni",
        4.5,
        "m",
        "minimal",
        "Avtoyuklagich bilan yuklash-tushirish",
        "SHNQ 2.09.03-23",
        "29-band",
        SOURCES["SHNQ_2_09_03_23"],
    ),
)

add(
    "Rampa ko'ndalang nishabi",
    norm(
        "Rampa",
        "Ko'ndalang nishab",
        1,
        "%",
        "talab",
        "Yuklash-tushirish rampasi",
        "SHNQ 2.09.03-23",
        "30-band",
        SOURCES["SHNQ_2_09_03_23"],
    ),
)

add(
    "Rampa ko'ndalang nishabi — gradus",
    norm(
        "Rampa",
        "Hisoblangan nishab",
        round(percent_to_degree(1), 2),
        "°",
        "hisoblangan",
        "1%",
        "SHNQ 2.09.03-23",
        "30-band",
        SOURCES["SHNQ_2_09_03_23"],
        "1% dan hisoblangan.",
        "hisoblangan",
    ),
)

add(
    "Rampa sath balandligi",
    norm(
        "Rampa",
        "Balandlik",
        1.2,
        "m",
        "talab",
        "Avtomobil yuklash-tushirish rampasi",
        "SHNQ 2.09.03-23",
        "31-band",
        SOURCES["SHNQ_2_09_03_23"],
    ),
)


# ============================================================
# 3. ESHIK
# ============================================================

add(
    "Maxsus kvartira eshigi",
    norm(
        "Eshik",
        "Minimal kenglik",
        0.9,
        "m",
        "minimal",
        "Maxsus kvartirali turar joy",
        "SHNQ 2.08.01-24",
        "181-band",
        SOURCES["SHNQ_2_08_01_24"],
    ),
)

add(
    "Maxsus kvartira eshigi — mm",
    norm(
        "Eshik",
        "Minimal kenglik",
        900,
        "mm",
        "minimal",
        "Maxsus kvartirali turar joy",
        "SHNQ 2.08.01-24",
        "181-band",
        SOURCES["SHNQ_2_08_01_24"],
        "0,9 m = 900 mm.",
        "hisoblangan",
    ),
)

add(
    "Ishlab chiqarish evakuatsiya eshigi",
    norm(
        "Eshik",
        "Minimal kenglik",
        0.8,
        "m",
        "minimal",
        "Ishlab chiqarish binolari",
        "SHNQ 2.09.02-23",
        "117-band",
        SOURCES["SHNQ_2_09_02_23"],
    ),
)

add(
    "Nogiron ishlovchi eshigi",
    norm(
        "Eshik",
        "Minimal kenglik",
        0.9,
        "m",
        "minimal",
        "Nogironligi bo'lgan xodimlar mavjud obyektlar",
        "SHNQ 2.09.02-23",
        "117-band",
        SOURCES["SHNQ_2_09_02_23"],
    ),
)


# ============================================================
# 4. YO'LAK
# ============================================================

add(
    "Maxsus kvartira yo'lagi",
    norm(
        "Yo'lak",
        "Minimal kenglik",
        1.8,
        "m",
        "minimal",
        "Maxsus kvartirali turar joy",
        "SHNQ 2.08.01-24",
        "181-band",
        SOURCES["SHNQ_2_08_01_24"],
    ),
)

add(
    "Maxsus kvartira yo'lagi — mm",
    norm(
        "Yo'lak",
        "Minimal kenglik",
        1800,
        "mm",
        "minimal",
        "Maxsus kvartirali turar joy",
        "SHNQ 2.08.01-24",
        "181-band",
        SOURCES["SHNQ_2_08_01_24"],
        "1,8 m = 1800 mm.",
        "hisoblangan",
    ),
)


# ============================================================
# 5. ZINA
# ============================================================

add(
    "Nogiron ishlovchi zina marsh eni",
    norm(
        "Zina",
        "Minimal marsh eni",
        1.2,
        "m",
        "minimal",
        "Nogironligi bo'lgan xodimlar mavjud ishlab chiqarish obyektlari",
        "SHNQ 2.09.02-23",
        "118-band",
        SOURCES["SHNQ_2_09_02_23"],
    ),
)

add(
    "Maxsus tashqi po'lat zina eni",
    norm(
        "Zina",
        "Minimal eni",
        0.7,
        "m",
        "minimal",
        "Maxsus tashqi evakuatsiya zinalari",
        "SHNQ 2.09.02-23",
        "280-band",
        SOURCES["SHNQ_2_09_02_23"],
        "Umumiy zina normasi emas. Faqat 280-band shartlari uchun.",
    ),
)

add(
    "Maxsus tashqi po'lat zina qiyaligi",
    norm(
        "Zina",
        "Maksimal qiyalik",
        "1:1",
        "nisbat",
        "maksimal",
        "Maxsus tashqi evakuatsiya zinalari",
        "SHNQ 2.09.02-23",
        "280-band",
        SOURCES["SHNQ_2_09_02_23"],
    ),
)

add(
    "Maxsus tashqi po'lat zina — gradus",
    norm(
        "Zina",
        "Hisoblangan qiyalik",
        45,
        "°",
        "hisoblangan",
        "1:1",
        "SHNQ 2.09.02-23",
        "280-band",
        SOURCES["SHNQ_2_09_02_23"],
        "1:1 = 45°.",
        "hisoblangan",
    ),
)


# ============================================================
# 6. EVAKUATSIYA
# ============================================================

add(
    "Evakuatsiya eshigi — ishlab chiqarish",
    norm(
        "Evakuatsiya",
        "Minimal kenglik",
        0.8,
        "m",
        "minimal",
        "Ishlab chiqarish binolari",
        "SHNQ 2.09.02-23",
        "117-band",
        SOURCES["SHNQ_2_09_02_23"],
    ),
)

add(
    "Evakuatsiya eshigi — nogiron xodim",
    norm(
        "Evakuatsiya",
        "Minimal kenglik",
        0.9,
        "m",
        "minimal",
        "Nogironligi bo'lgan xodimlar mavjud obyektlar",
        "SHNQ 2.09.02-23",
        "117-band",
        SOURCES["SHNQ_2_09_02_23"],
    ),
)

add(
    "Sport zali — bitta chiqish",
    norm(
        "Evakuatsiya",
        "Maksimal odam soni",
        600,
        "kishi",
        "maksimal",
        "Yopiq sport zallari",
        "SHNQ 2.08.02-23",
        "309-band",
        SOURCES["SHNQ_2_08_02_23"],
    ),
)


# ============================================================
# 7. OMBOR
# ============================================================

add(
    "Ombor ustunlar oralig'i",
    norm(
        "Konstruktiv reja",
        "Minimal ustunlar oralig'i",
        6,
        "m",
        "minimal",
        "Ombor binolari",
        "SHNQ 2.09.03-23",
        "14-band",
        SOURCES["SHNQ_2_09_03_23"],
    ),
)

add(
    "Ombor tabiiy ventilyatsiyasi",
    norm(
        "Ventilyatsiya",
        "Minimal havo almashinuvi",
        1,
        "marta/soat",
        "kamida",
        "Tegishli omborlar",
        "SHNQ 2.09.03-23",
        "57-band",
        SOURCES["SHNQ_2_09_03_23"],
    ),
)


# ============================================================
# 8. TA'LIM
# ============================================================

add(
    "Maktab bufet zali",
    norm(
        "Ta'lim",
        "Minimal maydon",
        20,
        "m²",
        "minimal",
        "Bufet zali",
        "SHNQ 2.08.06-23",
        "14-band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "Maktab bufet yordamchi xonasi",
    norm(
        "Ta'lim",
        "Minimal maydon",
        6,
        "m²",
        "minimal",
        "Bufet yordamchi xonasi",
        "SHNQ 2.08.06-23",
        "14-band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "Maktab tibbiyot xonasi — 600 gacha",
    norm(
        "Ta'lim",
        "Maydon",
        "14–16",
        "m²",
        "talab",
        "600 nafargacha o'quvchi",
        "SHNQ 2.08.06-23",
        "15-band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "Maktab muolaja xonasi",
    norm(
        "Ta'lim",
        "Minimal maydon",
        14,
        "m²",
        "minimal",
        "600 nafardan ko'p o'quvchi",
        "SHNQ 2.08.06-23",
        "15-band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "Maktab terapevt xonasi",
    norm(
        "Ta'lim",
        "Minimal maydon",
        12,
        "m²",
        "minimal",
        "600 nafardan ko'p o'quvchi",
        "SHNQ 2.08.06-23",
        "15-band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "Maktab stomatolog xonasi",
    norm(
        "Ta'lim",
        "Minimal maydon",
        14,
        "m²",
        "minimal",
        "600 nafardan ko'p o'quvchi",
        "SHNQ 2.08.06-23",
        "15-band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "Maktab rekreatsiya maydoni",
    norm(
        "Ta'lim",
        "Maydon",
        0.6,
        "m²/o'quvchi",
        "hisobiy",
        "Umumiy o'rta va professional ta'lim",
        "SHNQ 2.08.06-23",
        "16-band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "Ta'lim binosi sokol qavati",
    norm(
        "Ta'lim",
        "Maksimal pastlik",
        0.5,
        "m",
        "maksimal",
        "Sokol qavat",
        "SHNQ 2.08.06-23",
        "20-band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "Ta'lim binosi konstruksiya osti",
    norm(
        "Ta'lim",
        "Minimal balandlik",
        1.8,
        "m",
        "minimal",
        "Bo'rtib chiqib turuvchi konstruksiya osti",
        "SHNQ 2.08.06-23",
        "22-band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)


# ============================================================
# 9. MTT
# ============================================================

add(
    "MTT musiqa zali",
    norm(
        "MTT",
        "Minimal maydon",
        2,
        "m²/bola",
        "minimal",
        "Musiqa mashg'ulotlari",
        "SHNQ 2.08.06-23",
        "tegishli band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "MTT gimnastika zali",
    norm(
        "MTT",
        "Minimal maydon",
        3,
        "m²/bola",
        "minimal",
        "Gimnastika mashg'ulotlari",
        "SHNQ 2.08.06-23",
        "tegishli band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "MTT universal zal",
    norm(
        "MTT",
        "Minimal maydon",
        4,
        "m²/bola",
        "minimal",
        "Universal zal",
        "SHNQ 2.08.06-23",
        "tegishli band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "MTT gimnastika zali eni",
    norm(
        "MTT",
        "Minimal eni",
        9,
        "m",
        "minimal",
        "Gimnastika zali",
        "SHNQ 2.08.06-23",
        "tegishli band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "MTT gimnastika zali bo'yi",
    norm(
        "MTT",
        "Minimal bo'yi",
        9,
        "m",
        "minimal",
        "Gimnastika zali",
        "SHNQ 2.08.06-23",
        "tegishli band",
        SOURCES["SHNQ_2_08_06_23"],
    ),
)

add(
    "MTT gimnastika zali maydoni",
    norm(
        "MTT",
        "Minimal maydon",
        81,
        "m²",
        "minimal",
        "9 × 9 m zal",
        "SHNQ 2.08.06-23",
        "tegishli band",
        SOURCES["SHNQ_2_08_06_23"],
        "9 × 9 m.",
    ),
)


# ============================================================
# 10. YOTOQXONA
# ============================================================

YOTOQXONA = [
    ("Yotoqxona — o'quvchi 50 kishi", 2.6,
     "50 kishilik o'quvchilar yotoqxonasi"),

    ("Yotoqxona — o'quvchi 100 kishi", 2.5,
     "100 kishilik o'quvchilar yotoqxonasi"),

    ("Yotoqxona — o'quvchi 200 kishi", 2.5,
     "200 kishilik o'quvchilar yotoqxonasi"),

    ("Yotoqxona — talaba 50 kishi", 2.5,
     "50 kishilik talabalar yotoqxonasi"),

    ("Yotoqxona — talaba 100 kishi", 2.4,
     "100 kishilik talabalar yotoqxonasi"),

    ("Yotoqxona — ishchi 50 kishi", 2.3,
     "50 kishilik ishchi-xizmatchilar yotoqxonasi"),

    ("Yotoqxona — ishchi 100 kishi", 2.2,
     "100 kishilik ishchi-xizmatchilar yotoqxonasi"),

    ("Yotoqxona — kichik oila 50 kishi", 1.5,
     "Kichik oilalar yotoqxonasi"),

    ("Yotoqxona — kichik oila 100 kishi", 1.3,
     "Kichik oilalar yotoqxonasi"),
]

for name, value, usage in YOTOQXONA:

    add(
        name,
        norm(
            "Yotoqxona",
            "Maydon",
            value,
            "m²/kishi",
            "hisobiy",
            usage,
            "SHNQ 2.08.01-24",
            "3-jadval",
            SOURCES["SHNQ_2_08_01_24"],
        )
    )


# ============================================================
# 11. PARKING — HUJJAT REESTRI
# ============================================================

add(
    "Avtoturargohlar — asosiy normativ",
    norm(
        "Parking",
        "Asosiy hujjat",
        "SHNQ 2.05.07-24",
        "hujjat",
        "amaldagi",
        "Avtoturargohlarni loyihalash",
        "SHNQ 2.05.07-24",
        "amaldagi",
        SOURCES["SHNQ_2_05_07_24"],
        "Aniq joy o'lchamlari transport turi va sxema bo'yicha olinadi.",
        "reference",
    ),
)


# ============================================================
# 12. INKLYUZIVLIK
# ============================================================

add(
    "Inklyuziv loyihalash — asosiy hujjat",
    norm(
        "Inklyuzivlik",
        "Asosiy normativ",
        "SHNQ 2.07.02-24",
        "hujjat",
        "amaldagi",
        "Nogironligi bo'lgan shaxslar va keksalar ehtiyojini hisobga olish",
        "SHNQ 2.07.02-24",
        "amaldagi",
        SOURCES["SHNQ_2_07_02_24"],
        "Raqamli talablar obyekt turiga qarab tegishli banddan olinadi.",
        "reference",
    ),
)


# ============================================================
# 13. GENPLAN
# ============================================================

add(
    "Genplan — asosiy normativ",
    norm(
        "Genplan",
        "Asosiy hujjat",
        "SHNQ 2.07.01-23",
        "hujjat",
        "amaldagi",
        "Aholi punktlari hududlarini rejalashtirish",
        "SHNQ 2.07.01-23",
        "amaldagi",
        SOURCES["SHNQ_2_07_01_23"],
        "Hudud, ko'cha, transport va funksional zonalash bo'yicha talablar.",
        "reference",
    ),
)


# ============================================================
# 14. SHAHAR KO'CHA-YO'LLARI
# ============================================================

add(
    "Shahar ko'cha-yo'llari",
    norm(
        "Yo'l",
        "Asosiy normativ",
        "SHNQ 2.07.06-24",
        "hujjat",
        "amaldagi",
        "Shahar ko'cha-yo'llari",
        "SHNQ 2.07.06-24",
        "amaldagi",
        SOURCES["LEX_UZ"],
        "Piyoda, transport va harakat xavfsizligi talablari alohida qismlar bilan belgilanadi.",
        "reference",
    ),
)


# ============================================================
# 15. TOM
# ============================================================

add(
    "Tom va tom qoplamalari",
    norm(
        "Tom",
        "Asosiy normativ",
        "SHNQ 2.03.10-24",
        "hujjat",
        "amaldagi",
        "Tomlar va tom qoplamalari",
        "SHNQ 2.03.10-24",
        "amaldagi",
        SOURCES["SHNQ_2_03_10_24"],
        "Tom konstruksiyasi va qoplamasi bo'yicha asosiy hujjat.",
        "reference",
    ),
)


# ============================================================
# 16. SUV
# ============================================================

add(
    "Ichki suv ta'minoti",
    norm(
        "Suv",
        "Asosiy normativ",
        "SHNQ 2.04.01-22",
        "hujjat",
        "amaldagi",
        "Binolarning ichki suv ta'minoti va oqova suvlari",
        "SHNQ 2.04.01-22",
        "amaldagi",
        SOURCES["SHNQ_2_04_01_22"],
        "Diametr, sarf va bosim alohida hisoblanadi.",
        "reference",
    ),
)


# ============================================================
# 17. VENTILYATSIYA
# ============================================================

add(
    "Isitish va ventilyatsiya",
    norm(
        "Ventilyatsiya",
        "Asosiy normativ",
        "SHNQ 2.04.05-22",
        "hujjat",
        "amaldagi",
        "Isitish, ventilyatsiya va konditsiyalash",
        "SHNQ 2.04.05-22",
        "amaldagi",
        SOURCES["SHNQ_2_04_05_22"],
        "Havo almashinuvi xona vazifasi bo'yicha hisoblanadi.",
        "reference",
    ),
)


# ============================================================
# 18. YORITISH
# ============================================================

add(
    "Tabiiy va sun'iy yoritish",
    norm(
        "Yoritish",
        "Asosiy normativ",
        "SHNQ 2.01.05-24",
        "hujjat",
        "amaldagi",
        "Tabiiy va sun'iy yoritish",
        "SHNQ 2.01.05-24",
        "amaldagi",
        SOURCES["SHNQ_2_01_05_24"],
        "Yoritish qiymati xona funksiyasi bo'yicha aniqlanadi.",
        "reference",
    ),
)


# ============================================================
# 19. TURAR JOY
# ============================================================

add(
    "Turar joy obyektlari",
    norm(
        "Turar joy",
        "Asosiy normativ",
        "SHNQ 2.08.01-24",
        "hujjat",
        "amaldagi",
        "Turar joy obyektlarini loyihalash",
        "SHNQ 2.08.01-24",
        "amaldagi",
        SOURCES["SHNQ_2_08_01_24"],
        "2026-yilgi o'zgartirishlar bilan amaldagi tahrir tekshiriladi.",
        "reference",
    ),
)


# ============================================================
# 20. JAMOAT BINOLARI
# ============================================================

add(
    "Jamoat binolari",
    norm(
        "Jamoat binosi",
        "Asosiy normativ",
        "SHNQ 2.08.02-23",
        "hujjat",
        "amaldagi",
        "Jamoat binolari va inshootlari",
        "SHNQ 2.08.02-23",
        "amaldagi",
        SOURCES["SHNQ_2_08_02_23"],
        "Funksional guruhga qarab qo'shimcha talablar mavjud.",
        "reference",
    ),
)


# ============================================================
# QO'SHIMCHA HISOBLANGAN PARAMETRLAR
# ============================================================

CALCULATED_VALUES = {
    "5%": round(percent_to_degree(5), 2),
    "10%": round(percent_to_degree(10), 2),
    "16%": round(percent_to_degree(16), 2),

    "1:20": round(ratio_to_degree(20), 2),
    "1:10": round(ratio_to_degree(10), 2),
    "1:5": round(ratio_to_degree(5), 2),
    "1:4": round(ratio_to_degree(4), 2),
    "1:3": round(ratio_to_degree(3), 2),
    "1:2": round(ratio_to_degree(2), 2),
    "1:1": round(ratio_to_degree(1), 2),
}


# ============================================================
# NORMATIV HUJJATLAR REESTRI
# ============================================================

NORMATIVE_REGISTER = {

    "SHNQ 2.08.01-24": {
        "nomi": "Turar joy obyektlarini loyihalash",
        "manba": SOURCES["SHNQ_2_08_01_24"],
    },

    "SHNQ 2.08.02-23": {
        "nomi": "Jamoat binolari va inshootlari",
        "manba": SOURCES["SHNQ_2_08_02_23"],
    },

    "SHNQ 2.08.06-23": {
        "nomi": "Ta'lim tashkilotlari",
        "manba": SOURCES["SHNQ_2_08_06_23"],
    },

    "SHNQ 2.09.02-23": {
        "nomi": "Ishlab chiqarish va ma'muriy-maishiy binolar",
        "manba": SOURCES["SHNQ_2_09_02_23"],
    },

    "SHNQ 2.09.03-23": {
        "nomi": "Omborxonalar",
        "manba": SOURCES["SHNQ_2_09_03_23"],
    },

    "SHNQ 2.05.07-24": {
        "nomi": "Avtoturargohlar",
        "manba": SOURCES["SHNQ_2_05_07_24"],
    },

    "SHNQ 2.07.01-23": {
        "nomi": "Aholi punktlari hududlarini rejalashtirish",
        "manba": SOURCES["SHNQ_2_07_01_23"],
    },

    "SHNQ 2.07.02-24": {
        "nomi": "To'siqsiz muhit va inklyuziv loyihalash",
        "manba": SOURCES["SHNQ_2_07_02_24"],
    },

    "SHNQ 2.04.01-22": {
        "nomi": "Ichki suv ta'minoti va oqova suv",
        "manba": SOURCES["SHNQ_2_04_01_22"],
    },

    "SHNQ 2.04.05-22": {
        "nomi": "Isitish, ventilyatsiya va konditsiyalash",
        "manba": SOURCES["SHNQ_2_04_05_22"],
    },

    "SHNQ 2.01.05-24": {
        "nomi": "Tabiiy va sun'iy yoritish",
        "manba": SOURCES["SHNQ_2_01_05_24"],
    },

    "SHNQ 2.03.10-24": {
        "nomi": "Tomlar va tom qoplamalari",
        "manba": SOURCES["SHNQ_2_03_10_24"],
    },
}


# ============================================================
# QIDIRUV FUNKSIYALARI
# ============================================================

def get_dimension(name):
    return REVIT_DIMENSIONS.get(name)


def get_dimension_names():
    return list(REVIT_DIMENSIONS.keys())


def get_dimensions_by_category(category):

    return {
        name: data
        for name, data in REVIT_DIMENSIONS.items()
        if data["kategoriya"].lower() == category.lower()
    }


def search_dimensions(keyword):

    keyword = keyword.lower()

    result = {}

    for name, data in REVIT_DIMENSIONS.items():

        text = " ".join(
            [
                name,
                str(data.get("kategoriya", "")),
                str(data.get("parametr", "")),
                str(data.get("qollanish", "")),
                str(data.get("hujjat", "")),
                str(data.get("band", "")),
            ]
        ).lower()

        if keyword in text:
            result[name] = data

    return result


def get_normative_documents():
    return NORMATIVE_REGISTER


# ============================================================
# STATISTIKA
# ============================================================

def print_statistics():

    print("=" * 70)
    print("ARCHHELP — NORMATIV BAZA STATISTIKASI")
    print("=" * 70)

    print("Jami parametrlar:", len(REVIT_DIMENSIONS))

    categories = {}

    for data in REVIT_DIMENSIONS.values():

        category = data["kategoriya"]

        categories[category] = categories.get(category, 0) + 1

    print()
    print("KATEGORIYALAR:")

    for category, count in sorted(categories.items()):

        print(f"- {category}: {count} ta")

    print()
    print("NORMATIV HUJJATLAR:")

    for document, info in NORMATIVE_REGISTER.items():

        print(f"- {document} — {info['nomi']}")

    print()
    print("HISOBLANGAN NISHABLIKLAR:")

    for name, value in CALCULATED_VALUES.items():

        print(f"- {name} = {value}°")

    print("=" * 70)


# ============================================================
# ELEMENTNI CHIQARISH
# ============================================================

def print_dimension(name):

    data = get_dimension(name)

    if not data:

        print("Normativ topilmadi:", name)
        return

    print("=" * 70)

    print("ELEMENT:", name)
    print("Kategoriya:", data["kategoriya"])
    print("Parametr:", data["parametr"])
    print("Qiymat:", data["qiymat"])
    print("Birlik:", data["birlik"])
    print("Chegara:", data["chegara"])
    print("Status:", data["status"])
    print("Qo'llanish:", data["qollanish"])
    print("Hujjat:", data["hujjat"])
    print("Band:", data["band"])
    print("Izoh:", data["izoh"])
    print("Manba:", data["manba"])

    print("=" * 70)


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("ARCHHELP — REVIT NORMATIV BAZASI")
    print()

    print_statistics()

    print()

    print("NAMUNAVIY NORMATIVLAR:")
    print()

    print_dimension("Ombor tashqi pandusi")

    print()

    print_dimension("Avtoyuklagich rampasi eni")

    print()

    print_dimension("Maktab bufet zali")

    print()

    print_dimension("MTT gimnastika zali")

    print()

    print_dimension("Yotoqxona — talaba 100 kishi")

    print()

    print_dimension("Nogiron ishlovchi zina marsh eni")

    print()

    print_dimension("Jamoat binolari")