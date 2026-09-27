# Kumpulan Prompt Siap Pakai — Generate Halaman Website MVP WORMI

Dokumen ini berisi 8 prompt, satu untuk tiap halaman di sitemap PRD. Setiap prompt disusun dengan struktur: **Role → Context → Task → Requirements (must/should) → Constraints → Negative Examples → Output Format**, mengikuti praktik *prompt engineering* yang direkomendasikan (instruksi jelas & spesifik, contoh positif/negatif, format output eksplisit).

## Cara Pakai
1. Salin **Prompt 0 (Konteks Global)** terlebih dahulu ke setiap sesi baru sebelum meminta AI membuat halaman — ini menjaga konsistensi desain/brand di semua halaman.
2. Setelah itu, tempel salah satu **Prompt 1–8** sesuai halaman yang ingin dibuat.
3. Isi bagian bertanda `[...]` (mis. `[NOMOR_WA]`, `[INSTAGRAM_HANDLE]`) sebelum mengirim prompt.
4. Ulangi untuk tiap halaman di sesi/percakapan yang **terpisah atau baru**, tetap sertakan Prompt 0 di awal agar gaya visual antar halaman tidak melenceng.

---

## Prompt 0 — Konteks Global & Design System (wajib disertakan di setiap sesi)

```
Kamu adalah frontend developer yang membangun website MVP untuk "WORMI" — brand komposter dapur mini berkarakter cacing (worm) yang menyasar mahasiswa/anak kos, penghuni apartemen, dan rumah dengan lahan terbatas di Indonesia.

## Brand & Design Tokens (WAJIB konsisten di semua halaman)
- Warna utama:
  - Terracotta/Peach `#D98B6B` — badan karakter, aksen utama
  - Hijau tua `#2F4A3D` — header section, tombol CTA utama
  - Krem `#F7F1E5` — background halaman
  - Coklat tua `#4A3728` — elemen dasar produk (keran, wadah bawah)
- Palet warna kustomisasi produk (dipakai di fitur pilih warna layer): "Terracotta Klasik", "Hijau Lumut", "Krem Tanah", "Abu Arang"
- Tipografi: judul pakai font rounded/playful (mis. Poppins/Quicksand, weight bold), body pakai font sans-serif reguler (mis. Inter/Nunito), impor dari Google Fonts
- Gaya ilustrasi: karakter bulat menyerupai cacing dengan mata besar & senyum ramah, gaya kawaii/playful — bukan realistis
- Nada komunikasi (copywriting): ramah, ringan, playful tapi tetap kredibel, sasaran pembaca adalah mahasiswa/anak kos peduli lingkungan
- Layout: mobile-first, responsif penuh, section dengan padding lega, rounded corners besar (rounded-2xl/rounded-3xl), shadow lembut, banyak white space

## Batasan Teknis (WAJIB)
- Output berupa 1 file HTML5 mandiri (self-contained) per halaman, memakai Tailwind CSS via CDN (`<script src="https://cdn.tailwindcss.com"></script>`)
- JavaScript vanilla (tanpa framework/library eksternal selain Tailwind), taruh di dalam `<script>` pada file yang sama
- Jika halaman butuh menyimpan data sementara (mis. isi keranjang), gunakan `localStorage`, JANGAN gunakan session/cookie server-side karena tidak ada backend
- Navigasi antar halaman memakai tag `<a href="nama-file.html">` dengan nama file: `index.html`, `produk.html`, `cara-pakai.html`, `blog.html`, `testimoni.html`, `keranjang.html`, `eco-events.html`, `faq.html`
- Navbar dan footer HARUS identik strukturnya di semua halaman (logo/nama brand di kiri, menu di tengah/kanan, ikon keranjang dengan badge jumlah item di navbar, footer berisi tautan sosial & copyright)
- Semua gambar produk memakai placeholder `<img src="https://placehold.co/LEBARxTINGGI/D98B6B/FFFFFF?text=NAMA_GAMBAR">` dengan `alt` yang deskriptif, karena aset asli akan disisipkan manual nanti
- Sertakan meta viewport untuk mobile: `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

## Yang HARUS Dihindari
- Jangan pakai framework JS (React/Vue) kecuali diminta eksplisit di prompt halaman
- Jangan pakai lorem ipsum — semua copy harus relevan dengan konten WORMI (gunakan konten dari brief yang diberikan di tiap prompt halaman)
- Jangan membuat klaim data/testimoni sebagai fakta pasti jika prompt halaman menyebutnya sebagai data pilot/proyeksi — beri label eksplisit sesuai instruksi
- Jangan gunakan warna di luar palet yang ditentukan di atas

Konfirmasi bahwa kamu memahami konteks ini, lalu tunggu instruksi halaman spesifik berikutnya.
```

