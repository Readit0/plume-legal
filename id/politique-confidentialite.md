# Kebijakan Privasi Plume

**Terakhir diperbarui: 31 Juli 2026** — Versi 1.0

---

## Siapa yang bertanggung jawab atas data Anda

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Kontak: sogacmoi7@gmail.com

Aplikasi ini diterbitkan di Google Play dengan nama penerbit **openfunworld**.

Kebijakan ini menjelaskan apa yang dilakukan aplikasi Plume dalam versinya saat ini. Kebijakan ini ditulis dengan membaca kode aplikasi, bukan dari sebuah templat umum.

---

## Dalam satu menit

Plume membantu Anda menulis: ia menyusun ulang teks Anda langsung di dalam aplikasi tempat Anda sedang mengetik, dan ia dapat menerjemahkan teks yang tampil di layar.

Tiga hal yang perlu diingat:

1. **Plume tidak menyimpan satu pun teks Anda di servernya.** Baik teks yang Anda susun ulang, maupun teks yang dibaca di layar. Kami tidak menyimpan salinannya, tidak pula catatannya.
2. **Bergantung pada mesin yang Anda pilih, teks Anda keluar atau tidak keluar dari ponsel Anda.** Dua mesin (Kit lokal dan AI lokal) bekerja sepenuhnya di perangkat. Yang ketiga (AI Cloud) mengirimkan teks ke sebuah layanan kecerdasan buatan yang **berada di luar Uni Eropa**. Anda yang memilih, dan AI Cloud tidak pernah aktif tanpa persetujuan tegas dari Anda.
3. **Plume memerlukan izin-izin yang berdaya besar** (membaca konten yang ditampilkan di aplikasi lain, menangkap layar). Di bawah ini kami menjelaskan dengan tepat untuk apa izin itu digunakan dan untuk apa tidak.

---

## 1. Apa yang dibaca Plume di layar Anda, dan kapan

### 1.1 Layanan aksesibilitas

Untuk menulis ulang teks Anda di tempat Anda menulisnya, Plume menggunakan layanan aksesibilitas Android. Ini adalah izin yang Anda aktifkan sendiri, di pengaturan ponsel, setelah layar penjelasan yang ditampilkan Plume **sebelum** izin itu diminta kepada Anda.

Secara konkret:

- **Saat menganggur**, Plume hanya mengetahui aplikasi mana yang sedang terbuka dan pada saat mana Anda menempatkan kursor di sebuah kolom isian. Itulah yang memunculkan kapsul mengambang — dan hanya di aplikasi yang Anda sendiri konfigurasikan.
- **Isi kolom hanya dibaca pada saat persis Anda menyentuh kapsul**, untuk ditulis ulang lalu digantikan di tempatnya.
- **Kolom kata sandi dikecualikan.** Aplikasi mendeteksi kolom bertipe kata sandi (termasuk kode angka dan kolom web) dan menolak membacanya.
- Izin ini **tidak memungkinkan pengambilan gambar apa pun** dari layar Anda.
- Plume **tidak pernah menekan apa pun menggantikan Anda** di aplikasi lain: ia mengganti teks sebuah kolom, tidak lebih dari itu.

Dua fungsi yang Anda aktifkan sendiri — **Bacaan Terbantu dalam mode Teks** dan **penerjemahan pesan yang diterima** — membaca teks yang ditampilkan secara terus-menerus selama keduanya berjalan, dan berhenti begitu Anda mematikannya.

Jika Anda menolak layanan aksesibilitas, Plume tetap dapat digunakan: Anda dapat memilih sebuah teks lalu melewati menu "Plume" pada menu seleksi Android, atau membagikan sebuah teks ke Plume.

### 1.2 Tangkapan layar (Bacaan Terbantu)

Bacaan Terbantu menampilkan terjemahan di atas teks yang tampil — misalnya balon percakapan sebuah komik. Fungsi ini perlu melihat gambar layar.

