
from urllib.parse import quote_plus


AUTOCAD_ERRORS = {}


def add_error(error_name, sabab, yechim, maslahat, video_query=None):
    """
    AutoCAD xatosini bazaga qo'shadi.
    video_query berilmasa, error_name asosida YouTube qidiruvi yaratiladi.
    """
    if video_query is None:
        video_query = f"AutoCAD {error_name} fix"

    AUTOCAD_ERRORS[error_name] = {
        "sabab": sabab,
        "yechim": yechim,
        "maslahat": maslahat,
        "video": (
            "https://www.youtube.com/results?search_query="
            + quote_plus(video_query)
        )
    }


# =========================================================
# 💥 1. CRASH / FATAL / SYSTEM ERRORS
# =========================================================

add_error(
    "FATAL ERROR: Unhandled Access Violation Reading 0x0000",
    "AutoCAD xotiraga murojaat qilishda xatoga uchragan. Bunga buzilgan DWG, grafik driver, "
    "uchinchi tomon pluginlari yoki AutoCAD konfiguratsiyasi sabab bo'lishi mumkin.",
    [
        "AutoCADni to'liq yoping va qayta ishga tushiring.",
        "Muammoli DWGni RECOVER buyrug'i bilan oching.",
        "AUDIT buyrug'ini ishga tushirib, Yes orqali xatolarni tuzating.",
        "GRAPHICSCONFIG buyrug'i orqali Hardware Accelerationni vaqtincha o'chirib ko'ring.",
        "AutoCADni yangilang yoki Repair funksiyasidan foydalaning.",
        "Muammo faqat bitta DWGda bo'lsa, yangi DWGga obyektlarni bosqichma-bosqich ko'chirib tekshiring."
    ],
    "Xato takrorlansa, qaysi DWG yoki qaysi buyruqdan keyin crash bo'lganini aniqlash juda muhim."
)

add_error(
    "FATAL ERROR: Unhandled Access Violation Writing 0x0000",
    "AutoCAD xotiraga ma'lumot yozishda muammoga uchragan. Buzilgan drawing, plugin yoki grafik tizim sabab bo'lishi mumkin.",
    [
        "AutoCADni qayta ishga tushiring.",
        "DWGni RECOVER orqali oching.",
        "AUDIT → Yes bajaring.",
        "GRAPHICSCONFIG orqali Hardware Accelerationni tekshiring.",
        "Pluginlarni vaqtincha o'chirib ko'ring.",
        "AutoCAD Repair funksiyasini ishga tushiring."
    ],
    "Muhim DWG fayllarda muntazam backup saqlang."
)

add_error(
    "AutoCAD Error Aborting",
    "AutoCAD jiddiy ichki xatoga uchrab, joriy operatsiyani to'xtatmoqda.",
    [
        "AutoCADni qayta ishga tushiring.",
        "Drawing Recovery oynasini tekshiring.",
        "Muammoli DWGni RECOVER bilan oching.",
        "AUDIT bajaring.",
        "AutoCAD Update o'rnatilganini tekshiring.",
        "Muammo davom etsa Reset Settings yoki Repair funksiyasidan foydalaning."
    ],
    "Xato har safar bir xil faylda chiqsa, muammo drawingning o'zida bo'lishi ehtimoli yuqori."
)

add_error(
    "Unhandled Exception c0000005 (Access Violation)",
    "Windows yoki AutoCAD jarayoni ruxsatsiz xotira manziliga murojaat qilgan.",
    [
        "AutoCADni qayta ishga tushiring.",
        "GRAPHICSCONFIG orqali Hardware Accelerationni tekshiring.",
        "Video driverni yangilang.",
        "DWGni RECOVER orqali tekshiring.",
        "Uchinchi tomon ARX/LSP pluginlarini vaqtincha o'chiring.",
        "AutoCADni Repair qiling."
    ],
    "Pluginlar bilan bog'liq crashlarda pluginlarni bittadan tekshirish eng to'g'ri usul."
)

add_error(
    "System Error: Unhandled e0434352h Exception",
    ".NET komponenti yoki AutoCAD ichidagi managed kod bilan bog'liq exception yuzaga kelgan.",
    [
        "AutoCADni qayta ishga tushiring.",
        "Windows Update'ni tekshiring.",
        "Autodesk Desktop App yoki Autodesk Access orqali AutoCAD update qiling.",
        ".NET komponentlari va AutoCAD installation holatini tekshiring.",
        "AutoCADni Repair qiling."
    ],
    "Bu xato ko'pincha dastur komponentlari yoki pluginlar bilan bog'liq bo'lishi mumkin."
)

add_error(
    "FATAL ERROR: ASC initialization failed",
    "AutoCAD ishga tushish vaqtida ASC komponentini ishga tushira olmagan.",
    [
        "AutoCADni administrator sifatida ishga tushirib ko'ring.",
        "Autodesk servislarini tekshiring.",
        "AutoCAD installationini Repair qiling.",
        "Autodesk Access orqali yangilanishlarni o'rnating.",
        "Muammo davom etsa AutoCADni qayta o'rnatish kerak bo'lishi mumkin."
    ],
    "Installation papkalarini qo'lda o'chirishdan oldin backup va Autodesk uninstall vositalaridan foydalaning."
)

add_error(
    "Unable to load the Modeler DLLs",
    "AutoCAD Modeler uchun kerakli DLL fayllarni yuklay olmayapti.",
    [
        "AutoCADni qayta ishga tushiring.",
        "Installationni Repair qiling.",
        "GRAPHICSCONFIGni tekshiring.",
        "Autodesk Access orqali AutoCAD update qiling.",
        "Uchinchi tomon pluginlarini vaqtincha o'chiring."
    ],
    "DLL fayllarni internetdan noma'lum saytlardan alohida yuklab almashtirmang."
)

add_error(
    'FATAL ERROR: Unhandled Delayload "modlr.dll" Module Not Found',
    "AutoCAD kerakli modlr.dll modulini topa yoki yuklay olmayapti.",
    [
        "AutoCADni Repair qiling.",
        "Autodesk Access orqali update qiling.",
        "Windows tizim fayllarini tekshiring.",
        "AutoCAD installation papkasida modul mavjudligini tekshiring.",
        "Kerak bo'lsa AutoCADni qayta o'rnating."
    ],
    "DLL faylini noma'lum manbadan yuklab olish xavfli."
)

add_error(
    "Unhandled exception has occurred in a component in your application",
    "AutoCAD yoki uning komponentlaridan biri exception hosil qilgan.",
    [
        "AutoCADni qayta ishga tushiring.",
        "Windows va AutoCAD update'larini tekshiring.",
        "Muammoli pluginlarni vaqtincha o'chiring.",
        "AutoCADni Repair qiling.",
        "Muammo ma'lum DWGda bo'lsa RECOVER va AUDIT bajaring."
    ],
    "Xatolik qaysi amal paytida chiqqanini yozib olish diagnostikani osonlashtiradi."
)

add_error(
    "Exception from HRESULT: 0x800AC472",
    "AutoCAD COM/automation jarayoni boshqa operatsiya bilan band bo'lganida exception berishi mumkin.",
    [
        "Joriy commandni ESC orqali bekor qiling.",
        "AutoCADni qayta ishga tushiring.",
        "Bir vaqtning o'zida bir nechta automation dasturlarini ishlatmang.",
        "VBA/LISP/COM pluginlarini tekshiring.",
        "Muammo davom etsa AutoCAD Repair qiling."
    ],
    "Excel, VBA yoki boshqa dastur AutoCAD bilan ishlayotgan bo'lsa, ularni ham tekshiring."
)


# =========================================================
# 📁 2. DRAWING / DWG / RECOVERY
# =========================================================

add_error(
    '[number] errors were found in the drawing file during open',
    "DWG faylida ochilish vaqtida ma'lumotlar yoki obyektlar bilan bog'liq xatolar topilgan.",
    [
        "Drawing ochilgandan keyin AUDIT buyrug'ini ishga tushiring.",
        "Yes tanlab xatolarni tuzattiring.",
        "Faylni yangi nom bilan SAVE AS qiling.",
        "Kerak bo'lsa RECOVER bilan qayta oching.",
        "Backup nusxani ham tekshiring."
    ],
    "Original faylni ustidan yozishdan oldin backup nusxa oling."
)

add_error(
    "The drawing file requires recovery",
    "AutoCAD DWG faylni normal holatda ochish uchun recovery jarayonini talab qilmoqda.",
    [
        "RECOVER buyrug'ini ishga tushiring.",
        "Muammoli DWGni tanlang.",
        "Tekshiruv tugashini kuting.",
        "AUDIT → Yes bajaring.",
        "Faylni yangi nom bilan saqlang."
    ],
    "Recovery tugagandan keyin AUDITni ham bajarish foydali."
)

add_error(
    "Drawing file is not valid",
    "Fayl haqiqiy yoki to'liq DWG sifatida o'qilmayapti.",
    [
        "Fayl kengaytmasini tekshiring.",
        "RECOVER orqali ochishga urinib ko'ring.",
        "Backup nusxani tekshiring.",
        "Faylni boshqa AutoCAD kompyuterida tekshirib ko'ring.",
        "Fayl boshqa dasturdan eksport qilingan bo'lsa qayta eksport qiling."
    ],
    "DWG fayl nomini faqat .dwg qilib o'zgartirish buzilgan faylni tiklamaydi."
)

add_error(
    "Unable to open drawing",
    "DWG fayliga kirish, fayl buzilishi, permission yoki versiya muammosi bo'lishi mumkin.",
    [
        "Fayl joylashgan papkaga kirish huquqini tekshiring.",
        "DWGni lokal diskka ko'chirib ochib ko'ring.",
        "RECOVER buyrug'idan foydalaning.",
        "Backup nusxani tekshiring.",
        "AutoCAD versiyasi bilan mosligini tekshiring."
    ],
    "Network yoki USB diskdagi faylni avval lokal diskka ko'chirib ko'ring."
)