---

## Prompt 1 — Halaman Beranda (`index.html`)

```
<role>
Kamu adalah frontend developer yang menyusun landing page utama untuk website WORMI, mengikuti design system & batasan teknis yang sudah diberikan sebelumnya (Prompt 0).
</role>

<context>
WORMI adalah komposter dapur mini berkarakter cacing untuk kos/apartemen. Halaman ini adalah pintu masuk utama pengunjung — termasuk juri lomba business plan — sehingga harus langsung menjelaskan masalah, solusi, dan mengarahkan ke halaman produk.
</context>

<task>
Buat halaman `index.html` yang lengkap dan siap tampil, terdiri dari section-section berikut secara berurutan.
</task>

<must_include_content>
1. **Navbar**: logo teks "WORMI" + menu (Beranda, Produk, Cara Pakai, Blog, Testimoni, Eco Events, FAQ) + ikon keranjang dengan badge.
2. **Hero Section**:
   - Tagline besar: "Kecil di ukuran, besar manfaatnya!"
   - Sub-headline singkat: komposter dapur mini berkarakter cacing untuk mengolah sisa sayur & buah jadi kompos, cocok untuk kos, apartemen, dan rumah minimalis
   - Tombol CTA utama: "Pesan Sekarang" (link ke produk.html) dan CTA sekunder: "Lihat Cara Kerja" (link ke cara-pakai.html)
   - Gambar produk (placeholder)
3. **Section Masalah → Solusi → Kekuatan** (format 3 kartu berdampingan):
   - Masalah: "Sampah organik menyumbang porsi terbesar sampah rumah tangga, tapi orang kota tidak punya lahan untuk mengolahnya"
   - Solusi: "WORMI hadir dengan desain kos-friendly yang ringkas, praktis, dan bebas bau, sehingga siapa pun bisa mengolah sampah organik di ruang terbatas"
   - Kekuatan: "Bisa diuji langsung dan hasilnya (kompos) nyata; desain kos-friendly WORMI jadi pembeda dari komposter lain di pasaran"
4. **Preview Fitur Utama** (grid 5 kartu ikon, ambil dari daftar berikut, masing-masing dengan ikon SVG sederhana):
   - Desain bertingkat — kapasitas optimal dalam ukuran mini
   - Ventilasi udara — menjaga proses pengomposan tetap sehat & bebas bau
   - Keran penampung lindi — air lindi tertampung rapi, tidak mengotori area
   - Desain karakter cacing — lucu, cocok untuk kos & rumah
   - Ukuran compact — hemat tempat, mudah disimpan di dapur/balkon
   - Sertakan tombol "Lihat Semua Fitur" mengarah ke produk.html
5. **Preview Cara Pakai** (5 langkah bernomor, ringkas, dengan link "Lihat Panduan Lengkap" ke cara-pakai.html):
   1. Masukkan sisa sayur & buah
   2. Tutup kembali dan biarkan proses berjalan
   3. Ambil air lindi secara berkala (jika ada)
   4. Setelah beberapa minggu, kompos siap digunakan
   5. Gunakan untuk tanaman kesayangan kamu
6. **Social Proof ringkas**: 2–3 angka traksi (mis. jumlah pre-order, jumlah early adopter) dengan keterangan kecil "*data pilot/proyeksi tahap awal" di bawahnya, plus tombol "Lihat Testimoni Lengkap" ke testimoni.html
7. **CTA Section penutup**: ajakan pesan sekarang / gabung Eco Events berikutnya, dengan dua tombol
8. **Footer**: kontak WhatsApp `[NOMOR_WA]`, Instagram `[INSTAGRAM_HANDLE]`, email `[EMAIL]`, tautan cepat ke semua halaman, copyright "© 2026 WORMI Eco Solutions"
</must_include_content>

<constraints>
- Halaman harus terasa ringan dibuka (hindari gambar besar berlebihan, cukup 3–4 placeholder gambar)
- Urutan section tidak boleh diubah karena mengikuti alur storytelling masalah→solusi→bukti→ajakan
</constraints>

<negative_example>
JANGAN membuat hero section generik seperti "Welcome to Our Website" — headline harus persis memakai tagline yang diberikan di atas.
</negative_example>

<output_format>
Satu file HTML lengkap (`<!DOCTYPE html>` sampai `</html>`), siap disimpan sebagai `index.html`.
</output_format>
```

