# Plume-un məxfilik siyasəti

**Son yenilənmə: 1 oktyabr 2026** — Versiya 2.2

> *2.2 versiyasında nə dəyişib:* 2.1 versiyasında olmayan Plume-un səsli tərcüməçisi **Səsli ünsiyyət**i təsvir edirik: telefonunuzda nə qalır, AI Pro rejimində nə göndərilir və telefonun səs sintezi mühərrikinin ucadan oxuması (bax §4.1 və §9).

> *2.1 versiyasında nə dəyişib:* versiya 2.0-ın qeyd etmədiyi **Kamuflyaj rejimini** təsvir edirik və artıq dəqiq olmayan bir iddianı düzəldirik: həm şəxsi dillər, həm də Kamuflyaj üçün **mesajlarınızdakı hələ lüğətinizdə olmayan sözlər tək-tək saxlanılır** — heç vaxt cümlə deyil — onları əlavə etməyi sizə təklif edə bilmək üçün. Təfərrüat «Bir dəqiqədə» bölməsində, §2.2-də və §3-də yer alır. Biz həmçinin ikinci bir səhvi də düzəldirik: **fərdiləşdirilmiş personalarınız və onların avatarları serverlərimizdə ehtiyat nüsxə kimi saxlanılır** — onlar yalnız telefonunuzda qalmır (bax §3).

> *Versiya 1.0-dan bəri nə dəyişib və tətbiqdə qəbul ekranını yenidən niyə görə bilərsiniz:* artıq doğru olmayan iki iddianı düzəldirik. Birincisi, **şəxsi dillər** funksiyası yaratdığınız məzmunu (ad, əlifba, lüğət) serverlərimizdə saxlayır — versiya 1.0 səhvən heç bir mətnin saxlanmadığını bildirirdi. İkincisi, artıq bir **texniki nasazlıq hesabatı** aləti istifadə edirik — versiya 1.0 belə bir alətin mövcud olmadığını bildirirdi. Bu iki nöqtənin təfərrüatı aşağıdakı «Bir dəqiqədə» bölməsində, həmçinin §3 və §9-da yer alır. Bunlar tətbiqdə yeni razılıq tələbini yaradan tam olaraq iki dəyişiklik kateqoriyasıdır (bax §11).

---

## Məlumatlarınıza görə kim məsuliyyət daşıyır

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, Fransa
Əlaqə: sogacmoi7@gmail.com

Tətbiq Google Play-də **openfunworld** naşir adı ilə dərc olunur.

Bu siyasət Plume tətbiqinin hazırkı versiyasında nə etdiyini təsvir edir. O, ümumi bir şablon əsasında deyil, tətbiqin kodunu oxuyaraq yazılmışdır.

---

## Bir dəqiqədə

Plume sizə yazmaqda kömək edir: yazdığınız tətbiqin içində birbaşa mətninizi yenidən tərtib edir və ekranda göstərilən mətni tərcümə edə bilir.

Yadda saxlamalı üç şey:

1. **Plume nə yenidən tərtib etdiyiniz mətnləri, nə də ekranda oxunan mətni saxlamır.** Bunların nə surətini, nə də jurnalını saxlayırıq. **Şüurlu və könüllü istisnalar:** əgər bir **şəxsi dil** (öz qurduğunuz dil, sözlər lüğəti və onların tərifləri ilə) və ya **kamuflyaj lüğəti** (sözlərdən ibarət gizli kodunuzu) yaradarsanız, onun məzmunu serverlərimizdə **saxlanılır** — bu, onu başqa cihazda tapmağınıza, inkişaf etdirməyinizə və paylaşmağınıza imkan verən yeganə yoldur. Bu iki rejimdə yazdığınız zaman isə **mesajınızdakı hələ lüğətinizdə olmayan tək sözlər** tək-tək kənara qoyulur — heç vaxt cümlə deyil — onları əlavə etməyi sizə təklif etmək üçün. Təfərrüat §3-də yer alır.
2. **Seçdiyiniz mühərrikdən asılı olaraq, mətniniz telefonunuzu tərk edir və ya etmir.** İki mühərrik (Lokal Dəst və Lokal SI) tamamilə cihazda işləyir. Üçüncüsü (Bulud SI) mətni Avropa İttifaqından **kənarda** yerləşən süni intellekt xidmətinə göndərir. Siz seçirsiniz, və Bulud SI heç vaxt açıq razılığınız olmadan aktivləşmir.
3. **Plume güclü icazələr tələb edir** (digər tətbiqlərdə göstərilən məzmunu oxumaq, ekranı çəkmək). Aşağıda onların nəyə xidmət etdiyini və nəyə xidmət etmədiyini dəqiq izah edirik.

