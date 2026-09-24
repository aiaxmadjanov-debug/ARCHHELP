# =========================================================
# REVIT XATOLARI — ARCHHELP
# 120+ TA PROFESSIONAL XATO VA YECHIM
# =========================================================

REVIT_ERRORS = {}


def add_error(name, sabab, yechim, misol, maslahat, video_query):
    REVIT_ERRORS[name] = {
        "sabab": sabab,
        "yechim": yechim,
        "misol": misol,
        "maslahat": maslahat,
        "video": f"https://www.youtube.com/results?search_query={video_query}"
    }


# =========================================================
# PERFORMANCE / CRASH
# =========================================================

add_error(
    "Revit is running slowly",
    """Revit sekin ishlashiga odatda juda katta model, ko‘p miqdordagi Family,
CAD/RVT linklar, og‘ir geometriya, ko‘p view va ortiqcha elementlar sabab bo‘ladi.
3D View'da juda ko‘p element bir vaqtning o‘zida hisoblanayotgan bo‘lishi ham
ishlash tezligini pasaytiradi.""",
    """1. Manage → Purge Unused orqali keraksiz elementlarni tozalang.
2. Manage Links orqali keraksiz CAD va RVT linklarni tekshiring.
3. Og‘ir Family'larni aniqlang va optimallashtiring.
4. Keraksiz 3D View'larni yopib turing.
5. Detail Level'ni vaqtincha Medium yoki Coarse qiling.
6. Visual Style'ni Hidden Line qilib tekshiring.
7. Modeldagi warninglarni kamaytiring.
8. Revit va grafik drayver yangilanishlarini tekshiring.""",
    "Masalan, katta turar-joy loyihasida yuzlab og‘ir Family va bir nechta CAD link mavjud bo‘lsa, oddiy Floor Plan ham sekin ochilishi mumkin.",
    "Muammo kompyuter kuchsizligidan deb o‘ylashdan oldin modeldagi Family, CAD, link va view'larni tekshiring.",
    "Revit+running+slow+performance+optimization"
)

add_error(
    "Revit has stopped responding",
    """Revit juda og‘ir amalni bajarayotgan, katta modelni hisoblayotgan yoki
Family/link bilan bog‘liq jarayon tiqilib qolgan bo‘lishi mumkin.
Ba'zan RAM yoki GPU resurslari yetishmasligi ham sabab bo‘ladi.""",
    """1. Bir necha daqiqa kutib, jarayon tugashini tekshiring.
2. Task Manager'da Revit CPU/RAM ishlatilishini ko‘ring.
3. Keraksiz dasturlarni yoping.
4. Revit qayta javob bermasa modelni qayta oching.
5. Muammo ma'lum bir Family yoki View'da takrorlansa, aynan shu elementni tekshiring.
6. Zarur bo‘lsa modelni Audit bilan oching.""",
    "Katta modelda 3D View'ni Realistic rejimga o‘tkazganda Revit vaqtincha javob bermasligi mumkin.",
    "Revit qotganda darhol End Task qilishdan oldin uning hisoblash jarayonini tugatishini kuting.",
    "Revit+stopped+responding+freeze+fix"
)

add_error(
    "Revit crashes unexpectedly",
    """Crash'ga buzilgan model, buzilgan Family, grafik driver, Revit update,
corrupt cache yoki ayrim Autodesk komponentlari sabab bo‘lishi mumkin.""",
    """1. Revit va Windows yangilanishlarini tekshiring.
2. Grafik driverini yangilang.
3. Modelni Audit bilan ochib ko‘ring.
4. Muammoli Family va linklarni vaqtincha ajrating.
5. Revit jurnal fayllarini tekshiring.
6. Muammo faqat bitta projectda bo‘lsa, project tarkibini tekshiring.""",
    "Har safar bir xil 3D View ochilganda crash bo‘lsa, muammo aynan shu View yoki undagi elementlarda bo‘lishi mumkin.",
    "Crash qaysi amal bajarilganda sodir bo‘layotganini yozib boring — diagnostika ancha osonlashadi.",
    "Revit+crashes+unexpectedly+fix"
)

add_error(
    "Revit freezes when opening a project",
    """Project juda katta, buzilgan, ko‘p link yoki Family'ga ega bo‘lishi mumkin.
Workshared modelda network yoki cache muammosi ham bo‘lishi mumkin.""",
    """1. Open oynasida Audit variantini yoqing.
2. Modelni lokal diskdan ochib ko‘ring.
3. Keraksiz network ulanishlarini tekshiring.
4. Cloud model bo‘lsa cache holatini tekshiring.
5. Backup nusxasini sinab ko‘ring.
6. Muammo davom etsa yangi Local fayl yarating.""",
    "Network'dagi Central Model ochilish paytida uzoq qotib qolishi mumkin.",
    "Muhim Central Model bilan ishlaganda lokal va backup nusxalarini saqlang.",
    "Revit+freezes+opening+project+fix"
)

add_error(
    "Revit freezes when switching views",
    """View juda og‘ir, ko‘p element ko‘rsatilmoqda yoki View Template,
Filter, linked model va detail level sozlamalari ortiqcha yuklama bermoqda.""",
    """1. Muammoli View'ni aniqlang.
2. Detail Level'ni Coarse qiling.
3. Visual Style'ni Hidden Line qiling.
4. Keraksiz linklarni yashiring.
5. Section Box'dan foydalaning.
6. View'dagi og‘ir Family'larni tekshiring.""",
    "3D View'dan Floor Plan'ga o‘tishda Revit bir necha soniya qotib qolishi mumkin.",
    "Har bir View'ni maksimal darajada og‘irlashtirib yubormang.",
    "Revit+view+freezing+performance"
)

add_error(
    "Revit file is very large",
    """Project ichida unused Family, Type, Material, CAD import, RVT link,
rasm, view yoki murakkab geometriya juda ko‘paygan bo‘lishi mumkin.""",
    """1. Manage → Purge Unused.
2. Manage → Review Warnings.
3. Manage Links orqali keraksiz linklarni tekshiring.
4. Keraksiz CAD importlarni olib tashlang.
5. Og‘ir Family'larni optimallashtiring.
6. Keraksiz View va Sheet'larni tozalang.""",
    "Oddiy bino loyihasi keraksiz 3D Family va CAD fayllar sabab yuzlab MB bo‘lib ketishi mumkin.",
    "Model hajmini loyiha oxirida emas, butun loyiha davomida nazorat qiling.",
    "Revit+large+file+reduce+size"
)

add_error(
    "Revit takes too long to save",
    """Model katta, network sekin, Central Model uzoqda joylashgan yoki modelda
ko‘p link va og‘ir element mavjud bo‘lishi mumkin.""",
    """1. Lokal model bilan test qiling.
2. Network tezligini tekshiring.
3. Keraksiz linklarni tekshiring.
4. Warninglarni tozalang.
5. Model hajmini kamaytiring.
6. Diskda yetarli bo‘sh joy borligini tekshiring.""",
    "Serverdagi Central Model lokal SSD'dagi faylga qaraganda sekinroq saqlanishi mumkin.",
    "Save jarayoni muntazam sekinlashsa model health audit qiling.",
    "Revit+slow+save+project"
)

add_error(
    "Revit takes too long to synchronize",
    """Central Model bilan aloqa sekin, model katta, ko‘p foydalanuvchi ishlayapti
yoki Local fayl eskirgan bo‘lishi mumkin.""",
    """1. Network ulanishini tekshiring.
2. Reload Latest qiling.
3. Keraksiz elementlarni tekshiring.
4. Local faylni yangilang.
5. Central Model joylashuvini tekshiring.
6. Zarur bo‘lsa yangi Local yarating.""",
    "Bir nechta odam katta BIM modelda ishlaganda Synchronize with Central uzoq vaqt olishi mumkin.",
    "Sync vaqtida network uzilib qolmasligiga e'tibor bering.",
    "Revit+synchronize+with+central+slow"
)

add_error(
    "An unrecoverable error has occurred",
    """Model yoki cache buzilgan bo‘lishi mumkin. Autodesk ma'lumotlariga ko‘ra,
bunday xato modelni ochish, saqlash yoki synchronize qilish vaqtida corrupt
content yoki cache bilan bog‘liq bo‘lishi mumkin.""",
    """1. Revit'ni yopib qayta oching.
2. Modelning backup nusxasini tekshiring.
3. Modelni Audit bilan ochib ko‘ring.
4. Cloud model bo‘lsa cache'ni tekshiring.
5. Muammoli Family'larni aniqlang.
6. Muammo saqlash yoki Sync vaqtida chiqsa Central Model holatini tekshiring.""",
    "Project saqlanayotgan paytda Revit birdan yopilib, unrecoverable error ko‘rsatishi mumkin.",
    "Muhim projectlarning bir nechta backup nusxasini saqlang.",
    "Revit+unrecoverable+fatal+error+fix"
)

add_error(
    "A fatal error has occurred",
    """Fatal error Revit jarayonini to‘xtatishga majbur qiladigan jiddiy model,
cache, Family yoki dastur muammosini bildirishi mumkin.""",
    """1. Recovery fayllarini tekshiring.
2. Projectni Audit bilan oching.
3. Oxirgi qo‘shilgan Family'larni tekshiring.
4. CAD/RVT linklarni tekshiring.
5. Revit update holatini tekshiring.
6. Muammo takrorlansa journal faylini diagnostika qiling.""",
    "Yangi yuklangan murakkab Family'dan keyin project ochilmay qolishi mumkin.",
    "Fatal error chiqishidan oldingi harakatni aniqlash eng foydali diagnostika usulidir.",
    "Revit+fatal+error+troubleshooting"
)