---

## Prompt 2 — Halaman Produk & Fitur, dengan Kustomisasi Warna + Keranjang (`produk.html`)

```
<role>
Kamu adalah frontend developer yang menyusun halaman detail produk WORMI, termasuk fitur interaktif kustomisasi warna dan tambah ke keranjang.
</role>

<context>
Ini adalah halaman paling fungsional di MVP: pengunjung melihat detail produk, memilih warna untuk tiap tingkat (layer) komposter dari palet kurasi (BUKAN color picker bebas, agar konsisten dengan identitas brand), lalu menambahkan konfigurasi tersebut ke keranjang belanja yang disimpan di localStorage.
</context>

<task>
Buat halaman `produk.html` lengkap dengan bagian informasi produk DAN widget konfigurator interaktif yang berfungsi (bukan sekadar tampilan statis).
</task>

<must_include_content>
1. **Navbar & Footer**: identik dengan halaman lain (lihat Prompt 0).
2. **Galeri Produk**: 1 gambar utama besar (placeholder) + 3–4 thumbnail kecil di bawahnya.
3. **Detail 5 Fitur Utama**: sama seperti daftar di Prompt 1, tapi masing-masing dengan deskripsi 1–2 kalimat lebih lengkap.
4. **Diagram "Tampak Dalam"**: tampilkan sebagai daftar bertingkat dari atas ke bawah (boleh pakai ilustrasi stacked-box sederhana dengan CSS, tidak perlu SVG rumit):
   Tutup + ventilasi → Ruang kompos (bertingkat) → Saringan → Penampung lindi → Keran lindi
5. **Spesifikasi Produk** (tabel 2 kolom): Ukuran, Bahan, Kapasitas, Berat — isi dengan placeholder teks `[ISI_SPESIFIKASI]` yang jelas ditandai perlu diisi tim.
6. **Konfigurator Warna Interaktif (WAJIB BERFUNGSI)**:
   - Tampilkan 4 slot: "Layer 1", "Layer 2", "Layer 3", "Layer 4"
   - Untuk tiap slot, tampilkan 4 swatch warna bulat yang bisa diklik: Terracotta Klasik (#D98B6B), Hijau Lumut (#6B7A4F), Krem Tanah (#E8DCC8), Abu Arang (#4A4A48)
   - Saat swatch diklik, area preview produk (gunakan 4 `<div>` persegi panjang bertumpuk merepresentasikan layer) berubah warna sesuai pilihan secara real-time menggunakan JavaScript
   - Simpan pilihan warna tiap layer di variabel JS
7. **Kontrol Jumlah**: input number dengan tombol +/- , default 1, minimal 1
8. **Tombol "Tambah ke Keranjang" (WAJIB BERFUNGSI)**:
   - Saat diklik, buat object `{id: timestamp, colors: {layer1, layer2, layer3, layer4}, qty, price: [HARGA_SATUAN]}`
   - Ambil array existing dari `localStorage.getItem('wormi_cart')` (default `[]` jika belum ada), push object baru, simpan kembali dengan `localStorage.setItem`
   - Update angka badge keranjang di navbar
   - Tampilkan notifikasi kecil "Ditambahkan ke keranjang!" (toast sederhana, hilang otomatis setelah 2 detik)
9. **Cocok Untuk**: 3 ikon singkat — Rumah minimalis, Apartemen & kos, Siapa saja yang peduli lingkungan
</must_include_content>

<constraints>
- Warna yang bisa dipilih HANYA 4 warna di atas — jangan buat color picker bebas/hex input, ini keputusan desain yang disengaja untuk menjaga konsistensi brand
- Logika keranjang harus benar-benar jalan di JavaScript, bukan placeholder kosong
</constraints>

<negative_example>
JANGAN membuat tombol "Tambah ke Keranjang" yang hanya `alert("berhasil")` tanpa benar-benar menyimpan data ke localStorage — data harus persisten agar bisa dibaca halaman keranjang.html.
</negative_example>

<output_format>
Satu file HTML lengkap termasuk `<script>` dengan seluruh logika di atas, siap disimpan sebagai `produk.html`.
</output_format>
```