add_error(
    "AcDs Error: signature mismatch",
    "DWG ichidagi AcDs ma'lumotlari yoki fayl strukturasi bilan bog'liq mos kelmaslik yuzaga kelgan.",
    [
        "DWGni RECOVER orqali oching.",
        "AUDIT → Yes bajaring.",
        "PURGE bajaring.",
        "Faylni yangi nom bilan saqlang.",
        "Muammo davom etsa backup yoki boshqa DWG versiyasini tekshiring."
    ],
    "Eski va yangi AutoCAD versiyalari orasidagi konvertatsiyalarda backup saqlash foydali."
)

add_error(
    'Document "<filename>.dwg" has a command in progress.',
    "Drawingda oldingi command hali tugamagan yoki AutoCAD boshqa operatsiyani kutmoqda.",
    [
        "ESC tugmasini bir necha marta bosing.",
        "Command Line'dagi joriy buyruqni tekshiring.",
        "Enter orqali kutilayotgan qiymatni kiriting yoki commandni bekor qiling.",
        "Kerak bo'lsa AutoCADni qayta ishga tushiring."
    ],
    "Command Line'ni doim ochiq saqlash bunday muammolarni tushunishni osonlashtiradi."
)

add_error(
    "Drawing file is read-only",
    "DWG fayli faqat o'qish rejimida ochilgan yoki Windows fayl permissioni yozishga ruxsat bermayapti.",
    [
        "DWG ustiga o'ng tugma → Properties qiling.",
        "Read-only belgisi mavjudligini tekshiring.",
        "Faylni yozish mumkin bo'lgan papkaga ko'chiring.",
        "Network fayl bo'lsa permissionni tekshiring.",
        "Save As orqali yangi nusxa yarating."
    ],
    "Muhim loyihalarni OneDrive/Network orqali tahrirlashda fayl lock holatini tekshiring."
)

add_error(
    "Drawing is already open",
    "DWG boshqa AutoCAD oynasida yoki boshqa foydalanuvchi tomonidan ochilgan bo'lishi mumkin.",
    [
        "Boshqa AutoCAD oynalarini tekshiring.",
        "Task Manager orqali AutoCAD jarayonlarini tekshiring.",
        "Network fayl bo'lsa boshqa foydalanuvchi faylni ochganini tekshiring.",
        "Lock fayllari mavjudligini tekshiring."
    ],
    "Bir xil DWGni bir vaqtning o'zida bir nechta foydalanuvchi tahrirlamasligi kerak."
)

add_error(
    "Proxy Information dialog box",
    "DWGda original dastur yoki Object Enabler talab qiladigan proxy obyektlar mavjud.",
    [
        "Proxy obyektlar haqida ma'lumotni tekshiring.",
        "Kerak bo'lsa tegishli Object Enablerni o'rnating.",
        "PROXYSHOW sozlamasini tekshiring.",
        "Original dasturda faylni ochish imkonini tekshiring."
    ],
    "Proxy obyektlarni portlatish yoki o'chirishdan oldin ularning loyiha uchun zarurligini tekshiring."
)


# =========================================================
# ⌨️ 3. COMMAND / COMMAND LINE
# =========================================================

add_error(
    "Unknown command",
    "AutoCAD kiritilgan command nomini tanimayapti.",
    [
        "Command nomini to'g'ri yozilganini tekshiring.",
        "Alias ishlatilgan bo'lsa aliasni tekshiring.",
        "Buyruq AutoCAD versiyasida mavjudligini tekshiring.",
        "LISP yoki plugin commandi bo'lsa plugin yuklanganini tekshiring."
    ],
    "Command Line'dagi to'liq xabarni tekshiring."
)

add_error(
    "Command not found",
    "Kiritilgan command mavjud emas yoki kerakli modul/plugin yuklanmagan.",
    [
        "Command nomini tekshiring.",
        "AutoCAD standart commandini ishlatib ko'ring.",
        "Plugin kerak bo'lsa uning yuklanganini tekshiring.",
        "LISP ishlatilgan bo'lsa APPLOAD orqali qayta yuklang."
    ],
    "Uchinchi tomon commandlari uchun plugin versiyasi AutoCAD versiyasiga mos bo'lishi kerak."
)

add_error(
    "Invalid option keyword",
    "Command ichida mavjud bo'lmagan option tanlangan.",
    [
        "Command Line'dagi mavjud optionlarni o'qing.",
        "Kerakli optionning qisqa harfini to'g'ri kiriting.",
        "ESC bilan commandni bekor qilib qayta boshlang."
    ],
    "AutoCAD commandlari kontekstga qarab turli optionlarni ko'rsatishi mumkin."
)

add_error(
    "Invalid point",
    "AutoCAD kiritilgan koordinata yoki nuqtani to'g'ri qabul qila olmadi.",
    [
        "Koordinata formatini tekshiring.",
        "X,Y formatidan foydalanib ko'ring.",
        "Dynamic Inputni tekshiring.",
        "Object Snap sozlamalarini tekshiring."
    ],
    "Aniq nuqtalar uchun Object Snap juda foydali."
)

add_error(
    "Hit enter to cancel or [Retry]:",
    "AutoCAD joriy operatsiyada xatoga uchragan va qayta urinib ko'rish yoki bekor qilishni kutmoqda.",
    [
        "Muammoni davom ettirish kerak bo'lmasa Enter bosing.",
        "ESC bilan commandni to'liq bekor qilib ko'ring.",
        "Agar xato takrorlansa, oldingi commandni tekshiring."
    ],
    "Command Line'dagi undan oldingi xabar ko'pincha asl sababni ko'rsatadi."
)

add_error(
    "Command line is hidden",
    "Command Line oynasi yopilgan yoki interfeysdan chiqarib yuborilgan.",
    [
        "CTRL+9 tugmalarini bosing.",
        "Command Line qaytganini tekshiring.",
        "Workspace'ni qayta yuklang.",
        "AutoCAD interfeysini Reset Settings orqali tiklash mumkin."
    ],
    "Command Line AutoCAD diagnostikasi uchun eng muhim oynalardan biridir."
)

add_error(
    "Cannot invoke (command) from *error* without prior call",
    "AutoLISP error handler ichidan command chaqirilgan va command konteksti mavjud emas.",
    [
        "Muammoli LISP kodini tekshiring.",
        "Error handlerni tekshiring.",
        "LISPni qayta yuklang.",
        "Kerak bo'lsa LISP muallifining yangilangan versiyasidan foydalaning."
    ],
    "Bu odatda DWG emas, AutoLISP kodi bilan bog'liq muammo."
)

add_error(
    "(*pop-error-mode*) underflow",
    "AutoLISP error mode stack noto'g'ri boshqarilgan.",
    [
        "Oxirgi yuklangan LISP faylni aniqlang.",
        "LISPni vaqtincha o'chirib ko'ring.",
        "Error handler kodini tekshiring.",
        "LISPning yangilangan versiyasini o'rnating."
    ],
    "Har bir LISP faylini bittadan test qilish sababni topishni osonlashtiradi."
)

add_error(
    ".arx cannot find the procedure you need",
    "ARX modulida kerakli procedure mavjud emas yoki modul versiyasi AutoCAD bilan mos emas.",
    [
        "ARX fayl AutoCAD versiyasiga mosligini tekshiring.",
        "Pluginni qayta o'rnating.",
        "Pluginning yangilangan versiyasini yuklang.",
        "Kerak bo'lmasa pluginni vaqtincha olib tashlang."
    ],
    "ARX pluginlar AutoCAD versiyasiga juda bog'liq."
)

add_error(
    ".crx cannot find the procedure you need",
    "CRX modulida kerakli procedure topilmadi yoki plugin mos emas.",
    [
        "CRX plugin versiyasini tekshiring.",
        "Pluginni yangilang.",
        "AutoCADni qayta ishga tushiring.",
        "Kerak bo'lsa pluginni Repair yoki reinstall qiling."
    ],
    "Noma'lum manbadan CRX fayllarni o'rnatmang."
)

add_error(
    "Character ' ' is not allowed on the command line or in response files.",
    "Command yoki response file ichida ruxsat etilmagan bo'sh joy belgisi ishlatilgan.",
    [
        "Kiritilgan commandni tekshiring.",
        "Response file formatini tekshiring.",
        "Keraksiz belgilarni olib tashlang.",
        "Commandni qo'lda qayta kiriting."
    ],
    "Response file bilan ishlaganda formatga aniq rioya qiling."
)

add_error(
    "Character '[]' is not allowed on the command line or in response files.",
    "Command Line yoki response file ichida AutoCAD qabul qilmaydigan belgilar ishlatilgan.",
    [
        "Kiritilgan matnni tekshiring.",
        "Maxsus belgilarni olib tashlang.",
        "Response file sintaksisini tekshiring.",
        "Commandni oddiy formatda qayta kiriting."
    ],
    "Maxsus belgilar plugin yoki script fayllarida ham muammo keltirishi mumkin."
)


# =========================================================
# 🧱 4. LAYER / OBJECT
# =========================================================

add_error(
    "Layer is locked",
    "Obyekt joylashgan layer Lock qilingan.",
    [
        "Layer Properties Manager'ni oching.",
        "Kerakli layerning Lock belgisini o'chiring.",
        "Obyektni qayta tahrirlang."
    ],
    "Tayyor chizmada kerakli layerlarni Lock qilish tasodifiy o'zgarishlardan himoya qiladi."
)

add_error(
    "Layer is frozen",
    "Layer Freeze holatida bo'lgani uchun obyektlar ko'rinmaydi yoki tahrirlanmaydi.",
    [
        "Layer Propertiesni oching.",
        "Freeze holatini tekshiring.",
        "Kerakli layerni Thaw qiling.",
        "REGENALL bajaring."
    ],
    "Model va viewportdagi VP Freeze holatini alohida tekshiring."
)