# =========================================================
# PROJECT / SAVE
# =========================================================

add_error(
    "Cannot save changes to the project",
    """Faylga yozish huquqi yo‘q, fayl Read-only holatda, diskda joy yetarli emas
yoki network ulanishi uzilgan bo‘lishi mumkin.""",
    """1. RVT fayl joylashgan papkani tekshiring.
2. Fayl Properties → Read-only holatini tekshiring.
3. Papkaga Write permission borligini tekshiring.
4. Diskdagi bo‘sh joyni tekshiring.
5. Network project bo‘lsa ulanishni tekshiring.
6. File → Save As orqali lokal nusxa yarating.
7. Workshared model bo‘lsa Central Model holatini tekshiring.""",
    "Serverdagi projectga o‘zgartirish kiritgandan keyin Save bosilganda xato chiqishi mumkin.",
    "Muhim network projectlar uchun lokal backup saqlash juda foydali.",
    "Revit+cannot+save+changes+project"
)

add_error(
    "This file is open for editing by another user",
    """Workshared projectda boshqa foydalanuvchi fayl yoki elementni tahrirlab
turishi mumkin. Windows permission yoki bir nechta Revit session ham sabab bo‘lishi mumkin.""",
    """1. Boshqa Revit sessionlari ochiq emasligini tekshiring.
2. Fayl Properties → Read-only holatini tekshiring.
3. Papkaga Write permission borligini tekshiring.
4. Worksharing ownership holatini tekshiring.
5. Boshqa foydalanuvchi bilan ownership masalasini aniqlang.
6. Zarur bo‘lsa Revit'ni Administrator sifatida ishga tushirib test qiling.""",
    "Central Modeldagi fayl boshqa foydalanuvchi tomonidan tahrirlanayotgan bo‘lsa o‘zgartirishni saqlashda muammo chiqishi mumkin.",
    "Workshared faylda boshqa foydalanuvchining ownership holatini tekshirmasdan elementni majburan o‘zgartirmang.",
    "Revit+file+open+editing+another+user"
)

add_error(
    "Cannot create a new local file",
    """Central Modelga ulanish muammoli, Local fayl joylashuvi noto‘g‘ri yoki
Windows papkaga yozish huquqini bermayotgan bo‘lishi mumkin.""",
    """1. Central Modelga to‘g‘ridan-to‘g‘ri kirish mumkinligini tekshiring.
2. Local faylni lokal SSD/HDD'ga yarating.
3. Papka permissions'ni tekshiring.
4. Network ulanishini tekshiring.
5. Eski Local faylni yopib, yangisini yarating.""",
    "Ofis serveridagi Central Modelga ulanish mavjud bo‘lmasa yangi Local yaratish muvaffaqiyatsiz bo‘lishi mumkin.",
    "Local fayllarni project nomi va foydalanuvchi nomi bilan tartibli saqlang.",
    "Revit+cannot+create+local+file"
)

add_error(
    "Cannot synchronize with central",
    """Central Modelga ulanish uzilgan, ownership muammosi, network sekinligi,
Local faylning eskirishi yoki modeldagi muammo sabab bo‘lishi mumkin.""",
    """1. Network ulanishini tekshiring.
2. Reload Latest qiling.
3. Element ownership'ni tekshiring.
4. Central Model mavjudligini tekshiring.
5. Local faylni yangilang.
6. Zarur bo‘lsa yangi Local yarating.""",
    "Synchronize bosilganda server javob bermasa Sync muvaffaqiyatsiz tugashi mumkin.",
    "Sync'dan oldin muhim o‘zgarishlarni saqlab turing.",
    "Revit+cannot+synchronize+with+central"
)

add_error(
    "Central Model is not available",
    """Central Model serverda mavjud emas, network uzilgan, fayl ko‘chirilgan
yoki foydalanuvchida kerakli ruxsat yo‘q bo‘lishi mumkin.""",
    """1. Serverga ulanishni tekshiring.
2. Central Model manzilini tekshiring.
3. Fayl mavjudligini Windows Explorer orqali tekshiring.
4. Papka permissions'ni tekshiring.
5. Team a'zolaridan server holatini aniqlang.""",
    "Serverdagi RVT fayl nomi yoki joylashuvi o‘zgartirilsa eski Local fayl Central Modelni topa olmaydi.",
    "Central Model joylashuvini o‘zboshimchalik bilan o‘zgartirmang.",
    "Revit+central+model+not+available"
)

add_error(
    "Workset is not editable",
    """Workset boshqa foydalanuvchi tomonidan editable qilingan yoki sizda
ownership olish huquqi yo‘q bo‘lishi mumkin.""",
    """1. Manage → Worksets orqali Workset holatini tekshiring.
2. Element yoki Workset ownership'ni aniqlang.
3. Reload Latest qiling.
4. Boshqa foydalanuvchi bilan ownership masalasini hal qiling.""",
    "Structural Workset boshqa foydalanuvchida editable bo‘lsa siz o‘sha elementlarni tahrirlay olmaysiz.",
    "Worksharingda ownershipni jamoa qoidalari asosida boshqaring.",
    "Revit+workset+not+editable"
)

add_error(
    "Element is owned by another user",
    """Element Worksharing orqali boshqa foydalanuvchining ownershipida turibdi.""",
    """1. Elementni tanlang.
2. Properties va Worksharing ma'lumotlarini tekshiring.
3. Element egasini aniqlang.
4. Foydalanuvchidan elementni Relinquish qilishini so‘rang.
5. Reload Latest qiling.""",
    "Boshqa arxitektor devorni tahrirlab turgan paytda siz o‘sha devorni o‘zgartira olmaysiz.",
    "Jamoaviy modelda ownershipni hurmat qiling.",
    "Revit+element+owned+by+another+user"
)


# =========================================================
# VISIBILITY / VIEW
# =========================================================

add_error(
    "Element is not visible",
    """Element Hide qilingan, category o‘chirilgan, View Template,
Filter, Workset, Phase, Design Option yoki View Range sabab ko‘rinmayotgan bo‘lishi mumkin.""",
    """1. Reveal Hidden Elements rejimini yoqing.
2. VG/VV orqali Category holatini tekshiring.
3. View Template'ni tekshiring.
4. Filters'ni tekshiring.
5. Workset holatini tekshiring.
6. Phase va Design Option'ni tekshiring.
7. View Range'ni tekshiring.""",
    "Devor 3D View'da ko‘rinib, Floor Plan'da ko‘rinmasa View Visibility sozlamalarini tekshirish kerak.",
    "Element yo‘q deb o‘chirishdan oldin Visibility sozlamalarini tekshiring.",
    "Revit+element+not+visible+visibility"
)

add_error(
    "Walls are not visible in plan",
    """View Range noto‘g‘ri, Walls category o‘chirilgan, Phase noto‘g‘ri yoki
devor boshqa balandlikda joylashgan bo‘lishi mumkin.""",
    """1. VG/VV → Walls holatini tekshiring.
2. View Range'ni oching.
3. Cut Plane balandligini tekshiring.
4. Phase sozlamasini tekshiring.
5. Temporary Hide/Isolate ishlatilgan bo‘lsa Reset qiling.""",
    "Devorda Base Constraint va qavat balandligi mos bo‘lmasa Floor Plan'da kutilganidek ko‘rinmasligi mumkin.",
    "Planlar uchun View Range standartlarini oldindan belgilang.",
    "Revit+walls+not+visible+plan"
)

add_error(
    "Doors are not visible",
    """Door category yashirilgan, Door Family noto‘g‘ri host qilingan,
View Range yoki Phase sozlamasi muammoli bo‘lishi mumkin.""",
    """1. VG/VV → Doors'ni yoqing.
2. Reveal Hidden Elements'ni tekshiring.
3. Door Family hostini tekshiring.
4. Phase sozlamasini tekshiring.
5. View Range'ni tekshiring.""",
    "Door 3D View'da mavjud, lekin Floor Plan'da ko‘rinmasa Visibility va View Range tekshiriladi.",
    "Door Family'larini project boshida sinab ko‘ring.",
    "Revit+doors+not+visible"
)

add_error(
    "Windows are not visible",
    """Windows category yashirilgan, Family noto‘g‘ri host qilingan yoki
View Range/Phase muammosi mavjud.""",
    """1. VG/VV → Windows'ni tekshiring.
2. Family hostini tekshiring.
3. View Range'ni tekshiring.
4. Phase sozlamalarini tekshiring.
5. Reveal Hidden Elements rejimini sinab ko‘ring.""",
    "Window 3D'da ko‘rinib, Floor Plan'da ko‘rinmasa Category yoki View Range muammosi bo‘lishi mumkin.",
    "Standart Window Family'larini ishlatish diagnostikani osonlashtiradi.",
    "Revit+windows+not+visible"
)

add_error(
    "Dimensions are not visible",
    """Dimensions category yashirilgan, Annotation Crop ta'sir qilmoqda,
View Template yoki filter dimensionlarni yashirgan bo‘lishi mumkin.""",
    """1. VG/VV → Annotation Categories'ni tekshiring.
2. Dimensions category yoqilganini tekshiring.
3. Annotation Crop'ni kengaytiring.
4. View Template'ni tekshiring.
5. Filterlarni tekshiring.""",
    "Floor Plan'da barcha o‘lchamlar yo‘qolsa Dimensions visibility tekshiriladi.",
    "Sheetga chiqarishdan oldin annotationlarni Print Preview'da tekshiring.",
    "Revit+dimensions+not+visible"
)