---

## 1. Plume ekranınızda nəyi oxuyur, və nə vaxt

### 1.1 Əlçatanlıq xidməti

Mətninizi yazdığınız yerdə yenidən tərtib etmək üçün, Plume Android-in əlçatanlıq xidmətindən istifadə edir. Bu, Plume-un sizə **əvvəlcədən** izahat ekranı göstərdikdən sonra telefonunuzun ayarlarında özünüz aktivləşdirdiyiniz bir icazədir.

Konkret olaraq:

- **Sakit vəziyyətdə**, Plume yalnız hansı tətbiqin açıq olduğunu və kursoru nə vaxt bir daxiletmə sahəsinə qoyduğunuzu bilir. Bu, üzən kapsulun görünməsinə səbəb olur — və yalnız özünüz konfiqurasiya etdiyiniz tətbiqlərdə.
- **Sahənin məzmunu yalnız kapsula toxunduğunuz dəqiq anda oxunur**, yenidən tərtib edilib yerində əvəz olunmaq üçün.
- **Parol sahələri istisna edilir.** Tətbiq parol tipli sahələri (rəqəmsal kodlar və veb sahələri daxil olmaqla) aşkar edir və onları oxumaqdan imtina edir.
- Bu icazə ekranınızın **heç bir şəkildə çəkilməsinə imkan vermir**.
- Plume başqa bir tətbiqdə **heç vaxt sizin əvəzinizə toxunmur**: sahənin mətnini əvəz edir, bundan başqa heç nə etmir.

Özünüz aktivləşdirdiyiniz iki funksiya — **Mətn rejimində Dəstəkli Oxu** və **qəbul edilən mesajların tərcüməsi** — işlədikləri müddətdə göstərilən mətni fasiləsiz oxuyur və onları söndürən kimi dayanır.

Əlçatanlıq xidmətini rədd etsəniz, Plume yenə də istifadə oluna bilər: mətn seçib Android seçim menyusundakı «Plume» vasitəsilə keçə, yaxud mətni Plume-a paylaşa bilərsiniz.

### 1.2 Ekran görüntüsü (Dəstəkli Oxu)

Dəstəkli Oxu göstərilən mətnin üzərinə tərcümə yerləşdirir — məsələn, komiks qabarcıqlarının üzərinə. Bunun üçün ekranın görüntüsünü görməyə ehtiyacı var.

- O, defolt olaraq **deaktivdir** və yalnız açıq şəkildə, birər-birər icazə verdiyiniz tətbiqlərdə işləyir.
- **Android hər sessiya başlanğıcında öz razılığını tələb edir.** Bu, bir dəfəlik verilən icazə deyil: hər sessiya yeni razılıq tələb edir. Plume heç vaxt bu razılığı yenidən istifadə etməyə və ya yan keçməyə cəhd etmir.
- Bütün sessiya boyu, **daimi bir bildiriş və sistem göstəricisi görünür qalır**. Plume ekranınızı gizli şəkildə çəkə bilməz.
- Sessiya **ekran kilidləndikdə avtomatik dayanır**, və siz onu özünüz dayandırdıqda dərhal dayanır.
- Öz görüntüsünü qoruyan tətbiqlər (bank tətbiqləri, parol meneceriləri) Plume hər hansı bir şey almazdan əvvəl **Android tərəfindən qaralanır**. Bu, real, lakin qismən bir sistem qorunmasıdır: bütün həssas tətbiqlər onu aktivləşdirmir. Buna görə də biz onu mütləq bir zəmanət kimi təqdim etmirik.
- **Çəkilən şəkillər heç vaxt saxlanılmır və ya göndərilmir.** Hər şəkil mətni çıxarmaq üçün yaddaşda təhlil olunur, sonra atılır. Heç bir şəkil, seçilən mühərrikdən asılı olmayaraq, heç vaxt telefonunuzdan çıxmır.