add_error(
    "Layer is off",
    "Layer Off holatida.",
    [
        "Layer Properties Manager'ni oching.",
        "Layerni On qiling.",
        "REGENALL bajaring."
    ],
    "Layer Off va Freeze bir xil narsa emas."
)

add_error(
    "Object cannot be modified",
    "Obyekt Lock qilingan layerda, XREF ichida yoki tahrirlashga yaroqsiz obyekt bo'lishi mumkin.",
    [
        "Layer Lock holatini tekshiring.",
        "Obyekt XREF ekanini tekshiring.",
        "Properties oynasidan obyekt turini aniqlang.",
        "Kerak bo'lsa BEDIT yoki REFEDIT ishlating."
    ],
    "XREF obyektini asosiy DWG ichida to'g'ridan-to'g'ri tahrirlab bo'lmaydi."
)

add_error(
    "Object is on a locked layer",
    "Tanlangan obyekt Lock qilingan layerga tegishli.",
    [
        "Layer Propertiesni oching.",
        "Layerni Unlock qiling.",
        "Commandni qayta bajaring."
    ],
    "Lock qilingan layerda chizish va o'zgartirish cheklanadi."
)

add_error(
    "Object not found",
    "Tanlangan obyekt ko'rinmayotgan, o'chirilgan yoki boshqa layerda bo'lishi mumkin.",
    [
        "ZOOM EXTENTS bajaring.",
        "Layer holatini tekshiring.",
        "Qidiruv uchun QSELECT yoki SELECTSIMILAR ishlating.",
        "REGENALL bajaring."
    ],
    "Uzoqda qolgan obyekt Zoom Extentsni buzishi mumkin."
)

add_error(
    "Selection failed",
    "Obyektni tanlashda layer, selection mode yoki obyekt turi bilan bog'liq muammo bor.",
    [
        "Layer Lock holatini tekshiring.",
        "SELECTIONCYCLINGni tekshiring.",
        "QSELECTdan foydalaning.",
        "Quick Select orqali obyektni toping."
    ],
    "Selection Cycling ustma-ust obyektlarni tanlashda foydali."
)


# =========================================================
# 🟨 5. HATCH
# =========================================================

add_error(
    "Hatch boundary not found",
    "AutoCAD Hatch uchun yopiq boundary topa olmayapti.",
    [
        "Kontur yopiq ekanini tekshiring.",
        "PEDIT → Join orqali segmentlarni ulang.",
        "Gaplarni tekshiring.",
        "HATCH → Select Objects orqali boundaryni qo'lda tanlang."
    ],
    "Hatch uchun eng ishonchli variant yopiq polyline hisoblanadi."
)

add_error(
    "Hatch spacing too dense",
    "Hatch pattern juda zich bo'lib, chizma sekinlashishi mumkin.",
    [
        "Hatch Scale qiymatini oshiring.",
        "Juda zich patternni almashtiring.",
        "Keraksiz Hatchlarni kamaytiring."
    ],
    "Katta arxitektura chizmalarida juda zich Hatch ishlatishdan saqlaning."
)

add_error(
    "Hatch cannot be created",
    "Boundary noto'g'ri, ochiq yoki murakkab geometriyaga ega.",
    [
        "Boundaryni tekshiring.",
        "PEDIT → Close yoki Join ishlating.",
        "HATCH ichida Select Objectsdan foydalaning.",
        "Geometriyani soddalashtiring."
    ],
    "Hatch ishlamasa avval boundaryni tekshirish kerak."
)

add_error(
    "Hatch pattern not found",
    "Tanlangan Hatch pattern AutoCAD tomonidan topilmayapti.",
    [
        "Hatch pattern ro'yxatini tekshiring.",
        "Custom PAT faylini tekshiring.",
        "AutoCAD support path sozlamasini tekshiring.",
        "Kerakli PAT faylni to'g'ri joylashtiring."
    ],
    "PAT fayllarni AutoCAD Support Path ichida saqlash qulay."
)


# =========================================================
# 📐 6. DIMENSION / TEXT / FONT
# =========================================================

add_error(
    "Dimension style not found",
    "DWGda ishlatilgan Dimension Style mavjud emas yoki boshqa drawingdan to'liq o'tmagan.",
    [
        "DIMSTYLE buyrug'ini oching.",
        "Mavjud stylelarni tekshiring.",
        "Kerakli style yarating yoki import qiling.",
        "Dimensionlarni yangi stylega o'tkazing."
    ],
    "Template ichida standart DIMSTYLE saqlash foydali."
)

add_error(
    "Dimension value is incorrect",
    "Dimension obyektining o'lchovi yoki drawing Units sozlamasi noto'g'ri.",
    [
        "UNITS buyrug'ini tekshiring.",
        "Dimension Associativityni tekshiring.",
        "Geometriyaning haqiqiy o'lchamini DIST bilan tekshiring.",
        "DIMSTYLE sozlamalarini tekshiring."
    ],
    "Model Space'da geometriyani odatda 1:1 chizish kerak."
)

add_error(
    "Text style not found",
    "DWGda ishlatilgan Text Style mavjud emas yoki font bilan bog'liq muammo bor.",
    [
        "STYLE buyrug'ini oching.",
        "Text Style nomini tekshiring.",
        "Kerakli fontni tanlang.",
        "Textlarni qayta tekshiring."
    ],
    "Loyiha bilan ishlatilgan SHX va TTF fontlarni birga saqlang."
)

add_error(
    "Font not found",
    "DWG ishlatgan font Windows yoki AutoCAD tomonidan topilmadi.",
    [
        "STYLE buyrug'ini oching.",
        "Missing fontni aniqlang.",
        "Kerakli SHX yoki TTF fontni o'rnating.",
        "AutoCADni qayta ishga tushiring."
    ],
    "Fontni faqat ishonchli manbadan o'rnating."
)

add_error(
    "Text is not displayed",
    "Text layeri o'chirilgan, text height juda kichik yoki text rangi fon bilan bir xil bo'lishi mumkin.",
    [
        "Text layerini tekshiring.",
        "Text Height qiymatini tekshiring.",
        "Text rangini tekshiring.",
        "ZOOM EXTENTS va REGENALL bajaring."
    ],
    "Text uchun loyiha boshida standart Text Style yarating."
)

add_error(
    "Annotative object is not visible",
    "Annotative obyektning joriy annotation scale ro'yxatida kerakli scale mavjud emas.",
    [
        "Annotation Scale qiymatini tekshiring.",
        "Obyekt Properties orqali annotative ekanini tekshiring.",
        "ANNOALLVISIBLE sozlamasini tekshiring.",
        "Kerakli scale qo'shing."
    ],
    "Annotative obyektlar Layout viewportlarda ayniqsa muhim."
)


# =========================================================
# 🔗 7. XREF
# =========================================================

add_error(
    "XREF Unresolved",
    "AutoCAD XREF faylini ko'rsatilgan manzildan topa olmayapti.",
    [
        "XREF palitrasini oching.",
        "Unresolved XREFni tanlang.",
        "Select New Path orqali faylni ko'rsating.",
        "Reload qiling.",
        "Relative Path ishlatishni ko'rib chiqing."
    ],
    "XREF fayllarni loyiha papkasida tartibli saqlash eng qulay."
)

add_error(
    "XREF not found",
    "XREF fayli ko'chirilgan, o'chirilgan yoki path o'zgargan.",
    [
        "XREF Managerni oching.",
        "Pathni tekshiring.",
        "Select New Path orqali faylni toping.",
        "Reload qiling."
    ],
    "Loyiha papkasining ichki strukturasini o'zgartirmaslik yaxshi."
)

add_error(
    "XREF cannot be loaded",
    "XREF fayli mavjud bo'lsa ham AutoCAD uni yuklay olmayapti.",
    [
        "XREF faylni alohida ochib ko'ring.",
        "Fayl buzilgan bo'lsa RECOVER qiling.",
        "Pathni tekshiring.",
        "XREF versiyasi bilan AutoCAD mosligini tekshiring."
    ],
    "XREFning o'zi buzilgan bo'lsa asosiy DWGdagi sozlamalar yordam bermasligi mumkin."
)

add_error(
    "Circular reference detected",
    "XREFlar bir-biriga aylana shaklida reference qilmoqda.",
    [
        "XREF Managerni oching.",
        "Qaysi XREF qaysi faylni chaqirayotganini tekshiring.",
        "Circular chainni to'xtating.",
        "Keraksiz reference'ni olib tashlang."
    ],
    "XREF strukturasi sodda va bir yo'nalishli bo'lsa boshqarish oson."
)


# =========================================================
# 🧩 8. BLOCK
# =========================================================

add_error(
    "Cannot explode block",
    "Block Explodable emas yoki block turi oddiy block emas.",
    [
        "Blockni tanlang.",
        "Properties oynasini oching.",
        "Explodable xususiyatini tekshiring.",
        "BEDIT orqali blockni tekshiring.",
        "Dynamic Block bo'lsa uning xususiyatlarini tekshiring."
    ],
    "Blockni explode qilishdan oldin original block nusxasini saqlab qo'yish foydali."
)

add_error(
    "Block cannot be edited",
    "Block boshqa obyekt bilan bog'langan, XREF yoki tahrirlash rejimi cheklangan bo'lishi mumkin.",
    [
        "BEDIT buyrug'ini sinab ko'ring.",
        "Block nomini tekshiring.",
        "XREF ekanini tekshiring.",
        "Layer Lock holatini tekshiring."
    ],
    "XREF block kabi ko'rinishi mumkin, lekin uni asosiy DWGda oddiy BEDIT bilan tahrirlab bo'lmaydi."
)