---

## Prompt 3 — Halaman Cara Kerja / Panduan Penggunaan (`cara-pakai.html`)

```
<role>
Kamu adalah frontend developer yang menyusun halaman panduan penggunaan produk WORMI.
</role>

<context>
Halaman ini murni edukatif: menjelaskan langkah pakai produk secara detail dan mengurangi pertanyaan berulang soal perawatan.
</context>

<task>
Buat halaman `cara-pakai.html` dengan struktur berikut.
</task>

<must_include_content>
1. **Navbar & Footer** standar.
2. **Judul halaman**: "Cara Menggunakan WORMI" + sub-judul singkat.
3. **5 Langkah Utama**, tampilkan sebagai stepper vertikal (nomor besar + ilustrasi placeholder + deskripsi 2–3 kalimat tiap langkah, LEBIH DETAIL dari versi ringkas di beranda):
   1. Masukkan sisa sayur & buah — jelaskan jenis sampah organik yang cocok/tidak cocok (mis. hindari daging, minyak, tulang)
   2. Tutup kembali dan biarkan proses berjalan — jelaskan pentingnya ventilasi tetap terbuka sedikit
   3. Ambil air lindi secara berkala — jelaskan fungsi air lindi sebagai pupuk cair dan cara penggunaannya (diencerkan sebelum disiram ke tanaman)
   4. Setelah beberapa minggu, kompos siap digunakan — beri estimasi rentang waktu `[X-Y minggu]` dan ciri kompos yang sudah matang
   5. Gunakan untuk tanaman kesayangan kamu — beri contoh takaran sederhana
4. **Section Tips Perawatan & Troubleshooting** (format accordion/FAQ mini, minimal 4 poin):
   - Bau tidak sedap → penyebab & solusi
   - Muncul belatung/lalat kecil → penyebab & solusi
   - Kompos terlalu basah/becek → penyebab & solusi
   - Proses terlalu lambat → penyebab & solusi
5. **CTA penutup**: "Sudah paham cara kerjanya? Yuk pesan WORMI sekarang" dengan tombol ke produk.html
</must_include_content>

<constraints>
- Bahasa harus praktis dan mudah diikuti pemula yang belum pernah kompos sama sekali (asumsikan pembaca awam total)
</constraints>

<negative_example>
JANGAN menuliskan tips troubleshooting secara terlalu teknis/ilmiah (mis. istilah C/N ratio tanpa penjelasan awam) — jelaskan dengan bahasa sehari-hari.
</negative_example>

<output_format>
Satu file HTML lengkap, siap disimpan sebagai `cara-pakai.html`.
</output_format>
```

