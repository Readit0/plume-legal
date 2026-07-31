# Dasar Privasi Plume

**Kemas kini terakhir: 31 Julai 2026** — Versi 1.0

---

## Siapa yang bertanggungjawab ke atas data anda

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Hubungi: sogacmoi7@gmail.com

Aplikasi ini diterbitkan di Google Play di bawah nama penerbit **openfunworld**.

Dasar ini menerangkan apa yang dilakukan oleh aplikasi Plume dalam versinya yang semasa. Ia ditulis dengan membaca kod aplikasi, bukan daripada templat umum.

---

## Dalam satu minit

Plume membantu anda menulis: ia merumus semula teks anda terus di dalam aplikasi tempat anda sedang menaip, dan ia boleh menterjemah teks yang dipaparkan pada skrin.

Tiga perkara yang perlu diingat:

1. **Plume tidak menyimpan satu pun teks anda pada pelayannya.** Baik teks yang anda rumus semula, mahupun teks yang dibaca pada skrin. Kami tidak menyimpan salinannya, tidak juga lognya.
2. **Bergantung pada enjin yang anda pilih, teks anda keluar atau tidak keluar daripada telefon anda.** Dua enjin (Kit tempatan dan AI tempatan) berfungsi sepenuhnya pada peranti. Enjin ketiga (AI Awan) menghantar teks kepada sebuah perkhidmatan kecerdasan buatan yang **terletak di luar Kesatuan Eropah**. Anda yang memilih, dan AI Awan tidak pernah diaktifkan tanpa persetujuan jelas daripada anda.
3. **Plume memerlukan kebenaran yang berkuasa** (membaca kandungan yang dipaparkan dalam aplikasi lain, menangkap skrin). Di bawah ini kami menerangkan dengan tepat untuk apa kebenaran itu digunakan dan untuk apa ia tidak digunakan.

---

## 1. Apa yang dibaca oleh Plume pada skrin anda, dan bila

### 1.1 Perkhidmatan kebolehaksesan

Untuk menulis semula teks anda di tempat anda menulisnya, Plume menggunakan perkhidmatan kebolehaksesan Android. Ini ialah kebenaran yang anda hidupkan sendiri, dalam tetapan telefon, selepas satu skrin penerangan yang ditunjukkan oleh Plume **sebelum** ia memintanya daripada anda.

Secara konkrit:

- **Semasa melahu**, Plume hanya tahu aplikasi mana yang sedang dibuka dan pada saat mana anda meletakkan kursor di dalam sesuatu medan input. Itulah yang memunculkan kapsul terapung — dan hanya dalam aplikasi yang anda sendiri konfigurasikan.
- **Kandungan medan itu hanya dibaca pada saat tepat anda menyentuh kapsul**, untuk ditulis semula lalu digantikan di tempatnya.
- **Medan kata laluan dikecualikan.** Aplikasi mengesan medan berjenis kata laluan (termasuk kod berangka dan medan web) dan enggan membacanya.
- Kebenaran ini **tidak membolehkan sebarang penangkapan imej** skrin anda.
- Plume **tidak pernah menekan apa-apa bagi pihak anda** dalam aplikasi lain: ia menggantikan teks sesuatu medan, tidak lebih daripada itu.

Dua fungsi yang anda hidupkan sendiri — **Bacaan Berbantu dalam mod Teks** dan **terjemahan mesej yang diterima** — membaca teks yang dipaparkan secara berterusan selagi kedua-duanya berjalan, dan berhenti sebaik sahaja anda mematikannya.

Jika anda menolak perkhidmatan kebolehaksesan, Plume masih boleh digunakan: anda boleh memilih sesuatu teks lalu menggunakan menu "Plume" pada menu pemilihan Android, atau berkongsi sesuatu teks kepada Plume.

### 1.2 Tangkapan skrin (Bacaan Berbantu)

Bacaan Berbantu menindih terjemahan di atas teks yang dipaparkan — contohnya gelembung dialog sebuah komik. Ia perlu melihat imej skrin.