---

## 2. Telefonunuzda nə qalır və nə çıxır

Bu, bu siyasətdəki ən vacib fərqdir, və onu idarə edən sizsiniz.

### 2.1 Heç nəyi xaricə çıxarmayan mühərriklər

- **Lokal Dəst** (oflayn mətn tanıma və tərcümə) tamamilə cihazda işləyir.
- **Lokal SI** bir dəfə yüklənib sonra telefonunuzda saxlanan (təxminən 720 Mb) süni intellekt modelidir. O, cihazınızda işləyir.

Bu iki mühərriklə, **oxunan və ya yenidən tərtib edilən mətn telefonunuzu tərk etmir.** Mətninizin məzmunu ilə bağlı heç bir şəbəkə çağırışı yoxdur.

### 2.2 Bulud SI mühərriki

Bulud SI-ni seçdiyinizdə, və ya cihazınız Lokal SI üçün kifayət qədər güclü olmadıqda, müvafiq mətn serverlərimizə, sonra isə üçüncü tərəf süni intellekt xidmətinə ötürülür.

**Real marşrut haqqında aydın olmaq lazımdır:**

- Mətn **Avropa İttifaqında** (Mərkəzi Avropa regionu, Frankfurt) yerləşdirilən server infrastrukturumuz vasitəsilə keçir.
- Sonra o, Avropa İttifaqından **kənarda** yerləşən bir marşrutlaşdırma vasitəçisinə ötürülür, bu da onu üçüncü tərəfin süni intellekt modeli ilə işlətdirir.
- **Deməli, bu, Avropa İttifaqından kənara məlumat ötürülməsidir.** Biz əksini iddia etmirik və bu mərhələ üçün heç bir Avropa hostinq vədi vermirik.
- **Plume mətninizi saxlamır.** Server funksiyalarımızın heç biri mətninizin məzmununu yazmır: yalnız kvotanızı saymaq və sui-istifadəni aşkar etmək üçün texniki sorğu identifikatoru və cihazınızın identifikatorunu qeyd edirik. **Yeganə istisna:** Şəxsi dil rejimində və Kamuflyaj rejimində lüğətinizdə olmayan tək sözlər kənara qoyulur (bax §3).
- **Kamuflyaj və Şəxsi dil rejimləri eyni yolu izləyir** hər dəfə SI-yə ehtiyac duyduqda: lüğətinizin tam əhatə etmədiyi mesajı kamuflyaj etmək və ya deşifrə etmək, sözü uyğunlaşdırmaq və ya təsrif etmək, yaxud lüğətinizi böyütmək üçün (bu zaman gözləyən sözlər SI xidmətinə göndərilir). Kamuflyaj rejimini təqdim edən ekran bunu aktivləşdirməzdən əvvəl sizə bildirir.
- **Bu təchizatçıların öz tərəflərində nə etdiklərini zəmanət verə bilmirik.** Bunu sizə deməyi, yoxlaya bilmədiyimiz sıfır saxlama vəd etməkdən üstün tuturuq.

**Bulud SI heç vaxt öz-özünə aktivləşmir.** Xüsusi bir razılıq ekranı ilk göndərilişdən əvvəl bu məqamları izah edir, və siz qəbul etmədən heç nə göndərilmir. Lokal SI uğursuz olarsa, Plume səssizcə buluda keçmir: sizə bildirir və qərarınızı gözləyir. Bu razılığı istənilən vaxt ayarlarda ləğv edə bilərsiniz.

Göndərilən mətn məhdudlaşdırılıb: yenidən tərtib üçün 1200 simvol, ekran təhlili üçün 4000 simvol.