add_error(
    "Block insertion scale is incorrect",
    "Drawing Units va block Units mos kelmayapti.",
    [
        "UNITS buyrug'ini tekshiring.",
        "INSUNITS qiymatini tekshiring.",
        "Block insertion scale ni tekshiring.",
        "Blockni to'g'ri Units bilan qayta yarating."
    ],
    "Millimeter, centimeter va meter birliklarini aralashtirmang."
)

add_error(
    "Block reference not found",
    "Block reference yoki block definition bilan bog'liq ma'lumot to'liq emas.",
    [
        "PURGE bajaring.",
        "AUDIT → Yes bajaring.",
        "BEDIT orqali blockni tekshiring.",
        "Backup DWGni tekshiring."
    ],
    "Blocklarni boshqa drawinglardan import qilganda nomlar va Unitsni tekshiring."
)


# =========================================================
# ✂️ 9. TRIM / EXTEND / OFFSET / JOIN
# =========================================================

add_error(
    "Cannot trim selected object",
    "Tanlangan obyekt kesuvchi boundary bilan geometrik jihatdan mos emas.",
    [
        "TRIM buyrug'ini qayta ishga tushiring.",
        "Kesuvchi obyektni tekshiring.",
        "Obyektlarning Z koordinatalarini tekshiring.",
        "Quick Mode va Standard Mode farqini tekshiring."
    ],
    "3D yoki turli Z koordinatalarida TRIM kutilmagan natija berishi mumkin."
)

add_error(
    "Cannot extend selected object",
    "Obyekt tanlangan boundarygacha geometrik jihatdan yetib bora olmayapti.",
    [
        "EXTEND buyrug'ini qayta ishga tushiring.",
        "Boundaryni to'g'ri tanlang.",
        "Z koordinatalarni tekshiring.",
        "Obyektlarni bir xil plane'ga keltiring."
    ],
    "PLAN yoki FLATTEN ayrim 2D chizmalarda yordam berishi mumkin."
)

add_error(
    "Cannot offset selected object",
    "Obyekt Offset uchun mos emas yoki distance qiymati noto'g'ri.",
    [
        "OFFSET buyrug'ini ishga tushiring.",
        "Distance kiriting.",
        "Obyektni tanlang.",
        "Offset yo'nalishini belgilang.",
        "Obyekt turini tekshiring."
    ],
    "Murakkab 3D obyektlarda OFFSET 2D geometriyadagi kabi ishlamasligi mumkin."
)

add_error(
    "Cannot join selected objects",
    "Obyektlar bir-biriga ulanmagan, turli Z koordinatasida yoki mos obyekt turi emas.",
    [
        "Endpointlarni tekshiring.",
        "Z koordinatalarni tekshiring.",
        "PEDIT → Join ishlatib ko'ring.",
        "JOIN yoki FILLET radius 0 usulini sinab ko'ring."
    ],
    "Kichik gaplar Join operatsiyasiga xalaqit berishi mumkin."
)

add_error(
    "Polyline cannot be closed",
    "Polyline oxirgi nuqtasi boshlang'ich nuqtaga ulanmagan yoki geometriya muammoli.",
    [
        "PEDIT buyrug'ini ishga tushiring.",
        "Polyline ni tanlang.",
        "Close opsiyasini tanlang.",
        "Kerak bo'lsa Join ishlating."
    ],
    "Maydon hisoblashdan oldin boundaryni yopiq holatga keltiring."
)


# =========================================================
# 📏 10. SCALE / ROTATE / MOVE / COPY
# =========================================================

add_error(
    "Invalid scale factor",
    "SCALE commandida noto'g'ri qiymat kiritilgan.",
    [
        "Scale factor musbat son ekanini tekshiring.",
        "Masalan 2 yoki 0.5 kabi qiymatdan foydalaning.",
        "Reference opsiyasidan foydalaning."
    ],
    "Aniq masshtablashda Reference juda qulay."
)

add_error(
    "Invalid rotation angle",
    "ROTATE commandida burchak noto'g'ri kiritilgan.",
    [
        "Burchakni son sifatida kiriting.",
        "Positive va negative angle yo'nalishini tekshiring.",
        "Reference opsiyasidan foydalaning."
    ],
    "Aniq aylantirishda Reference ishlatish xatoni kamaytiradi."
)

add_error(
    "Cannot move selected object",
    "Obyekt Lock qilingan layerda yoki tahrirlash cheklangan obyekt.",
    [
        "Layer Lock holatini tekshiring.",
        "XREF ekanini tekshiring.",
        "MOVE commandini qayta bajaring.",
        "Object Propertiesni tekshiring."
    ],
    "Layer Lock holatini tekshirish birinchi qadam bo'lsin."
)

add_error(
    "Cannot copy selected object",
    "Selection yoki obyekt turi bilan bog'liq muammo mavjud.",
    [
        "Obyektni qayta tanlang.",
        "Layer Lock holatini tekshiring.",
        "COPY commandini qayta bajaring.",
        "XREF yoki proxy obyekt ekanini tekshiring."
    ],
    "Oddiy obyektlarda COPY muammosi ko'pincha layer yoki selection bilan bog'liq."
)


# =========================================================
# 🖥️ 11. VIEW / ZOOM / SNAP / ORTHO
# =========================================================

add_error(
    "Object is not visible",
    "Obyekt boshqa layerda, Freeze/Off holatida yoki kamera ko'rish maydonidan tashqarida.",
    [
        "ZOOM EXTENTS bajaring.",
        "Layer holatini tekshiring.",
        "REGENALL bajaring.",
        "Object Propertiesni tekshiring."
    ],
    "ZOOM EXTENTSdan keyin layerlarni tekshirish juda foydali."
)

add_error(
    "Zoom extents shows objects very far away",
    "DWGda asosiy chizmadan juda uzoqda keraksiz obyekt mavjud.",
    [
        "ZOOM EXTENTS bajaring.",
        "Uzoqdagi obyektni toping.",
        "Keraksiz obyektni o'chiring.",
        "PURGE va AUDIT bajaring."
    ],
    "Bitta tasodifiy nuqta ham butun chizmaning juda kichik ko'rinishiga sabab bo'lishi mumkin."
)

add_error(
    "Object Snap is not working",
    "Object Snap o'chirilgan yoki kerakli snap turlari belgilanmagan.",
    [
        "F3 tugmasini bosing.",
        "DSETTINGS oynasini oching.",
        "Endpoint, Midpoint, Center va kerakli snaplarni belgilang.",
        "Object Snap Trackingni tekshiring."
    ],
    "F3 — Object Snap uchun asosiy shortcut."
)

add_error(
    "Ortho mode is not working",
    "Ortho rejimi o'chirilgan yoki boshqa tracking rejimi faol.",
    [
        "F8 tugmasini bosing.",
        "Status Bar'dagi Ortho indikatorini tekshiring.",
        "Command Line holatini tekshiring."
    ],
    "Ortho faqat gorizontal va vertikal yo'nalishni cheklaydi."
)

add_error(
    "Snap mode is not working",
    "Grid Snap o'chirilgan yoki Snap spacing noto'g'ri.",
    [
        "F9 tugmasini bosing.",
        "DSETTINGS oynasini oching.",
        "Snap spacing qiymatini tekshiring.",
        "Grid sozlamalarini tekshiring."
    ],
    "Grid Snap va Object Snap ikki xil funksiya."
)

add_error(
    "View is not regenerating correctly",
    "Ekrandagi drawing ko'rinishi AutoCAD graphics cache yoki regeneration bilan bog'liq muammoga ega.",
    [
        "REGEN buyrug'ini bajaring.",
        "REGENALL bajaring.",
        "GRAPHICSCONFIGni tekshiring.",
        "AutoCADni qayta ishga tushiring."
    ],
    "REGENALL ko'rinishdagi ko'plab vaqtinchalik muammolarni tuzatishi mumkin."
)


# =========================================================
# 📄 12. LAYOUT / VIEWPORT / PLOT / PDF
# =========================================================

add_error(
    "Layout is blank",
    "Viewport yo'q, layerlar Freeze qilingan yoki Page Setup noto'g'ri bo'lishi mumkin.",
    [
        "Layoutga o'ting.",
        "Viewport mavjudligini tekshiring.",
        "VP Freeze holatini tekshiring.",
        "Page Setupni tekshiring.",
        "REGENALL bajaring."
    ],
    "Layout va Model Space layer sozlamalarini alohida tekshiring."
)

add_error(
    "Viewport is locked",
    "Viewport Display Locked holatida.",
    [
        "Viewport chegarasini tanlang.",
        "Properties oynasini oching.",
        "Display Locked qiymatini No qiling.",
        "Masshtabni o'zgartiring."
    ],
    "Masshtabni o'rnatgandan keyin viewportni qayta Lock qilish tavsiya etiladi."
)

add_error(
    "Viewport scale is incorrect",
    "Viewport scale noto'g'ri tanlangan yoki Annotation Scale bilan mos emas.",
    [
        "Viewportni tanlang.",
        "Properties orqali Standard Scale ni tekshiring.",
        "Kerakli scale ni tanlang.",
        "Display Locked ni Yes qiling."
    ],
    "Arxitektura chizmalarida 1:50, 1:100 va 1:200 kabi scale'larni oldindan standartlashtiring."
)

add_error(
    "Plotter configuration cannot be found",
    "Tanlangan PC3 plotter konfiguratsiyasi topilmayapti.",
    [
        "PAGESETUP buyrug'ini oching.",
        "Printer/Plotter ro'yxatini tekshiring.",
        "DWG To PDF.pc3ni tanlab ko'ring.",
        "PC3 fayl yo'lini tekshiring."
    ],
    "PDF uchun DWG To PDF.pc3 odatda qulay variant."
)