---

## Prompt 4 — Halaman Edukasi & Blog (`blog.html`)

```
<role>
Kamu adalah frontend developer sekaligus content writer yang menyusun halaman blog edukasi WORMI.
</role>

<context>
Halaman ini bertujuan membangun kredibilitas dan SEO, sekaligus mengurangi pertanyaan berulang seputar sampah organik dan kompos.
</context>

<task>
Buat halaman `blog.html` berisi daftar artikel dalam format single-page (semua konten artikel ditampilkan langsung di halaman ini via anchor/section, TIDAK perlu file terpisah per artikel untuk tahap MVP).
</task>

<must_include_content>
1. **Navbar & Footer** standar.
2. **Judul halaman**: "Edukasi Seputar Sampah Organik & Kompos"
3. **3 Artikel**, masing-masing sebagai card ringkas di bagian atas (judul, thumbnail placeholder, ringkasan 1 kalimat, link "Baca Selengkapnya" yang scroll ke section artikel lengkap di bawah):
   - Artikel 1: "Kenapa Sampah Organik Jadi Masalah Besar di Kota?" — bahas data bahwa sampah rumah tangga adalah penyumbang terbesar sampah nasional dan sisa makanan mendominasi, dampaknya jika tidak diolah (gas metana, air lindi mencemari tanah)
   - Artikel 2: "5 Manfaat Kompos untuk Tanaman & Lingkungan" — bahas manfaat kompos padat untuk kesuburan tanah, mengurangi sampah ke TPA, hemat biaya pupuk
   - Artikel 3: "Cara Pakai Pupuk Cair (Air Lindi) yang Benar" — bahas cara dilusi/pengenceran air lindi, frekuensi penyiraman, tanaman yang cocok
4. **Isi lengkap tiap artikel** (300–400 kata per artikel) di section terpisah di bawah daftar card, masing-masing dengan anchor id yang sesuai
5. **CTA di akhir tiap artikel**: ajakan mencoba WORMI, link ke produk.html
</must_include_content>

<constraints>
- Tulisan harus orisinal (bukan hasil salin-tempel dari sumber lain), gaya santai tapi informatif, sesuai nada brand
- Setiap artikel harus scannable: gunakan sub-heading dan bullet point, jangan paragraf panjang tanpa jeda
</constraints>

<negative_example>
JANGAN menulis artikel dalam satu paragraf panjang tanpa struktur — pembaca web menyukai konten yang mudah dipindai (scannable).
</negative_example>

<output_format>
Satu file HTML lengkap, siap disimpan sebagai `blog.html`.
</output_format>
```

---

## Prompt 5 — Halaman Testimoni & Traction (`testimoni.html`)