---

## 3. Saxladığımız məlumatlar

§5-də təsvir olunan reklamdan başqa **heç bir auditoriya təhlili aləti və heç bir üçüncü tərəf reklam izləyicisi** istifadə etmirik. **Texniki nasazlıq hesabatı aləti istifadə edirik**: o, yalnız proqram xətalarını görür (xəta növü, texniki çağırış yığını, tətbiqin versiyası, əməliyyat sistemi), heç vaxt istifadənizi və ya marşrutunuzu görmür, və heç vaxt yazdığınız mətni görmür — hər hansı göndərilişdən əvvəl xüsusi bir filtr buna qadağa qoyur. Təfərrüat §9-da yer alır.

Serverlərimizdə saxlanılan hər şey budur:

| Məlumat | Nə üçün | Müddət |
|---|---|---|
| **Cihaz identifikatoru** (Plume tərəfindən yaradılan təsadüfi nömrə, kimliyinizlə və ya reklam identifikatoru ilə heç bir əlaqəsi olmayan) | Cihazı hesaba bağlamaq, kvotaları tətbiq etmək, sui-istifadəni bloklamaq | Hesabınız silinənə qədər |
| **Hesabın e-poçt ünvanı** (e-poçt vasitəsilə və ya Google ilə hesab yaratsanız) | Sizi doğrulamaq, abunəliyinizi bağlamaq | Hesabınız silinənə qədər |
| **İstifadə sayğacları** (gündəlik və aylıq yenidən tərtiblərin sayı — mətn deyil, rəqəmlər) | Kvotaları tətbiq etmək | Hesabınız silinənə qədər |
| **Alış tarixçəsi** (Google Play əməliyyat identifikatoru, tarixlər, abunəlik statusu) | Ödədiyiniz şeyə giriş vermək, yenilənmələri idarə etmək, mühasibat öhdəliklərimizə əməl etmək | Hesabın silinməsindən sonra da saxlanılır, lakin **kimliyinizdən ayrılmış** (bax §6) |
| **Könüllü göndərilən təkliflər** (tətbiqdən bizə persona təklifi göndərsəniz) | Kataloqu təkmilləşdirmək. Bu təkliflər heç vaxt dərc olunmur. | Hesabınız silinənə qədər |
| **Sui-istifadənin texniki siqnalları** (təkrarlanan aşımlar, tamlıq yoxlamasının uğursuzluğu — heç bir mətn olmadan) | Təhlükəsizlik, fırıldaqçılıqla mübarizə | Hesabın silinməsi zamanı kimliyinizdən ayrılır |
| **Tətbiqin dili və versiyası** | Doğru məzmunu təqdim etmək | Hesabınız silinənə qədər |
| **Yaratdığınız şəxsi dillərin məzmunu** (adı, əlifbası və lüğəti — sizin və ya digər şəxslərin orada yazdığı sözlər və tərifləri) | Dilinizi başqa cihazda tapmağınıza, onu inkişaf etdirməyinizə və digər istifadəçilərlə paylaşmağınıza imkan vermək | Dil mövcud olduğu müddətcə. Onu silsəniz, onun kartı yox olur — lakin artıq **başqa bir şəxs tərəfindən idxal edilmiş** bir surət artıq ona məxsusdur və **yaşamağa davam edir**, üçüncü tərəfin artıq aldığı bir mesaj kimi ki, onu onların yanında silə bilmirik |
| **Fərdiləşdirilmiş personalarınız** (adı, təlimatları, seçilmiş avatar və əgər şəkil idxal etmisinizsə, ən çoxu 512 piksellik miniatür — şəxsi dilin idxal edilmiş emblemi üçün də eynilə) | Onları yenidən quraşdırmadan sonra və ya başqa cihazda tapmağınıza və paylaşmağınıza imkan vermək. Personanın təlimatı onu istifadə edən hər yenidən formalaşdırmada süni intellekt xidmətinə göndərilir | Persona mövcud olduğu müddətcə. Zibil qutusuna atılmış persona 30 gün sonra, personalar siyahınızı növbəti dəfə açdığınız zaman silinir. Hesabınız silindikdə hər şey yoxa çıxır |
| **Kamuflyaj lüğətləriniz** (adı, mövzusu, dili, seçilmiş emblem və «real söz → kod sözü» söz cütləri) | Mesajlarınızı kamuflyaj etmək və deşifrə etmək, lüğətinizi başqa cihazda tapmağınıza, inkişaf etdirməyinizə və paylaşmağınıza imkan vermək | Lüğət mövcud olduğu müddətcə. Zibil qutusuna atılmış lüğət 30 gün ərzində bərpa edilə bilər, sonra lüğətlərinizi növbəti dəfə açdığınız zaman silinir. Hesabınız silindikdə hər şey yoxa çıxır |
| **Gözləyən sözlər** (şəxsi dil və Kamuflyaj): mesajlarınızdakı hələ lüğətinizdə olmayan tək sözlər — heç vaxt cümlə deyil —, görünmə sayı və ilk və son görünmə tarixləri ilə | Onları lüğətinizə əlavə etməyi sizə təklif etmək və lüğətinizi böyütdüyünüz zaman SI xidməti tərəfindən emal etdirmək | Əlavə edildikdən sonra da, dil və ya lüğət mövcud olduğu müddətcə saxlanılır. **Əgər başqa şəxsin sizinlə paylaşdığı kamuflyaj lüğəti ilə yazırsınızsa**, ona çatışmayan sözlər **onun lüğətində** kənara qoyulur və o şəxs onları görə bilər |
| **Dillərinizin və lüğətlərinizin paylaşımı** (paylaşım jetonu, yalnız barmaq izi (heş) şəklində saxlanılır; idxalların və bağlantıların tarixçəsi) | Yaxınlarınızın mesajlarınızı oxumasına imkan vermək. Lüğətin sahibi ona bağlı olan şəxslərin siyahısını görür (göstərilən ad və Google profil şəkli — heç vaxt e-poçt ünvanı deyil) | Jetonun müddəti bitir. Ləğv edilmiş paylaşımın izi saxlanılır |
| **Kamuflyaj edilməmiş fraqmentlər** (lüğətsiz Kamuflyaj rejimi: kamuflyajdan sonra oxunaqlı qalmış mesajın qısa parçaları, ən çox 40 simvol) | Ümumi kamuflyaj şəbəkəsini yaxşılaşdırmaq | Hesab identifikatoru olmadan, yalnız cihazın psevdonim barmaq izinə bağlı. Hələ heç bir müddət müəyyən edilməyib və hesab silindikdə silinmirlər |
| **Sözlərin tərifləri** (söz və onun yaradılmış tərifi, lüğətinizdəki sözün tərifini istədiyiniz zaman) | Eyni tərifi iki dəfə yaratmamaq | Hamı üçün ümumi keş, hesab və ya dil **identifikatoru olmadan**. Hesab silindikdə silinmir |
| **Texniki nasazlıq hesabatları** (xəta növü, kəsilmiş texniki çağırış yığını, tətbiqin versiyası, əməliyyat sistemi — heç vaxt mətn məzmunu deyil) | Tətbiqin nasazlıqlarını diaqnoz qoymaq və düzəltmək | Nasazlıq hesabatı təchizatçımız tərəfindən idarə olunur (bax §9). Bu toplama razılığınıza və istənilən vaxt, tətbiq yeniləməsi olmadan, söndürə biləcəyimiz bir açara tabedir |