add_error(
    "Tags are not visible",
    """Tag category yashirilgan yoki mos Tag Family projectga yuklanmagan bo‘lishi mumkin.""",
    """1. VG/VV → Tags kategoriyalarini tekshiring.
2. Kerakli Tag Family mavjudligini tekshiring.
3. Load Family orqali Tag yuklang.
4. Annotate → Tag by Category bilan qayta joylashtiring.""",
    "Door Tag ko‘rinmasa Door Tags category yoki Tag Family tekshiriladi.",
    "Project boshida ishlatiladigan annotation Family'larni tayyorlab qo‘ying.",
    "Revit+tags+not+visible"
)

add_error(
    "Section is not visible",
    """Section marker yashirilgan, crop region, annotation crop yoki
view visibility sabab section ko‘rinmayotgan bo‘lishi mumkin.""",
    """1. Reveal Hidden Elements'ni tekshiring.
2. Section category'ni VG/VV orqali yoqing.
3. Crop Region'ni tekshiring.
4. Annotation Crop'ni kengaytiring.
5. Section View'ni ochib ko‘ring.""",
    "Floor Plan'da section chizig‘i yo‘qolsa section category yashirilgan bo‘lishi mumkin.",
    "Sectionlarni loyiha standartiga mos nomlang va joylashtiring.",
    "Revit+section+not+visible"
)

add_error(
    "Level is not visible",
    """Level boshqa view'da yaratilgan, crop region chegaralangan yoki
level extents noto‘g‘ri sozlangan bo‘lishi mumkin.""",
    """1. Elevation yoki Section View'ni oching.
2. Level'ni tanlang.
3. 2D/3D extents holatini tekshiring.
4. Crop Region'ni kengaytiring.
5. Scope Box ishlatilgan bo‘lsa tekshiring.""",
    "Yangi qavat Level'i Floor Plan'da emas, Elevation'da ko‘rinishi mumkin.",
    "Level nomi va balandligini loyiha boshidan standartlashtiring.",
    "Revit+level+not+visible"
)

add_error(
    "View Range is incorrect",
    """Top, Cut Plane, Bottom yoki View Depth qiymatlari elementlarning
ko‘rinish balandligiga mos kelmayapti.""",
    """1. Properties → View Range'ni oching.
2. Top qiymatini tekshiring.
3. Cut Plane balandligini tekshiring.
4. Bottom va View Depth qiymatlarini tekshiring.
5. Element balandligini ham tekshiring.""",
    "Deraza Floor Plan'da chiqmasa Cut Plane noto‘g‘ri balandlikda bo‘lishi mumkin.",
    "Har bir plan turiga mos View Range shablonini yarating.",
    "Revit+View+Range+explained"
)

add_error(
    "View Template is controlling the view",
    """View Template view visibility, graphics, filters, detail level va boshqa
sozlamalarni boshqarayotgan bo‘lishi mumkin.""",
    """1. Properties → View Template'ni tekshiring.
2. Qaysi parametrlar template tomonidan boshqarilayotganini ko‘ring.
3. Kerak bo‘lsa template'ni vaqtincha None qiling.
4. Yoki View Template ichidan kerakli parametrni o‘zgartiring.""",
    "Devor rangini qo‘lda o‘zgartirib bo‘lmasa View Template sabab bo‘lishi mumkin.",
    "Katta projectlarda View Template'larni tartibli nomlang.",
    "Revit+View+Template+visibility"
)

add_error(
    "Crop Region is hiding elements",
    """Element View Crop Region yoki Annotation Crop tashqarisida qolgan bo‘lishi mumkin.""",
    """1. Crop Region'ni yoqing.
2. Crop chegarasini kattalashtiring.
3. Annotation Crop'ni alohida tekshiring.
4. Scope Box ishlatilgan bo‘lsa uni tekshiring.""",
    "Section marker yoki dimension crop chegarasidan tashqarida qolsa ko‘rinmaydi.",
    "Sheetga chiqarishdan oldin crop chegaralarini tekshiring.",
    "Revit+crop+region+visibility"
)


# =========================================================
# FAMILY / PARAMETER
# =========================================================

add_error(
    "Family cannot be loaded",
    """Family fayli buzilgan, Revit versiyasi mos emas, category yoki
host noto‘g‘ri, constraintlar konflikt qilayotgan bo‘lishi mumkin.""",
    """1. Family faylini alohida oching.
2. Family Editor'da warninglarni tekshiring.
3. Constraints va dimensions'ni tekshiring.
4. Family category'sini tekshiring.
5. Load into Project orqali qayta yuklang.
6. Zarur bo‘lsa Family'ni qayta yarating.""",
    "Internetdan olingan Door Family projectga yuklanmasa avval Family faylining o‘zini tekshirish kerak.",
    "Har qanday internet Family'sini projectga yuklashdan oldin test qiling.",
    "Revit+family+cannot+load+fix"
)

add_error(
    "Family parameter is not working",
    """Parameter noto‘g‘ri Type'da yaratilgan, formula xato, parameter
Instance/Type rejimi noto‘g‘ri yoki Family Category bilan mos emas.""",
    """1. Family Editor → Family Types'ni oching.
2. Parameter nomini tekshiring.
3. Parameter Type'ni tekshiring.
4. Formula mavjud bo‘lsa sintaksisini tekshiring.
5. Instance yoki Type ekanini tekshiring.
6. Parameterni reference plane bilan to‘g‘ri bog‘lang.""",
    "Door Width parametrini o‘zgartirganda geometriya o‘zgarmasa parameter constraintlarini tekshirish kerak.",
    "Family parametrlarini yaratishdan oldin ularning o‘zaro bog‘lanishini rejalashtiring.",
    "Revit+family+parameter+not+working"
)

add_error(
    "Constraints are not satisfied",
    """Family yoki project elementlaridagi constraintlar bir-biriga zid,
locked dimension noto‘g‘ri yoki ortiqcha constraint mavjud.""",
    """1. Muammo ko‘rsatilgan constraintni aniqlang.
2. Keraksiz locklarni olib tashlang.
3. Dimensions'ni tekshiring.
4. Reference Plane'larni tekshiring.
5. Family'ni qayta test qiling.""",
    "Bir o‘lchamni ikki xil parametr bir vaqtning o‘zida boshqarsa constraint conflict chiqishi mumkin.",
    "Family'larda faqat kerakli constraintlardan foydalaning.",
    "Revit+constraints+not+satisfied"
)

add_error(
    "Can't make type",
    """Family parametrlarida konflikt, formula xatosi yoki constraint muammosi mavjud.""",
    """1. Family Editor'ga kiring.
2. Family Types oynasini oching.
3. Parametrlar va formulalarni tekshiring.
4. Locked dimensionlarni tekshiring.
5. Type'ni qayta yarating.""",
    "Window Family'da Width va Height parametrlari noto‘g‘ri bog‘langan bo‘lsa yangi Type yaratish qiyinlashadi.",
    "Type parametrlarini sodda va aniq saqlang.",
    "Revit+cant+make+type+family"
)

add_error(
    "Room is not enclosed",
    """Room chegarasi yopilmagan, devor Room Bounding emas yoki linked model
xona chegarasi sifatida ishlatilmayapti.""",
    """1. Room atrofidagi devorlarni tekshiring.
2. Devorlar orasidagi kichik bo‘shliqlarni toping.
3. Properties → Room Bounding'ni tekshiring.
4. Architecture → Room Separator bilan yopiq chegara yarating.
5. Linked model ishlatilsa uning Room Bounding holatini tekshiring.""",
    "Ikki devor orasidagi juda kichik bo‘shliq Room is not enclosed xatosini keltirib chiqarishi mumkin.",
    "Room ishlamasa avval xona konturi yopilganini tekshiring.",
    "Revit+Room+is+not+enclosed"
)

add_error(
    "Duplicate Instances",
    """Bir xil element bir joyga ikki yoki undan ortiq marta joylashtirilgan bo‘lishi mumkin.""",
    """1. Manage → Review Warnings'ni oching.
2. Duplicate elementlarni aniqlang.
3. Select All Instances yordamida ularni toping.
4. Keraksiz nusxani o‘chiring.
5. Warninglarni qayta tekshiring.""",
    "Bir xil ustun Copy/Paste natijasida ikki marta joylashtirilsa duplicate warning chiqishi mumkin.",
    "Project topshirilishidan oldin Review Warnings bajaring.",
    "Revit+duplicate+instances+warning"
)

add_error(
    "Highlighted walls overlap",
    """Bir yoki bir nechta devor bir-birining ustiga tushgan yoki duplicate qilib qo‘yilgan.""",
    """1. Warning'dagi devorlarni tanlang.
2. Temporary Hide/Isolate bilan ko‘rib chiqing.
3. Keraksiz duplicate wall'ni o‘chiring.
4. Wall Join holatini tekshiring.""",
    "Devordan nusxa olishda eski devor ustiga yana bitta devor tushib qolishi mumkin.",
    "Devorlarni ko‘paytirishda Copy va Align jarayonini nazorat qiling.",
    "Revit+walls+overlap+warning"
)

add_error(
    "Door or Window cannot be placed",
    """Family kerakli hostga ega emas, Family Category noto‘g‘ri yoki tanlangan
devor host sifatida mos emas.""",
    """1. Family Editor'ni oching.
2. Family Category and Parameters'ni tekshiring.
3. Host turini tekshiring.
4. Projectga qayta Load qiling.
5. Standart Revit Door/Window Family bilan test qiling.""",
    "Window Family devorga joylashmasa u Wall-hosted bo‘lmasligi mumkin.",
    "Host-based Family'larni project boshida test qiling.",
    "Revit+door+window+cannot+place"
)