- Fungsi ini **nonaktif secara bawaan** dan hanya bekerja di aplikasi yang Anda izinkan secara eksplisit, satu per satu.
- **Android meminta persetujuannya sendiri kepada Anda setiap kali sesi dimulai.** Ini bukan izin yang diberikan sekali untuk selamanya: setiap sesi menuntut persetujuan baru. Plume tidak pernah berusaha menggunakan ulang atau menyiasati persetujuan ini.
- Selama sesi berlangsung, **sebuah notifikasi permanen dan sebuah indikator sistem tetap terlihat**. Plume tidak dapat menangkap layar Anda secara diam-diam.
- Sesi **berhenti otomatis saat layar terkunci**, dan seketika saat Anda sendiri menghentikannya.
- Aplikasi yang melindungi tampilannya (aplikasi perbankan, pengelola kata sandi) **ditutupi oleh Android sendiri** sebelum Plume menerima apa pun. Ini adalah perlindungan sistem, yang nyata tetapi sebagian: tidak semua aplikasi sensitif mengaktifkannya. Karena itu kami tidak menyajikannya sebagai jaminan mutlak.
- **Gambar yang ditangkap tidak pernah disimpan maupun dikirim.** Setiap gambar dianalisis di memori untuk mengambil teksnya, lalu ditinggalkan. Tidak ada gambar yang keluar dari ponsel Anda, tidak pernah, apa pun mesin yang dipilih.

---

## 2. Apa yang tetap di ponsel Anda dan apa yang keluar

Inilah pembedaan terpenting dalam kebijakan ini, dan Andalah yang mengendalikannya.

### 2.1 Mesin yang tidak mengeluarkan apa pun

- **Kit lokal** (pengenalan dan penerjemahan teks secara luring) bekerja sepenuhnya di perangkat.
- **AI lokal** adalah sebuah model kecerdasan buatan yang diunduh satu kali lalu disimpan di ponsel Anda (sekitar 720 MB). Model itu dijalankan di perangkat Anda.

Dengan kedua mesin ini, **teks yang dibaca atau disusun ulang tidak keluar dari ponsel Anda.** Tidak ada panggilan jaringan apa pun yang berkaitan dengan isi teks Anda.

### 2.2 Mesin AI Cloud

Ketika Anda memilih AI Cloud, atau ketika perangkat Anda tidak cukup bertenaga untuk AI lokal, teks yang bersangkutan dikirimkan ke server kami, lalu ke sebuah layanan kecerdasan buatan pihak ketiga.

**Perjalanan yang sebenarnya harus dijelaskan dengan terus terang:**

- Teks melewati infrastruktur kami (Supabase), yang dihosting di **Uni Eropa** (wilayah Eropa Tengah, Frankfurt).
- Teks kemudian dikirimkan ke **openrouter.ai**, sebuah perantara perutean yang **berada di luar Uni Eropa**, yang menyerahkan pemrosesannya kepada model **Mistral Small**.
- **Jadi, ini merupakan transfer data ke luar Uni Eropa.** Kami tidak menyatakan sebaliknya, dan kami tidak menampilkan janji hosting Eropa apa pun untuk tahap ini.
- **Plume tidak menyimpan teks Anda.** Tidak satu pun fungsi server kami menuliskan isi teks Anda: kami hanya mencatat sebuah identitas teknis permintaan dan identitas perangkat Anda, untuk menghitung kuota Anda dan mendeteksi penyalahgunaan.
- **Apa yang dilakukan para penyedia itu di pihak mereka, tidak dapat kami jamin.** Kami lebih memilih mengatakannya kepada Anda daripada menjanjikan penyimpanan nol yang tidak mampu kami verifikasi.

**AI Cloud tidak pernah aktif dengan sendirinya.** Sebuah layar persetujuan khusus menjelaskan hal-hal ini kepada Anda sebelum pengiriman pertama, dan tidak ada yang keluar selama Anda belum menerimanya. Jika AI lokal gagal, Plume tidak beralih ke cloud secara diam-diam: ia memberi tahu Anda dan menunggu keputusan Anda. Anda dapat menarik persetujuan ini kapan saja di pengaturan.

Teks yang dikirim dibatasi: 1.200 karakter untuk satu penyusunan ulang, 4.000 karakter untuk satu analisis layar.