- Ia **dimatikan secara lalai** dan hanya berfungsi dalam aplikasi yang anda benarkan secara nyata, satu demi satu.
- **Android meminta persetujuannya sendiri daripada anda pada setiap permulaan sesi.** Ini bukan kebenaran yang diberikan sekali untuk selama-lamanya: setiap sesi menuntut persetujuan baharu. Plume tidak pernah cuba menggunakan semula atau memintas persetujuan ini.
- Sepanjang sesi berlangsung, **satu pemberitahuan kekal dan satu penunjuk sistem sentiasa kelihatan**. Plume tidak boleh menangkap skrin anda secara senyap.
- Sesi **berhenti secara automatik apabila skrin dikunci**, dan serta-merta apabila anda sendiri menghentikannya.
- Aplikasi yang melindungi paparannya (aplikasi perbankan, pengurus kata laluan) **dilindungi oleh Android sendiri** sebelum Plume menerima apa-apa. Ini ialah perlindungan sistem, yang nyata tetapi separa: bukan semua aplikasi sensitif menghidupkannya. Oleh itu kami tidak membentangkannya sebagai jaminan mutlak.
- **Imej yang ditangkap tidak pernah disimpan mahupun dihantar.** Setiap imej dianalisis dalam memori untuk mengeluarkan teksnya, kemudian ditinggalkan. Tiada imej yang keluar daripada telefon anda, tidak pernah, apa jua enjin yang dipilih.

---

## 2. Apa yang kekal pada telefon anda dan apa yang keluar

Inilah pembezaan paling penting dalam dasar ini, dan andalah yang mengawalnya.

### 2.1 Enjin yang tidak mengeluarkan apa-apa

- **Kit tempatan** (pengecaman dan terjemahan teks di luar talian) berfungsi sepenuhnya pada peranti.
- **AI tempatan** ialah sebuah model kecerdasan buatan yang dimuat turun sekali lalu disimpan pada telefon anda (kira-kira 720 MB). Ia dijalankan pada peranti anda.

Dengan kedua-dua enjin ini, **teks yang dibaca atau dirumus semula tidak keluar daripada telefon anda.** Tiada sebarang panggilan rangkaian yang berkaitan dengan kandungan teks anda.

### 2.2 Enjin AI Awan

Apabila anda memilih AI Awan, atau apabila peranti anda tidak cukup berkuasa untuk AI tempatan, teks berkenaan dihantar kepada pelayan kami, kemudian kepada sebuah perkhidmatan kecerdasan buatan pihak ketiga.

**Perjalanan sebenarnya perlu dinyatakan dengan jelas:**

- Teks itu melalui infrastruktur kami (Supabase), yang dihoskan di **Kesatuan Eropah** (wilayah Eropah Tengah, Frankfurt).
- Ia kemudiannya dihantar kepada **openrouter.ai**, sebuah perantara penghalaan yang **terletak di luar Kesatuan Eropah**, yang menyerahkan pemprosesannya kepada model **Mistral Small**.
- **Jadi, ini merupakan pemindahan data ke luar Kesatuan Eropah.** Kami tidak mendakwa sebaliknya, dan kami tidak memaparkan sebarang janji pengehosan Eropah bagi peringkat ini.
- **Plume tidak menyimpan teks anda.** Tiada satu pun fungsi pelayan kami menulis kandungan teks anda: kami hanya merekodkan satu pengecam teknikal permintaan dan pengecam peranti anda, untuk mengira kuota anda dan mengesan penyalahgunaan.
- **Apa yang dilakukan oleh pembekal tersebut di pihak mereka, kami tidak dapat menjaminnya.** Kami lebih suka memberitahu anda daripada menjanjikan penyimpanan sifar yang kami tidak mampu mengesahkannya.

**AI Awan tidak pernah aktif dengan sendirinya.** Satu skrin persetujuan khusus menerangkan perkara-perkara ini kepada anda sebelum penghantaran pertama, dan tiada apa-apa yang keluar selagi anda belum menerimanya. Jika AI tempatan gagal, Plume tidak beralih kepada awan secara senyap: ia memberitahu anda dan menunggu keputusan anda. Anda boleh menarik balik persetujuan ini pada bila-bila masa dalam tetapan.

Teks yang dihantar dihadkan: 1,200 aksara untuk satu rumusan semula, 4,000 aksara untuk satu analisis skrin.

