# Plume Gizlilik Politikası

**Son güncelleme: 31 Temmuz 2026** — Sürüm 1.0

---

## Verilerinizden kim sorumludur

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
İletişim: sogacmoi7@gmail.com

Uygulama, Google Play'de **openfunworld** yayıncı adıyla yayımlanmaktadır.

Bu politika, Plume uygulamasının mevcut sürümünde ne yaptığını açıklar. Genel bir şablondan değil, uygulamanın kodu okunarak yazılmıştır.

---

## Bir dakikada

Plume yazmanıza yardımcı olur: metninizi, yazmakta olduğunuz uygulamanın içinde doğrudan yeniden ifade eder ve ekranda görüntülenen metni çevirebilir.

Aklınızda tutmanız gereken üç şey:

1. **Plume metinlerinizin hiçbirini sunucularında saklamaz.** Ne yeniden ifade edilen metinlerinizi, ne de ekrandan okunan metni. Bunların ne bir kopyasını ne de bir kaydını tutarız.
2. **Seçtiğiniz motora göre metniniz telefonunuzdan çıkar ya da çıkmaz.** İki motor (yerel Kit ve yerel yapay zekâ) tamamen cihaz üzerinde çalışır. Üçüncüsü (Bulut yapay zekâ), metni **Avrupa Birliği dışında bulunan** bir yapay zekâ hizmetine gönderir. Seçim sizindir ve Bulut yapay zekâ, açık rızanız olmadan asla etkinleşmez.
3. **Plume'ün güçlü izinlere ihtiyacı vardır** (diğer uygulamalarda görüntülenen içeriği okumak, ekranı yakalamak). Bunların tam olarak neye yaradığını ve neye yaramadığını aşağıda açıklıyoruz.

---

## 1. Plume ekranınızda neyi ve ne zaman okur

### 1.1 Erişilebilirlik hizmeti

Metninizi yazdığınız yerde yeniden yazabilmek için Plume, Android'in erişilebilirlik hizmetini kullanır. Bu, telefonun ayarlarından kendinizin etkinleştirdiği bir izindir; Plume bu izni istemeden **önce** size açıklayıcı bir ekran gösterir.

Somut olarak:

- **Beklemede olduğunda** Plume yalnızca hangi uygulamanın açık olduğunu ve imleci bir metin alanına ne zaman yerleştirdiğinizi bilir. Yüzen kapsülü ortaya çıkaran budur — ve yalnızca kendinizin yapılandırdığı uygulamalarda.
- **Alanın içeriği yalnızca kapsüle dokunduğunuz anda okunur**; yeniden yazılıp yerine konulmak üzere.
- **Parola alanları hariç tutulur.** Uygulama, parola türündeki alanları (sayısal kodlar ve web alanları dâhil) algılar ve bunları okumayı reddeder.
- Bu izin, ekranınızın **hiçbir görüntüsünün yakalanmasına imkân vermez**.
- Plume başka bir uygulamada **asla sizin yerinize dokunmaz**: yalnızca bir alanın metnini değiştirir, başka hiçbir şey yapmaz.

Kendinizin etkinleştirdiği iki işlev — **Metin modunda Destekli Okuma** ve **alınan mesajların çevirisi** — çalıştıkları sürece görüntülenen metni sürekli okur ve siz onları kapattığınız anda durur.

Erişilebilirlik hizmetini reddederseniz Plume yine de kullanılabilir kalır: bir metni seçip Android seçim menüsündeki "Plume" seçeneğini kullanabilir ya da bir metni Plume ile paylaşabilirsiniz.

### 1.2 Ekran yakalama (Destekli Okuma)

Destekli Okuma, görüntülenen metnin üzerine bir çeviri bindirir — örneğin bir çizgi romanın konuşma balonlarının üzerine. Bunun için ekranın görüntüsünü görmesi gerekir.