add_error(
    "The plotter cannot be opened",
    "Printer yoki plotter konfiguratsiyasi noto'g'ri yoki Windows printer bilan muammo bor.",
    [
        "Printer holatini tekshiring.",
        "PC3 konfiguratsiyasini tekshiring.",
        "Boshqa plotter bilan sinab ko'ring.",
        "PDFga chiqarishni tekshiring."
    ],
    "Avval PDFga chiqarib, keyin printerga berish diagnostika uchun qulay."
)

add_error(
    "Nothing to plot",
    "Plot Area ichida chop etiladigan obyekt aniqlanmagan.",
    [
        "Plot Area sozlamasini tekshiring.",
        "Display, Extents, Window yoki Layout variantlarini tekshiring.",
        "Preview qiling.",
        "Layer Plot belgilarini tekshiring."
    ],
    "Preview chop etishdan oldin eng muhim tekshiruv."
)

add_error(
    "PDF output is missing lines",
    "Layer Plot o'chirilgan, lineweight yoki plot style noto'g'ri bo'lishi mumkin.",
    [
        "Layer Propertiesni oching.",
        "Plot ustunini tekshiring.",
        "CTB/STB plot style faylini tekshiring.",
        "Lineweightlarni tekshiring.",
        "Preview qiling."
    ],
    "PDFga chiqarishdan oldin Previewni tekshirish odat bo'lsin."
)

add_error(
    "PDF output is blurry",
    "Raster obyektlar yoki PDF plot sifati/DPI sozlamalari past bo'lishi mumkin.",
    [
        "DWG To PDF.pc3ni tanlang.",
        "PDF quality sozlamalarini tekshiring.",
        "Raster image resolutionni tekshiring.",
        "Preview qiling."
    ],
    "Vektor chiziqlar odatda raster rasmlarga qaraganda aniqroq chiqadi."
)


# =========================================================
# 🧹 13. PURGE / AUDIT / OVERKILL / PERFORMANCE
# =========================================================

add_error(
    "Drawing is extremely slow",
    "DWG juda katta, ortiqcha layer, block, Hatch, XREF yoki proxy obyektlar ko'p.",
    [
        "PURGE bajaring.",
        "AUDIT → Yes bajaring.",
        "OVERKILL ishlating.",
        "Keraksiz XREFlarni tekshiring.",
        "Keraksiz layerlarni Freeze qiling.",
        "GRAPHICSCONFIGni tekshiring."
    ],
    "Katta loyihalarni muntazam optimallashtirib boring."
)

add_error(
    "AutoCAD freezes or hangs",
    "AutoCAD katta yoki murakkab drawing, Hatch, XREF, plugin yoki grafik resurslar sabab javob bermay qolishi mumkin.",
    [
        "Bir necha daqiqa kutib, command tugashini tekshiring.",
        "ESC tugmasini sinab ko'ring.",
        "PURGE va AUDIT bajaring.",
        "XREF va Hatchlarni tekshiring.",
        "GRAPHICSCONFIGni tekshiring."
    ],
    "AutoCAD javob bermayotgan paytda darhol Task Manager orqali yopishdan oldin recovery imkoniyatini hisobga oling."
)

add_error(
    "Purge cannot remove some objects",
    "Ba'zi obyektlar drawingda ishlatilayotgan, nested yoki maxsus reference sabab PURGE qilinmayapti.",
    [
        "PURGE oynasidagi View Items That Cannot Be Purged variantini tekshiring.",
        "Object qayerda ishlatilayotganini aniqlang.",
        "Keraksiz block yoki layer reference'larini olib tashlang.",
        "Keyin PURGEni qayta bajaring."
    ],
    "PURGE hamma narsani majburan o'chirmaydi."
)

add_error(
    "AUDIT found errors",
    "Drawing database ichida xatolar topilgan.",
    [
        "AUDIT buyrug'ini ishga tushiring.",
        "Yes orqali xatolarni tuzattiring.",
        "Audit tugagach faylni SAVE AS qiling.",
        "Zarur bo'lsa RECOVER bilan qayta tekshiring."
    ],
    "Audit natijasini Command Line'dan o'qib chiqing."
)

add_error(
    "OVERKILL could not process objects",
    "Tanlangan obyektlar murakkab, proxy yoki mos kelmaydigan turda bo'lishi mumkin.",
    [
        "Oddiy LINE/POLYLINE obyektlarida sinab ko'ring.",
        "Proxy obyektlarni tekshiring.",
        "Selectionni kichik qismlarga bo'lib ishlating.",
        "Keyin OVERKILLni qayta bajaring."
    ],
    "Juda katta selectionni birdaniga OVERKILL qilish AutoCADni sekinlashtirishi mumkin."
)


# =========================================================
# 💾 14. SAVE / FILE / PERMISSION
# =========================================================

add_error(
    "Unable to save drawing",
    "Faylga yozish huquqi, disk joyi, network yoki DWG buzilishi sabab save ishlamayapti.",
    [
        "Diskda bo'sh joy borligini tekshiring.",
        "Faylni boshqa lokal papkaga SAVE AS qiling.",
        "Read-only holatini tekshiring.",
        "Network ulanishini tekshiring.",
        "AUDIT bajaring."
    ],
    "Muhim fayllarni bir nechta versiyada saqlang."
)

add_error(
    "Access is denied",
    "Windows joriy fayl yoki papkaga yozish huquqini bermayapti.",
    [
        "Fayl Properties → Security bo'limini tekshiring.",
        "Faylni Desktop kabi yozish mumkin bo'lgan papkaga ko'chirib ko'ring.",
        "Read-only holatini tekshiring.",
        "Kerak bo'lsa AutoCADni administrator sifatida ishga tushiring."
    ],
    "Administrator rejimi doimiy yechim emas; avval fayl permissionlarini tekshiring."
)

add_error(
    "The disk is full",
    "DWGni saqlash uchun diskda yetarli bo'sh joy yo'q.",
    [
        "Diskdagi bo'sh joyni tekshiring.",
        "Keraksiz vaqtinchalik fayllarni tozalang.",
        "DWGni boshqa diskka saqlab ko'ring.",
        "Windows Storage sozlamalarini tekshiring."
    ],
    "Loyiha diskida doimo yetarli bo'sh joy qoldiring."
)


# =========================================================
# 🧰 15. INSTALLATION ERRORS
# =========================================================

add_error(
    "Installation Failed",
    "AutoCAD yoki Autodesk komponenti o'rnatilishi muvaffaqiyatsiz tugagan.",
    [
        "Windowsni qayta ishga tushiring.",
        "Installer'ni administrator sifatida ishga tushiring.",
        "Oldingi Autodesk installationlarini tekshiring.",
        "Windows Update'ni tekshiring.",
        "Diskda yetarli bo'sh joy borligini tekshiring.",
        "Autodesk Installation log fayllarini tekshiring.",
        "Muammo davom etsa Autodesk uninstall/reinstall vositasidan foydalaning."
    ],
    "O'rnatishdan oldin boshqa Autodesk installer oynalarini yoping."
)

add_error(
    "Error 1603: A fatal error occurred during installation",
    "Windows Installer installation jarayonida jiddiy xato yuz bergan. Permission, eski Autodesk komponentlari yoki installer cache sabab bo'lishi mumkin.",
    [
        "Windowsni restart qiling.",
        "Barcha Autodesk dasturlarini yoping.",
        "Installer'ni Run as administrator bilan ishga tushiring.",
        "Oldingi Autodesk komponentlarini tekshiring.",
        "Temp papkasini tozalang.",
        "Windows Installer xizmatini tekshiring.",
        "Installation log orqali qaysi komponent xato berganini aniqlang."
    ],
    "1603 juda umumiy installer xatosi; log fayli aniq sababni topishda muhim."
)

add_error(
    "Error 1618: Another installation is already in progress",
    "Windows Installer ayni paytda boshqa installation jarayonini bajaryapti.",
    [
        "Boshqa installer oynalarini yoping.",
        "Windows Update tugashini kuting.",
        "Task Manager orqali boshqa installation jarayonlarini tekshiring.",
        "Kompyuterni restart qiling.",
        "Keyin AutoCAD installationini qayta ishga tushiring."
    ],
    "Bir vaqtning o'zida ikkita installer ishlatmang."
)

add_error(
    "Error 1601: Windows Installer service could not be accessed",
    "Windows Installer service ishlamayapti yoki unga murojaat qilishda muammo bor.",
    [
        "Win + R bosing.",
        "services.msc yozing.",
        "Windows Installer xizmatini toping.",
        "Service holatini tekshiring.",
        "Windowsni restart qiling.",
        "Installationni qayta urinib ko'ring."
    ],
    "Windows Installer xizmatini tasodifiy o'chirib qo'ymang."
)

add_error(
    "The installer has encountered an unexpected error",
    "Installer kutilmagan holatga duch kelgan.",
    [
        "Windowsni restart qiling.",
        "Installerni administrator sifatida ishga tushiring.",
        "Temp papkasini tozalang.",
        "Windows Update'ni tekshiring.",
        "Autodesk installation loglarini tekshiring."
    ],
    "Aniq sabab uchun installation logini tekshirish kerak."
)

add_error(
    "Failed to install",
    "Autodesk mahsuloti yoki komponenti o'rnatilmagan.",
    [
        "Installerni qayta ishga tushiring.",
        "Internet ulanishini tekshiring.",
        "Disk joyini tekshiring.",
        "Administrator huquqlarini tekshiring.",
        "Eski Autodesk komponentlarini tekshiring.",
        "Installation logini ko'ring."
    ],
    "O'rnatishdan oldin antivirus yoki firewall bloklayotganini ham tekshirish mumkin."
)