**Toplamadığımız:** adınız, kontaktlarınız, məkanınız, ünvan kitabçanız, fotolarınız, təqviminiz, tətbiqlərinizin tarixçəsi. Plume bu icazələrdən heç birini tələb etmir.

**Yalnız telefonunuzda qalan:** ayarlarınız, tətbiq üzrə qaydalarınız, Dəstəkli Oxunun tərcümə keşi (hər sessiyanın sonunda silinir). Bunlardan heç biri serverlərimizə göndərilmir.

---

## 4. Səsli diktə

Bir mikrofon düyməsi yazmaq əvəzinə diktə etməyə imkan verir. Mikrofona giriş icazəsi **məhz bu düyməyə basdığınız anda** tələb olunur, heç vaxt başlanğıcda deyil, və mikrofon yalnız o an açılır. Plume heç vaxt arxa fonda dinləmir.

**Plume heç bir səs yazısı almır, saxlamır və ötürmür.** Diktə telefonunuza daxil edilmiş səs tanıma mühərrikinə (Android-in özününkünə) həvalə edilir. Plume yalnız transkript edilmiş mətni alır.

**Vacib və dürüst bir nöqtə:** bu sistem mühərriki telefonunuza, adətən Google-a məxsusdur. Cihazınızdan, onun ayarlarından və quraşdırılmış dil modullarından asılı olaraq, **o, səsi transkript etmək üçün naşirinin serverlərinə ötürə bilər.** Bu emal Plume-dan kənardır və əməliyyat sisteminizin naşirinin məxfilik siyasətinə tabedir. Buna görə də səsinizin cihazda qaldığını təsdiq edə bilmirik — bu telefonunuzdan asılıdır, bizdən deyil.