```
<role>
Kamu adalah frontend developer yang menyusun halaman bukti sosial (social proof) dan data traksi WORMI.
</role>

<context>
Halaman ini akan dilihat juri lomba business plan, sehingga KEJUJURAN data sangat penting. Karena produk belum diproduksi massal, sebagian data adalah proyeksi, bukan data aktual — ini HARUS diberi label jelas, jangan disamarkan seolah data nyata.
</context>

<task>
Buat halaman `testimoni.html` dengan dua bagian yang dipisah jelas: data yang sudah nyata (dari pilot) dan data yang masih proyeksi.
</task>

<must_include_content>
1. **Navbar & Footer** standar.
2. **Judul halaman**: "Apa Kata Pengguna Awal Kami" + sub-judul.
3. **Section Testimoni** (grid 3 kartu): tiap kartu berisi placeholder foto bulat, nama `[NAMA_PENGGUNA]`, status `[mis. Mahasiswa Kos Bojongsoang]`, dan kutipan testimoni placeholder `[KUTIPAN_TESTIMONI]` — beri komentar HTML `<!-- Ganti dengan testimoni asli dari hasil pilot -->` di atas section ini.
4. **Section Angka Traksi Aktual** (jika tersedia): 3 angka besar dengan label, contoh format "`[JUMLAH]` Unit Terjual dalam Pilot", "`[JUMLAH]` Pembeli Puas", "`[PERSEN]`% Repeat Order" — beri label kecil di bawah section "Data per [TANGGAL], dari hasil uji coba pilot"
5. **Section Data Proyeksi** (WAJIB terpisah secara visual, mis. dengan background beda warna & badge "PROYEKSI"):
   - Judul section: "Proyeksi Pertumbuhan (Estimasi, Bukan Data Aktual)"
   - Tabel ringkas proyeksi *Customer Repeat Rate* per bulan (boleh pakai 4–6 baris contoh, bukan 12 bulan penuh, cukup ilustratif)
   - Catatan kecil jelas: "Angka di bagian ini adalah proyeksi bisnis untuk keperluan perencanaan, bukan hasil yang sudah tercapai"
6. **CTA penutup**: ajakan jadi salah satu pengguna awal, link ke produk.html
</must_include_content>

<constraints>
- Section data aktual dan data proyeksi TIDAK BOLEH digabung dalam satu tabel/section yang sama — harus ada pemisah visual yang jelas (border, warna background berbeda, atau badge)
</constraints>

<negative_example>
JANGAN menampilkan angka proyeksi seolah-olah itu hasil penjualan yang sudah terjadi — ini bisa dianggap menyesatkan oleh juri.
</negative_example>

<output_format>
Satu file HTML lengkap, siap disimpan sebagai `testimoni.html`.
</output_format>
```

---

## Prompt 6 — Halaman Keranjang & Checkout (`keranjang.html`)

```
<role>
Kamu adalah frontend developer yang menyusun halaman keranjang dan checkout WORMI yang membaca data dari localStorage dan menghasilkan ringkasan pesanan terstruktur ke WhatsApp.
</role>

<context>
PENTING: halaman ini BUKAN sistem pembayaran. "Checkout" di sini berarti menyusun pesanan secara rapi lalu meneruskannya ke WhatsApp admin untuk konfirmasi manual (ongkir & pembayaran). Ini keputusan desain yang disengaja untuk tahap MVP, bukan kekurangan — jangan buat form seolah-olah ini adalah transaksi pembayaran final.
</context>

<task>
Buat halaman `keranjang.html` dengan DUA state yang bisa berpindah: (1) tampilan isi keranjang, dan (2) form checkout, dalam satu halaman yang sama.
</task>

<must_include_content>
1. **Navbar & Footer** standar.
2. **State 1 — Halaman Keranjang**:
   - Baca array dari `localStorage.getItem('wormi_cart')` dengan JavaScript, render tiap item sebagai baris: thumbnail placeholder, ringkasan warna tiap layer (mis. "Layer 1: Terracotta, Layer 2: Hijau Lumut, ..."), jumlah unit, subtotal (`qty * price`)
   - Tombol "+"/"-" untuk ubah jumlah (update localStorage & re-render)
   - Tombol "Hapus" per item (update localStorage & re-render)
   - Tampilkan Total keseluruhan di bagian bawah
   - Jika keranjang kosong, tampilkan pesan "Keranjangmu masih kosong" + tombol "Lihat Produk" ke produk.html
   - Tombol "Lanjut ke Checkout" (disable jika keranjang kosong) yang memunculkan/scroll ke State 2
3. **State 2 — Form Checkout**:
   - Field: Nama Lengkap (required), Nomor WhatsApp (required, validasi minimal angka), Domisili (dropdown: Kos, Apartemen, Rumah, Kontrakan), Alamat Pengiriman Lengkap (textarea, required), Catatan (opsional)
   - Tombol "Kirim Pesanan via WhatsApp"
4. **Logika Kirim Pesanan (WAJIB BERFUNGSI)**:
   - Saat form disubmit dan valid, susun teks pesan otomatis berisi: nama, nomor HP, domisili, alamat, daftar item beserta warna & jumlah, dan total
   - Buka link `https://wa.me/[NOMOR_WA_ADMIN]?text=` + teks pesan yang sudah di-`encodeURIComponent()`, di tab baru
   - Setelah itu tampilkan pesan konfirmasi di halaman: "Pesanan diterima, tim kami akan menghubungi Anda untuk konfirmasi ongkos kirim & pembayaran"
   - Kosongkan `localStorage` keranjang setelah pesanan terkirim
