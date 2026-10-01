# -*- coding: utf-8 -*-
"""
Generator halaman artikel blog WORMI (tambahan).

Menghasilkan dua halaman artikel yang tampilannya konsisten dengan
artikel-sampah-organik.html, namun isi kontennya disesuaikan dengan judul:

  1. artikel-gaya-hidup-minim-sampah.html  -> "Memulai Gaya Hidup Minim Sampah dari Dapur Kost"
  2. artikel-manfaat-kompos.html           -> "5 Manfaat Kompos untuk Tanaman dan Lingkungan"

Script juga memperbarui tautan "Baca Selengkapnya"/"Baca" pada blog.html
agar mengarah ke halaman baru tersebut.

Jalankan: python create_artikel_pages.py
"""

TEMPLATE = 'artikel-sampah-organik.html'
MARKER_HEADER = '<!-- ===================== ARTIKEL HEADER ===================== -->'
MARKER_FOOTER = '<!-- ===================== FOOTER ===================== -->'
OLD_TITLE = '<title>WORMI Komposter Dapur Mini Berkarakter Cacing</title>'
OLD_META = ('content="WORMI adalah komposter dapur mini berkarakter cacing untuk mengolah sisa sayur & '
            'buah jadi kompos. Cocok untuk kos, apartemen, dan rumah minimalis.">')

SHARE = """                <div class="mt-12 pt-8 border-t border-black/10 flex flex-col sm:flex-row items-center justify-between gap-6">
                    <div class="flex items-center gap-3">
                        <span class="font-heading font-bold text-brown-dark">Bagikan artikel ini:</span>
                        <div class="flex gap-2">
                            <button class="w-10 h-10 rounded-full bg-cream-dark flex items-center justify-center hover:bg-terracotta hover:text-white transition-colors text-brown-dark"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg></button>
                            <button class="w-10 h-10 rounded-full bg-cream-dark flex items-center justify-center hover:bg-terracotta hover:text-white transition-colors text-brown-dark"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></button>
                        </div>
                    </div>
                </div>"""

def related_card(img, alt, cat, title, desc, date, read, href):
    return """                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group">
                    <div class="h-48 relative overflow-hidden">
                        <img src="%(img)s"
                            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                            alt="%(alt)s">
                        <div
                            class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">
                            %(cat)s</div>
                    </div>
                    <div class="p-6">
                        <h3
                            class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">
                            %(title)s</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">%(desc)s</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none"
                                        stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                    </svg> %(date)s</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none"
                                        stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg> %(read)s</span>
                            </div>
                            <a href="%(href)s"
                                class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca
                                <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>""" % {
        'img': img, 'alt': alt, 'cat': cat, 'title': title,
        'desc': desc, 'date': date, 'read': read, 'href': href,
    }


def render(nav, footer, *, title, meta_desc, category, date, readtime,
           hero_img, hero_alt, body_html, related_html):
    parts = """

    <!-- ===================== ARTIKEL HEADER ===================== -->
    <section class="pt-32 pb-8 bg-cream">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-6 flex items-center gap-2 text-sm font-semibold font-heading text-brown-medium">
                <a href="blog.html" class="hover:text-terracotta transition-colors">Blog</a>
                <span>/</span>
                <span class="text-terracotta">{category}</span>
            </div>
            <h1 class="text-3xl md:text-5xl font-heading font-bold text-green-dark leading-tight mb-6">{title}</h1>

            <div class="flex items-center gap-6 mb-8 text-sm text-brown-medium font-semibold font-heading border-b border-black/10 pb-6">
                <div class="flex items-center gap-2">
                    <img src="assets/favicon.ico" class="w-8 h-8 rounded-full border border-black/10" alt="Tim WORMI">
                    <span>Oleh <span class="text-brown-dark">Tim WORMI</span></span>
                </div>
                <div class="flex items-center gap-4 text-xs">
                    <span class="flex items-center gap-1"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> {date}</span>
                    <span class="flex items-center gap-1"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> {readtime}</span>
                </div>
            </div>
        </div>
    </section>

    <!-- ===================== ARTIKEL CONTENT ===================== -->
    <section class="pb-16 bg-cream">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Hero Image -->
            <div class="rounded-3xl overflow-hidden shadow-soft border border-black/5 mb-12 h-[300px] md:h-[500px]">
                <img src="{hero_img}" class="w-full h-full object-cover" alt="{hero_alt}">
            </div>

            <!-- Body Text -->
            <article class="max-w-3xl mx-auto text-lg text-brown-medium leading-relaxed font-body space-y-8 bg-white p-8 md:p-12 rounded-3xl shadow-soft border border-black/5">
{body_html}
{SHARE}
            </article>
        </div>
    </section>

    <!-- ===================== BACA JUGA ===================== -->
    <section class="py-16 bg-white border-t border-black/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-heading font-bold text-green-dark mb-10 text-center">Baca Artikel Lainnya</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-5xl mx-auto">
{related_html}
            </div>
        </div>
    </section>
""".format(category=category, title=title, date=date, readtime=readtime,
           hero_img=hero_img, hero_alt=hero_alt, body_html=body_html,
           SHARE=SHARE, related_html=related_html)

    page = nav + parts + footer
    page = page.replace(OLD_TITLE, '<title>' + title + ' | Blog WORMI</title>')
    page = page.replace(OLD_META, 'content="' + meta_desc + '">')
    return page