Mikrofon icazəsini rədd etsəniz, klaviatura ilə yazma təbii ki, əlçatan qalır.

### 4.1 Səsli ünsiyyət (səsli tərcüməçi)

Səsli ünsiyyət iki nəfər arasındakı söhbəti ucadan tərcümə edir. **Mikrofon yalnız kürəyə toxunduğunuz zaman açılır** və hər cümlənin sonunda bağlanır.

- **Nitq** diktə ilə eyni telefon səs tanıma mühərriki ilə mətnə çevrilir, yuxarıdakı eyni qeydlərlə. **Plume yalnız mətni alır, heç vaxt səsi almır.** Dilin oflayn modulu yoxdursa, Plume telefondan onu yükləməyi xahiş edir; bu arada telefonun mühərriki onlayn şəkildə mətnə çevirə bilər.
- **Lokal dəst rejimində** (pulsuz) tərcümə **telefonunuzda** edilir.
- **AI Pro rejimində** (abunəçilər) mətnə çevrilmiş mətn serverlərimizə, oradan da dinləmə səhvlərini düzəldib tərcümə edən süni intellektlə emal xidməti təchizatçımıza göndərilir — §2.2-dəki ilə eyni yolla. **Nə mətni, nə də onun tərcüməsini saxlamırıq.**
- **Ucadan oxumanı** telefonun səs sintezi mühərriki (adətən Google-un mühərriki) həyata keçirir. Hər iki rejimdə Plume ondan daha təbii olan **onlayn səslərini** istəyir: bu halda tərcümə olunmuş mətn tələffüz üçün onun naşirinə ötürülür. Bağlantı olmadıqda telefonda quraşdırılmış səs onu əvəz edir.
- **Söhbət tarixçəsi telefonunuzda qalır** və ekrandan çıxdıqda silinir. Cihazda yalnız seçilmiş dil cütü, seçilmiş mühərrik və söhbətlərin sayı (pulsuz səviyyənin reklamı üçün) yadda saxlanılır.

---

## 5. Reklam

Xidmət gündəlik müəyyən istifadə həddi daxilində pulsuzdur. Bundan sonra, əlavə istifadələri açmaq üçün mükafatlı reklam izləməyi **seçə** bilərsiniz. Bu heç vaxt məcburi deyil: reklam izləməsəniz, sadəcə haqqınız olana sahib olursunuz.