add_error(
    "Unable to install Autodesk Desktop Connector",
    "Autodesk Desktop Connector o'rnatilishida eski versiya, Windows Installer yoki Autodesk komponentlari muammosi bo'lishi mumkin.",
    [
        "Eski Desktop Connector versiyasini tekshiring.",
        "Windowsni restart qiling.",
        "Installerni administrator sifatida ishga tushiring.",
        "Autodesk Desktop Connectorning mos versiyasidan foydalaning.",
        "Installation logini tekshiring."
    ],
    "Desktop Connector AutoCADning o'zidan alohida komponent ekanini hisobga oling."
)

add_error(
    "A newer version of this product is already installed",
    "Kompyuterda ushbu mahsulotning yangiroq versiyasi allaqachon mavjud.",
    [
        "Windows Settings → Apps bo'limini oching.",
        "Autodesk mahsulotini toping.",
        "O'rnatilgan versiyani tekshiring.",
        "Kerak bo'lsa mavjud versiyani Repair qiling.",
        "Eski installer bilan yangiroq versiyani ustidan o'rnatishga urinmang."
    ],
    "Avval o'rnatilgan versiya raqamini aniqlang."
)

add_error(
    "This product is already installed",
    "AutoCAD yoki uning komponenti allaqachon o'rnatilgan.",
    [
        "Windows Settings → Apps bo'limidan mahsulotni toping.",
        "Repair yoki Modify mavjudligini tekshiring.",
        "Alohida installer o'rniga Autodesk Access orqali update qiling."
    ],
    "Bir xil mahsulotni qayta-qayta o'rnatishdan oldin Repair variantini tekshiring."
)

add_error(
    "The installation log file could not be opened",
    "Installer log fayliga kirish yoki uni yaratish bilan bog'liq permission/path muammosi mavjud.",
    [
        "Temp papkasiga kirishni tekshiring.",
        "Diskda bo'sh joyni tekshiring.",
        "Installerni administrator sifatida ishga tushiring.",
        "Windows TEMP va TMP environment variablelarini tekshiring.",
        "Installation log papkasini tekshiring."
    ],
    "Log fayllari installation muammosining aniq sababini topishda juda muhim."
)

add_error(
    "System Error: 5. Access is denied",
    "Windows installer yoki dastur kerakli fayl yoki papkaga kirish huquqiga ega emas.",
    [
        "Installerni Run as administrator bilan ishga tushiring.",
        "Installation papkasining Security permissionlarini tekshiring.",
        "Antivirus blokini tekshiring.",
        "Temp papkasiga yozish mumkinligini tekshiring."
    ],
    "Administrator huquqi bilan ishlatish permission muammosini aniqlash uchun test sifatida qo'llanadi."
)

add_error(
    "Error 1303: The installer has insufficient privileges",
    "Installer kerakli papkaga o'zgartirish kiritish uchun yetarli huquqqa ega emas.",
    [
        "Installerni administrator sifatida ishga tushiring.",
        "Installation papkasining Security permissionlarini tekshiring.",
        "Oldingi installation jarayonlarini yoping.",
        "Windowsni restart qiling.",
        "Keyin installationni qayta urinib ko'ring."
    ],
    "Program Files kabi himoyalangan papkalarda permission muammosi tez-tez uchraydi."
)

add_error(
    "Error 1719: Windows Installer service could not be accessed",
    "Windows Installer service mavjud emas, ishlamayapti yoki unga murojaat qilish imkoni yo'q.",
    [
        "Win + R → services.msc ni oching.",
        "Windows Installer xizmatini toping.",
        "Service holatini tekshiring.",
        "Windowsni restart qiling.",
        "Windows Update holatini tekshiring."
    ],
    "Windows Installer tizimdagi boshqa dasturlar installationi uchun ham kerak."
)

add_error(
    "The installation source for this product is not available",
    "Installer kerakli source fayllarni topa olmayapti.",
    [
        "Installer fayllari to'liq yuklanganini tekshiring.",
        "Network location o'rniga lokal diskdan foydalaning.",
        "Installer cache holatini tekshiring.",
        "Autodesk installerini qayta yuklab ko'ring."
    ],
    "Installer papkasini boshqa joyga ko'chirganda source path buzilishi mumkin."
)

add_error(
    "The feature you are trying to use is on a network resource that is unavailable",
    "Installation uchun kerakli fayllar mavjud bo'lmagan network manzilda joylashgan.",
    [
        "Network ulanishini tekshiring.",
        "Fayl serverga kirishni tekshiring.",
        "Installer source'ini lokal diskka ko'chiring.",
        "Installationni qayta boshlang."
    ],
    "Lokal installer ko'pincha network source muammolarini kamaytiradi."
)

add_error(
    "Another version of this product is already installed",
    "Kompyuterda shu mahsulotning boshqa versiyasi mavjud.",
    [
        "Installed Apps ro'yxatini tekshiring.",
        "Mavjud Autodesk versiyasini aniqlang.",
        "Kerak bo'lsa uninstall yoki Repair qiling.",
        "Mos installer versiyasidan foydalaning."
    ],
    "Turli AutoCAD versiyalarini bir kompyuterda ishlatishda installation talablarini tekshiring."
)

add_error(
    "The installation was interrupted",
    "Installation foydalanuvchi, Windows yoki boshqa jarayon tomonidan to'xtatilgan.",
    [
        "Kompyuterni restart qiling.",
        "Boshqa installerlarni yoping.",
        "Autodesk installerini qayta ishga tushiring.",
        "Internet va disk joyini tekshiring."
    ],
    "Installation vaqtida kompyuterni o'chirmang."
)

add_error(
    "Installation cannot continue",
    "Installer kerakli shartlardan biri bajarilmagani sabab davom eta olmayapti.",
    [
        "Windows versiyasi talabga mosligini tekshiring.",
        "Disk bo'sh joyini tekshiring.",
        "Administrator huquqlarini tekshiring.",
        "Windows Update'ni tekshiring.",
        "Oldingi Autodesk komponentlarini tekshiring."
    ],
    "AutoCADning aynan o'rnatayotgan versiyasi uchun system requirementsni tekshiring."
)

add_error(
    "The operating system is not supported",
    "O'rnatilayotgan AutoCAD versiyasi joriy Windows versiyasini qo'llab-quvvatlamasligi mumkin.",
    [
        "AutoCAD versiyasining system requirementsini tekshiring.",
        "Windows Update'ni tekshiring.",
        "Mos AutoCAD installeridan foydalaning."
    ],
    "Eski AutoCAD versiyalarini yangi Windowsda o'rnatishda compatibility muammolari bo'lishi mumkin."
)

add_error(
    "Insufficient disk space",
    "AutoCAD installationi uchun diskda yetarli bo'sh joy yo'q.",
    [
        "Diskdagi bo'sh joyni tekshiring.",
        "Keraksiz fayllarni tozalang.",
        "Windows Storage Cleanup ishlating.",
        "Kerak bo'lsa boshqa diskni tanlang."
    ],
    "Installationdan oldin installer talab qiladigan bo'sh joyni tekshiring."
)

add_error(
    "Internet connection required",
    "Installer kerakli komponentlarni yuklash uchun internetga ulanishni talab qilmoqda.",
    [
        "Internet ulanishini tekshiring.",
        "VPN/proxy sozlamalarini tekshiring.",
        "Firewall bloklamayotganini tekshiring.",
        "Installerni qayta ishga tushiring."
    ],
    "Barqaror internet Autodesk installation jarayonini ancha yengillashtiradi."
)

add_error(
    "Download failed",
    "Installer kerakli Autodesk komponentini internetdan yuklay olmadi.",
    [
        "Internetni tekshiring.",
        "VPNni vaqtincha tekshiring.",
        "Firewall/antivirus blokini tekshiring.",
        "Installerni qayta ishga tushiring.",
        "Kerak bo'lsa installer cache'ini yangilang."
    ],
    "Wi-Fi beqaror bo'lsa boshqa internet ulanishini sinab ko'ring."
)

add_error(
    "Unable to download installation files",
    "Installation fayllari Autodesk serverlaridan yuklanmagan.",
    [
        "Internet ulanishini tekshiring.",
        "Autodesk serverlariga kirish bloklanmaganini tekshiring.",
        "Installerni administrator sifatida ishga tushiring.",
        "Autodesk Access orqali installationni urinib ko'ring."
    ],
    "Firewall yoki corporate proxy bunday xatoga sabab bo'lishi mumkin."
)


# =========================================================
# 🔐 16. LICENSING / SIGN-IN
# =========================================================

add_error(
    "License Manager is not functioning",
    "Autodesk Licensing Service ishlamayapti yoki buzilgan.",
    [
        "Autodesk Licensing Service holatini tekshiring.",
        "Windows Services oynasini oching.",
        "Autodesk Access orqali licensing komponentlarini yangilang.",
        "AutoCADni qayta ishga tushiring."
    ],
    "License muammosida Autodesk Licensing Service muhim komponent hisoblanadi."
)

add_error(
    "Your license is not valid",
    "AutoCAD litsenziyani tasdiqlay olmayapti.",
    [
        "Autodesk Account'dagi license holatini tekshiring.",
        "Internet ulanishini tekshiring.",
        "Autodesk Access orqali sign-in qiling.",
        "License turini tekshiring."
    ],
    "Litsenziya bilan bog'liq muammolarda faqat rasmiy Autodesk Accountdan foydalaning."
)

add_error(
    "Sign-in failed",
    "Autodesk Accountga kirish jarayonida muammo yuzaga kelgan.",
    [
        "Internetni tekshiring.",
        "Autodesk Account ma'lumotlarini tekshiring.",
        "Brauzer orqali Autodesk Accountga kirib ko'ring.",
        "AutoCADdan sign out/sign in qilib ko'ring."
    ],
    "Account muammosi bo'lsa parolni taxmin qilish o'rniga rasmiy recoverydan foydalaning."
)