def point_link(html, marker, new_href):
    """Ganti href="#" pertama yang muncul setelah sebuah penanda judul."""
    idx = html.find(marker)
    if idx == -1:
        raise ValueError('penanda tidak ditemukan: ' + marker)
    hidx = html.find('href="#"', idx)
    if hidx == -1:
        raise ValueError('href="#" tidak ditemukan setelah: ' + marker)
    return html[:hidx] + 'href="' + new_href + '"' + html[hidx + len('href="#"'):]


ART1_BODY = """                <p class="text-xl leading-relaxed text-brown-dark font-medium">Tinggal di kamar kost dengan dapur seadanya sering membuat kita berpikir bahwa hidup ramah lingkungan itu rumit dan butuh tempat luas. Padahal, justru dapur kost adalah titik paling strategis untuk memulai gaya hidup minim sampah. Dari dapur kecil inilah sebagian besar sisa makanan dan kemasan sekali pakai dihasilkan setiap hari.</p>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">Kenapa Dapur Kost Jadi Titik Awal yang Tepat?</h2>
                <p>Setiap kali kamu memasak atau makan di kamar, selalu ada sisa yang tertinggal: kulit bawang, potongan sayur, sisa nasi, sampai bungkus mi instan. Kalau semuanya dibuang ke satu tempat sampah, sampah pun bercampur dan berakhir menumpuk di TPA. Padahal dengan sedikit perubahan kebiasaan, kamu bisa memangkas jumlah sampah harianmu tanpa harus mengubah gaya hidup secara drastis.</p>
                <p>Anak kos sebenarnya punya satu keunggulan: pola konsumsinya lebih sederhana. Kamu biasanya memasak dalam porsi kecil, berbelanja kebutuhan harian, dan punya kendali penuh atas apa yang masuk dan keluar dari kamar. Itu modal besar untuk membangun kebiasaan baru yang lebih ramah lingkungan.</p>

                <div class="bg-green-light border-l-4 border-green-dark p-6 rounded-r-2xl my-8">
                    <p class="font-heading font-semibold text-green-darker italic text-lg m-0">"Gaya hidup minim sampah bukan soal sempurna sejak hari pertama, tapi soal memulai satu langkah kecil dan mengulanginya setiap hari."</p>
                </div>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">5 Langkah Memulai dari Dapur Kost</h2>
                <ol class="list-decimal pl-6 space-y-3 text-brown-dark">
                    <li><strong>Pilah dari sumbernya.</strong> Siapkan dua wadah kecil di bawah wastafel atau sudut dapur: satu untuk sisa organik (sisa sayur &amp; buah) dan satu untuk sampah anorganik. Memilah saat membuang jauh lebih mudah daripada memilah nanti.</li>
                    <li><strong>Kurangi kemasan sekali pakai.</strong> Bawa kantong belanja sendiri, pilih sayur dan buah tanpa plastik tambahan, dan biasakan membawa tumbler untuk minuman. Sedikit usaha, pengurangan sampahnya besar.</li>
                    <li><strong>Olah sisa organik jadi kompos.</strong> Jangan langsung buang sisa sayur &amp; buah. Gunakan komposter mini berdesain tertutup seperti WORMI yang muat di sudut dapur, bebas bau, dan tidak mengundang lalat sehingga aman untuk kamar kost.</li>
                    <li><strong>Simpan sisa makanan dengan benar.</strong> Sisa masakan boleh disimpan, tapi bukan berarti dibiarkan terbuka. Taruh di wadah kedap udara dan simpan di kulkas agar tahan lebih lama dan tidak terbuang sia-sia.</li>
                    <li><strong>Bersihkan kemasan sebelum dibuang.</strong> Bilas dan keringkan kaleng, botol, atau kemasan plastik sebelum dibuang agar tidak berbau dan lebih mudah didaur ulang oleh pemulung atau bank sampah.</li>
                </ol>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">Tantangan di Kost dan Cara Menyiasatinya</h2>
                <p>Memulai di ruang sempit tentu punya tantangan tersendiri. Berikut beberapa solusi praktis yang bisa kamu coba:</p>
                <ul class="list-disc pl-6 space-y-3 text-brown-dark">
                    <li><strong>Takut bau dan lalat:</strong> pilih komposter tertutup dengan penyaring udara, bukan ember terbuka. Bau yang tertahan juga menjaga kenyamanan kamu dan tetangga kamar.</li>
                    <li><strong>Ruang terbatas:</strong> manfaatkan sudut dapur, bawah meja, atau rak sempit. Komposter mini berukuran ringkas tidak memakan banyak tempat.</li>
                    <li><strong>Muncul jamur atau belatung:</strong> biasanya karena kelembapan berlebih. Tambahkan bahan kering seperti sisa kertas atau sekam, dan pastikan ada sirkulasi udara.</li>
                    <li><strong>Teman sekamar belum terbiasa:</strong> ajak perlahan. Mulai dengan satu wadah pemilahan bersama, lalu tunjukkan bahwa dapur jadi lebih bersih dan bebas bau.</li>
                </ul>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">Mulai Kecil, Konsisten, dan Rasakan Dampaknya</h2>
                <p>Kamu tidak perlu menunggu punya rumah sendiri untuk hidup lebih ramah lingkungan. Mulai dari satu wadah pemilahan dan satu komposter mini di dapur kost, kamu sudah mengurangi beban TPA dan mengembalikan nutrisi ke tanah. Kalau dilakukan bersama teman sekamar, dampaknya akan terasa lebih besar lagi.</p>
                <p>Ingat, perubahan besar selalu dimulai dari langkah kecil yang dilakukan berulang. Jadi, langkah pertamamu hari ini mau apa?</p>"""