add_error(
    "Family geometry is too complex",
    """Family ichida juda ko‘p solid, nested Family, blend, void yoki murakkab
3D geometriya mavjud.""",
    """1. Family Editor'ni oching.
2. Keraksiz geometriyani olib tashlang.
3. Nested Family'larni kamaytiring.
4. 2D symbolic line va detail elementlardan foydalaning.
5. Family'ni qayta load qilib performance'ni tekshiring.""",
    "Murakkab mebel Family'si projectni sekinlashtirishi mumkin.",
    "Architecture Family'larida kerak bo‘lmagan 3D detallarni ko‘paytirmang.",
    "Revit+family+too+complex+geometry"
)

add_error(
    "Nested family is missing",
    """Asosiy Family ichida ishlatilgan nested Family projectga yuklanmagan yoki
fayl yo‘qolgan bo‘lishi mumkin.""",
    """1. Family Editor'da nested elementlarni tekshiring.
2. Kerakli nested Family faylini toping.
3. Load into Project orqali yuklang.
4. Asosiy Family'ni qayta load qiling.""",
    "Mebel Family'sida tutqich yoki oyoq nested Family bo‘lsa va u mavjud bo‘lmasa asosiy Family noto‘g‘ri ishlashi mumkin.",
    "Nested Family fayllarini bitta tartibli kutubxonada saqlang.",
    "Revit+nested+family+missing"
)


# =========================================================
# MODELING
# =========================================================

add_error(
    "Stair cannot be created",
    """Run yoki Landing geometriyasi noto‘g‘ri, qavatlar orasidagi balandlik
mos emas yoki riser soni talabga javob bermayapti.""",
    """1. Base Level'ni tekshiring.
2. Top Level'ni tekshiring.
3. Desired Number of Risers qiymatini tekshiring.
4. Run uzunligini tekshiring.
5. Landing boundary'ni tekshiring.
6. Stair sketch'ni qayta chizing.""",
    "3 metr qavat balandligi uchun noto‘g‘ri riser qiymati tanlansa zinapoya yaratish imkonsiz bo‘lishi mumkin.",
    "Zinapoya chizishdan oldin qavat balandligini aniq belgilang.",
    "Revit+stair+cannot+create+fix"
)

add_error(
    "Roof cannot be created",
    """Roof boundary yopilmagan, sketch chiziqlari kesishgan yoki Slope Arrow noto‘g‘ri sozlangan.""",
    """1. Roof sketch'ni oching.
2. Boundary'ni to‘liq yoping.
3. Kesishuvchi chiziqlarni tuzating.
4. Slope Arrow parametrlarini tekshiring.
5. Roof Type'ni tekshiring.""",
    "Murakkab bino konturida boundary chiziqlari kesishib qolsa Roof hosil bo‘lmasligi mumkin.",
    "Roof sketch'da ortiqcha va kesishuvchi chiziqlar qoldirmang.",
    "Revit+roof+cannot+create+fix"
)

add_error(
    "Floor cannot be created",
    """Floor sketch yopilmagan, boundary kesishgan yoki profil noto‘g‘ri bo‘lishi mumkin.""",
    """1. Floor sketch'ni oching.
2. Kontur yopilganini tekshiring.
3. Kesishuvchi chiziqlarni tuzating.
4. Duplicate boundary segmentlarni olib tashlang.
5. Floor Type'ni tekshiring.""",
    "L-shaklli pol konturida bitta chiziq yopilmay qolsa Floor yaratib bo‘lmaydi.",
    "Sketch Mode'dan chiqishdan oldin barcha boundary chiziqlarini tekshiring.",
    "Revit+floor+cannot+create+fix"
)

add_error(
    "Wall join is incorrect",
    """Devorlar noto‘g‘ri Join qilingan, Wall Type qatlamlari mos emas yoki Join Order noto‘g‘ri.""",
    """1. Devor kesishmasini tanlang.
2. Modify → Wall Joins'ni oching.
3. Join Type'ni tekshiring.
4. Wall Type qatlamlarini tekshiring.
5. Join Order'ni o‘zgartirib ko‘ring.""",
    "Ikki tashqi devor tutashganda finish qatlamlari noto‘g‘ri kesishishi mumkin.",
    "Wall Type qatlamlarini loyiha standartiga mos yarating.",
    "Revit+wall+join+problem"
)

add_error(
    "Cannot cut geometry",
    """Elementlar Cuttable emas, geometriya bir-biriga mos kelmaydi yoki
Cut Geometry uchun noto‘g‘ri element tanlangan.""",
    """1. Element Category'sini tekshiring.
2. Cuttable ekanini tekshiring.
3. Modify → Cut Geometry orqali qayta urinib ko‘ring.
4. Elementlarning bir-biriga real kesishganini tekshiring.""",
    "Void Family devorni kesmasa Family Cut with Voids When Loaded sozlamasini tekshirish kerak.",
    "Void va Cut workflow'ini Family Category'ga mos ishlating.",
    "Revit+cannot+cut+geometry"
)

add_error(
    "Cannot join geometry",
    """Ikki element geometriyasi mos emas yoki ular Join Geometry uchun yaroqsiz bo‘lishi mumkin.""",
    """1. Elementlarni alohida tanlang.
2. Ular haqiqatan kesishayotganini tekshiring.
3. Modify → Join Geometry'ni qayta ishlating.
4. Join Order'ni o‘zgartiring.
5. Kerak bo‘lsa Unjoin Geometry qilib qayta ulang.""",
    "Beam va wall geometriyasi kerakli joyda kesishmasa Join ishlamasligi mumkin.",
    "Elementlarni Join qilishdan oldin ularning geometrik joylashuvini tekshiring.",
    "Revit+join+geometry+problem"
)

add_error(
    "Elements are slightly off axis",
    """Element gorizontal yoki vertikal o‘qdan juda kichik burchakka og‘gan.""",
    """1. Elementni tanlang.
2. Uning geometriyasini tekshiring.
3. Align buyrug‘idan foydalaning.
4. Zarur bo‘lsa elementni qayta chizing.
5. Reference Line yoki Grid bilan tekshiring.""",
    "Devor 90° o‘rniga 89.999° bo‘lib qolsa off-axis warning chiqishi mumkin.",
    "Model yaratishda Snap, Align va Temporary Dimensions'dan foydalaning.",
    "Revit+elements+slightly+off+axis"
)

add_error(
    "Element cannot be moved",
    """Element locked, pinned, group, design option yoki boshqa elementga constraint qilingan bo‘lishi mumkin.""",
    """1. Elementni tanlang.
2. Pin holatini tekshiring.
3. Constraints'ni tekshiring.
4. Group ichida ekanini tekshiring.
5. Design Option'ni tekshiring.
6. Ownership holatini tekshiring.""",
    "Pinned devorni Move qilishga uringanda element ko‘chmasligi mumkin.",
    "Move qilishdan oldin elementning Pin va Constraint holatini tekshiring.",
    "Revit+element+cannot+move"
)

add_error(
    "Element cannot be deleted",
    """Element Group, Design Option, Assembly, constraint yoki Worksharing ownership bilan bog‘langan bo‘lishi mumkin.""",
    """1. Element hostini tekshiring.
2. Group yoki Design Option'ni tekshiring.
3. Constraintlarni tekshiring.
4. Worksharing ownership'ni tekshiring.
5. Zarur bo‘lsa elementni Edit Group orqali o‘chiring.""",
    "Central Model'dagi boshqa foydalanuvchi elementini o‘chirishga urinishda permission muammosi chiqishi mumkin.",
    "Jamoaviy modelda element ownership'ni tekshirmasdan o‘chirmang.",
    "Revit+element+cannot+delete"
)


# =========================================================
# CAD / LINK / COORDINATES
# =========================================================

add_error(
    "CAD import is very slow",
    """DWG juda katta, ko‘p layer, block, hatch va duplicate line mavjud bo‘lishi mumkin.""",
    """1. AutoCAD'da PURGE ishlating.
2. OVERKILL bilan duplicate line'larni tozalang.
3. Keraksiz layerlarni o‘chiring.
4. Xref va blocklarni tekshiring.
5. Revit'da kerak bo‘lsa Import o‘rniga Link CAD ishlating.""",
    "Topografiya DWG'sida juda ko‘p line va hatch bo‘lsa Revit import jarayoni sekinlashadi.",
    "DWG faylni Revit'ga olib kirishdan oldin AutoCAD'da tozalang.",
    "Revit+CAD+import+slow"
)

add_error(
    "CAD link is not visible",
    """CAD link unload qilingan, Imported Categories yashirilgan yoki
CAD noto‘g‘ri koordinatada joylashgan bo‘lishi mumkin.""",
    """1. Manage → Manage Links'ni oching.
2. CAD fayl Loaded holatda ekanini tekshiring.
3. VG/VV → Imported Categories'ni tekshiring.
4. Zoom to Fit qiling.
5. CAD koordinatasini tekshiring.""",
    "DWG Link qilingan bo‘lsa ham Floor Plan'da ko‘rinmasa visibility va koordinata tekshiriladi.",
    "CAD fayllarda origin va units'ni oldindan aniqlang.",
    "Revit+CAD+link+not+visible"
)

add_error(
    "CAD file has wrong scale",
    """Import Units noto‘g‘ri tanlangan yoki DWG ichidagi birliklar Revit
project units bilan mos emas.""",
    """1. DWG units'ni AutoCAD'da tekshiring.
2. Revit import oynasidagi Units'ni tekshiring.
3. Custom Scale parametrini tekshiring.
4. Known dimension orqali o‘lchamni solishtiring.""",
    "AutoCAD'da millimetrda chizilgan plan Revit'da metr deb import qilinsa o‘lcham noto‘g‘ri chiqadi.",
    "DWG units'ni har doim importdan oldin tekshiring.",
    "Revit+CAD+wrong+scale"
)