add_error(
    "License checkout failed",
    "AutoCAD foydalanish uchun license server yoki accountdan license ola olmadi.",
    [
        "Internet ulanishini tekshiring.",
        "Autodesk Account holatini tekshiring.",
        "Licensing Service ishlayotganini tekshiring.",
        "AutoCADni qayta ishga tushiring."
    ],
    "Tarmoq orqali license ishlatilsa firewall va proxy sozlamalari muhim."
)


# =========================================================
# 🧱 17. 3D / MODELING
# =========================================================

add_error(
    "Unable to create 3D solid",
    "Geometriya yopiq emas yoki 3D solid yaratish uchun mos emas.",
    [
        "Boundaryni tekshiring.",
        "PEDIT orqali polyline'ni yopiq qiling.",
        "PRESSPULL yoki EXTRUDEni qayta sinab ko'ring.",
        "Z koordinatalarni tekshiring."
    ],
    "3D solid yaratishda yopiq va toza geometriya ishlating."
)

add_error(
    "3D operation failed",
    "3D Boolean yoki modeling operatsiyasi geometriya sabab muvaffaqiyatsiz tugagan.",
    [
        "INTERFERE yoki CHECK orqali geometriyani tekshiring.",
        "Solidlarni alohida tekshiring.",
        "Keraksiz murakkablikni kamaytiring.",
        "UNION/SUBTRACT/INTERSECTni qayta sinab ko'ring."
    ],
    "Murakkab 3D modelni kichik qismlarga bo'lib tekshirish osonroq."
)

add_error(
    "Boolean operation failed",
    "Solidlar bir-biriga mos kelmayapti yoki geometriyada muammo bor.",
    [
        "Solidlarning haqiqiy 3D solid ekanini tekshiring.",
        "INTERFERE orqali kesishishni tekshiring.",
        "Geometriyani soddalashtiring.",
        "UNION yoki SUBTRACTni qayta bajaring."
    ],
    "Boolean operatsiyadan oldin solidlar haqiqatan kesishayotganini tekshiring."
)


# =========================================================
# 📐 18. UNITS / COORDINATES
# =========================================================

add_error(
    "Drawing units are incorrect",
    "DWG birliklari noto'g'ri o'rnatilgan.",
    [
        "UNITS buyrug'ini oching.",
        "Insertion Scale qiymatini tekshiring.",
        "Millimeter, centimeter yoki meter tanlovini tekshiring.",
        "Geometriya o'lchamini DIST bilan tekshiring."
    ],
    "Arxitektura loyihalarida birliklarni loyiha boshida aniqlab oling."
)

add_error(
    "Objects inserted at the wrong scale",
    "Source va destination drawing Units bir-biriga mos emas.",
    [
        "UNITSni ikkala DWGda ham tekshiring.",
        "INSUNITS qiymatini tekshiring.",
        "INSERT scale qiymatini tekshiring.",
        "Blockni to'g'ri birlik bilan qayta import qiling."
    ],
    "DWGlar orasida block almashishda Units eng muhim sozlamalardan biridir."
)

add_error(
    "Coordinates are incorrect",
    "Obyekt noto'g'ri koordinatada joylashgan yoki UCS/WCS sozlamasi o'zgargan.",
    [
        "UCS buyrug'ini tekshiring.",
        "PLAN → World orqali WCS ko'rinishini tekshiring.",
        "Properties orqali koordinatalarni tekshiring.",
        "MOVE yoki ALIGN bilan joylashuvni tuzating."
    ],
    "Aniq loyiha uchun WCS va UCS holatini tushunish muhim."
)


# =========================================================
# 🛠️ 19. AUTODESK / PLUGIN
# =========================================================

add_error(
    "Plugin failed to load",
    "Plugin AutoCAD tomonidan yuklanmadi yoki versiya bilan mos emas.",
    [
        "Plugin versiyasini tekshiring.",
        "APPLOAD orqali qayta yuklang.",
        "Pluginning AutoCAD versiyasi bilan mosligini tekshiring.",
        "Kerak bo'lsa pluginni qayta o'rnating."
    ],
    "Pluginni faqat ishonchli manbadan o'rnating."
)

add_error(
    "Application failed to load",
    "AutoCAD application yoki plugin kerakli komponentni yuklay olmadi.",
    [
        "Plugin fayllarini tekshiring.",
        "APPLOAD orqali yuklashni sinab ko'ring.",
        "AutoCADni restart qiling.",
        "Plugin versiyasini yangilang."
    ],
    "Noma'lum DLL/ARX fayllarini tasodifiy saytlardan yuklamang."
)

add_error(
    "Object Enabler is required",
    "Drawingdagi custom/proxy obyektlarni to'liq ko'rish uchun tegishli Object Enabler kerak.",
    [
        "Obyekt qaysi Autodesk mahsulotiga tegishli ekanini aniqlang.",
        "Tegishli Object Enablerni rasmiy Autodesk manbasidan o'rnating.",
        "DWGni qayta oching."
    ],
    "Object Enablerni faqat mos AutoCAD versiyasi uchun tanlang."
)


# =========================================================
# 📋 20. ADDITIONAL COMMON ERRORS
# =========================================================

add_error(
    "Invalid file name",
    "Fayl nomida Windows qabul qilmaydigan belgilar yoki noto'g'ri path mavjud.",
    [
        "Fayl nomini soddalashtiring.",
        "Maxsus belgilarni olib tashlang.",
        "Faylni qisqa lokal pathga ko'chiring.",
        "Save As orqali yangi nom bering."
    ],
    "Loyiha papkalari nomlarini sodda va tartibli saqlash foydali."
)

add_error(
    "Path not found",
    "AutoCAD ko'rsatilgan fayl yoki papka manzilini topa olmayapti.",
    [
        "Pathni tekshiring.",
        "Fayl mavjudligini Windows Explorer orqali tekshiring.",
        "XREF yoki support path bo'lsa qayta ko'rsating.",
        "Relative Path ishlatishni ko'rib chiqing."
    ],
    "Network disk har doim mavjud bo'lishiga ishonch hosil qiling."
)

add_error(
    "File not found",
    "Kerakli fayl o'chirilgan, ko'chirilgan yoki boshqa joyga saqlangan.",
    [
        "Windows Search orqali faylni qidiring.",
        "XREF Manager pathini tekshiring.",
        "Backup papkani tekshiring.",
        "Select New Path orqali yangi manzilni ko'rsating."
    ],
    "Loyiha papkasidagi fayllarni nomini o'zgartirishdan oldin XREF bog'lanishlarini hisobga oling."
)

add_error(
    "Invalid drawing version",
    "DWG boshqa yoki qo'llab-quvvatlanmaydigan format/versionda saqlangan bo'lishi mumkin.",
    [
        "DWGni mos AutoCAD versiyasida oching.",
        "DWG TrueView yoki mos Autodesk vositasi orqali konvertatsiya qiling.",
        "Faylni kerakli DWG formatida SAVE AS qiling."
    ],
    "Eski AutoCAD versiyalariga topshiriladigan fayl formatini oldindan aniqlang."
)

add_error(
    "Cannot find specified template",
    "AutoCAD DWT template faylini ko'rsatilgan joydan topa olmayapti.",
    [
        "OPTIONS → Files orqali Template pathni tekshiring.",
        "DWT fayl mavjudligini tekshiring.",
        "Default template sozlamalarini tekshiring.",
        "Kerakli template pathni qayta qo'shing."
    ],
    "O'z template'laringizni alohida loyiha papkasida saqlang."
)

add_error(
    "Template file cannot be opened",
    "DWT template buzilgan yoki unga kirish imkoni yo'q.",
    [
        "DWT faylni Windows Explorer orqali tekshiring.",
        "Boshqa template bilan sinab ko'ring.",
        "Template'ni qayta yarating.",
        "Permissionlarni tekshiring."
    ],
    "Standart template uchun backup nusxa saqlang."
)

add_error(
    "Cannot load customization file",
    "CUI/CUIX customization fayli topilmagan yoki buzilgan.",
    [
        "CUI buyrug'ini oching.",
        "Customization fayl pathini tekshiring.",
        "CUIX faylni qayta yuklang.",
        "AutoCAD settingsni reset qilib ko'ring."
    ],
    "CUIX faylingizni backup qilib qo'yish foydali."
)

add_error(
    "Workspace not found",
    "Tanlangan Workspace mavjud emas yoki CUIX sozlamasida yo'q.",
    [
        "WORKSPACE commandini tekshiring.",
        "Boshqa workspace tanlang.",
        "CUI orqali workspace mavjudligini tekshiring.",
        "AutoCAD settingsni reset qilib ko'ring."
    ],
    "O'zingiz yaratgan workspace'ni backup qilib qo'ying."
)

add_error(
    "Cannot load partial customization file",
    "Partial CUIX fayli topilmagan yoki noto'g'ri pathga ega.",
    [
        "CUI buyrug'ini oching.",
        "Partial Customization Files bo'limini tekshiring.",
        "Fayl pathini tuzating.",
        "Keraksiz partial CUIXni olib tashlang."
    ],
    "Pluginlar o'z CUIX fayllarini o'rnatishi mumkin."
)

add_error(
    "Menu file cannot be loaded",
    "Menu yoki CUI fayli topilmagan yoki o'qilmayapti.",
    [
        "CUI buyrug'ini oching.",
        "Menu fayl pathini tekshiring.",
        "Fayl mavjudligini tekshiring.",
        "Kerak bo'lsa customizationni qayta yuklang."
    ],
    "Custom interface fayllarining backupini saqlang."
)

add_error(
    "Cannot open palette",
    "Tool Palette yoki boshqa AutoCAD palette oynasi yuklanmagan.",
    [
        "TOOLPALETTES commandini ishga tushiring.",
        "Palettes sozlamalarini tekshiring.",
        "Workspace'ni qayta yuklang.",
        "AutoCAD settingsni reset qilib ko'ring."
    ],
    "Tool Palette fayllari joylashuvini OPTIONS → Files orqali tekshirish mumkin."
)