- Reklamlar **Google AdMob** tərəfindən təqdim olunur.
- Onlar **yalnız Plume tətbiqinin özündə** görünür, heç vaxt üzən kapsulda və heç vaxt başqa bir tətbiqin üzərində deyil.
- **Abunəçilər heç bir reklam görmür.**
- Avropa İqtisadi Zonasında, Birləşmiş Krallıqda və İsveçrədə, Google tərəfindən sertifikatlaşdırılmış bir platforma tərəfindən təqdim olunan razılıq forması sizə **ilk reklamdan əvvəl** təqdim olunur. Seçiminiz toplanmayana qədər, heç bir reklam tələb olunmur. Rədd etsəniz, reklamlar **fərdiləşdirilməmiş** qalır və **heç bir funksiya sizdən alınmır**. Bu seçimi istənilən vaxt ayarlardan dəyişə bilərsiniz.
- Mükafatınızı etibarlı şəkildə hesablamaq üçün, Plume cihaz identifikatorunuz AdMob-a ötürülür. Google əlavə olaraq öz məxfilik siyasətinə uyğun olaraq öz məlumatlarını toplaya bilər.

*Bu sənədin yazıldığı tarixdə, reklam yayımı server tərəfindən deaktiv edilib. Bu bölmə aktivləşdirildikdən sonra necə işləyəcəyini təsvir edir.*

---

## 6. Abunəliklər və alışlar

Abunəliklər və paketlər **Google Play** vasitəsilə satılır. Biz heç vaxt bank məlumatlarınızı görmürük: onlar faktura mənasında satıcı olan Google tərəfindən emal olunur.

Google-dan bir alış sübutu alırıq, serverimiz onu yoxlayır, və izini saxlayırıq (əməliyyat identifikatoru, tarixlər, status). Bu iz mühasibat səbəblərinə görə və eyni alışın iki dəfə istifadə olunmasının qarşısını almaq üçün saxlanılır — lakin hesabınızı sildikdə **kimliyinizdən ayrılır**.

---

## 7. Hüquqlarınız

GDPR tərəfindən nəzərdə tutulan giriş, düzəliş, silinmə, məhdudlaşdırma, etiraz və köçürülmə hüquqlarına sahibsiniz.

**Ən sadəsi və ən sürətlisi: silinmə tətbiqə inteqrasiya edilib.**
Ayarlar → Məxfilik → Məlumatlarımı sil. O, **dərhal icra olunur**, növbəyə qoyulmur. Nələrin silindiyinin və nələrin saxlandığının təfərrüatı xüsusi səhifəmizdə yer alır: `https://readit0.github.io/plume-legal/suppression-compte`.

Tətbiqi quraşdırmadan da, sogacmoi7@gmail.com ünvanına yazaraq hesabınızı silə bilərsiniz.

Hər hansı digər sorğu üçün **sogacmoi7@gmail.com** ünvanına yazın. Bir ay ərzində cavab veririk.

**Hüquqi əsaslar:** müqavilənin icrası (tələb etdiyiniz xidməti təqdim etmək, abunəliyinizi idarə etmək), razılığınız (əlçatanlıq xidməti, ekran görüntüsü, Bulud SI-ə göndərmə, fərdiləşdirilmiş reklam), qanuni maraqımız (təhlükəsizlik, fırıldaqçılıqla mübarizə) və qanuni öhdəliklərimiz (mühasibatlıq).

Şikayətinizi naşirin nəzarət orqanı olan **CNIL**-ə (www.cnil.fr), və ya **Avropa İttifaqında yaşayırsınızsa**, yaşadığınız ölkənin nəzarət orqanına təqdim edə bilərsiniz — GDPR-in 77-ci maddəsi seçimi sizə buraxır.

---

## 8. Yetkinlik yaşına çatmayanlar

Plume **16 yaşdan yuxarı** auditoriya üçün nəzərdə tutulmuş bir yazı köməkçisi vasitəsidir. 16 yaşından kiçik yetkinlik yaşına çatmayanların məlumatlarını şüurlu şəkildə toplamırıq və tətbiq onlar üçün nə hazırlanmış, nə də təbliğ edilmişdir. Valideynlik hüququna sahibsinizsə və uşağınızın bizə məlumat ötürdüyünü düşünürsünüzsə, sogacmoi7@gmail.com ünvanına yazın: hesabı siləcəyik.

Tətbiq sərbəst mətnin yenidən tərtibinə imkan verdiyi və reklam göstərdiyi üçün, o, Google Play-in ailələr üçün nəzərdə tutulmuş proqramlarına uyğun deyil.