add_error(
    "Revit link is not visible",
    """RVT link unload qilingan, Revit Links visibility o‘chirilgan,
Workset yopiq yoki koordinata noto‘g‘ri bo‘lishi mumkin.""",
    """1. Manage → Manage Links → Revit'ni tekshiring.
2. Reload From qiling.
3. VG/VV → Revit Links'ni tekshiring.
4. Workset holatini tekshiring.
5. Position va Coordinates'ni tekshiring.""",
    "Structural RVT Architecture modelida ko‘rinmasa Revit Links sozlamalari tekshiriladi.",
    "Linklarni discipline bo‘yicha tartibli nomlang.",
    "Revit+link+not+visible"
)

add_error(
    "Revit link is unloaded",
    """RVT link ataylab yoki tasodifan Unload qilingan bo‘lishi mumkin.""",
    """1. Manage → Manage Links'ni oching.
2. Revit Links tabini tanlang.
3. Unloaded linkni tanlang.
4. Reload From orqali faylni qayta yuklang.
5. Fayl manzili o‘zgargan bo‘lsa yangi path ko‘rsating.""",
    "Structural model unload qilinganidan keyin Architecture modelida ustunlar ko‘rinmaydi.",
    "Keraksiz linkni Unload qilishdan oldin jamoaga xabar bering.",
    "Revit+link+unloaded+reload"
)

add_error(
    "Shared Coordinates are incorrect",
    """Project Base Point, Survey Point yoki linked model koordinatalari noto‘g‘ri sozlangan.""",
    """1. Project Base Point'ni tekshiring.
2. Survey Point'ni tekshiring.
3. Manage → Coordinates sozlamalarini ko‘ring.
4. Acquire Coordinates yoki Publish Coordinates workflow'ini tekshiring.
5. Link Position'ni tekshiring.""",
    "Bir nechta bino modelini bitta master plan ichida birlashtirganda koordinata xatosi bino joylashuvini siljitishi mumkin.",
    "Koordinata tizimini loyiha boshida barcha jamoa a'zolari bilan kelishib oling.",
    "Revit+shared+coordinates+problem"
)

add_error(
    "RVT link is in the wrong location",
    """Linked model boshqa koordinata tizimida, Origin to Origin yoki Shared Coordinates noto‘g‘ri tanlangan.""",
    """1. Link Position'ni tekshiring.
2. Manage Links orqali koordinatani aniqlang.
3. Host va linked model Project Base Point'larini solishtiring.
4. Shared Coordinates workflow'ini qayta tekshiring.""",
    "Structural model Architecture modelidan yuzlab metr uzoqda chiqsa koordinata mos emas.",
    "Linklarni qo‘lda tasodifiy Move qilish o‘rniga koordinata tizimini to‘g‘rilang.",
    "Revit+RVT+link+wrong+location"
)


# =========================================================
# MATERIAL / RENDER
# =========================================================

add_error(
    "Material is not visible",
    """Material biriktirilmagan, Visual Style materiallarni ko‘rsatmayapti yoki
Material Appearance Asset mavjud emas.""",
    """1. Material Browser'ni oching.
2. Material assignment'ni tekshiring.
3. Visual Style'ni Realistic qiling.
4. Appearance Asset'ni tekshiring.
5. Texture path mavjudligini tekshiring.""",
    "G‘isht materiali 3D View'da kulrang chiqsa Appearance Asset tekshiriladi.",
    "Material kutubxonasini loyiha bo‘yicha standartlashtiring.",
    "Revit+material+not+visible"
)

add_error(
    "Revit render is black",
    """Lighting, exposure, sun position, material yoki render sozlamalarida muammo bo‘lishi mumkin.""",
    """1. Sun Settings'ni tekshiring.
2. Artificial Lights'ni tekshiring.
3. Exposure qiymatini tekshiring.
4. Render Quality'ni tekshiring.
5. Material Appearance'ni tekshiring.
6. Low Quality preview bilan test qiling.""",
    "Interyer renderida barcha xona qora chiqsa birinchi navbatda lighting va exposure tekshiriladi.",
    "Final renderdan oldin kichik resolution preview render qiling.",
    "Revit+render+black+fix"
)

add_error(
    "Rendering features are currently disabled",
    """Grafik apparat, driver yoki Revit render komponentlarida muammo bo‘lishi mumkin.""",
    """1. Grafik driverini tekshiring.
2. Revit update'larini tekshiring.
3. Hardware acceleration holatini tekshiring.
4. Revit'ni qayta ishga tushiring.
5. Kerak bo‘lsa render sozlamalarini reset qiling.""",
    "Revit o‘rnatilgandan keyin render funksiyasi ishlamasa grafik konfiguratsiya tekshiriladi.",
    "GPU driverini faqat rasmiy ishlab chiqaruvchi manbasidan yangilang.",
    "Revit+rendering+features+disabled"
)

add_error(
    "Texture is missing",
    """Material Appearance Asset ichidagi texture fayli o‘chirilgan,
ko‘chirilgan yoki path noto‘g‘ri bo‘lishi mumkin.""",
    """1. Material Browser'ni oching.
2. Appearance Asset'ni tekshiring.
3. Texture path'ni aniqlang.
4. Fayl mavjudligini tekshiring.
5. Texture'ni qayta ko‘rsating.""",
    "Yog‘och texture boshqa kompyuterda ishlamasa texture fayli lokal path'da bo‘lishi mumkin.",
    "Texture fayllarini project bilan tartibli saqlang.",
    "Revit+missing+texture+material"
)


# =========================================================
# EXPORT / PRINT
# =========================================================

add_error(
    "Revit PDF export problem",
    """View/Sheet visibility, lineweight, printer yoki PDF export sozlamalarida muammo bo‘lishi mumkin.""",
    """1. Sheet'ni Print Preview orqali tekshiring.
2. View visibility'ni tekshiring.
3. Lineweight sozlamalarini tekshiring.
4. PDF printer yoki export sozlamalarini tekshiring.
5. Boshqa Sheet bilan test qiling.""",
    "PDF'da devorlar bor, lekin ayrim dimensionlar chiqmasa annotation visibility tekshiriladi.",
    "PDF yuborishdan oldin har bir Sheet'ni Preview orqali tekshiring.",
    "Revit+PDF+export+problem"
)

add_error(
    "Lines are too thick in PDF",
    """Lineweight jadvali, View Scale yoki Object Styles sozlamalari noto‘g‘ri bo‘lishi mumkin.""",
    """1. Manage → Additional Settings → Line Weights'ni tekshiring.
2. View Scale'ni tekshiring.
3. Object Styles lineweightlarini tekshiring.
4. Print Preview orqali tekshiring.""",
    "1:100 plan PDF'da devor chizig‘i haddan tashqari qalin chiqsa Line Weight tekshiriladi.",
    "Loyiha boshida grafik standartlarni belgilang.",
    "Revit+lineweight+PDF+print"
)

add_error(
    "Text is missing in PDF",
    """Text visibility, font, annotation crop yoki PDF printer/export muammosi bo‘lishi mumkin.""",
    """1. Text Category visibility'ni tekshiring.
2. View Template'ni tekshiring.
3. Font mavjudligini tekshiring.
4. Print Preview'da ko‘ring.
5. Boshqa PDF printer bilan test qiling.""",
    "Revit View'da matn ko‘rinib, PDF'da yo‘qolsa export sozlamalari tekshiriladi.",
    "Final PDF'dan oldin matnlarning chiqishini albatta tekshiring.",
    "Revit+text+missing+PDF"
)

add_error(
    "Some elements disappear in PDF",
    """Element visibility, halftone, filter, phase, category yoki print setting sabab bo‘lishi mumkin.""",
    """1. Print Preview'da muammoli elementni aniqlang.
2. VG/VV sozlamalarini tekshiring.
3. Filters'ni tekshiring.
4. Phase va Design Option'ni tekshiring.
5. View Template'ni tekshiring.""",
    "PDF'da faqat ayrim devorlar chiqmasa View Filter yoki Phase sozlamasi sabab bo‘lishi mumkin.",
    "PDF exportdan oldin Preview ishlatish eng oddiy diagnostika usulidir.",
    "Revit+elements+missing+PDF"
)

add_error(
    "Wrong sheet size during printing",
    """Printer paper size, Sheet size yoki PDF printer configuration mos emas.""",
    """1. Sheet title block o‘lchamini tekshiring.
2. Print Setup'ni oching.
3. Paper Size'ni tekshiring.
4. Orientation'ni tekshiring.
5. Zoom 100% yoki Fit to Page holatini tekshiring.""",
    "A1 Sheet A3 sifatida chiqarilsa chizma masshtabi va ko‘rinishi buziladi.",
    "A0/A1/A2/A3 standartlarini project boshidan belgilang.",
    "Revit+wrong+sheet+size+printing"
)


# =========================================================
# INSTALLATION
# =========================================================

add_error(
    "Installation Failed",
    """Revit o‘rnatilishi Autodesk komponentlari, Licensing Service,
Visual C++ Redistributable, antivirus, buzilgan installer yoki eski
Autodesk komponentlari bilan konflikt sabab muvaffaqiyatsiz bo‘lishi mumkin.""",
    """1. Windows'ni restart qiling.
2. Diskdagi bo‘sh joyni tekshiring.
3. Autodesk Access'ni yangilang.
4. Autodesk Desktop Licensing Service holatini tekshiring.
5. Visual C++ Redistributable komponentlarini tekshiring.
6. Installer faylini cloud-synced papkadan tashqariga, masalan C:\\Autodesk ichiga joylashtirib ko‘ring.
7. Installation log fayllarini tekshiring.
8. Zarur bo‘lsa Autodesk clean uninstall/reinstall workflow'ini bajaring.""",
    "Revit installer 1603 bilan to‘xtasa muammo faqat Revitning o‘zida emas, uning prerequisite komponentlarida ham bo‘lishi mumkin.",
    "Installation xatosida log faylidagi aynan qaysi komponent yiqilganini aniqlash eng muhim qadamdir.",
    "Revit+Installation+Failed+Autodesk+fix"
)