---

## 3. Data yang kami simpan

Kami tidak menggunakan **alat analitik audiens apa pun, pelacak iklan pihak ketiga apa pun, maupun alat pelaporan kerusakan apa pun**. Aplikasi tidak memuat SDK pengukuran.

Berikut keseluruhan yang disimpan di server kami:

| Data | Untuk apa | Jangka waktu |
|---|---|---|
| **Identitas perangkat** (sebuah nomor acak yang dibuat oleh Plume, tanpa kaitan dengan identitas Anda maupun dengan sebuah identitas periklanan) | Menautkan sebuah perangkat ke sebuah akun, menerapkan kuota, memblokir penyalahgunaan | Sampai akun Anda dihapus |
| **Alamat e-mail akun** (jika Anda membuat akun melalui e-mail atau melalui Google) | Mengautentikasi Anda, menautkan langganan Anda | Sampai akun Anda dihapus |
| **Penghitung penggunaan** (jumlah penyusunan ulang per hari dan per bulan — angka, bukan teks) | Menerapkan kuota | Sampai akun Anda dihapus |
| **Riwayat pembelian** (identitas transaksi Google Play, tanggal, status langganan) | Memberi Anda akses ke apa yang telah Anda bayar, mengelola perpanjangan, memenuhi kewajiban akuntansi kami | Disimpan bahkan setelah akun dihapus, tetapi **dilepaskan dari identitas Anda** (lihat §6) |
| **Saran yang dikirim secara sukarela** (jika Anda menulis kepada kami sebuah usulan persona dari dalam aplikasi) | Menyempurnakan katalog. Saran-saran ini tidak pernah dipublikasikan. | Sampai akun Anda dihapus |
| **Sinyal teknis penyalahgunaan** (pelampauan berulang, kegagalan pemeriksaan integritas — tanpa teks apa pun) | Keamanan, pemberantasan kecurangan | Dilepaskan dari identitas Anda saat akun dihapus |
| **Bahasa dan versi aplikasi** | Menyajikan konten yang tepat | Sampai akun Anda dihapus |

**Apa yang tidak kami kumpulkan:** nama Anda, kontak Anda, lokasi Anda, buku alamat Anda, foto Anda, kalender Anda, riwayat aplikasi Anda. Plume tidak meminta satu pun izin tersebut.

**Apa yang tetap hanya di ponsel Anda:** persona kustom Anda beserta avatarnya, pengaturan Anda, aturan per aplikasi Anda, cache terjemahan Bacaan Terbantu (dihapus pada akhir setiap sesi). Tidak satu pun dari semua itu dikirim ke server kami.

---

## 4. Dikte suara

Sebuah tombol mikrofon memungkinkan Anda mendikte alih-alih mengetik. Izin akses mikrofon diminta **tepat pada saat Anda menekan tombol tersebut**, tidak pernah saat aplikasi dijalankan, dan mikrofon baru terbuka pada saat itu. Plume tidak pernah mendengarkan di latar belakang.

**Plume tidak menerima, tidak menyimpan, dan tidak mengirimkan rekaman audio apa pun.** Dikte diserahkan kepada mesin pengenalan suara yang terpasang di ponsel Anda (mesin milik Android). Plume hanya mengambil teks hasil transkripsi.

**Poin penting dan jujur:** mesin sistem tersebut milik ponsel Anda, umumnya milik Google. Bergantung pada perangkat Anda, pengaturannya, dan modul bahasa yang terpasang, **mesin itu dapat mengirimkan audio ke server penerbitnya** untuk ditranskripsikan. Pemrosesan tersebut berada di luar kendali Plume dan tunduk pada kebijakan privasi penerbit sistem Anda. Karena itu kami tidak dapat menyatakan bahwa suara Anda tetap berada di perangkat — hal itu bergantung pada ponsel Anda, bukan pada kami.

Jika Anda menolak izin mikrofon, pengetikan melalui papan ketik tentu saja tetap tersedia.

---

## 5. Periklanan