ART1_RELATED = "\n".join([
    related_card(
        'assets/blog-4.png', 'Cara Memilah Sampah Organik', 'Gaya Hidup',
        'Cara Memilah Sampah Organik di Rumah dengan Mudah',
        'Mulai dari dapur, kamu bisa memisahkan sampah organik dengan cara sederhana. Ikuti langkah-langkahnya di sini.',
        '5 Sep 2025', '4 mnt', '#'),
    related_card(
        'assets/blog-3.png', '5 Manfaat Kompos', 'Tips Kompos',
        '5 Manfaat Kompos untuk Tanaman dan Lingkungan',
        'Kompos bukan hanya menyuburkan tanaman, tapi juga membantu mengurangi sampah rumah tangga dan menjaga bumi tetap sehat.',
        '8 Sep 2025', '6 mnt', 'artikel-manfaat-kompos.html'),
    related_card(
        'assets/blog-1.png', 'Sampah Organik', 'Sampah Organik',
        'Kenapa Sampah Organik Masih Jadi Masalah Besar di Kota?',
        'Sampah rumah tangga menjadi penyumbang terbesar sampah di Indonesia. Yuk, pahami penyebab dan cara menguranginya.',
        '12 Sep 2025', '5 mnt', 'artikel-sampah-organik.html'),
])