---

## 3. Data yang kami simpan

Kami **tidak menggunakan sebarang alat analitis khalayak, sebarang penjejak pengiklanan pihak ketiga, mahupun sebarang alat laporan ranap**. Aplikasi ini tidak mengandungi SDK pengukuran.

Berikut ialah keseluruhan apa yang disimpan pada pelayan kami:

| Data | Mengapa | Tempoh |
|---|---|---|
| **Pengecam peranti** (satu nombor rawak yang dijana oleh Plume, tanpa kaitan dengan identiti anda mahupun dengan pengecam pengiklanan) | Mengaitkan sesuatu peranti kepada sesuatu akaun, mengenakan kuota, menyekat penyalahgunaan | Sehingga akaun anda dipadam |
| **Alamat e-mel akaun** (jika anda membuka akaun melalui e-mel atau melalui Google) | Mengesahkan anda, mengaitkan langganan anda | Sehingga akaun anda dipadam |
| **Kaunter penggunaan** (bilangan rumusan semula setiap hari dan setiap bulan — nombor, bukan teks) | Mengenakan kuota | Sehingga akaun anda dipadam |
| **Sejarah pembelian** (pengecam transaksi Google Play, tarikh, status langganan) | Memberi anda akses kepada apa yang telah anda bayar, mengurus pembaharuan, mematuhi kewajipan perakaunan kami | Disimpan walaupun selepas akaun dipadam, tetapi **dilepaskan daripada identiti anda** (lihat §6) |
| **Cadangan yang dihantar secara sukarela** (jika anda menulis kepada kami satu cadangan persona daripada aplikasi) | Menambah baik katalog. Cadangan ini tidak pernah diterbitkan. | Sehingga akaun anda dipadam |
| **Isyarat teknikal penyalahgunaan** (pelanggaran had berulang, kegagalan semakan integriti — tanpa sebarang teks) | Keselamatan, pembanterasan penipuan | Dilepaskan daripada identiti anda apabila akaun dipadam |
| **Bahasa dan versi aplikasi** | Menyampaikan kandungan yang betul | Sehingga akaun anda dipadam |

**Apa yang tidak kami kumpul:** nama anda, kenalan anda, lokasi anda, buku alamat anda, gambar anda, kalendar anda, sejarah aplikasi anda. Plume tidak meminta satu pun kebenaran tersebut.

**Apa yang kekal hanya pada telefon anda:** persona tersuai anda dan avatarnya, tetapan anda, peraturan setiap aplikasi anda, cache terjemahan Bacaan Berbantu (dipadam pada penghujung setiap sesi). Tiada satu pun daripada semua itu dihantar kepada pelayan kami.

---

## 4. Pendiktean suara

Satu butang mikrofon membolehkan anda mendikte dan bukannya menaip. Kebenaran akses kepada mikrofon diminta **pada saat tepat anda menekan butang tersebut**, tidak pernah semasa aplikasi dimulakan, dan mikrofon hanya terbuka pada saat itu. Plume tidak pernah mendengar di latar belakang.

**Plume tidak menerima, tidak menyimpan dan tidak menghantar sebarang rakaman audio.** Pendiktean diserahkan kepada enjin pengecaman suara yang terbina dalam telefon anda (enjin Android). Plume hanya mengambil teks yang telah ditranskripsikan.

**Perkara penting dan jujur:** enjin sistem tersebut milik telefon anda, lazimnya milik Google. Bergantung pada peranti anda, tetapannya dan modul bahasa yang dipasang, **ia boleh menghantar audio kepada pelayan penerbitnya** untuk ditranskripsikan. Pemprosesan itu berada di luar kawalan Plume dan tertakluk kepada dasar privasi penerbit sistem anda. Oleh itu kami tidak boleh menegaskan bahawa suara anda kekal pada peranti — perkara itu bergantung pada telefon anda, bukan pada kami.

Jika anda menolak kebenaran mikrofon, kemasukan teks melalui papan kekunci sudah tentu masih tersedia.

---

## 5. Pengiklanan

