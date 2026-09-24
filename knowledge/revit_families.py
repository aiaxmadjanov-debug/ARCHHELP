REVIT_FAMILIES = {

    "Family nima?": {
        "kategoriya": "Asoslar",
        "vazifasi": "Revitdagi model elementlari Family asosida tashkil qilinadi.",
        "tushuntirish": "Door, Window, Furniture, Lighting va ko‘plab boshqa elementlar Family orqali boshqariladi.",
        "misol": "Bir xil eshikning 900x2100 mm va 1000x2100 mm variantlari bitta Family ichidagi Type bo‘lishi mumkin.",
        "maslahat": "Family, Type va Instance farqini tushunish Revitda juda muhim."
    },

    "System Family": {
        "kategoriya": "Family turlari",
        "vazifasi": "Revitning o‘zida mavjud bo‘lgan Family turidir.",
        "tushuntirish": "Wall, Floor, Roof, Ceiling, Stair kabi elementlar System Family hisoblanadi.",
        "misol": "Basic Wall yoki Floor Type.",
        "maslahat": "System Family odatda Project ichida Type sifatida boshqariladi."
    },

    "Loadable Family": {
        "kategoriya": "Family turlari",
        "vazifasi": "Alohida RFA fayl sifatida yaratiladigan va loyihaga yuklanadigan Family.",
        "tushuntirish": "Door, Window, Furniture, Plumbing Fixture va boshqa ko‘plab obyektlar Loadable Family bo‘lishi mumkin.",
        "misol": "Furniture Chair.rfa.",
        "maslahat": "Kerakli Familyni Load into Project orqali loyihaga yuklash mumkin."
    },

    "In-Place Family": {
        "kategoriya": "Family turlari",
        "vazifasi": "Faqat ma’lum loyiha uchun Project ichida yaratiladigan maxsus element.",
        "tushuntirish": "Standart Family mos kelmaydigan noyob geometriyalar uchun ishlatiladi.",
        "misol": "Noodatiy shakldagi dekorativ fasad elementi.",
        "maslahat": "In-Place Familyni haddan tashqari ko‘p ishlatish modelni og‘irlashtirishi mumkin."
    },

    "Type nima?": {
        "kategoriya": "Asoslar",
        "vazifasi": "Bitta Family ichidagi oldindan belgilangan variantni ifodalaydi.",
        "tushuntirish": "Type parametrlari o‘sha Type'ga tegishli barcha instance'larga ta’sir qiladi.",
        "misol": "Door 900x2100 va Door 1000x2100.",
        "maslahat": "Bir xil parametrli ko‘p element kerak bo‘lsa Type yaratish qulay."
    },

    "Instance Parameter": {
        "kategoriya": "Parametrlar",
        "vazifasi": "Faqat tanlangan elementning parametrini boshqaradi.",
        "tushuntirish": "Bir Family'dagi har bir element Instance parameter orqali alohida qiymatga ega bo‘lishi mumkin.",
        "misol": "Bitta derazaning sill height qiymatini boshqasidan alohida o‘zgartirish.",
        "maslahat": "Elementlar bir-biridan farq qilishi kerak bo‘lsa Instance parameter ishlat."
    },

    "Type Parameter": {
        "kategoriya": "Parametrlar",
        "vazifasi": "Bitta Type'ga tegishli barcha elementlarni boshqaradi.",
        "tushuntirish": "Type parameter o‘zgartirilsa, shu Type'dagi barcha instance'larga ta’sir qiladi.",
        "misol": "Bitta Door Type kengligini 900 mm dan 1000 mm ga o‘zgartirish.",
        "maslahat": "Bir xil standartni ko‘p elementga qo‘llash uchun Type parameter qulay."
    },

    "Family Editor": {
        "kategoriya": "Yaratish",
        "vazifasi": "Family yaratish va tahrirlash uchun maxsus muhit.",
        "tushuntirish": "Family Editor ichida reference plane, parameter, geometry va boshqa elementlar bilan ishlanadi.",
        "misol": "Parametrik stol yoki eshik Family yaratish.",
        "maslahat": "Family yaratishni reference plane va constraints bilan boshlash yaxshi amaliyot."
    },

    "New Family": {
        "kategoriya": "Yaratish",
        "vazifasi": "Yangi Family yaratish.",
        "tushuntirish": "Kerakli Family template tanlanadi va Family Editor ochiladi.",
        "misol": "Metric Generic Model template orqali obyekt yaratish.",
        "maslahat": "Family turiga mos template tanlash juda muhim."
    },

    "Family Template": {
        "kategoriya": "Yaratish",
        "vazifasi": "Family yaratish uchun boshlang‘ich shablon.",
        "tushuntirish": "Door, Window, Furniture, Generic Model va boshqa maqsadlar uchun turli template mavjud.",
        "misol": "Metric Door.rft.",
        "maslahat": "Noto‘g‘ri template tanlansa Familyning host va parametrik xatti-harakati noto‘g‘ri bo‘lishi mumkin."
    },

    "Reference Plane": {
        "kategoriya": "Parametrik model",
        "vazifasi": "Family geometriyasini boshqaruvchi tayanch tekislik yaratish.",
        "tushuntirish": "Reference Plane Family ichidagi asosiy o‘lcham va constraintlarni boshqarishda ishlatiladi.",
        "misol": "Stolning chap, o‘ng, old va orqa chegaralarini belgilash.",
        "maslahat": "Geometriyani to‘g‘ridan-to‘g‘ri boshqa elementga bog‘lashdan ko‘ra Reference Plane bilan boshqarish barqarorroq."
    },

    "Reference Line": {
        "kategoriya": "Parametrik model",
        "vazifasi": "Family ichida yo‘nalish yoki aylanish uchun tayanch chiziq yaratish.",
        "tushuntirish": "Murakkab va aylanuvchi geometriyalarni boshqarishda foydali.",
        "misol": "Aylanuvchi quyosh soyaboni yoki parametrik panel.",
        "maslahat": "Oddiy tekis tayanchlar uchun Reference Plane yetarli bo‘lishi mumkin."
    },

    "Dimension Parameter": {
        "kategoriya": "Parametrlar",
        "vazifasi": "Family o‘lchamlarini parametr orqali boshqarish.",
        "tushuntirish": "Dimension qiymatini parametrga bog‘lab, Family o‘lchamini keyinchalik o‘zgartirish mumkin.",
        "misol": "Width = 900 mm, Height = 2100 mm.",
        "maslahat": "Parametr nomlarini tushunarli va standart tarzda ber."
    },

    "Family Parameter": {
        "kategoriya": "Parametrlar",
        "vazifasi": "Family ichida geometriya va ma’lumotlarni boshqaruvchi parametr.",
        "tushuntirish": "Length, Width, Height, Material va boshqa qiymatlarni boshqarishi mumkin.",
        "misol": "Table_Width yoki Door_Height.",
        "maslahat": "Keraksiz parametrlarni ko‘paytirma."
    },

    "Shared Parameter": {
        "kategoriya": "Parametrlar",
        "vazifasi": "Turli Family va loyihalarda umumiy foydalanish mumkin bo‘lgan parametr.",
        "tushuntirish": "Schedule, Tag va boshqa hujjatlashtirish jarayonlarida juda foydali.",
        "misol": "Mark, Manufacturer yoki Fire Rating.",
        "maslahat": "Katta BIM loyihalarda Shared Parameter tizimini boshidan standartlashtir."
    },

    "Material Parameter": {
        "kategoriya": "Parametrlar",
        "vazifasi": "Family geometriyasining materialini parametr orqali boshqarish.",
        "tushuntirish": "Materialni Family ichidagi parametrga bog‘lash mumkin.",
        "misol": "Chair Material yoki Door Frame Material.",
        "maslahat": "Material parameter yordamida bitta Family'dan bir nechta variant yaratish mumkin."
    },

    "Associate Family Parameter": {
        "kategoriya": "Parametrlar",
        "vazifasi": "Nested Family parametrini asosiy Family parametriga bog‘lash.",
        "tushuntirish": "Nested Family ichidagi parametrni host Family orqali boshqarish imkonini beradi.",
        "misol": "Eshik ichidagi tutqich turini asosiy Door Family'dan boshqarish.",
        "maslahat": "Murakkab parametrik Family yaratishda juda foydali."
    },

    "Nested Family": {
        "kategoriya": "Murakkab Family",
        "vazifasi": "Bitta Family ichiga boshqa Family joylashtirish.",
        "tushuntirish": "Murakkab obyektlarni modulli tarzda yaratish imkonini beradi.",
        "misol": "Eshik Family ichida Door Handle Family.",
        "maslahat": "Nested Family sonini keragidan ortiq ko‘paytirma."
    },

    "Shared Nested Family": {
        "kategoriya": "Murakkab Family",
        "vazifasi": "Nested Family'ni Project ichida alohida schedule yoki tag qilish imkonini beradigan usul.",
        "tushuntirish": "Nested Family Shared bo‘lsa, ayrim holatlarda loyiha ichida alohida element sifatida ishlashi mumkin.",
        "misol": "Yoritgich ichidagi alohida lampalar.",
        "maslahat": "Faqat haqiqatan alohida hisob yoki identifikatsiya kerak bo‘lsa Shared qil."
    },

    "Flex Family": {
        "kategoriya": "Test",
        "vazifasi": "Family parametrlarini o‘zgartirib, geometriyaning to‘g‘ri ishlashini tekshirish.",
        "tushuntirish": "Familyning turli o‘lchamlarda buzilmasdan ishlashi test qilinadi.",
        "misol": "Width 600, 900, 1200 mm qilib tekshirish.",
        "maslahat": "Familyni Projectga yuklashdan oldin turli qiymatlarda Flex qilib ko‘r."
    },

    "Lock Geometry": {
        "kategoriya": "Parametrik model",
        "vazifasi": "Geometriyani Reference Plane yoki boshqa tayanchga bog‘lash.",
        "tushuntirish": "Lock orqali elementning kerakli holati saqlanadi.",
        "misol": "Eshik geometriyasini Left va Right Reference Plane'ga bog‘lash.",
        "maslahat": "Keraksiz locklardan foydalanish constraint muammolarini keltirib chiqarishi mumkin."
    },

    "Family Constraint": {
        "kategoriya": "Parametrik model",
        "vazifasi": "Family elementlari orasidagi geometrik bog‘lanishni nazorat qilish.",
        "tushuntirish": "Equal, Align, Lock va boshqa constraintlar ishlatiladi.",
        "misol": "Deraza ramkasini markazga tenglashtirish.",
        "maslahat": "Constraintlarni minimal va mantiqiy qilib tuz."
    },

    "Equal Constraint": {
        "kategoriya": "Parametrik model",
        "vazifasi": "Ikki yoki undan ko‘p masofani tenglashtirish.",
        "tushuntirish": "Geometriyaning markazda yoki simmetrik joylashishida foydali.",
        "misol": "Panelning ikki yonidagi masofani teng qilish.",
        "maslahat": "Simmetrik Familylar uchun juda foydali."
    },

    "Void Form": {
        "kategoriya": "Geometriya",
        "vazifasi": "Solid geometriyadan materialni kesib olish.",
        "tushuntirish": "Eshik, deraza, teshik va murakkab kesimlarni yaratishda ishlatiladi.",
        "misol": "Devordagi maxsus dekorativ opening.",
        "maslahat": "Void geometriyasini keragidan ortiq murakkablashtirma."
    },

    "Extrusion": {
        "kategoriya": "Geometriya",
        "vazifasi": "2D profilni to‘g‘ri yo‘nalishda cho‘zib 3D solid yaratish.",
        "tushuntirish": "Family yaratishda eng ko‘p ishlatiladigan geometriya usullaridan biri.",
        "misol": "Oddiy stol usti yoki eshik paneli.",
        "maslahat": "Oddiy shakllarda Extrusiondan foydalanish Familyni yengil saqlaydi."
    },

    "Blend": {
        "kategoriya": "Geometriya",
        "vazifasi": "Ikki xil profil orasida o‘zgaruvchi 3D shakl yaratish.",
        "tushuntirish": "Pastki va yuqori profillar orqali shakl hosil qilinadi.",
        "misol": "Dekorativ ustun yoki maxsus mebel detali.",
        "maslahat": "Murakkab geometriya kerak bo‘lganda ishlat."
    },

    "Revolve": {
        "kategoriya": "Geometriya",
        "vazifasi": "Profilni o‘q atrofida aylantirib 3D geometriya yaratish.",
        "tushuntirish": "Aylana asosidagi obyektlar uchun qulay.",
        "misol": "Ustun, vaza yoki dumaloq dekorativ element.",
        "maslahat": "Aylanish o‘qini to‘g‘ri belgila."
    },

    "Sweep": {
        "kategoriya": "Geometriya",
        "vazifasi": "Profilni yo‘l bo‘ylab olib borib 3D geometriya yaratish.",
        "tushuntirish": "Uzun profil yoki molding kabi elementlar uchun ishlatiladi.",
        "misol": "Dekorativ karniz.",
        "maslahat": "Path va Profile mosligini tekshir."
    },

    "Swept Blend": {
        "kategoriya": "Geometriya",
        "vazifasi": "Yo‘l bo‘ylab ikki xil profil orasida o‘zgaruvchi geometriya yaratish.",
        "tushuntirish": "Sweep va Blend imkoniyatlarini birlashtiradi.",
        "misol": "Murakkab dekorativ profil.",
        "maslahat": "Faqat murakkab shakl zarur bo‘lganda ishlat."
    },

    "Family Visibility": {
        "kategoriya": "Grafika",
        "vazifasi": "Family geometriyasining qaysi detail level yoki viewda ko‘rinishini boshqarish.",
        "tushuntirish": "Coarse, Medium va Fine darajalari bo‘yicha ko‘rinishni sozlash mumkin.",
        "misol": "Mebelning Fine viewda batafsil, Coarse viewda soddalashtirilgan ko‘rinishi.",
        "maslahat": "Performance uchun Coarse va Medium ko‘rinishlarini ham to‘g‘ri sozla."
    },

    "Symbolic Lines": {
        "kategoriya": "Grafika",
        "vazifasi": "Family uchun 2D ko‘rinishdagi grafik chiziqlar yaratish.",
        "tushuntirish": "Modelni og‘irlashtirmasdan plan yoki elevationda kerakli grafikani ko‘rsatishga yordam beradi.",
        "misol": "Eshik ochilish yoyini ko‘rsatish.",
        "maslahat": "Model geometriyasi o‘rniga 2D grafik kerak bo‘lsa Symbolic Lines ishlat."
    },

    "Model Lines": {
        "kategoriya": "Grafika",
        "vazifasi": "3D model bilan bog‘langan chiziq yaratish.",
        "tushuntirish": "Model Line turli viewlarda ko‘rinishi mumkin.",
        "misol": "Maxsus dekorativ chiziq yoki konstruktiv belgi.",
        "maslahat": "Oddiy 2D grafik uchun Symbolic Line afzal."
    },

    "Family Category": {
        "kategoriya": "Sozlamalar",
        "vazifasi": "Familyning qaysi Revit kategoriyasiga tegishli ekanini belgilash.",
        "tushuntirish": "Category Familyning Projectdagi xatti-harakatiga va parametrlariga ta’sir qiladi.",
        "misol": "Furniture, Generic Model yoki Lighting Fixtures.",
        "maslahat": "Family yaratishda to‘g‘ri Category tanlash juda muhim."
    },

    "Family Category and Parameters": {
        "kategoriya": "Sozlamalar",
        "vazifasi": "Family Category va unga tegishli parametrik xususiyatlarni sozlash.",
        "tushuntirish": "Familyning hosting, material, visibility va boshqa xususiyatlariga ta’sir qilishi mumkin.",
        "misol": "Door Familyni kerakli kategoriya bilan sozlash.",
        "maslahat": "Categoryni keyinchalik o‘zgartirish har doim ham barcha xatti-harakatni saqlab qolmaydi."
    },

    "Host-based Family": {
        "kategoriya": "Family turlari",
        "vazifasi": "Ma’lum host elementga bog‘lanib ishlaydigan Family.",
        "tushuntirish": "Door va Window kabi elementlar odatda host elementga, masalan devorga bog‘lanadi.",
        "misol": "Derazani faqat devorga joylashtirish.",
        "maslahat": "Family template tanlashda host talabini oldindan aniqlash kerak."
    },

    "Work Plane-based Family": {
        "kategoriya": "Family turlari",
        "vazifasi": "Familyni ma’lum Work Plane'ga joylashtirish.",
        "tushuntirish": "Host kerak bo‘lmagan, lekin ma’lum tekislikka bog‘lanishi kerak bo‘lgan elementlar uchun foydali.",
        "misol": "Maxsus yoritish yoki dekorativ element.",
        "maslahat": "Work Plane noto‘g‘ri bo‘lsa Family kerakli joyga joylashmasligi mumkin."
    },

    "Face-based Family": {
        "kategoriya": "Family turlari",
        "vazifasi": "Familyni boshqa element yuzasiga joylashtirish.",
        "tushuntirish": "Turli yuzalarga moslashadigan komponentlar uchun qulay.",
        "misol": "Devorga yoki shiftga o‘rnatiladigan jihoz.",
        "maslahat": "Host yuzasining yo‘nalishi va normalini hisobga ol."
    },

    "Family Type Catalog": {
        "kategoriya": "Katta Familylar",
        "vazifasi": "Ko‘p Type'li Familylarni kerakli variantlar bilan boshqarish.",
        "tushuntirish": "Type Catalog katta miqdordagi Type'larni boshqarishda foydali.",
        "misol": "Ko‘plab o‘lchamdagi deraza yoki eshik Family.",
        "maslahat": "Juda ko‘p Type'li Familylar uchun Type Catalog modelni yengilroq boshqarishga yordam beradi."
    },

    "Load into Project": {
        "kategoriya": "Project bilan ishlash",
        "vazifasi": "Familyni Family Editor'dan Projectga yuklash.",
        "tushuntirish": "Family tayyor bo‘lgach Projectga yuklanadi va loyihada ishlatiladi.",
        "misol": "Yangi Door Familyni arxitektura loyihasiga qo‘shish.",
        "maslahat": "Yuklashdan oldin Familyni Flex qilib tekshir."
    },

    "Load Family": {
        "kategoriya": "Project bilan ishlash",
        "vazifasi": "RFA fayldagi Familyni loyihaga yuklash.",
        "tushuntirish": "Tayyor Family Librarydan Projectga qo‘shiladi.",
        "misol": "Mebel Familyni Projectga qo‘shish.",
        "maslahat": "Keraksiz Familylarni ko‘p yuklab modelni og‘irlashtirma."
    },

    "Edit Family": {
        "kategoriya": "Tahrirlash",
        "vazifasi": "Project ichidagi Familyni Family Editor'da tahrirlash.",
        "tushuntirish": "Family geometriyasi va parametrlarini o‘zgartirish mumkin.",
        "misol": "Door Family kengligini parametrik qilish.",
        "maslahat": "Tahrirdan keyin Familyni Projectga qayta Load qilish kerak."
    },

    "Save Family": {
        "kategoriya": "Tahrirlash",
        "vazifasi": "Familyni RFA fayl sifatida saqlash.",
        "tushuntirish": "Familyni alohida Library sifatida saqlab, boshqa loyihalarda qayta ishlatish mumkin.",
        "misol": "Office_Door_900x2100.rfa.",
        "maslahat": "Family Library uchun aniq papka va nomlash tizimi yarat."
    },

    "Family Naming": {
        "kategoriya": "Standart",
        "vazifasi": "Family va Type nomlarini tartibli boshqarish.",
        "tushuntirish": "To‘g‘ri nomlash katta loyihalarda kerakli Familyni tez topishga yordam beradi.",
        "misol": "DOOR_Single_900x2100.",
        "maslahat": "Kategoriya, obyekt turi va asosiy o‘lchamlarni nomlash standartiga qo‘shish mumkin."
    },

    "Family Library": {
        "kategoriya": "Standart",
        "vazifasi": "Tasdiqlangan Familylarni tartibli saqlash.",
        "tushuntirish": "Loyiha davomida bir xil Familylarni qayta ishlatish uchun markaziy kutubxona kerak.",
        "misol": "Doors, Windows, Furniture, Sanitary, Lighting papkalari.",
        "maslahat": "Har bir Familyning tasdiqlangan versiyasini saqlab bor."
    },

    "Family Backup": {
        "kategoriya": "Xavfsizlik",
        "vazifasi": "Muhim Familylarning alohida nusxasini saqlash.",
        "tushuntirish": "Family buzilib qolsa yoki noto‘g‘ri o‘zgarish kiritilsa eski versiyani tiklash mumkin.",
        "misol": "Door_v03.rfa.",
        "maslahat": "Muhim Familylarni faqat bitta papkada saqlab qo‘yma."
    },

    "Family Performance": {
        "kategoriya": "Optimallashtirish",
        "vazifasi": "Familyning Revit modeliga ortiqcha yuk tushirmasligini ta’minlash.",
        "tushuntirish": "Keraksiz geometriya, material, nested Family va yuqori detail darajasi performance'ga ta’sir qiladi.",
        "misol": "Oddiy stul uchun juda murakkab 3D model ishlatmaslik.",
        "maslahat": "Familyni imkon qadar yengil va parametrik qil."
    },

    "Family Testing": {
        "kategoriya": "Tekshirish",
        "vazifasi": "Familyni Projectga yuklashdan oldin turli sharoitlarda tekshirish.",
        "tushuntirish": "O‘lcham, material, visibility, hosting va parametrlar sinab ko‘riladi.",
        "misol": "Door Familyni 700, 800, 900 va 1000 mm kengliklarda tekshirish.",
        "maslahat": "Family buziladigan ekstremal qiymatlarni ham sinab ko‘r."
    },

    "Professional Family Workflow": {
        "kategoriya": "Workflow",
        "vazifasi": "Professional Family yaratish ketma-ketligini tashkil qilish.",
        "qadamlar": [
            "To‘g‘ri Family Template tanlash.",
            "Reference Plane va asosiy o‘qlarni yaratish.",
            "Asosiy o‘lcham parametrlarini yaratish.",
            "Geometriyani Reference Plane'ga bog‘lash.",
            "Material va visibility sozlamalarini berish.",
            "Flex orqali turli qiymatlarda test qilish.",
            "Family nomi va Type nomlarini standartlashtirish.",
            "Projectga Load qilib tekshirish.",
            "Kerak bo‘lsa Familyni qayta tahrirlash.",
            "Tasdiqlangan RFA nusxasini Libraryga saqlash."
        ],
        "maslahat": "Avval parametrik skeletni yarat, keyin detal va materiallarni qo‘sh. Shunda Familyni boshqarish ancha oson bo‘ladi."
    }
}


def get_revit_family(family_name):
    return REVIT_FAMILIES.get(family_name)


def get_revit_family_names():
    return list(REVIT_FAMILIES.keys())


if __name__ == "__main__":
    print(f"REVIT FAMILIES: {len(REVIT_FAMILIES)} ta")