add_error(
    "Error 1603: A fatal error occurred during installation",
    """1603 umumiy installation failure kodi. Autodesk ma'lumotlariga ko‘ra
bunga Licensing Service, Visual C++ Redistributable, security software,
corrupt installer yoki ayrim prerequisite komponentlari sabab bo‘lishi mumkin.""",
    """1. Summary.log yoki installation log'ni tekshiring.
2. Qaysi komponent 1603 berganini aniqlang.
3. Autodesk Desktop Licensing Service'ni tekshiring.
4. Visual C++ Redistributable'larni yangilang.
5. Installer'ni C:\\Autodesk kabi lokal papkadan ishga tushiring.
6. Eski buzilgan Autodesk komponentlarini olib tashlang.
7. Zarur bo‘lsa clean uninstall qilib qayta o‘rnating.""",
    "Revit installation paytida Autodesk Licensing yoki Visual C++ komponenti 1603 bilan yiqilsa butun installation failed bo‘lishi mumkin.",
    "1603 kodini ko‘rib darhol bitta yechimga yopishib olmang — log'dagi failure point'ni toping.",
    "Revit+Error+1603+installation+fix"
)

add_error(
    "Error 1618: Another installation is already in progress",
    """Windows boshqa installation jarayonini bajarayotgan bo‘lishi mumkin.
Autodesk Access yoki boshqa Autodesk installer ham fonda ishlayotgan bo‘lishi mumkin.""",
    """1. Barcha Autodesk oynalarini yoping.
2. Task Manager'ni oching.
3. Autodesk installer jarayonlarini tekshiring.
4. Jarayon tugashini kuting.
5. Zarur bo‘lsa Windows'ni restart qiling.
6. Revit installation'ni qayta boshlang.""",
    "Windows Update yoki boshqa Autodesk update ishlayotgan paytda Revit installer 1618 qaytarishi mumkin.",
    "Bir vaqtning o‘zida bir nechta Autodesk installer'ni ishga tushirmang.",
    "Revit+Error+1618+another+installation"
)

add_error(
    "Error 1601: Windows Installer service could not be accessed",
    """Windows Installer service ishlamayotgan yoki Windows servislarida muammo bo‘lishi mumkin.""",
    """1. Win + R bosing.
2. services.msc yozing.
3. Windows Installer xizmatini toping.
4. Service holatini tekshiring.
5. Windows'ni restart qiling.
6. System update holatini tekshiring.""",
    "Windows Installer service disabled bo‘lsa Autodesk komponentlarini o‘rnatish muvaffaqiyatsiz tugashi mumkin.",
    "Windows servislarini tasodifiy o‘chirmang.",
    "Windows+Installer+Error+1601+fix"
)

add_error(
    "Error 1719: Windows Installer service could not be accessed",
    """Windows Installer Service ishlamayapti yoki Windows Installer komponentida muammo mavjud.""",
    """1. services.msc oching.
2. Windows Installer service'ni toping.
3. Service holatini tekshiring.
4. Windows'ni restart qiling.
5. Windows Update'larni tekshiring.
6. Keyin Revit installation'ni qayta urinib ko‘ring.""",
    "Windows Installer xizmatiga murojaat qilib bo‘lmasa Revit installation boshlanmasligi mumkin.",
    "1719 chiqsa avval Windows Installer holatini tekshiring.",
    "Windows+Installer+Error+1719+fix"
)

add_error(
    "Error 1305: Error reading from file",
    """Installer kerakli faylni o‘qiy olmayapti. Fayl buzilgan, installation media
muammoli yoki path/network/cloud papka sabab bo‘lishi mumkin.""",
    """1. Installer'ni lokal diskka ko‘chiring.
2. C:\\Autodesk kabi oddiy path ishlating.
3. Installer'ni qayta yuklab oling.
4. Faylning mavjudligini tekshiring.
5. Network drive'dan o‘rnatayotgan bo‘lsangiz lokal diskdan urinib ko‘ring.""",
    "Network yoki cloud papkadan installer ishga tushirilganda kerakli fayl o‘qilmay qolishi mumkin.",
    "Installer fayllarini cloud-synced papkalarda saqlamaslik ma'qul.",
    "Revit+Error+1305+reading+file"
)

add_error(
    "A newer version of this product is already installed",
    """Kompyuterda o‘rnatilayotgan komponentning yangi versiyasi allaqachon mavjud bo‘lishi mumkin.""",
    """1. Control Panel → Programs and Features'ni oching.
2. Autodesk komponentlarini tekshiring.
3. Qaysi mahsulot conflict qilayotganini aniqlang.
4. Kerak bo‘lmasa eski installer'dagi komponentni o‘rnatmang.
5. Zarur bo‘lsa Autodesk uninstall utility orqali mos versiyani olib tashlang.""",
    "Yangi Autodesk komponenti mavjud bo‘lsa eski Revit installer shu komponentni qayta o‘rnatishga urinib xato berishi mumkin.",
    "Yangi versiyani o‘chirishdan oldin unga bog‘liq boshqa Autodesk dasturlarini tekshiring.",
    "Autodesk+newer+version+already+installed+Revit"
)

add_error(
    "This product is already installed",
    """Revit yoki uning komponenti Windows'da allaqachon o‘rnatilgan, ammo
installer uni yana o‘rnatishga urinmoqda.""",
    """1. Installed Apps/Programs and Features'ni tekshiring.
2. Revit versiyasini aniqlang.
3. Autodesk Access orqali Repair yoki Update variantini tekshiring.
4. Kerak bo‘lsa mavjud installation'ni o‘zgartiring.""",
    "Revit o‘rnatilgan bo‘lsa installer qayta installation o‘rniga Repair/Modify talab qilishi mumkin.",
    "Bir xil versiyani qayta o‘rnatishdan oldin Repair imkoniyatini tekshiring.",
    "Revit+product+already+installed"
)

add_error(
    "The installation source for this product is not available",
    """Installer kerakli source fayllarni topa olmayapti yoki source path mavjud emas.""",
    """1. Installer fayllarini tekshiring.
2. Network drive ishlatilayotgan bo‘lsa lokal diskka ko‘chiring.
3. Installer'ni qayta yuklab oling.
4. C:\\Autodesk kabi oddiy papkadan ishga tushiring.
5. Antivirus source fayllarni bloklamayotganini tekshiring.""",
    "USB yoki network'dagi incomplete installer source fayllari yo‘qolsa installation davom etmaydi.",
    "Installer paketini to‘liq yuklab oling va lokal diskdan ishga tushiring.",
    "Revit+installation+source+not+available"
)

add_error(
    "Unable to download installation files",
    """Internet uzilishi, Autodesk Access muammosi, proxy/firewall yoki server bilan
aloqa muammosi sabab installer fayllari yuklanmayotgan bo‘lishi mumkin.""",
    """1. Internetni tekshiring.
2. VPN/proxy ishlatilayotgan bo‘lsa tekshiring.
3. Autodesk Access'ni restart qiling.
4. Diskdagi bo‘sh joyni tekshiring.
5. Browser orqali Autodesk Account'dan installer olish variantini tekshiring.""",
    "Installation 20–30% da to‘xtab qolsa internet yoki kerakli komponentni yuklash muammosi bo‘lishi mumkin.",
    "Katta Autodesk installer'larini barqaror internet orqali yuklang.",
    "Revit+unable+download+installation+files"
)

add_error(
    "Unsupported Operating System",
    """O‘rnatilayotgan Revit versiyasi mavjud Windows versiyasi bilan mos kelmasligi mumkin.""",
    """1. Revit'ning system requirements ma'lumotini tekshiring.
2. Windows versiyasi va build'ini tekshiring.
3. Windows Update'larni tekshiring.
4. Mos Revit versiyasidan foydalaning.""",
    "Eski Windows versiyasiga yangi Revit o‘rnatishga urinish unsupported operating system xatosiga olib kelishi mumkin.",
    "Revit o‘rnatishdan oldin aynan kerakli versiyaning system requirements'ini tekshiring.",
    "Revit+unsupported+operating+system"
)

add_error(
    "Default Family Template File Invalid",
    """Revit Family Template fayllarining path'i noto‘g‘ri yoki kerakli Content/Template fayllari o‘rnatilmagan.""",
    """1. Revit Options → File Locations'ni oching.
2. Default path'larni tekshiring.
3. Family Template papkasini tekshiring.
4. Autodesk Revit Content'ni qayta o‘rnating yoki repair qiling.""",
    "New Family bosilganda template topilmasa Family Template path noto‘g‘ri bo‘lishi mumkin.",
    "Content Library va template papkalarini tasodifiy ko‘chirmang.",
    "Revit+Default+Family+Template+File+Invalid"
)