Perkhidmatan ini percuma dalam had penggunaan tertentu setiap hari. Melebihi had itu, anda **boleh memilih** untuk menonton satu iklan berganjaran bagi membuka penggunaan tambahan. Ia tidak pernah dipaksakan: jika anda tidak menonton iklan, anda cuma mengekalkan apa yang menjadi hak anda.

- Iklan dibekalkan oleh **Google AdMob**.
- Iklan muncul **hanya di dalam aplikasi Plume itu sendiri**, tidak pernah dalam kapsul terapung dan tidak pernah di atas aplikasi lain.
- **Pelanggan berbayar tidak melihat sebarang iklan.**
- Di Kawasan Ekonomi Eropah, di United Kingdom dan di Switzerland, satu borang persetujuan yang dibekalkan oleh sebuah platform yang diperakui oleh Google dipaparkan kepada anda **sebelum iklan pertama**. Selagi pilihan anda belum dikumpulkan, tiada iklan diminta. Jika anda menolak, iklan kekal **tidak diperibadikan** dan **tiada fungsi ditarik balik daripada anda**. Anda boleh mengubah pilihan ini pada bila-bila masa daripada tetapan.
- Untuk mengkreditkan ganjaran anda secara boleh dipercayai, pengecam peranti Plume anda dihantar kepada AdMob. Google juga boleh mengumpul datanya sendiri menurut dasar privasinya.

*Pada tarikh penulisan, penyiaran iklan dimatikan di pihak pelayan. Bahagian ini menerangkan cara ia berfungsi sebaik sahaja ia dihidupkan.*

---

## 6. Langganan dan pembelian

Langganan dan pakej dijual **melalui Google Play**. Kami tidak pernah melihat butiran bank anda: butiran itu diproses oleh Google, yang merupakan penjual dari segi pengebilan.

Kami menerima daripada Google satu bukti pembelian yang disahkan oleh pelayan kami, dan kami menyimpan jejaknya (pengecam transaksi, tarikh, status). Jejak ini disimpan atas sebab perakaunan dan untuk menghalang satu pembelian yang sama digunakan dua kali — tetapi ia **dilepaskan daripada identiti anda** apabila anda memadam akaun anda.

---

## 7. Hak anda

Anda mempunyai hak akses, pembetulan, pemadaman, sekatan, bantahan dan mudah alih data yang diperuntukkan oleh GDPR (Peraturan Perlindungan Data Umum Kesatuan Eropah).

**Yang paling mudah dan paling pantas: pemadaman itu terbina di dalam aplikasi.**
Tetapan → Privasi → Padam data saya. Ia **dilaksanakan serta-merta**, bukan dimasukkan ke dalam baris gilir. Butiran tentang apa yang dipadam dan apa yang disimpan terdapat pada halaman khusus kami: `https://readit0.github.io/plume-legal/suppression-compte`.

Anda juga boleh memadam akaun anda **tanpa memasang aplikasi**, dengan menulis kepada sogacmoi7@gmail.com.

Bagi sebarang permintaan lain, tulislah kepada **sogacmoi7@gmail.com**. Kami menjawab dalam tempoh satu bulan.

**Asas undang-undang:** pelaksanaan kontrak (menyediakan perkhidmatan yang anda minta, mengurus langganan anda), persetujuan anda (perkhidmatan kebolehaksesan, tangkapan skrin, penghantaran kepada AI Awan, pengiklanan yang diperibadikan), kepentingan sah kami (keselamatan, pembanterasan penipuan) dan kewajipan undang-undang kami (perakaunan).

Anda boleh membuat aduan kepada **CNIL** (www.cnil.fr), pihak berkuasa penyeliaan bagi penerbit, atau, **jika anda bermastautin di Kesatuan Eropah**, kepada pihak berkuasa penyeliaan negara tempat anda bermastautin — Perkara 77 GDPR memberi anda pilihan itu.

---

## 8. Kanak-kanak bawah umur

Plume ialah alat bantuan menulis, yang ditujukan kepada khalayak **berumur 16 tahun ke atas**. Kami tidak mengumpul data kanak-kanak bawah 16 tahun dengan sedar dan aplikasi ini tidak direka bentuk mahupun dipromosikan untuk mereka. Jika anda pemegang kuasa ibu bapa dan berpendapat bahawa anak anda telah menghantar data kepada kami, tulislah kepada sogacmoi7@gmail.com: kami akan memadam akaun tersebut.