- **Varsayılan olarak devre dışıdır** ve yalnızca tek tek, açıkça izin verdiğiniz uygulamalarda çalışır.
- **Android her oturum başlangıcında size kendi onayını sorar.** Bu, bir kez verilip sonsuza kadar geçerli olan bir izin değildir: her oturum yeni bir onay gerektirir. Plume bu onayı yeniden kullanmaya ya da aşmaya asla çalışmaz.
- Oturum boyunca **kalıcı bir bildirim ve bir sistem göstergesi görünür kalır**. Plume ekranınızı gizlice yakalayamaz.
- Oturum, **ekran kilitlendiğinde otomatik olarak** ve siz kendiniz durdurduğunuzda anında sona erer.
- Görüntüsünü koruyan uygulamalar (bankacılık uygulamaları, parola yöneticileri), Plume herhangi bir şey almadan önce **Android'in kendisi tarafından karartılır**. Bu bir sistem korumasıdır; gerçektir ama kısmidir: hassas uygulamaların hepsi bunu etkinleştirmez. Bu nedenle bunu mutlak bir güvence olarak sunmuyoruz.
- **Yakalanan görüntüler asla kaydedilmez ve gönderilmez.** Her görüntü, metnini çıkarmak için bellekte çözümlenir, sonra bırakılır. Seçilen motor ne olursa olsun, hiçbir görüntü telefonunuzdan asla çıkmaz.

---

## 2. Telefonunuzda ne kalır ve ne çıkar

Bu, bu politikanın en önemli ayrımıdır ve onu denetleyen sizsiniz.

### 2.1 Dışarıya hiçbir şey çıkarmayan motorlar

- **Yerel Kit** (çevrimdışı metin tanıma ve çevirisi) tamamen cihaz üzerinde çalışır.
- **Yerel yapay zekâ**, bir kez indirilip telefonunuzda saklanan bir yapay zekâ modelidir (yaklaşık 720 MB). Cihazınızda çalışır.

Bu iki motorla, **okunan ya da yeniden ifade edilen metin telefonunuzdan çıkmaz.** Metninizin içeriğine bağlı hiçbir ağ çağrısı yoktur.

### 2.2 Bulut yapay zekâ motoru

Bulut yapay zekâyı seçtiğinizde ya da cihazınız yerel yapay zekâ için yeterince güçlü olmadığında, ilgili metin sunucularımıza, ardından üçüncü taraf bir yapay zekâ hizmetine iletilir.

**Gerçek güzergâh konusunda açık olmak gerekir:**

- Metin, **Avrupa Birliği**'nde (Orta Avrupa bölgesi, Frankfurt) barındırılan altyapımızdan (Supabase) geçer.
- Ardından, **Avrupa Birliği dışında bulunan** bir yönlendirme aracısı olan **openrouter.ai**'ya iletilir; o da metni **Mistral Small** modeline işletir.
- **Dolayısıyla bu, Avrupa Birliği dışına yapılan bir veri aktarımıdır.** Aksini iddia etmiyoruz ve bu aşama için hiçbir Avrupa'da barındırma vaadi göstermiyoruz.
- **Plume metninizi saklamaz.** Sunucu işlevlerimizin hiçbiri metninizin içeriğini yazmaz: yalnızca teknik bir istek kimliğini ve cihazınızın kimliğini kaydederiz; kotanızı saymak ve kötüye kullanımları tespit etmek için.
- **Bu sağlayıcıların kendi taraflarında ne yaptıklarını ise garanti edemeyiz.** Doğrulayacak durumda olmadığımız sıfır saklama vaadinde bulunmaktansa bunu size söylemeyi tercih ediyoruz.

**Bulut yapay zekâ asla kendiliğinden etkinleşmez.** İlk gönderimden önce özel bir rıza ekranı size bu noktaları açıklar ve siz kabul etmediğiniz sürece hiçbir şey gönderilmez. Yerel yapay zekâ başarısız olursa Plume sessizce buluta geçmez: durumu size bildirir ve kararınızı bekler. Bu rızayı ayarlardan istediğiniz zaman geri alabilirsiniz.

Gönderilen metin sınırlıdır: bir yeniden ifade için 1 200 karakter, bir ekran çözümlemesi için 4 000 karakter.

---

## 3. Sakladığımız veriler