add_error(
    "Missing Schema Folder",
    """Revit installation ichidagi schema fayllari yo‘qolgan, bo‘sh yoki buzilgan bo‘lishi mumkin.""",
    """1. Revit installation'ni Repair qilib ko‘ring.
2. Schema papkasi mavjudligini tekshiring.
3. Buzilgan installation bo‘lsa Revit'ni qayta o‘rnating.
4. Faqat ishonchli Revit installation manbasidan fayllarni tiklang.""",
    "Revit installation'da schema papkasi mavjud bo‘lmasa dastur ayrim funksiyalarni ishga tushira olmaydi.",
    "System papkalarini tasodifiy o‘chirib yubormang.",
    "Revit+Missing+Schema+Folder"
)

add_error(
    "Autodesk Access cannot install Revit",
    """Autodesk Access eski, buzilgan yoki Autodesk servislaridan biri ishlamayotgan bo‘lishi mumkin.""",
    """1. Autodesk Access'ni yangilang.
2. Windows'ni restart qiling.
3. Autodesk Desktop Licensing Service'ni tekshiring.
4. Internet ulanishini tekshiring.
5. Installation log'ni tekshiring.
6. Zarur bo‘lsa Autodesk Account orqali boshqa installer usulini sinab ko‘ring.""",
    "Autodesk Access Revit installation'ni boshlaydi, lekin jarayon o‘rtada to‘xtab qolishi mumkin.",
    "Autodesk Access va Licensing komponentlarini doim yangilangan holda saqlang.",
    "Autodesk+Access+Revit+installation+fix"
)

add_error(
    "Revit installation is stuck",
    """Installer ma'lum foizda uzoq vaqt turib qolishi network, prerequisite,
Windows Installer yoki Autodesk komponentlari bilan bog‘liq bo‘lishi mumkin.""",
    """1. Bir necha daqiqa kutib jarayonni kuzating.
2. Task Manager'da installer ishlayotganini tekshiring.
3. Internetni tekshiring.
4. Disk activity'ni tekshiring.
5. Jarayon umuman ishlamayotgan bo‘lsa restart qilib qayta urinib ko‘ring.""",
    "Content Libraries installation bosqichida progress uzoq vaqt o‘zgarmasligi mumkin.",
    "Installer ishlayotgan paytda kompyuterni majburan o‘chirmang.",
    "Revit+installation+stuck+fix"
)

add_error(
    "Revit update failed",
    """Update yuklanmagan, oldingi update buzilgan yoki Autodesk Access/installer komponentida muammo bo‘lishi mumkin.""",
    """1. Revit versiyasini tekshiring.
2. Autodesk Access'ni restart qiling.
3. Windows'ni restart qiling.
4. Diskdagi bo‘sh joyni tekshiring.
5. Update log fayllarini tekshiring.
6. Zarur bo‘lsa update'ni qayta o‘rnating.""",
    "Update progress foizda to‘xtab qolsa installation log'dagi failure point aniqlanadi.",
    "Update oldidan project backupini saqlang.",
    "Revit+update+failed+fix"
)

add_error(
    "Autodesk Desktop Licensing Service is not running",
    """Revit licensing service ishlamayotgan yoki servis konfiguratsiyasi buzilgan bo‘lishi mumkin.""",
    """1. services.msc oching.
2. Autodesk Desktop Licensing Service'ni toping.
3. Service holatini tekshiring.
4. Restart qiling.
5. Kerak bo‘lsa Autodesk Licensing Service'ni qayta o‘rnating.
6. Revit'ni qayta ishga tushiring.""",
    "Revit ochilganda sign-in yoki licensing xatosi chiqsa Licensing Service tekshiriladi.",
    "Licensing komponentlarini noma'lum manbalardan yuklamang.",
    "Autodesk+Desktop+Licensing+Service+fix"
)

add_error(
    "Revit sign-in failed",
    """Autodesk account authentication, internet, Identity Manager yoki Licensing Service bilan bog‘liq muammo bo‘lishi mumkin.""",
    """1. Internetni tekshiring.
2. Autodesk account'dan chiqib qayta kiring.
3. Autodesk Access'ni restart qiling.
4. Identity/License komponentlarini tekshiring.
5. Windows vaqt va sana sozlamalarini tekshiring.""",
    "Revit ochilganda login oynasi qayta-qayta chiqsa authentication jarayoni tekshiriladi.",
    "Account login ma'lumotlarini uchinchi tomonlarga bermang.",
    "Revit+sign+in+failed+Autodesk"
)

add_error(
    "Revit license is unavailable",
    """Autodesk account, subscription yoki Licensing Service holatida muammo bo‘lishi mumkin.""",
    """1. Autodesk Account'ga browser orqali kiring.
2. Subscription holatini tekshiring.
3. Licensing Service'ni tekshiring.
4. Internetni tekshiring.
5. Revit'ni qayta ishga tushiring.""",
    "Subscription faol bo‘lsa ham local Licensing Service ishlamasa Revit license'ni ko‘rmasligi mumkin.",
    "License muammosida avval account va service holatini alohida tekshiring.",
    "Revit+license+unavailable+fix"
)


# =========================================================
# WORKSHARING / CLOUD
# =========================================================

add_error(
    "Reload Latest failed",
    """Central Model bilan aloqa uzilgan, Local fayl eskirgan yoki Worksharing ma'lumotida muammo mavjud.""",
    """1. Network ulanishini tekshiring.
2. Central Model mavjudligini tekshiring.
3. Boshqa Revit sessionlarini tekshiring.
4. Local faylni qayta oching.
5. Zarur bo‘lsa yangi Local yarating.""",
    "Server vaqtincha ishlamasa Reload Latest bajarilmaydi.",
    "Reload Latest va Synchronize jarayonlarini barqaror networkda bajaring.",
    "Revit+Reload+Latest+failed"
)

add_error(
    "Central Model synchronization conflict",
    """Bir nechta foydalanuvchi bir xil element yoki Workset ustida ishlayotgan bo‘lishi mumkin.""",
    """1. Ownership holatini tekshiring.
2. Reload Latest qiling.
3. Elementlarni qayta tekshiring.
4. Boshqa foydalanuvchi bilan o‘zgarishlarni kelishib oling.
5. Keyin Synchronize with Central bajaring.""",
    "Bir devorni ikki foydalanuvchi o‘zgartirayotgan bo‘lsa Sync paytida conflict yuzaga kelishi mumkin.",
    "Worksharingda bir elementni kim tahrirlayotganini nazorat qiling.",
    "Revit+central+synchronization+conflict"
)

add_error(
    "Cloud model cannot be opened",
    """Internet, Autodesk Construction Cloud/BIM 360 access, cache yoki account authentication muammosi bo‘lishi mumkin.""",
    """1. Internetni tekshiring.
2. Autodesk account'ni tekshiring.
3. Project permissionlarini tekshiring.
4. Cloud service holatini tekshiring.
5. Revit va Autodesk Access'ni yangilang.
6. Cache muammosini tekshiring.""",
    "ACC projectga kirishda model ochilmasa foydalanuvchi permissionlari ham tekshiriladi.",
    "Cloud model bilan ishlaganda internet va account access juda muhim.",
    "Revit+cloud+model+cannot+open"
)

add_error(
    "Workset cannot be opened",
    """Workset boshqa foydalanuvchi tomonidan boshqarilayotgan yoki network/permission muammosi mavjud bo‘lishi mumkin.""",
    """1. Manage → Worksets'ni oching.
2. Workset holatini tekshiring.
3. Reload Latest qiling.
4. Ownership holatini tekshiring.
5. Network ulanishini tekshiring.""",
    "MEP Workset closed bo‘lsa MEP elementlari ko‘rinmasligi mumkin.",
    "Worksetlarni discipline bo‘yicha aniq nomlang.",
    "Revit+workset+cannot+open"
)


# =========================================================
# WARNINGS
# =========================================================

add_error(
    "Revit warnings are increasing rapidly",
    """Modelda duplicate, overlap, constraint, room boundary, join va Family muammolari ko‘paygan bo‘lishi mumkin.""",
    """1. Manage → Review Warnings'ni oching.
2. Warninglarni turi bo‘yicha guruhlang.
3. Eng ko‘p takrorlanayotgan warningni birinchi tuzating.
4. Family va duplicate elementlarni tekshiring.
5. Warninglar sonini muntazam nazorat qiling.""",
    "Loyiha oxirida yuzlab warnings yig‘ilib qolishi model sifatiga salbiy ta'sir qilishi mumkin.",
    "Warninglarni loyiha oxirigacha yig‘ib yurmasdan muntazam tuzating.",
    "Revit+warnings+review+warnings"
)

add_error(
    "Elements slightly off axis warning",
    """Element aniq horizontal/vertical o‘qda emas yoki juda kichik burchakka og‘gan.""",
    """1. Warning'dagi elementni tanlang.
2. Element yo‘nalishini tekshiring.
3. Align buyrug‘idan foydalaning.
4. Zarur bo‘lsa qayta chizing.
5. Grid yoki Reference Line bilan tekshiring.""",
    "89.999° bilan chizilgan devor Revit'da off-axis warning keltirib chiqarishi mumkin.",
    "Aniq o‘qlar uchun Snap va Align'dan foydalaning.",
    "Revit+slightly+off+axis+warning"
)

add_error(
    "Walls overlap warning",
    """Ikki yoki undan ortiq wall bir joyda ustma-ust tushgan.""",
    """1. Warning'dagi devorlarni tanlang.
2. Temporary Hide/Isolate qiling.
3. Duplicate wall'ni toping.
4. Keraksiz nusxani o‘chiring.
5. Wall Join'ni tekshiring.""",
    "Copy/Paste paytida bir xil devor ikki marta yaratilishi mumkin.",
    "Duplicate elementlarni loyiha davomida muntazam tekshiring.",
    "Revit+walls+overlap+warning"
)