Oleh sebab aplikasi ini membolehkan perumusan semula teks bebas dan memaparkan iklan, ia tidak layak untuk program Google Play yang ditujukan kepada keluarga.

---

## 9. Pemproses data dan penerima

| Pembekal | Peranan | Di mana |
|---|---|---|
| **Supabase** | Pengehosan pangkalan data, pengesahan, fungsi pelayan | Kesatuan Eropah (Frankfurt) |
| **OpenRouter** | Penghalaan permintaan kepada model AI | **Di luar Kesatuan Eropah** |
| **Mistral AI** (melalui OpenRouter) | Model yang memproses teks (Mistral Small) | Pemprosesan melalui perantara di atas |
| **Google Play / Google Billing** | Pembayaran, langganan | Google Ireland / Amerika Syarikat |
| **Google AdMob** | Pengiklanan berganjaran | Google Ireland / Amerika Syarikat |
| **Google (perkhidmatan sistem telefon)** | Pengecaman suara, modul terjemahan luar talian | Mengikut peranti anda |

**Kami tidak menjual sebarang data dan tidak menyerahkan sebarang data kepada broker data.**

**Pemindahan ke luar Kesatuan Eropah:** penggunaan OpenRouter, Google Play dan AdMob melibatkan pemindahan data ke luar Kesatuan Eropah. Rangka kerja undang-undang bagi pemindahan tersebut (klausa kontrak standard, keputusan kecukupan) **mesti disemak dan didokumentasikan oleh seorang profesional sebelum penerbitan** — lihat nota di penghujung dokumen.

---

## 10. Keselamatan

Pertukaran antara aplikasi dan pelayan kami disulitkan (HTTPS/TLS). Akses kepada data dalam pangkalan data dihadkan oleh peraturan pelayan: fungsi sensitif tidak boleh dicapai daripada aplikasi. Tiada sistem yang sempurna selamat, tetapi tiada satu pun teks yang anda rumus semula disimpan pada kami — yang secara mekanikal menghadkan apa yang boleh didedahkan oleh sesuatu pencerobohan.

---

## 11. Pindaan

Setiap pindaan kepada dasar ini akan diterbitkan di alamat `https://readit0.github.io/plume-legal` dengan tarikh yang baharu. Sekiranya berlaku perubahan penting mengenai peredaran data anda, kami akan memaklumkan anda di dalam aplikasi.

---

## Terma dan syarat am

Terma penggunaan perkhidmatan (kuota, langganan, penamatan) terkandung dalam dokumen berasingan: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Untuk disemak oleh seorang profesional
>
> Dokumen ini ditulis dengan mengukur kelakuan sebenar aplikasi, tetapi **ia tidak ditulis oleh seorang peguam**. Empat perkara yang paling memerlukan nasihat profesional:
>
> 1. **Pemindahan data ke luar Kesatuan Eropah** kepada OpenRouter. Inilah perkara yang paling sensitif: mekanisme pemindahan yang terpakai perlu ditentukan, perlu disahkan bahawa satu perjanjian pemprosesan data wujud dengan pembekal tersebut, dan ia perlu ditulis di sini. Selagi perkara itu belum dilakukan, dokumen ini menerangkan pemindahan tersebut tanpa menegaskan bahawa ia berada dalam rangka kerja yang sewajarnya.
> 2. **Asas undang-undang** yang dipilih dalam §7, khususnya pembahagian antara persetujuan dan kepentingan sah bagi perkhidmatan kebolehaksesan.
> 3. **Umur minimum** (16 tahun) dan keselarasannya dengan soal selidik penilaian kandungan Google Play.
> 4. **Kenyataan berkenaan AI** di bawah peraturan Eropah mengenai kecerdasan buatan (kewajipan ketelusan bagi sistem berisiko terhad).

---

Dokumen ini ialah terjemahan versi bahasa Perancis, yang boleh didapati di alamat https://readit0.github.io/plume-legal/. Ia disediakan untuk makluman anda. Sekiranya terdapat percanggahan, sila hubungi kami di sogacmoi7@gmail.com.