Layanan ini gratis dalam batas penggunaan tertentu per hari. Di luar batas itu, Anda **dapat memilih** untuk menonton sebuah iklan berhadiah guna membuka penggunaan tambahan. Hal itu tidak pernah dipaksakan: jika Anda tidak menonton iklan, Anda tetap memperoleh apa yang menjadi hak Anda.

- Iklan disediakan oleh **Google AdMob**.
- Iklan hanya muncul **di dalam aplikasi Plume itu sendiri**, tidak pernah di kapsul mengambang dan tidak pernah di atas aplikasi lain.
- **Pelanggan berbayar tidak melihat iklan apa pun.**
- Di Wilayah Ekonomi Eropa, di Britania Raya, dan di Swiss, sebuah formulir persetujuan yang disediakan oleh platform bersertifikasi Google ditampilkan kepada Anda **sebelum iklan pertama**. Selama pilihan Anda belum dikumpulkan, tidak ada iklan yang diminta. Jika Anda menolak, iklan tetap **tidak dipersonalisasi** dan **tidak ada fungsi yang dicabut dari Anda**. Anda dapat mengubah pilihan ini kapan saja dari pengaturan.
- Untuk mengkreditkan hadiah Anda secara andal, identitas perangkat Plume Anda dikirimkan ke AdMob. Google juga dapat mengumpulkan datanya sendiri sesuai dengan kebijakan privasinya.

*Pada tanggal penulisan, penayangan iklan dinonaktifkan di sisi server. Bagian ini menjelaskan cara kerjanya begitu penayangan itu diaktifkan.*

---

## 6. Langganan dan pembelian

Langganan dan paket dijual **melalui Google Play**. Kami tidak pernah melihat data kartu pembayaran Anda: data itu diproses oleh Google, yang merupakan penjual dalam arti penagihan.

Kami menerima dari Google sebuah bukti pembelian yang diverifikasi oleh server kami, dan kami menyimpan jejaknya (identitas transaksi, tanggal, status). Jejak ini disimpan untuk alasan akuntansi dan untuk mencegah satu pembelian yang sama dipakai dua kali — tetapi jejak itu **dilepaskan dari identitas Anda** ketika Anda menghapus akun Anda.

---

## 7. Hak-hak Anda

Anda memiliki hak akses, pembetulan, penghapusan, pembatasan, keberatan, dan portabilitas yang diatur oleh GDPR (Peraturan Perlindungan Data Umum Uni Eropa).

**Yang paling sederhana dan paling cepat: penghapusan sudah terpasang di dalam aplikasi.**
Pengaturan → Privasi → Hapus data saya. Penghapusan itu **dijalankan seketika**, bukan dimasukkan ke antrean. Rincian tentang apa yang dihapus dan apa yang disimpan terdapat di halaman khusus kami: `https://readit0.github.io/plume-legal/suppression-compte`.

Anda juga dapat menghapus akun Anda **tanpa memasang aplikasi**, dengan menulis ke sogacmoi7@gmail.com.

Untuk permintaan lainnya, tulislah ke **sogacmoi7@gmail.com**. Kami menjawab dalam waktu satu bulan.

**Dasar hukum:** pelaksanaan kontrak (menyediakan layanan yang Anda minta, mengelola langganan Anda), persetujuan Anda (layanan aksesibilitas, tangkapan layar, pengiriman ke AI Cloud, iklan yang dipersonalisasi), kepentingan sah kami (keamanan, pemberantasan kecurangan), dan kewajiban hukum kami (akuntansi).

Anda dapat mengajukan pengaduan kepada **CNIL** (www.cnil.fr), otoritas pengawas penerbit, atau, **jika Anda tinggal di Uni Eropa**, kepada otoritas pengawas negara tempat tinggal Anda — Pasal 77 GDPR memberi Anda pilihan itu.

---

## 8. Anak di bawah umur

Plume adalah alat bantu menulis, yang ditujukan untuk khalayak **berusia 16 tahun ke atas**. Kami tidak dengan sengaja mengumpulkan data anak di bawah 16 tahun dan aplikasi ini tidak dirancang maupun dipromosikan untuk mereka. Jika Anda pemegang kuasa asuh dan menduga anak Anda telah menyampaikan data kepada kami, tulislah ke sogacmoi7@gmail.com: kami akan menghapus akun tersebut.