</must_include_content>

<constraints>
- Validasi form harus mencegah submit jika field wajib kosong, tampilkan pesan error inline (bukan `alert()`)
- Jangan gunakan library eksternal untuk validasi, cukup vanilla JS
</constraints>

<negative_example>
JANGAN membuat tombol "Bayar Sekarang" atau elemen apapun yang menyiratkan pembayaran online selesai di halaman ini — tidak ada payment gateway di MVP ini.
</negative_example>

<output_format>
Satu file HTML lengkap termasuk seluruh logika JavaScript di atas, siap disimpan sebagai `keranjang.html`.
</output_format>
```

---

## Prompt 7 — Halaman Eco Events (`eco-events.html`)

```
<role>
Kamu adalah frontend developer yang menyusun halaman daftar acara keberlanjutan lingkungan untuk WORMI.
</role>

<context>
Halaman ini membedakan dua jenis acara: acara pihak lain yang dikurasi WORMI (tidak menambah beban operasional tim), dan acara kecil yang diselenggarakan WORMI sendiri. Pembedaan ini harus terlihat jelas di UI, bukan disamarkan seolah semua acara diadakan WORMI.
</context>

<task>
Buat halaman `eco-events.html` dengan daftar acara berformat kartu, dikelompokkan berdasarkan penyelenggara.
</task>

<must_include_content>
1. **Navbar & Footer** standar.
2. **Judul halaman**: "Eco Events — Yuk Ikut Gerakan Hidup Berkelanjutan" + sub-judul singkat.
3. **Filter/Tab** di atas daftar: "Semua", "Diselenggarakan WORMI", "Rekomendasi Komunitas Lain" (fungsional dengan JavaScript sederhana untuk show/hide card sesuai kategori)
4. **Minimal 4 kartu event contoh** (boleh placeholder, tandai jelas untuk diganti data asli), tiap kartu berisi:
   - Badge kategori ("Diselenggarakan WORMI" warna hijau tua, atau "Rekomendasi" warna terracotta)
   - Judul event
   - Tanggal & waktu `[TANGGAL]`
   - Lokasi (Offline: `[LOKASI]` / Online: `[LINK]`)
   - Deskripsi singkat 1–2 kalimat
   - Tombol "Daftar" yang mengarah ke link WhatsApp/Google Form/situs mitra (placeholder link `[LINK_PENDAFTARAN]`)
   Contoh isi 4 kartu (silakan pakai sebagai draft):
   - "Workshop Kompos Dasar untuk Anak Kos" (Diselenggarakan WORMI, online via Zoom, gratis)
   - "Kelas Zero-Waste Living" (Rekomendasi, kerja sama komunitas lingkungan kampus)
   - "Bersih-Bersih & Edukasi Sampah di Area Kos Bojongsoang" (Diselenggarakan WORMI, offline)
   - "Seminar Ekonomi Sirkular Kota" (Rekomendasi, kerja sama pemerintah kota/komunitas)
5. **Section Arsip Dokumentasi** (di bawah daftar event aktif): grid 3 foto placeholder dari event yang sudah lewat, dengan caption singkat
6. **CTA penutup**: ajakan gabung komunitas/ikuti media sosial WORMI untuk info event terbaru
</must_include_content>

<constraints>
- Badge kategori harus konsisten warnanya di semua kartu agar mudah dibedakan sekilas
</constraints>

<negative_example>
JANGAN menampilkan event rekomendasi/kurasi dengan cara yang membuatnya terlihat seolah diselenggarakan langsung oleh WORMI — ini bisa menyesatkan pengunjung.
</negative_example>

