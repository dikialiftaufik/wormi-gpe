import re

def build():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    head_nav = content.split('<!-- ===================== HERO SECTION ===================== -->')[0]
    footer_scripts = '<!-- ===================== FOOTER ===================== -->' + content.split('<!-- ===================== FOOTER ===================== -->')[1]
    
    artikel_content = """
    <!-- ===================== ARTIKEL HEADER ===================== -->
    <section class="pt-32 pb-8 bg-cream">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="mb-6 flex items-center gap-2 text-sm font-semibold font-heading text-brown-medium">
                <a href="blog.html" class="hover:text-terracotta transition-colors">Blog</a>
                <span>/</span>
                <span class="text-terracotta">Sampah Organik</span>
            </div>
            <h1 class="text-3xl md:text-5xl font-heading font-bold text-green-dark leading-tight mb-6">Kenapa Sampah Organik Masih Jadi Masalah Besar di Kota?</h1>
            
            <div class="flex items-center gap-6 mb-8 text-sm text-brown-medium font-semibold font-heading border-b border-black/10 pb-6">
                <div class="flex items-center gap-2">
                    <img src="assets/favicon.ico" class="w-8 h-8 rounded-full border border-black/10" alt="Tim WORMI">
                    <span>Oleh <span class="text-brown-dark">Tim WORMI</span></span>
                </div>
                <div class="flex items-center gap-4 text-xs">
                    <span class="flex items-center gap-1"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> 12 Sep 2025</span>
                    <span class="flex items-center gap-1"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 5 menit baca</span>
                </div>
            </div>
        </div>
    </section>

    <!-- ===================== ARTIKEL CONTENT ===================== -->
    <section class="pb-16 bg-cream">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Hero Image -->
            <div class="rounded-3xl overflow-hidden shadow-soft border border-black/5 mb-12 h-[300px] md:h-[500px]">
                <img src="assets/blog-1.png" class="w-full h-full object-cover" alt="Kenapa Sampah Organik Masih Jadi Masalah Besar di Kota?">
            </div>

            <!-- Body Text -->
            <article class="max-w-3xl mx-auto text-lg text-brown-medium leading-relaxed font-body space-y-8 bg-white p-8 md:p-12 rounded-3xl shadow-soft border border-black/5">
                
                <p class="text-xl leading-relaxed text-brown-dark font-medium">Pernahkah kamu memperhatikan berapa banyak sisa makanan yang terbuang setiap harinya di rumah? Mulai dari sisa potongan sayur saat memasak, kulit buah, hingga nasi yang tidak habis dimakan. Di tingkat rumah tangga, hal ini mungkin terlihat sepele, namun tahukah kamu bahwa ini adalah salah satu sumber masalah lingkungan terbesar di Indonesia?</p>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">Realita Sampah Organik di Indonesia</h2>
                <p>Menurut data dari Kementerian Lingkungan Hidup dan Kehutanan (KLHK), lebih dari 50% komposisi sampah di Indonesia adalah sampah sisa makanan dan sampah organik lainnya. Sebagian besar dari sampah ini berakhir di Tempat Pembuangan Akhir (TPA).</p>
                <p>Ketika sampah organik menumpuk di TPA dan tertimpa oleh sampah plastik atau material lain, proses pembusukannya terjadi tanpa oksigen (anaerobik). Proses inilah yang menghasilkan gas metana, salah satu gas rumah kaca yang 25 kali lebih berbahaya bagi atmosfer kita dibandingkan karbon dioksida.</p>

                <div class="bg-green-light border-l-4 border-green-dark p-6 rounded-r-2xl my-8">
                    <p class="font-heading font-semibold text-green-darker italic text-lg m-0">"Membuang sisa makanan ke tempat sampah bukan berarti masalahnya selesai. Itu justru baru awal dari masalah lingkungan yang lebih besar."</p>
                </div>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">Dampak Terhadap Lingkungan Kota</h2>
                <p>Masalah sampah organik di perkotaan sangat terasa dampaknya. Beberapa konsekuensi nyata yang sering kita temui meliputi:</p>
                <ul class="list-disc pl-6 space-y-3 text-brown-dark">
                    <li><strong>Bau Tak Sedap:</strong> Penumpukan sampah di tempat sampah rumah atau TPS sementara memicu bau busuk yang mengganggu kenyamanan.</li>
                    <li><strong>Sumber Penyakit:</strong> Sampah organik yang membusuk secara terbuka mengundang lalat, tikus, dan kecoa yang dapat menyebarkan penyakit.</li>
                    <li><strong>Air Lindi Beracun:</strong> Cairan yang keluar dari tumpukan sampah (lindi) dapat meresap ke dalam tanah dan mencemari sumber air tanah jika tidak dikelola dengan benar.</li>
                    <li><strong>Kapasitas TPA Penuh:</strong> Banyak kota besar di Indonesia saat ini menghadapi krisis lahan TPA yang nyaris penuh akibat volume sampah harian yang tidak terkendali.</li>
                </ul>

                <h2 class="text-2xl font-heading font-bold text-green-dark mt-12 mb-4">Apa Solusinya? Mulai dari Dapur Sendiri</h2>
                <p>Kabar baiknya, masalah besar ini bisa kita cegah mulai dari langkah-langkah kecil di dapur kita sendiri. Mengelola sampah organik bukan hal yang mustahil, bahkan bagi kamu yang tinggal di lahan terbatas atau apartemen.</p>
                
                <p>Langkah paling efektif adalah dengan melakukan <strong>pengomposan (composting)</strong>. Dengan mengkompos, kita mengembalikan nutrisi sisa organik kembali ke alam. Dan dengan hadirnya inovasi seperti komposter mini berdesain tertutup yang estetik, proses mengkompos kini menjadi mudah, bebas bau, dan menyenangkan.</p>

                <div class="mt-12 pt-8 border-t border-black/10 flex flex-col sm:flex-row items-center justify-between gap-6">
                    <div class="flex items-center gap-3">
                        <span class="font-heading font-bold text-brown-dark">Bagikan artikel ini:</span>
                        <div class="flex gap-2">
                            <button class="w-10 h-10 rounded-full bg-cream-dark flex items-center justify-center hover:bg-terracotta hover:text-white transition-colors text-brown-dark"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"/></svg></button>
                            <button class="w-10 h-10 rounded-full bg-cream-dark flex items-center justify-center hover:bg-terracotta hover:text-white transition-colors text-brown-dark"><svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg></button>
                        </div>
                    </div>
                </div>
            </article>
        </div>
    </section>

    <!-- ===================== BACA JUGA ===================== -->
    <section class="py-16 bg-white border-t border-black/5">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-heading font-bold text-green-dark mb-10 text-center">Baca Artikel Lainnya</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-5xl mx-auto">
                <!-- Card 1 -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group">
                    <div class="h-48 relative overflow-hidden">
                        <img src="assets/blog-4.png"
                            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                            alt="Gaya Hidup">
                        <div
                            class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">
                            Gaya Hidup</div>
                    </div>
                    <div class="p-6">
                        <h3
                            class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">
                            Cara Memilah Sampah Organik di Rumah dengan Mudah</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">Mulai dari dapur, kamu bisa memisahkan
                            sampah organik dengan cara sederhana. Ikuti langkah-langkahnya di sini.</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none"
                                        stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                    </svg> 5 Sep 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none"
                                        stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg> 4 mnt</span>
                            </div>
                            <a href="#"
                                class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca
                                <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>

                <!-- Card 2 -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group">
                    <div class="h-48 relative overflow-hidden">
                        <img src="assets/blog-7.png"
                            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                            alt="Kompos di Apartemen">
                        <div
                            class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">
                            Gaya Hidup</div>
                    </div>
                    <div class="p-6">
                        <h3
                            class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">
                            Kompos di Apartemen? Bisa Banget!</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">Hunian terbatas bukan halangan. Temukan
                            tips dan solusi mengelola sampah organik di apartemen atau kos.</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none"
                                        stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                    </svg> 24 Agu 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none"
                                        stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg> 5 mnt</span>
                            </div>
                            <a href="#"
                                class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca
                                <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>

                <!-- Card 3 -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group hidden lg:block">
                    <div class="h-48 relative overflow-hidden">
                        <img src="assets/blog-5.png"
                            class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                            alt="Tanaman & Kebun">
                        <div
                            class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">
                            Tanaman & Kebun</div>
                    </div>
                    <div class="p-6">
                        <h3
                            class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">
                            Tanaman yang Cocok Menggunakan Kompos</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">Tidak semua tanaman sama. Cari tahu jenis
                            tanaman yang paling cocok dan cara menggunakannya agar hasilnya maksimal.</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none"
                                        stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                    </svg> 1 Sep 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none"
                                        stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round"
                                            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg> 5 mnt</span>
                            </div>
                            <a href="#"
                                class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca
                                <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>
    """
    
    with open('artikel-sampah-organik.html', 'w', encoding='utf-8') as f:
        f.write(head_nav + artikel_content + footer_scripts)
        
if __name__ == '__main__':
    build()