ART2_BODY = """                <p class="text-xl leading-relaxed text-brown-dark font-medium">Kompos sering dianggap sekadar "pupuk biasa". Padahal, di balik gundukan tanah gelap yang gembur itu tersimpan segudang manfaat bagi tanaman, tanah, dan lingkungan sekitar kita. Buat kamu yang baru mulai mengompos, mengenali manfaatnya bisa jadi alasan kuat untuk tetap konsisten.</p>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">Apa Itu Kompos?</h2>
                <p>Kompos adalah hasil penguraian bahan organik, seperti sisa sayur, kulit buah, dan daun kering, oleh mikroorganisme dan cacing. Proses ini mengubah sampah yang tadinya mengganggu menjadi bahan kaya hara yang berwarna gelap, bertekstur gembur, dan berbau seperti tanah segar.</p>
                <p>Berbeda dengan pupuk kimia, kompos bekerja perlahan sambil memperbaiki struktur tanah, bukan sekadar menyuplai nutrisi. Inilah yang membuat kompos begitu istimewa bagi tanaman maupun lingkungan.</p>

                <div class="bg-green-light border-l-4 border-green-dark p-6 rounded-r-2xl my-8">
                    <p class="font-heading font-semibold text-green-darker italic text-lg m-0">"Kompos bukan hanya menyuburkan tanaman di tamanmu, tapi juga ikut menjaga bumi tetap sehat."</p>
                </div>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">5 Manfaat Kompos untuk Tanaman dan Lingkungan</h2>

                <h3 class="text-xl font-heading font-bold text-brown-dark mt-8 mb-3">1. Menyuburkan Tanah Secara Alami</h3>
                <p>Kompos mengandung nitrogen, fosfor, kalium, serta mikroba baik yang dibutuhkan tanah. Pemberian kompos secara rutin membuat tanah lebih gembur, subur, dan mampu menahan air dengan lebih baik dibandingkan tanah yang hanya diberi pupuk kimia.</p>

                <h3 class="text-xl font-heading font-bold text-brown-dark mt-8 mb-3">2. Membantu Tanaman Tumbuh Lebih Sehat</h3>
                <p>Tanaman yang tumbuh di media dengan campuran kompos biasanya lebih kuat, berdaun hijau segar, dan lebih tahan terhadap penyakit. Kandungan hara yang lengkap dan seimbang membuat akar berkembang optimal sehingga tanaman tidak mudah stres.</p>

                <h3 class="text-xl font-heading font-bold text-brown-dark mt-8 mb-3">3. Mengurangi Sampah Rumah Tangga ke TPA</h3>
                <p>Lebih dari setengah sampah rumah tangga adalah sampah organik. Dengan mengompos, kamu mengalihkan sisa dapur dari TPA dan mengubahnya menjadi sesuatu yang bermanfaat. Ini adalah cara paling sederhana untuk mengurangi volume sampah yang kamu hasilkan setiap hari.</p>

                <h3 class="text-xl font-heading font-bold text-brown-dark mt-8 mb-3">4. Menjaga Kelembapan Tanah dan Mencegah Erosi</h3>
                <p>Kompos mampu menyerap dan menyimpan air jauh lebih baik daripada tanah biasa. Ketika dicampur ke media tanam, kompos membantu menjaga kelembapan, mengurangi kebutuhan penyiraman, dan meminimalkan risiko erosi pada permukaan tanah.</p>

                <h3 class="text-xl font-heading font-bold text-brown-dark mt-8 mb-3">5. Menekan Emisi Gas Rumah Kaca</h3>
                <p>Ketika sampah organik membusuk tanpa oksigen di TPA, ia menghasilkan gas metana yang jauh lebih berbahaya daripada karbon dioksida. Dengan mengompos di rumah secara aerobik, proses ini tidak terjadi, sehingga kita turut menekan emisi gas rumah kaca penyebab pemanasan global.</p>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">Bagaimana Cara Memulainya?</h2>
                <p>Kamu tidak perlu lahan luas untuk mulai mengompos. Cukup dengan komposter mini berdesain tertutup seperti WORMI, sisa sayur dan buah dari dapur bisa kamu olah sendiri menjadi kompos setiap hari, tanpa bau dan tanpa ribet, bahkan di kos atau apartemen.</p>
                <p>Mulai dari satu kebiasaan kecil: <strong>pisahkan sampah organikmu, masukkan ke komposter, dan biarkan alam bekerja.</strong> Beberapa minggu kemudian, kamu sudah punya kompos yang siap menyuburkan tanamanmu.</p>"""