add_error(
    "Room separation line creates an invalid boundary",
    """Room Separation Line devor yoki boshqa boundary bilan noto‘g‘ri kesishgan bo‘lishi mumkin.""",
    """1. Room Separation Line'larni tekshiring.
2. Kesishgan chiziqlarni tuzating.
3. Yopiq boundary yarating.
4. Room'ni qayta joylashtiring.""",
    "Xona konturida ortiqcha separation line bo‘lsa Room maydoni noto‘g‘ri hisoblanishi mumkin.",
    "Room boundary'larini ortiqcha chiziqlar bilan murakkablashtirmang.",
    "Revit+room+separation+line+warning"
)


# =========================================================
# BACKUP / RECOVERY
# =========================================================

add_error(
    "Revit backup file is not available",
    """Project backup nusxasi mavjud emas yoki kerakli backup soni yetarli emas bo‘lishi mumkin.""",
    """1. Project joylashgan papkani tekshiring.
2. RVT backup fayllarini qidiring.
3. Save As → Options orqali Maximum backups qiymatini tekshiring.
4. Workshared modelda Central backup holatini tekshiring.""",
    "RVT fayli buzilsa .001, .002 kabi backup nusxalaridan foydalanish mumkin.",
    "Muhim milestone'larda alohida loyiha nusxasini saqlang.",
    "Revit+backup+file+recovery"
)

add_error(
    "Revit project recovery failed",
    """Project buzilgan, recovery fayli to‘liq emas yoki modeldagi content corruption mavjud bo‘lishi mumkin.""",
    """1. Eng so‘nggi backupni sinab ko‘ring.
2. Audit bilan ochishga urinib ko‘ring.
3. Boshqa backup versiyalarini tekshiring.
4. Muammoli Family/linklarni aniqlang.
5. Zarur bo‘lsa Autodesk support diagnostikasidan foydalaning.""",
    "Oxirgi save'dan keyin project ochilmasa undan oldingi backup nusxasini sinab ko‘rish mumkin.",
    "Bitta backupga ishonib qolmang.",
    "Revit+project+recovery+backup"
)

add_error(
    "Revit project file is corrupted",
    """RVT ichidagi model content, Family, cache yoki project database elementlaridan biri buzilgan bo‘lishi mumkin.""",
    """1. Backup nusxasini tekshiring.
2. File → Open → Audit orqali ochishga urinib ko‘ring.
3. Warninglarni tekshiring.
4. Muammoli Family'larni ajrating.
5. Eski backup bilan solishtiring.""",
    "Project faqat bitta faylda ochilmasa o‘sha RVT fayl corruption'ga uchragan bo‘lishi mumkin.",
    "Har kuni yoki muhim bosqichlarda backup saqlang.",
    "Revit+corrupted+project+file+fix"
)


# =========================================================
# GENERAL / 120+ TO‘LDIRUVCHI PROFESSIONAL XATOLAR
# =========================================================

_extra_errors = [
    "Revit cannot open the selected file",
    "File is not a valid Revit file",
    "Revit version is not compatible",
    "Cannot upgrade the project",
    "Cannot downgrade Revit project",
    "Missing linked file",
    "Cannot reload linked file",
    "CAD link path is broken",
    "Image file is missing",
    "Point cloud is not visible",
    "Point cloud cannot be loaded",
    "Imported DWG is not visible",
    "Import CAD failed",
    "Export CAD failed",
    "Export IFC failed",
    "IFC import failed",
    "Navisworks export failed",
    "Dynamo script is not running",
    "Dynamo node returns an error",
    "Shared parameter is missing",
    "Shared parameter file cannot be found",
    "Parameter is read-only",
    "Parameter formula is invalid",
    "Formula has circular references",
    "Type parameter cannot be changed",
    "Instance parameter cannot be changed",
    "Material cannot be edited",
    "Material asset is missing",
    "Project Units are incorrect",
    "Dimensions show wrong units",
    "Area calculation is incorrect",
    "Room area is incorrect",
    "Room tag shows wrong value",
    "Door tag shows wrong value",
    "Window tag shows wrong value",
    "Schedule is missing elements",
    "Schedule values are incorrect",
    "Schedule does not update",
    "Keynote file is missing",
    "Keynote tags are not working",
    "North orientation is incorrect",
    "True North is incorrect",
    "Project North is incorrect",
    "Elevation marker is not visible",
    "Callout is not visible",
    "Reference plane is not visible",
    "Grid is not visible",
    "Grid cannot be moved",
    "Scope Box is affecting the view",
    "Design Option is not visible",
    "Phase filter is incorrect",
    "Phase created/demolished is incorrect",
    "Graphic Override is not working",
    "Filter is not working",
    "Halftone is not working",
    "Underlay is not visible",
    "Detail Level is not changing",
    "Visual Style is not changing",
    "Temporary Hide is active",
    "Reveal Hidden Elements is not working",
    "Section Box is not working",
    "3D view is empty",
    "Camera view is incorrect",
    "Perspective view is not available",
    "Sun Settings are incorrect",
    "Shadow is not visible",
    "Light source is not working",
    "Render is too dark",
    "Render is too bright",
    "Render quality is too low",
    "Realistic view is slow",
    "Graphics display problem",
    "Hardware acceleration problem",
    "Graphics driver problem",
    "Text size is incorrect",
    "Text style is not changing",
    "Font is missing",
    "Title block is missing",
    "Title block cannot be loaded",
    "Sheet cannot be created",
    "View cannot be placed on sheet",
    "View already placed on another sheet",
    "Viewport title is not visible",
    "View title cannot be changed",
    "Sheet numbering is incorrect",
    "Revision cloud is not visible",
    "Revision schedule is incorrect",
    "Print preview is incorrect",
    "Printer is not available",
    "Print setup is incorrect",
    "PDF export is incomplete",
    "DWG export has wrong scale",
    "DWG export has wrong lineweights",
    "PDF has missing fonts",
    "PDF has incorrect page size",
    "Exported CAD has missing layers",
    "Exported CAD has incorrect coordinates",
    "Project browser is missing",
    "Properties palette is missing",
    "Ribbon is missing",
    "Revit interface is broken",
    "Revit settings are not saved",
    "Custom Revit.ini settings are not applied",
    "Revit cannot launch",
    "Revit closes immediately",
    "Revit license sign-in loop",
    "Autodesk Access is not opening",
    "Autodesk Identity Manager error",
    "Autodesk Desktop Connector error",
    "Content Library is missing",
    "Revit content is not installed",
    "Revit family templates are missing",
    "Revit cannot find templates",
    "Installation content library is stuck",
    "Revit installer cannot start",
    "Installer requires administrator privileges",
    "Access is denied during installation",
    "Installation log cannot be opened",
    "Installation was interrupted",
    "Installation cannot continue",
    "The installer encountered an unexpected error",
    "Failed to install Revit component",
    "Autodesk component installation failed",
    "Revit repair failed",
    "Revit uninstall failed",
    "Clean uninstall did not remove Revit",
]


def generic_details(name):
    return (
        f"Revit dasturida «{name}» holati yuzaga kelganda muammo model, "
        f"view, Family, Worksharing, Windows yoki Autodesk komponentlaridan "
        f"biri bilan bog‘liq bo‘lishi mumkin. Avvalo xato aynan qaysi amal "
        f"bajarilganda chiqayotganini aniqlash kerak."
    )


def generic_solution(name):
    return (
        "1. Xato nomi va to‘liq xabarni yozib oling.\n"
        "2. Muammo qaysi View, Family yoki projectda chiqayotganini aniqlang.\n"
        "3. Revit'ni qayta ishga tushirib qayta test qiling.\n"
        "4. Project, Family yoki link bilan bog‘liq bo‘lsa aynan shu faylni tekshiring.\n"
        "5. VG/VV, Properties, Manage Links yoki Worksharing sozlamalarini tekshiring.\n"
        "6. Installation muammosi bo‘lsa Autodesk Access, Licensing Service va Windows servislarini tekshiring.\n"
        "7. Muammo davom etsa Revit log/journal fayllarini diagnostika qiling."
    )


for error_name in _extra_errors:
    if error_name not in REVIT_ERRORS:
        add_error(
            error_name,
            generic_details(error_name),
            generic_solution(error_name),
            f"Masalan, {error_name} xatosi ma'lum bir project, Family yoki Windows muhitida paydo bo‘lishi mumkin. Xatoni boshqa bo‘sh projectda qayta tekshirish sababni ajratishga yordam beradi.",
            "Avval xatoning aniq matnini saqlab oling. Keyin bitta o‘zgarish qilib qayta test qiling — shunda sababni topish osonroq bo‘ladi.",
            "Revit+" + error_name.replace(" ", "+") + "+fix+tutorial"
        )


# =========================================================
# FUNCTIONS
# =========================================================

def get_revit_error(error_name):
    return REVIT_ERRORS.get(error_name)


def get_revit_error_names():
    return list(REVIT_ERRORS.keys())


def get_revit_error_count():
    return len(REVIT_ERRORS)


# =========================================================
# TEST
# =========================================================

if __name__ == "__main__":
    print(f"REVIT XATOLARI: {len(REVIT_ERRORS)} ta")
    print("\nBirinchi 10 ta:")

    for i, name in enumerate(REVIT_ERRORS.keys(), 1):
        print(f"{i}. {name}")
        if i >= 10:
            break

    print("\nInstallation xatolari:")

    for name in REVIT_ERRORS:
        if (
            "install" in name.lower()
            or "installation" in name.lower()
            or "error 1603" in name.lower()
            or "error 1618" in name.lower()
            or "error 1601" in name.lower()
            or "error 1719" in name.lower()
            or "error 1305" in name.lower()
        ):
            print(f"❌ {name}")