---

## 9. Alt-podratçılar və alıcılar

| Təchizatçı | Rolu | Harada |
|---|---|---|
| **Hostinq təchizatçımız** | Verilənlər bazasının hostinqi, doğrulama, server funksiyaları | Avropa İttifaqı (Frankfurt) |
| **SI emalı təchizatçımız** | Sorğuların yönləndirilməsi və mətnin üçüncü tərəfin süni intellekt modeli ilə emalı | **Avropa İttifaqından kənarda** |
| **Google Play / Google Billing** | Ödəniş, abunəliklər | Google Ireland / ABŞ |
| **Google AdMob** | Mükafatlı reklam | Google Ireland / ABŞ |
| **Google (telefonun sistem xidmətləri)** | Səs tanıma, səs sintezi (Səsli ünsiyyət üçün ucadan oxuma), oflayn tərcümə modulları | Cihazınızdan asılı olaraq |
| **Nasazlıq hesabatı təchizatçımız** | Texniki nasazlıq hesabatı — yalnız göndərilməzdən əvvəl filtrlənmiş proqram xətaları: heç vaxt mətniniz deyil | ABŞ |

**Heç bir məlumat satmırıq və heç birini məlumat brokerlərinə ötürmürük.**

**Avropa İttifaqından kənar ötürmələr:** SI emalı təchizatçımızdan, Google Play, AdMob və nasazlıq hesabatı təchizatçımızdan istifadə Avropa İttifaqından kənara məlumat ötürülməsini nəzərdə tutur.

---

## 10. Təhlükəsizlik

Tətbiq ilə serverlərimiz arasındakı mübadilələr şifrələnib (HTTPS/TLS). Verilənlər bazasındakı məlumatlara giriş server qaydaları ilə məhdudlaşdırılıb: həssas funksiyalara tətbiqdən daxil olmaq mümkün deyil. Heç bir sistem tam təhlükəsiz deyil. Yenidən tərtib etdiyiniz mətn və Dəstəkli Oxunun ekranda göstərdiyi mətn bizdə saxlanılmır, bu da bir müdaxilənin onlar haqqında nə açıqlaya biləcəyini mexaniki olaraq məhdudlaşdırır. **Bu, hər şey üçün doğru deyil:** yaratdığınız şəxsi dillərin lüğəti, kamuflyaj lüğətləriniz və gözləyən sözlər **saxlanılır** (bax §3), və real bir müdaxilə baş versə, bu siyasətin digər hər hansı məlumatı kimi ifşa olunardı — biz onu qalanı ilə eyni server giriş qaydaları ilə qoruyuruq.

---

## 11. Dəyişikliklər

Bu siyasətə hər hansı dəyişiklik yeni bir tarixlə `https://readit0.github.io/plume-legal` ünvanında dərc olunacaq. Məlumatlarınızın dövriyyəsində əhəmiyyətli bir dəyişiklik olarsa, sizə tətbiqdə xəbər verəcəyik.

**Versiya 2.0-dan bəri, bu vədin arxasında konkret bir mexanizm var.** Sadə bir forma düzəlişi (tarix, ünvan, aydınlıq) sizdən artıq heç nə tələb etmir. Lakin ƏHƏMİYYƏTLİ bir dəyişiklik — məlumatlarınızın yeni bir alıcısı, toplanan məlumatların yeni bir kateqoriyası, yeni bir məqsəd, və ya hüquqlarınızın yaxud qiymətin dəyişməsi — tətbiqdə qəbul ekranını bir dəfə yenidən göstərir, dəyişənlərin xülasəsi və iki yenilənmiş sənədlə birlikdə. Bu versiya 2.0 üçün baş verən məhz budur (bu sənədin əvvəlindəki qeydə baxın).

---

## Ümumi şərtlər

Xidmətin istifadə şərtləri (kvotalar, abunəliklər, ləğvetmə) ayrı bir sənəddə yer alır: `https://readit0.github.io/plume-legal/conditions-generales`.

---