add_error(
    "Command is not available in the current workspace",
    "Joriy workspace yoki AutoCAD konfiguratsiyasi kerakli command/panelni ko'rsatmayapti.",
    [
        "Workspace'ni almashtirib ko'ring.",
        "CUI orqali command mavjudligini tekshiring.",
        "Command Line orqali commandni qo'lda kiriting."
    ],
    "Ribbon yoki toolbar ko'rinmasa ham command Line orqali ko'plab funksiyalarni ishga tushirish mumkin."
)

add_error(
    "Cannot create temporary file",
    "AutoCAD TEMP papkasiga vaqtinchalik fayl yarata olmayapti.",
    [
        "Windows TEMP papkasini tekshiring.",
        "Diskda bo'sh joyni tekshiring.",
        "TEMP environment variablelarini tekshiring.",
        "Windows permissionlarini tekshiring."
    ],
    "TEMP papkasiga yozish huquqi AutoCAD uchun muhim."
)

add_error(
    "Cannot write to temporary directory",
    "AutoCAD Windows vaqtinchalik papkasiga yozolmayapti.",
    [
        "TEMP papkasiga kirishni tekshiring.",
        "Disk bo'sh joyini tekshiring.",
        "Antivirus blokini tekshiring.",
        "Windowsni restart qiling."
    ],
    "Windows TEMP yo'li noto'g'ri bo'lsa ko'plab dasturlarda muammo chiqishi mumkin."
)

add_error(
    "Graphics device initialization failed",
    "AutoCAD grafik qurilmani to'g'ri ishga tushira olmayapti.",
    [
        "GRAPHICSCONFIGni oching.",
        "Hardware Accelerationni vaqtincha o'chiring.",
        "Video driverni yangilang.",
        "AutoCADni qayta ishga tushiring."
    ],
    "GPU driver va AutoCAD graphics settingsni birgalikda tekshirish kerak."
)

add_error(
    "Hardware acceleration is unavailable",
    "GPU yoki driver AutoCAD Hardware Acceleration talablarini bajarmayapti.",
    [
        "Video driverni yangilang.",
        "GRAPHICSCONFIGni tekshiring.",
        "GPU compatibilityni tekshiring.",
        "Kerak bo'lsa Hardware Accelerationni o'chiring."
    ],
    "Noutbuklarda AutoCAD qaysi GPUdan foydalanayotganini tekshirish foydali."
)

add_error(
    "Regeneration failed",
    "Drawing regeneration jarayonida geometriya yoki graphics bilan bog'liq muammo yuzaga kelgan.",
    [
        "REGENALL bajaring.",
        "AUDIT → Yes bajaring.",
        "GRAPHICSCONFIGni tekshiring.",
        "Muammoli obyektlarni aniqlang."
    ],
    "Regeneration muammosi takrorlansa DWG integrityni tekshiring."
)

add_error(
    "Cannot load font",
    "AutoCAD kerakli font faylini yuklay olmayapti.",
    [
        "Font faylini tekshiring.",
        "SHX/TTF faylini to'g'ri joylashtiring.",
        "STYLE orqali fontni tekshiring.",
        "AutoCADni qayta ishga tushiring."
    ],
    "Fontlarni loyiha bilan birga saqlash yaxshi amaliyot."
)

add_error(
    "Missing SHX file",
    "DWGda ishlatilgan SHX font yoki shape fayli kompyuterda topilmadi.",
    [
        "Missing SHX nomini aniqlang.",
        "Kerakli SHX faylni o'rnating.",
        "STYLE orqali text style'ni tekshiring.",
        "DWGni qayta oching."
    ],
    "SHX fayllarni faqat ishonchli manbadan oling."
)

add_error(
    "Missing referenced file",
    "Drawing boshqa faylga reference qilgan, lekin u topilmayapti.",
    [
        "XREF Managerni oching.",
        "Missing faylni aniqlang.",
        "Select New Path orqali yangi manzilni ko'rsating.",
        "Reload qiling."
    ],
    "Loyiha papkasini ko'chirganda reference pathlarni saqlang."
)

add_error(
    "Cannot bind XREF",
    "XREF bind qilishda fayl, layer yoki reference bilan bog'liq muammo yuzaga kelgan.",
    [
        "XREFni alohida ochib tekshiring.",
        "AUDIT bajaring.",
        "PURGE bajaring.",
        "XREFni qayta Reload qiling.",
        "Keyin Bindni qayta sinab ko'ring."
    ],
    "Bind qilishdan oldin original DWG backupini saqlang."
)

add_error(
    "Cannot detach XREF",
    "XREF boshqa reference bilan bog'langan yoki drawing holati muammoli.",
    [
        "XREF Managerdan reference'ni tekshiring.",
        "Nested XREFlarni aniqlang.",
        "AUDIT bajaring.",
        "Kerak bo'lsa XREF source faylini tekshiring."
    ],
    "Nested XREF strukturasini Bind/Detach qilishdan oldin tushunib oling."
)

add_error(
    "Cannot reload XREF",
    "XREF fayli mavjud bo'lsa ham AutoCAD uni qayta yuklay olmayapti.",
    [
        "XREF pathini tekshiring.",
        "Source DWGni alohida ochib ko'ring.",
        "Source DWGni RECOVER bilan tekshiring.",
        "Pathni qayta belgilang."
    ],
    "Source XREF fayli buzilgan bo'lsa Reload yordam bermaydi."
)

add_error(
    "Cannot save changes to XREF",
    "XREF source fayliga yozish huquqi yoki file lock muammosi mavjud.",
    [
        "Source DWGni alohida ochib ko'ring.",
        "Read-only holatini tekshiring.",
        "Network permissionlarni tekshiring.",
        "Save As orqali lokal nusxa yarating."
    ],
    "XREF source fayllari uchun alohida backup tizimi bo'lsin."
)

add_error(
    "Cannot edit external reference",
    "Tashqi reference yoki XREFni joriy DWG ichida tahrirlash cheklangan.",
    [
        "REFEDIT yoki XOPEN imkoniyatlarini tekshiring.",
        "XREF source faylini alohida oching.",
        "Source DWGni tahrirlang va saqlang.",
        "Asosiy DWGda Reload qiling."
    ],
    "XREF source faylini tahrirlash ko'pincha eng xavfsiz usul."
)

add_error(
    "Corrupt proxy object detected",
    "DWGda proxy obyekt yoki uning ma'lumotlari bilan bog'liq muammo mavjud.",
    [
        "PROXYSHOW sozlamasini tekshiring.",
        "Object Enabler talab qilinishini tekshiring.",
        "AUDIT bajaring.",
        "Original applicationda DWGni tekshiring."
    ],
    "Proxy obyektlarni o'chirishdan oldin loyiha uchun ahamiyatini aniqlang."
)

add_error(
    "Cannot convert object",
    "Obyekt boshqa turga o'tkazilayotganda geometriya yoki object type bilan bog'liq muammo yuzaga kelgan.",
    [
        "Obyekt turini Properties orqali tekshiring.",
        "EXPLODE yoki CONVERTPSTYLES kabi kerakli commandni to'g'ri tanlang.",
        "Geometriyani soddalashtiring.",
        "AUDIT bajaring."
    ],
    "Har bir object type uchun mos commanddan foydalaning."
)

add_error(
    "Invalid selection",
    "Tanlangan obyekt joriy command talablariga mos emas.",
    [
        "Command Line'dagi selection talablarini o'qing.",
        "Faqat mos obyektlarni tanlang.",
        "ESC bilan commandni qayta boshlang."
    ],
    "Command qaysi object turini qabul qilishini Command Line ko'rsatadi."
)

add_error(
    "Nothing selected",
    "Command uchun hech qanday obyekt tanlanmagan.",
    [
        "Commandni qayta ishga tushiring.",
        "Kerakli obyektni tanlang.",
        "Enter bosing."
    ],
    "Selection bosqichida Command Line xabarini o'qing."
)

add_error(
    "No objects found",
    "Qidirilayotgan yoki tanlanayotgan shartga mos obyekt topilmadi.",
    [
        "Selection kriteriyasini tekshiring.",
        "Layer holatini tekshiring.",
        "Qidiruv hududini kengaytiring.",
        "QSELECT yoki SELECTSIMILAR bilan tekshiring."
    ],
    "Qidiruvdan oldin obyektning layer va type qiymatini aniqlash foydali."
)


# =========================================================
# 🎥 YOUTUBE LINKLAR
# =========================================================

# Har bir errorga yuqorida avtomatik YouTube search URL biriktirilgan.
# Masalan:
# AUTOCAD_ERRORS["Installation Failed"]["video"]


# =========================================================
# 🔧 HELPER FUNCTIONS
# =========================================================

def get_autocad_error(error_name):
    return AUTOCAD_ERRORS.get(error_name)


def get_autocad_error_names():
    return list(AUTOCAD_ERRORS.keys())


def get_autocad_error_count():
    return len(AUTOCAD_ERRORS)


if __name__ == "__main__":
    print(f"AUTOCAD XATOLARI: {len(AUTOCAD_ERRORS)} ta")

    print("\nBirinchi 10 ta:")
    for i, name in enumerate(AUTOCAD_ERRORS.keys(), 1):
        if i > 10:
            break
        print(f"{i}. {name}")

    print("\nInstallation xatolari:")
    installation_words = (
        "Installation",
        "install",
        "Installer",
        "Error 160",
        "Error 1303",
        "Error 1719",
        "Desktop Connector",
        "Windows Installer",
    )

    for name in AUTOCAD_ERRORS:
        if any(word.lower() in name.lower() for word in installation_words):
            print(f"❌ {name}")