ART2_RELATED = "\n".join([
    related_card(
        'assets/blog-4.png', 'Cara Memilah Sampah Organik', 'Gaya Hidup',
        'Cara Memilah Sampah Organik di Rumah dengan Mudah',
        'Mulai dari dapur, kamu bisa memisahkan sampah organik dengan cara sederhana. Ikuti langkah-langkahnya di sini.',
        '5 Sep 2025', '4 mnt', '#'),
    related_card(
        'assets/blog-2.png', 'Gaya Hidup Minim Sampah', 'Gaya Hidup',
        'Memulai Gaya Hidup Minim Sampah dari Dapur Kost',
        'Tinggal di tempat sempit bukan halangan untuk peduli lingkungan. Simak cara mudah memilah sampah dan mengompos meski anak kos.',
        '10 Sep 2025', '4 mnt', 'artikel-gaya-hidup-minim-sampah.html'),
    related_card(
        'assets/blog-1.png', 'Sampah Organik', 'Sampah Organik',
        'Kenapa Sampah Organik Masih Jadi Masalah Besar di Kota?',
        'Sampah rumah tangga menjadi penyumbang terbesar sampah di Indonesia. Yuk, pahami penyebab dan cara menguranginya.',
        '12 Sep 2025', '5 mnt', 'artikel-sampah-organik.html'),
])


def main():
    with open(TEMPLATE, 'r', encoding='utf-8') as f:
        tpl = f.read()

    nav = tpl.split(MARKER_HEADER)[0].rstrip()
    footer = MARKER_FOOTER + tpl.split(MARKER_FOOTER, 1)[1]

    art1 = render(
        nav, footer,
        title='Memulai Gaya Hidup Minim Sampah dari Dapur Kost',
        meta_desc='Panduan memulai gaya hidup minim sampah dari dapur kost: memilah sampah, mengurangi kemasan sekali pakai, dan mengompos di ruang terbatas.',
        category='Gaya Hidup',
        date='10 Sep 2025',
        readtime='4 menit baca',
        hero_img='assets/blog-2.png',
        hero_alt='Memulai Gaya Hidup Minim Sampah dari Dapur Kost',
        body_html=ART1_BODY,
        related_html=ART1_RELATED,
    )
    with open('artikel-gaya-hidup-minim-sampah.html', 'w', encoding='utf-8') as f:
        f.write(art1)

    art2 = render(
        nav, footer,
        title='5 Manfaat Kompos untuk Tanaman dan Lingkungan',
        meta_desc='Kompos bukan sekadar pupuk. Kenali 5 manfaat kompos untuk tanaman dan lingkungan, mulai dari menyuburkan tanah hingga menekan emisi gas rumah kaca.',
        category='Tips Kompos',
        date='8 Sep 2025',
        readtime='6 menit baca',
        hero_img='assets/blog-3.png',
        hero_alt='5 Manfaat Kompos untuk Tanaman dan Lingkungan',
        body_html=ART2_BODY,
        related_html=ART2_RELATED,
    )
    with open('artikel-manfaat-kompos.html', 'w', encoding='utf-8') as f:
        f.write(art2)

    # Perbarui tautan pada blog.html agar mengarah ke halaman artikel baru.
    with open('blog.html', 'r', encoding='utf-8') as f:
        blog = f.read()
    blog = point_link(
        blog, 'Memulai Gaya Hidup Minim Sampah dari Dapur Kost',
        'artikel-gaya-hidup-minim-sampah.html')
    blog = point_link(
        blog, '5 Manfaat Kompos untuk Tanaman dan Lingkungan',
        'artikel-manfaat-kompos.html')
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(blog)

    print('OK: artikel-gaya-hidup-minim-sampah.html')
    print('OK: artikel-manfaat-kompos.html')
    print('OK: tautan blog.html diperbarui')


if __name__ == '__main__':
    main()