**Hiçbir kitle ölçüm aracı, hiçbir üçüncü taraf reklam izleyicisi, hiçbir çökme raporlama aracı** kullanmıyoruz. Uygulama, ölçüm SDK'sı içermez.

Sunucularımızda saklananların tamamı şudur:

| Veri | Neden | Süre |
|---|---|---|
| **Cihaz kimliği** (Plume tarafından üretilen rastgele bir numara; kimliğinizle ya da bir reklam kimliğiyle bağlantısı yoktur) | Bir cihazı bir hesaba bağlamak, kotaları uygulamak, kötüye kullanımları engellemek | Hesabınızın silinmesine kadar |
| **Hesabın e-posta adresi** (e-posta ile ya da Google üzerinden hesap oluşturursanız) | Kimliğinizi doğrulamak, aboneliğinizi bağlamak | Hesabınızın silinmesine kadar |
| **Kullanım sayaçları** (günlük ve aylık yeniden ifade sayısı — sayılar, metinler değil) | Kotaları uygulamak | Hesabınızın silinmesine kadar |
| **Satın alma geçmişi** (Google Play işlem kimliği, tarihler, abonelik durumu) | Ödediğiniz şeye erişim vermek, yenilemeleri yönetmek, muhasebe yükümlülüklerimize uymak | Hesap silindikten sonra da saklanır, ancak **kimliğinizden ayrılmış olarak** (bkz. §6) |
| **Gönüllü olarak gönderilen öneriler** (uygulamadan bize bir persona önerisi yazarsanız) | Kataloğu iyileştirmek. Bu öneriler asla yayımlanmaz. | Hesabınızın silinmesine kadar |
| **Teknik kötüye kullanım sinyalleri** (tekrarlanan aşımlar, bütünlük denetimi başarısızlığı — hiçbir metin içermez) | Güvenlik, dolandırıcılıkla mücadele | Hesap silindiğinde kimliğinizden ayrılır |
| **Uygulamanın dili ve sürümü** | Doğru içeriği sunmak | Hesabınızın silinmesine kadar |

**Toplamadıklarımız:** adınız, kişileriniz, konumunuz, adres defteriniz, fotoğraflarınız, takviminiz, uygulama geçmişiniz. Plume bu izinlerin hiçbirini istemez.

**Yalnızca telefonunuzda kalanlar:** kişiselleştirdiğiniz personalar ve avatarları, ayarlarınız, uygulama başına kurallarınız, Destekli Okuma'nın çeviri önbelleği (her oturumun sonunda silinir). Bunların hiçbiri sunucularımıza gönderilmez.

---

## 4. Sesli dikte

Bir mikrofon düğmesi, yazmak yerine dikte etmenizi sağlar. Mikrofona erişim izni **tam olarak bu düğmeye bastığınız anda** istenir, asla açılışta değil; ve mikrofon yalnızca o anda açılır. Plume arka planda asla dinlemez.