Karena aplikasi ini memungkinkan penyusunan ulang teks bebas dan menampilkan iklan, aplikasi ini tidak memenuhi syarat untuk program Google Play yang ditujukan bagi keluarga.

---

## 9. Prosesor data dan penerima

| Penyedia | Peran | Di mana |
|---|---|---|
| **Supabase** | Hosting basis data, autentikasi, fungsi server | Uni Eropa (Frankfurt) |
| **OpenRouter** | Perutean permintaan menuju model AI | **Di luar Uni Eropa** |
| **Mistral AI** (melalui OpenRouter) | Model yang memproses teks (Mistral Small) | Pemrosesan melalui perantara di atas |
| **Google Play / Google Billing** | Pembayaran, langganan | Google Ireland / Amerika Serikat |
| **Google AdMob** | Iklan berhadiah | Google Ireland / Amerika Serikat |
| **Google (layanan sistem ponsel)** | Pengenalan suara, modul terjemahan luring | Sesuai perangkat Anda |

**Kami tidak menjual data apa pun dan tidak menyerahkan data apa pun kepada pialang data.**

**Transfer ke luar Uni Eropa:** penggunaan OpenRouter, Google Play, dan AdMob menimbulkan transfer data ke luar Uni Eropa. Kerangka hukum transfer tersebut (klausul kontraktual standar, keputusan kecukupan) **harus diverifikasi dan didokumentasikan oleh seorang profesional sebelum publikasi** — lihat catatan di akhir dokumen.

---

## 10. Keamanan

Pertukaran antara aplikasi dan server kami dienkripsi (HTTPS/TLS). Akses ke data di basis data dibatasi oleh aturan server: fungsi-fungsi sensitif tidak dapat dijangkau dari aplikasi. Tidak ada sistem yang sepenuhnya aman, tetapi tidak satu pun teks yang Anda susun ulang disimpan pada kami — sehingga secara mekanis hal itu membatasi apa yang dapat diungkap oleh sebuah pembobolan.

---

## 11. Perubahan

Setiap perubahan kebijakan ini akan dipublikasikan di alamat `https://readit0.github.io/plume-legal` dengan tanggal yang baru. Jika terjadi perubahan penting mengenai peredaran data Anda, kami akan memberi tahu Anda di dalam aplikasi.

---

## Syarat dan ketentuan umum

Syarat penggunaan layanan (kuota, langganan, pengakhiran) terdapat dalam dokumen terpisah: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Untuk ditinjau oleh seorang profesional
>
> Dokumen ini ditulis dengan mengukur perilaku nyata aplikasi, tetapi **tidak ditulis oleh seorang ahli hukum**. Empat hal yang paling memerlukan pendapat profesional:
>
> 1. **Transfer data ke luar Uni Eropa** menuju OpenRouter. Inilah titik yang paling sensitif: perlu ditetapkan mekanisme transfer yang berlaku, diverifikasi bahwa terdapat perjanjian pemrosesan data dengan penyedia tersebut, dan hal itu dituliskan di sini. Selama hal itu belum dilakukan, dokumen ini menjelaskan transfer tersebut tanpa menyatakan bahwa transfer itu telah diberi kerangka hukum.
> 2. **Dasar hukum** yang dipilih pada §7, khususnya pembagian antara persetujuan dan kepentingan sah untuk layanan aksesibilitas.
> 3. **Usia minimum** (16 tahun) dan kesesuaiannya dengan kuesioner klasifikasi konten Google Play.
> 4. **Pernyataan mengenai AI** berdasarkan peraturan Eropa tentang kecerdasan buatan (kewajiban transparansi untuk sistem berisiko terbatas).

---

Dokumen ini adalah terjemahan dari versi bahasa Prancis, yang tersedia di alamat https://readit0.github.io/plume-legal/. Terjemahan ini disediakan untuk informasi Anda. Jika terdapat perbedaan, hubungi kami di sogacmoi7@gmail.com.
