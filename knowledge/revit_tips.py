REVIT_TIPS = {

    "Revitni tezlashtirish": {
        "tushuntirish": "Revit sekinlashishining asosiy sabablari og‘ir familylar, keraksiz CAD fayllar, yuqori poligonli obyektlar va ortiqcha viewlardir.",
        "maslahat": "Keraksiz view, import qilingan CAD, og‘ir family va yuqori poligonli 3D obyektlarni kamaytir.",
        "qadamlar": [
            "Keraksiz CAD importlarni o‘chir yoki Link qil.",
            "Og‘ir familylarni yengillashtir.",
            "Keraksiz 3D elementlarni o‘chir.",
            "Purge Unused orqali ishlatilmayotgan elementlarni tozalab tur."
        ],
        "misol": "500 MB dan katta modelda keraksiz CAD va og‘ir familylarni kamaytirish Revitning ishlashini sezilarli yaxshilashi mumkin.",
        "foyda": "Model tezroq ochiladi, saqlanadi va ishlaydi."
    },

    "CAD bilan to‘g‘ri ishlash": {
        "tushuntirish": "DWG fayllarni Revitga qo‘shishda Link CAD odatda Import CADga qaraganda qulayroq. Link qilingan fayl tashqi manba sifatida boshqariladi va kerak bo‘lganda yangilanadi.",
        "maslahat": "DWG faylni imkon qadar Import emas, Link CAD orqali ulash.",
        "qadamlar": [
            "Insert → Link CAD buyrug‘ini tanla.",
            "DWG faylni tanla.",
            "Kerakli Units ni tekshir.",
            "Current View Only kerak bo‘lsa yoq.",
            "Keraksiz layerlarni CAD faylining o‘zida tozalab ol."
        ],
        "misol": "Arxitektura planidagi mavjud DWGni Revitga asos sifatida qo‘shishda Insert → Link CAD ishlatish mumkin.",
        "foyda": "Revit modeli ortiqcha og‘irlashmaydi va CAD faylni tashqi manba sifatida boshqarish osonlashadi."
    },

    "Familylarni optimallashtirish": {
        "tushuntirish": "Family ichidagi ortiqcha geometriya va juda ko‘p nested elementlar loyiha hajmini oshirishi mumkin.",
        "maslahat": "Family ichida ortiqcha 3D geometriya va juda ko‘p detail ishlatmaslik kerak.",
        "qadamlar": [
            "Keraksiz solidlarni kamaytir.",
            "Nested Family sonini nazorat qil.",
            "Detail Level bo‘yicha geometriyani boshqar.",
            "Kerak bo‘lmagan parametrlarni olib tashla."
        ],
        "misol": "Oddiy stol familysi uchun ko‘rinmaydigan murakkab bolt va vintlarni yuqori poligonli 3D shaklda yaratish shart emas.",
        "foyda": "Model performance yaxshilanadi."
    },

    "View Template ishlatish": {
        "tushuntirish": "View Template bir nechta viewlarda bir xil grafik va ko‘rinish sozlamalarini standartlashtirishga yordam beradi.",
        "maslahat": "Bir xil grafik sozlamalarni qo‘lda qayta-qayta o‘zgartirma. View Template ishlat.",
        "qadamlar": [
            "View → View Templates bo‘limini och.",
            "Kerakli template yarat.",
            "Scale, Visibility, Detail Level va grafik sozlamalarni belgila.",
            "Bir nechta viewga bir xil template ber."
        ],
        "misol": "Barcha 1-qavat planlariga bir xil grafik ko‘rinish berish uchun bitta View Template yaratish mumkin.",
        "foyda": "Loyiha grafikasi bir xil va tartibli bo‘ladi."
    },

    "Project Browserni tartiblash": {
        "tushuntirish": "Katta Revit loyihalarida viewlar ko‘payganda Project Browserni tartiblash ish jarayonini ancha tezlashtiradi.",
        "maslahat": "Katta loyihalarda Project Browser tartibsiz bo‘lsa, kerakli viewni topish qiyinlashadi.",
        "qadamlar": [
            "Browser Organizationni och.",
            "Viewlarni discipline bo‘yicha ajrat.",
            "Floor Plan, Ceiling Plan, Section va 3D viewlarni tartibla.",
            "Nomlash standartidan foydalan."
        ],
        "misol": "A-101, A-102 kabi standart nomlar orqali arxitektura viewlarini tez topish mumkin.",
        "foyda": "Loyihada navigatsiya ancha osonlashadi."
    },

    "View va Sheet nomlash": {
        "tushuntirish": "View va Sheet nomlarini boshidan standart asosida berish katta loyihalarda hujjatlarni boshqarishni osonlashtiradi.",
        "maslahat": "View va sheet nomlarini boshidan standart asosida ber.",
        "qadamlar": [
            "Loyiha nomlash standartini oldindan belgila.",
            "Viewlarni bir xil formatda nomla.",
            "Sheet raqamlarini tartibli ber.",
            "Bir xil nomdagi viewlarni takrorlashdan saqlan."
        ],
        "misol": "A-101 — 1-qavat plan; A-201 — fasad; A-301 — kesim.",
        "foyda": "Loyiha professional va tushunarli ko‘rinadi."
    },

    "Workset bilan ishlash": {
        "tushuntirish": "Worksetlar katta yoki jamoaviy loyihalarda elementlarni mantiqiy guruhlarga ajratib boshqarishga yordam beradi.",
        "maslahat": "Katta loyihalarda Worksetlardan foydalanish modelni boshqarishni osonlashtiradi.",
        "qadamlar": [
            "Arxitektura elementlarini mantiqiy guruhlarga ajrat.",
            "Keraksiz Worksetlarni ochiq qoldirma.",
            "Workset nomlarini standartlashtir.",
            "Central Model bilan ishlaganda Synchronize with Centralni vaqtida bajar."
        ],
        "misol": "Architecture, Interior va Furniture kabi Worksetlar orqali elementlarni alohida boshqarish mumkin.",
        "foyda": "Jamoaviy ishlash va model boshqaruvi yaxshilanadi."
    },

    "Modelni muntazam tozalash": {
        "tushuntirish": "Loyiha davomida ishlatilmayotgan family, material, view va boshqa elementlar yig‘ilib borishi mumkin.",
        "maslahat": "Loyiha davomida modelda keraksiz elementlar yig‘ilib borishiga yo‘l qo‘ymaslik kerak.",
        "qadamlar": [
            "Purge Unused ishlat.",
            "Warninglarni tekshir.",
            "Keraksiz View va Sheetlarni o‘chir.",
            "Ortiqcha CAD va familylarni tekshir."
        ],
        "misol": "Sinov uchun yuklangan, lekin ishlatilmayotgan familylarni Purge Unused orqali aniqlash mumkin.",
        "foyda": "Model toza va boshqariladigan holatda qoladi."
    },

    "Warninglarni nazorat qilish": {
        "tushuntirish": "Revit warninglari modeldagi overlap, duplicate instance va boshqa muammolar haqida xabar beradi.",
        "maslahat": "Warninglarni yig‘ilib ketguncha kutmaslik kerak.",
        "qadamlar": [
            "Warnings oynasini muntazam tekshir.",
            "Duplicate Instanceslarni aniqlab o‘chir.",
            "Overlap muammolarini tuzat.",
            "Critical warninglarni alohida nazorat qil."
        ],
        "misol": "Bir xil joyda ikkita devor turib qolsa, Revit duplicate yoki overlap haqida warning berishi mumkin.",
        "foyda": "Keyinchalik katta model xatolarining oldi olinadi."
    },

    "Room bilan ishlash": {
        "tushuntirish": "Room maydon va hajmlarni aniqlashda xona chegaralaridan foydalanadi. Shuning uchun chegaralar to‘g‘ri tashkil qilinishi muhim.",
        "maslahat": "Room noto‘g‘ri chiqsa, avvalo xona chegaralari yopiq ekanini tekshir.",
        "qadamlar": [
            "Room Separation Lines mavjudligini tekshir.",
            "Devorlarning Room Bounding holatini tekshir.",
            "Room chegarasida bo‘shliq yo‘qligini tekshir.",
            "Room Calculation Point sozlamalarini tekshir."
        ],
        "misol": "Devor Room Bounding bo‘lmasa, xona maydoni kutilganidan boshqacha hisoblanishi mumkin.",
        "foyda": "Xona maydonlari aniqroq hisoblanadi."
    },

    "Levelni to‘g‘ri tashkil qilish": {
        "tushuntirish": "Level Revitdagi qavatlar va balandliklarni boshqaruvchi asosiy datum elementlardan biridir.",
        "maslahat": "Level nomlari va balandliklarini loyiha boshida tartibga sol.",
        "qadamlar": [
            "Asosiy ±0.000 balandlikni belgila.",
            "Har bir qavat uchun Level yarat.",
            "Level nomlarini standartlashtir.",
            "Keraksiz Levellarni ko‘paytirma."
        ],
        "misol": "±0.000, +3.300, +6.600, +9.900.",
        "foyda": "Qavatlar, planlar, sectionlar va elementlar bilan ishlash osonlashadi."
    },

    "Grid bilan ishlash": {
        "tushuntirish": "Gridlar binoning asosiy konstruktiv va geometrik o‘qlarini tashkil qilishda ishlatiladi.",
        "maslahat": "Gridlarni bino konstruktiv o‘qlariga mos va mantiqiy tartibda joylashtir.",
        "qadamlar": [
            "Asosiy o‘qlarni boshidan belgila.",
            "Grid nomlarini tartibli ber.",
            "Keraksiz gridlarni ko‘paytirma.",
            "Fasad va sectionlarda grid ko‘rinishini tekshir."
        ],
        "misol": "Vertikal o‘qlar 1, 2, 3, 4; gorizontal o‘qlar A, B, C, D tarzida tashkil qilinishi mumkin.",
        "foyda": "Bino geometriyasini boshqarish ancha osonlashadi."
    },

    "Coordinatesni to‘g‘ri sozlash": {
        "tushuntirish": "Revitdagi Project Base Point, Survey Point, Project North va True North koordinatalar tizimini boshqarishda muhim.",
        "maslahat": "Katta loyiha yoki boshqa dasturlar bilan ishlaganda koordinatalarni boshidan to‘g‘ri tashkil qil.",
        "qadamlar": [
            "Project Base Pointni tekshir.",
            "Survey Pointni tekshir.",
            "True North va Project North farqini tushun.",
            "Link modellarda koordinatalarni tekshir."
        ],
        "misol": "Arxitektura modeli bilan boshqa Revit modelini birlashtirishda Shared Coordinates ishlatilishi mumkin.",
        "foyda": "CAD, Revit va boshqa modellarni bir-biriga to‘g‘ri joylashtirish osonlashadi."
    },

    "Link va Import farqi": {
        "tushuntirish": "Link tashqi faylni model bilan bog‘lab turadi, Import esa fayl ma’lumotlarini loyiha ichiga olib kiradi. Qaysi usul kerakligi ish jarayoniga bog‘liq.",
        "maslahat": "Tashqi faylni loyihaga qo‘shishda Link va Import farqini hisobga ol.",
        "qadamlar": [
            "Fayl doimiy yangilanib turadimi — tekshir.",
            "Yangilanadigan tashqi fayllar uchun Link variantini ko‘rib chiq.",
            "Fayl loyiha ichida mustaqil bo‘lishi kerak bo‘lsa Import kerak bo‘lishi mumkin.",
            "Import qilingan og‘ir geometriyalarni nazorat qil."
        ],
        "misol": "DWG fayli tez-tez yangilanadigan loyiha uchun Link CAD qulay bo‘lishi mumkin.",
        "foyda": "Asosiy loyiha keragidan ortiq og‘irlashishining oldini olishga yordam beradi."
    },

    "Backup qilish": {
        "tushuntirish": "Backup loyiha fayli buzilganda yoki noto‘g‘ri o‘zgarish qilinganda oldingi holatga qaytish imkonini beradi.",
        "maslahat": "Muhim loyiha faylining alohida backup nusxasini saqla.",
        "qadamlar": [
            "Loyiha bosqichlarini alohida nusxala.",
            "Muhim revisionlardan oldin backup qil.",
            "Central Model bilan ishlaganda backup tizimini nazorat qil.",
            "Backupni faqat kompyuterning bitta papkasida saqlab qo‘yma."
        ],
        "misol": "Muhim topshirishdan oldin loyiha faylining alohida sana bilan nomlangan nusxasini saqlash mumkin.",
        "foyda": "Fayl buzilganda yoki xato qilinganda loyihani tiklash imkoniyati bo‘ladi."
    },

    "Render uchun model tayyorlash": {
        "tushuntirish": "Renderdan oldin modeldagi keraksiz geometriya, material va yuqori poligonli obyektlarni nazorat qilish render jarayonini yengillashtiradi.",
        "maslahat": "Renderdan oldin ko‘rinmaydigan yoki keraksiz geometriyani kamaytir.",
        "qadamlar": [
            "Kamera ko‘rinishidan tashqaridagi keraksiz detallarni tekshir.",
            "Materiallarni tartibla.",
            "High-poly obyektlarni nazorat qil.",
            "Lighting va exposure sozlamalarini tekshir."
        ],
        "misol": "Interyer renderida kameraga umuman tushmaydigan keraksiz 3D obyektlarni kamaytirish mumkin.",
        "foyda": "Render tezligi va umumiy loyiha performance yaxshilanadi."
    },

    "Materiallarni tartiblash": {
        "tushuntirish": "Material nomlarini standartlashtirish loyiha davomida kerakli materialni tez topish va almashtirishga yordam beradi.",
        "maslahat": "Material nomlarini boshidan standartlashtir.",
        "qadamlar": [
            "Material nomlash standartini belgila.",
            "Bir xil materiallarni keraksiz takrorlama.",
            "Materiallarni kategoriya bo‘yicha tartibla.",
            "Keraksiz materiallarni tekshir."
        ],
        "misol": "Concrete_Gray, Brick_Red, Glass_Clear, Wood_Oak.",
        "foyda": "Materiallarni topish va almashtirish osonlashadi."
    },

    "Dimensionlarni tartibli ishlatish": {
        "tushuntirish": "Dimensionlar chizmada bino geometriyasini tushuntirish va tekshirish uchun aniq iyerarxiyada joylashtirilishi kerak.",
        "maslahat": "Dimensionlarni tasodifiy joylashtirma. Muhim o‘lchamlarni aniq iyerarxiyada ber.",
        "qadamlar": [
            "Umumiy bino o‘lchamlarini ber.",
            "O‘qlar orasidagi masofalarni ko‘rsat.",
            "Xona va devor o‘lchamlarini ber.",
            "Eshik va deraza o‘lchamlarini ko‘rsat."
        ],
        "misol": "Avval bino umumiy uzunligi, keyin o‘qlar va undan keyin ichki xona o‘lchamlari beriladi.",
        "foyda": "Chizma o‘qilishi va tekshirilishi osonlashadi."
    },

    "Modelni juda katta qilib yubormaslik": {
        "tushuntirish": "Juda katta va og‘ir Revit modeli ishlash tezligini pasaytirishi mumkin. Modelni mantiqiy qismlarga ajratish ayrim loyihalarda foydali.",
        "maslahat": "Bitta Revit modeliga keraksiz barcha narsani tiqishtirma.",
        "qadamlar": [
            "Katta binolarni zarurat bo‘lsa link modellarga ajrat.",
            "Og‘ir familylarni optimallashtir.",
            "Keraksiz geometriyani olib tashla.",
            "CAD importlarini nazorat qil."
        ],
        "misol": "Katta majmuada arxitektura, interyer yoki boshqa qismlarni alohida link modellarda tashkil qilish mumkin.",
        "foyda": "Katta loyihalarda Revit barqarorroq ishlashi mumkin."
    },

    "Revitni yopishdan oldin": {
        "tushuntirish": "Revitni yopishdan oldin oxirgi o‘zgarishlarni saqlash va markaziy model bilan ishlayotgan bo‘lsang sinxronlash muhim.",
        "maslahat": "Dasturdan chiqishdan oldin loyihani saqlash va muhim o‘zgarishlarni tekshirish odat bo‘lsin.",
        "qadamlar": [
            "Save qil.",
            "Markaziy model bo‘lsa Synchronize with Central qil.",
            "Muhim warninglarni tekshir.",
            "Backup nusxasini nazorat qil."
        ],
        "misol": "Ish tugagach Save → Synchronize with Central → kerak bo‘lsa backup tekshiruvi.",
        "foyda": "Mehnatni yo‘qotish xavfi kamayadi."
    },

    "Professional workflow": {
        "tushuntirish": "Revitda tartibli workflow loyiha boshidan oxirigacha bir xil mantiq asosida ishlashga yordam beradi. Avval asosiy geometriya, keyin detallar va hujjatlashtirish bajariladi.",
        "maslahat": "Revitda avval bino skeletini, keyin detallarni qurish eng qulay usullardan biri.",
        "qadamlar": [
            "Project Units va Levelsni sozla.",
            "Gridlarni yarat.",
            "Asosiy devor va konstruksiyalarni qur.",
            "Eshik va derazalarni joylashtir.",
            "Room va zonalarni tashkil qil.",
            "Views va Sheetslarni tartibla.",
            "Dimension va annotationlarni qo‘sh.",
            "Material va grafikalarni sozla.",
            "Print/PDF chiqarishdan oldin tekshir."
        ],
        "misol": "Avval Level va Grid → keyin devorlar → eshik/derazalar → Room → Sheets → dimension va annotationlar.",
        "foyda": "Loyiha boshidan oxirigacha tartibli yuritiladi."
    }
}


def get_revit_tip(tip_name):
    return REVIT_TIPS.get(tip_name)


def get_revit_tip_names():
    return list(REVIT_TIPS.keys())


if __name__ == "__main__":
    print(f"REVIT FOYDALI MASLAHATLARI: {len(REVIT_TIPS)} ta")