<output_format>
Satu file HTML lengkap termasuk logika filter tab, siap disimpan sebagai `eco-events.html`.
</output_format>
```

---

## Prompt 8 — Halaman FAQ & Kontak (`faq.html`)

```
<role>
Kamu adalah frontend developer yang menyusun halaman FAQ sekaligus kontak WORMI dalam satu halaman.
</role>

<context>
Halaman ini menggabungkan pertanyaan umum dan informasi kontak di bagian bawahnya, sehingga pengunjung yang pertanyaannya belum terjawab bisa langsung menghubungi tim.
</context>

<task>
Buat halaman `faq.html` dengan accordion FAQ dan blok kontak di bagian bawah.
</task>

<must_include_content>
1. **Navbar & Footer** standar.
2. **Judul halaman**: "Pertanyaan yang Sering Diajukan"
3. **Accordion FAQ (WAJIB BERFUNGSI expand/collapse via JavaScript)**, minimal 7 pertanyaan berikut (jawaban 2–4 kalimat tiap poin):
   - Apakah WORMI menimbulkan bau?
   - Berapa lama sampai kompos jadi?
   - Apakah WORMI memakai cacing sungguhan atau hanya karakter desain? *(catatan: jawab sesuai fakta produk sebenarnya — jika hanya karakter desain tanpa cacing hidup, tegaskan itu dengan jelas agar tidak menyesatkan pembeli)*
   - Bagaimana cara memakai air lindi (pupuk cair)?
   - Bagaimana cara memilih warna produk saat pemesanan?
   - Apakah bisa pesan lebih dari 1 unit dengan warna berbeda?
   - Bagaimana proses pemesanan sampai barang diterima? (jelaskan singkat: pilih warna di web → checkout → konfirmasi via WhatsApp → pengiriman)
4. **Kotak pencarian FAQ sederhana** di atas accordion (filter pertanyaan berdasarkan kata kunci yang diketik, real-time dengan JavaScript, tanpa reload halaman)
5. **Section Kontak** (di bawah FAQ, dengan heading jelas "Masih Ada Pertanyaan? Hubungi Kami"):
   - Tombol besar "Chat via WhatsApp" → link `https://wa.me/[NOMOR_WA_ADMIN]`
   - Instagram: `[INSTAGRAM_HANDLE]` dengan link
   - Email: `[EMAIL]` dengan `mailto:`
   - Jam operasional respons `[JAM_OPERASIONAL]`
</must_include_content>

<constraints>
- Accordion harus bisa dibuka satu per satu tanpa reload halaman (native JS, tidak perlu library)
- Jawaban soal cacing sungguhan HARUS jujur berdasarkan fakta produk — jangan mengarang jika informasinya belum pasti, tulis placeholder `[KONFIRMASI_FAKTA_PRODUK]` jika tim belum menentukan jawaban final
</constraints>

<negative_example>
JANGAN membuat FAQ generik yang tidak spesifik untuk produk WORMI (mis. "Bagaimana cara membayar?" tanpa menyebut alur checkout→WhatsApp yang sebenarnya dipakai).
</negative_example>

<output_format>
Satu file HTML lengkap termasuk logika accordion & search filter, siap disimpan sebagai `faq.html`.
</output_format>
```

---

## Catatan Penutup

- Jika ingin men-generate ulang halaman produk/keranjang di sesi terpisah, pastikan struktur `localStorage` key `wormi_cart` dan format objeknya **tetap sama** di semua prompt agar kedua halaman tetap saling terhubung.
- Setelah semua 8 halaman digenerate, cek kembali navbar/footer agar strukturnya benar-benar identik antar file (AI generatif kadang sedikit berbeda tiap kali dijalankan) — bila perlu, salin navbar/footer dari 1 halaman "master" ke halaman lain secara manual.
- Isi seluruh placeholder `[...]` sebelum di-deploy: nomor WhatsApp, Instagram, email, harga produk, spesifikasi, dan data testimoni/proyeksi asli.