**Plume hiçbir ses kaydını almaz, saklamaz ve iletmez.** Dikte, telefonunuzda yerleşik olan konuşma tanıma motoruna (Android'inkine) bırakılır. Plume yalnızca yazıya dökülen metni alır.

**Önemli ve dürüst bir nokta:** bu sistem motoru telefonunuza, genellikle de Google'a aittir. Cihazınıza, ayarlarına ve yüklü dil modüllerine bağlı olarak, **sesi yazıya dökmek için yayıncısının sunucularına iletebilir**. Bu işleme Plume'ün elinde değildir ve sisteminizin yayıncısının gizlilik politikasına tabidir. Bu nedenle sesinizin cihazda kaldığını ileri süremeyiz — bu bize değil, telefonunuza bağlıdır.

Mikrofon iznini reddederseniz, klavyeyle yazma elbette kullanılabilir kalır.

---

## 5. Reklam

Hizmet, günlük belirli bir kullanım sınırına kadar ücretsizdir. Bunun ötesinde, ek kullanımların kilidini açmak için ödüllü bir reklam izlemeyi **seçebilirsiniz**. Bu asla dayatılmaz: reklam izlemezseniz, yalnızca hakkınız olanı korursunuz.

- Reklamlar **Google AdMob** tarafından sağlanır.
- Yalnızca **Plume uygulamasının kendi içinde** görünür; asla yüzen kapsülde ve asla başka bir uygulamanın üzerinde değil.
- **Aboneler hiçbir reklam görmez.**
- Avrupa Ekonomik Alanı'nda, Birleşik Krallık'ta ve İsviçre'de, Google tarafından sertifikalandırılmış bir platformun sağladığı bir rıza formu size **ilk reklamdan önce** sunulur. Seçiminiz alınmadığı sürece hiçbir reklam istenmez. Reddederseniz reklamlar **kişiselleştirilmemiş** kalır ve **hiçbir işlev sizden geri alınmaz**. Bu seçimi ayarlardan istediğiniz zaman değiştirebilirsiniz.
- Ödülünüzü güvenilir biçimde hesabınıza geçirmek için Plume cihaz kimliğiniz AdMob'a iletilir. Google ayrıca, kendi gizlilik politikasına uygun olarak kendi verilerini toplayabilir.

*Bu metnin yazıldığı tarihte reklam yayını sunucu tarafında devre dışıdır. Bu bölüm, etkinleştirildiğinde nasıl işleyeceğini açıklar.*

---

## 6. Abonelikler ve satın almalar

Abonelikler ve paketler **Google Play üzerinden** satılır. Banka bilgilerinizi asla görmeyiz: bunlar, faturalandırma anlamında satıcı olan Google tarafından işlenir.

Google'dan, sunucumuzun doğruladığı bir satın alma belgesi alırız ve bunun izini saklarız (işlem kimliği, tarihler, durum). Bu iz, muhasebe nedenleriyle ve aynı satın almanın iki kez kullanılmasını engellemek için saklanır — ancak hesabınızı sildiğinizde **kimliğinizden ayrılır**.

---

## 7. Haklarınız

GDPR'nin öngördüğü erişim, düzeltme, silme, işlemenin kısıtlanması, itiraz ve veri taşınabilirliği haklarına sahipsiniz.

**En basiti ve en hızlısı: silme işlevi uygulamanın içine yerleştirilmiştir.**
Ayarlar → Gizlilik → Verilerimi sil. Bu işlem **anında yürütülür**, bir kuyruğa alınmaz. Neyin silindiğinin ve neyin saklandığının ayrıntısı, kendisine ayrılmış sayfamızda yer alır: `https://readit0.github.io/plume-legal/suppression-compte`.

Hesabınızı **uygulamayı yüklemeden** de, sogacmoi7@gmail.com adresine yazarak silebilirsiniz.

Diğer her talep için **sogacmoi7@gmail.com** adresine yazın. Bir ay içinde yanıt veriyoruz.

**Hukuki dayanaklar:** sözleşmenin ifası (istediğiniz hizmeti sunmak, aboneliğinizi yönetmek), açık rızanız (erişilebilirlik hizmeti, ekran yakalama, Bulut yapay zekâya gönderim, kişiselleştirilmiş reklam), meşru menfaatimiz (güvenlik, dolandırıcılıkla mücadele) ve yasal yükümlülüklerimiz (muhasebe).

**CNIL**'e (www.cnil.fr), yani yayıncının denetim makamına ya da, **Avrupa Birliği'nde ikamet ediyorsanız**, ikamet ettiğiniz ülkenin denetim makamına şikâyette bulunabilirsiniz — GDPR'nin 77. maddesi seçimi size bırakır.

---

## 8. Küçükler

Plume, **16 yaş ve üzeri** bir kitleye yönelik bir yazma yardımcısıdır. 16 yaşından küçük çocukların verilerini bilerek toplamıyoruz; uygulama onlar için tasarlanmadı ve onlara yönelik tanıtılmıyor. Velayet hakkı sahibiyseniz ve çocuğunuzun bize veri gönderdiğini düşünüyorsanız sogacmoi7@gmail.com adresine yazın: hesabı sileceğiz.

Uygulama serbest bir metnin yeniden ifade edilmesine izin verdiği ve reklam gösterdiği için, Google Play'in ailelere yönelik programlarına uygun değildir.

---

## 9. Veri işleyenler ve alıcılar

| Sağlayıcı | Rol | Nerede |
|---|---|---|
| **Supabase** | Veritabanı barındırma, kimlik doğrulama, sunucu işlevleri | Avrupa Birliği (Frankfurt) |
| **OpenRouter** | İsteklerin yapay zekâ modeline yönlendirilmesi | **Avrupa Birliği dışında** |
| **Mistral AI** (OpenRouter üzerinden) | Metni işleyen model (Mistral Small) | Yukarıdaki aracı üzerinden işleme |
| **Google Play / Google Billing** | Ödeme, abonelikler | Google Ireland / Amerika Birleşik Devletleri |
| **Google AdMob** | Ödüllü reklam | Google Ireland / Amerika Birleşik Devletleri |
| **Google (telefonun sistem hizmetleri)** | Konuşma tanıma, çevrimdışı çeviri modülleri | Cihazınıza göre değişir |

**Hiçbir veriyi satmıyoruz ve hiçbirini veri simsarlarına devretmiyoruz.**

**Avrupa Birliği dışına aktarımlar:** OpenRouter'a, Google Play'e ve AdMob'a başvurulması, Avrupa Birliği dışına bir veri aktarımı içerir. Bu aktarımların hukuki çerçevesi (standart sözleşme hükümleri, yeterlilik kararı) **yayımdan önce bir uzman tarafından doğrulanmalı ve belgelenmelidir** — belgenin sonundaki nota bakın.

---

## 10. Güvenlik

Uygulama ile sunucularımız arasındaki alışverişler şifrelidir (HTTPS/TLS). Veritabanındaki verilere erişim sunucu kurallarıyla sınırlandırılmıştır: hassas işlevlere uygulamadan erişilemez. Hiçbir sistem tam olarak güvenli değildir, ancak yeniden ifade ettiğiniz hiçbir metin bizde saklanmaz — bu da bir izinsiz girişin açığa çıkarabileceğini mekanik olarak sınırlar.

---

## 11. Değişiklikler

Bu politikadaki her değişiklik, `https://readit0.github.io/plume-legal` adresinde yeni bir tarihle yayımlanacaktır. Verilerinizin dolaşımıyla ilgili önemli bir değişiklik olması hâlinde sizi uygulama içinde bilgilendireceğiz.

---

## Genel koşullar

Hizmetin kullanım koşulları (kotalar, abonelikler, fesih) ayrı bir belgede yer alır: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Bir uzman tarafından gözden geçirilmelidir
>
> Bu belge, uygulamanın gerçek davranışı ölçülerek yazılmıştır, ancak **bir hukukçu tarafından yazılmamıştır**. Öncelikli olarak dört nokta uzman görüşü gerektirir:
>
> 1. **Avrupa Birliği dışına, OpenRouter'a yapılan veri aktarımı.** En hassas nokta budur: uygulanacak aktarım mekanizması belirlenmeli, bu sağlayıcıyla bir veri işleme sözleşmesinin bulunduğu doğrulanmalı ve burada yazılmalıdır. Bu yapılmadığı sürece, bu belge aktarımı, çerçevelenmiş olduğunu ileri sürmeden açıklamaktadır.
> 2. **§7'de benimsenen hukuki dayanaklar**, özellikle erişilebilirlik hizmeti için açık rıza ile meşru menfaat arasındaki dağılım.
> 3. **Asgari yaş** (16 yaş) ve bunun Google Play içerik derecelendirme anketiyle tutarlılığı.
> 4. **Yapay zekâya ilişkin bildirim**, Avrupa yapay zekâ tüzüğü kapsamında (sınırlı riskli bir sistem için şeffaflık yükümlülüğü).

---

Bu belge, https://readit0.github.io/plume-legal/ adresinde bulunan Fransızca sürümün bir çevirisidir. Bilgilendirme amacıyla sunulmuştur. Herhangi bir farklılık olması hâlinde sogacmoi7@gmail.com adresinden bize ulaşın.
