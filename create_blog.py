import re

def build():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    head_nav = content.split('<!-- ===================== HERO SECTION ===================== -->')[0]
    footer_scripts = '<!-- ===================== FOOTER ===================== -->' + content.split('<!-- ===================== FOOTER ===================== -->')[1]
    
    # We will remove the scroll-reveal observer from footer_scripts since we might want our own or just keep it
    
    blog_content = """
    <!-- ===================== KATEGORI ===================== -->
    <section class="pt-32 pb-10 bg-cream">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-wrap items-center justify-center gap-4">
                <button class="bg-green-dark text-white px-6 py-2.5 rounded-full font-heading font-bold flex items-center gap-2 shadow-sm transition-transform hover:-translate-y-1">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16m-7 6h7"/></svg>
                    Semua Artikel
                </button>
                <button class="bg-white text-brown-dark border border-black/5 px-6 py-2.5 rounded-full font-heading font-bold flex items-center gap-2 shadow-sm transition-transform hover:-translate-y-1 hover:border-green-dark">
                    <span class="text-xl leading-none">🌱</span> Tips Kompos
                </button>
                <button class="bg-white text-brown-dark border border-black/5 px-6 py-2.5 rounded-full font-heading font-bold flex items-center gap-2 shadow-sm transition-transform hover:-translate-y-1 hover:border-green-dark">
                    <span class="text-xl leading-none">🗑️</span> Sampah Organik
                </button>
                <button class="bg-white text-brown-dark border border-black/5 px-6 py-2.5 rounded-full font-heading font-bold flex items-center gap-2 shadow-sm transition-transform hover:-translate-y-1 hover:border-green-dark">
                    <span class="text-xl leading-none">🌿</span> Tanaman & Kebun
                </button>
                <button class="bg-white text-brown-dark border border-black/5 px-6 py-2.5 rounded-full font-heading font-bold flex items-center gap-2 shadow-sm transition-transform hover:-translate-y-1 hover:border-green-dark">
                    <span class="text-xl leading-none">🏡</span> Gaya Hidup
                </button>
            </div>
        </div>
    </section>

    <!-- ===================== ARTIKEL PILIHAN (SLIDER) ===================== -->
    <section class="pb-16 bg-cream">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="relative rounded-[2rem] overflow-hidden bg-white shadow-soft border border-black/5" id="headline-slider">
                
                <!-- Slide 1 -->
                <div class="slide active flex flex-col md:flex-row h-auto md:h-[400px] w-full transition-opacity duration-1000 opacity-100 z-10 relative">
                    <div class="w-full md:w-1/2 h-64 md:h-full relative">
                        <img src="assets/dokumentasi-1.png" class="w-full h-full object-cover" alt="Sampah Organik">
                        <div class="absolute top-4 left-4 bg-terracotta text-white px-3 py-1 text-xs font-bold rounded-full font-heading">ARTIKEL PILIHAN</div>
                    </div>
                    <div class="w-full md:w-1/2 p-8 md:p-12 flex flex-col justify-center bg-white relative">
                        <div class="bg-peach-light text-terracotta text-xs font-bold px-3 py-1 rounded-full w-max mb-4">Sampah Organik</div>
                        <h2 class="text-3xl lg:text-4xl font-heading font-bold text-green-dark mb-4 leading-tight">Kenapa Sampah Organik Masih Jadi Masalah Besar di Kota?</h2>
                        <p class="text-brown-medium mb-8 line-clamp-3">Sampah rumah tangga, terutama sisa makanan, menjadi penyumbang terbesar sampah di Indonesia. Yuk, pahami penyebab, dampaknya, dan bagaimana kita bisa mulai menguranginya dari rumah.</p>
                        
                        <div class="flex items-center justify-between mt-auto">
                            <div class="flex items-center gap-4 text-xs text-brown-medium font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> 12 Sep 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 5 menit baca</span>
                            </div>
                            <a href="#" class="font-heading font-bold text-terracotta hover:text-brown-dark transition-colors flex items-center gap-1">Baca Selengkapnya <span class="text-lg">&rarr;</span></a>
                        </div>
                    </div>
                </div>

                <!-- Slide 2 -->
                <div class="slide absolute inset-0 flex flex-col md:flex-row h-auto md:h-[400px] w-full transition-opacity duration-1000 opacity-0 z-0">
                    <div class="w-full md:w-1/2 h-64 md:h-full relative">
                        <img src="assets/dokumentasi-2.png" class="w-full h-full object-cover" alt="Gaya Hidup">
                        <div class="absolute top-4 left-4 bg-terracotta text-white px-3 py-1 text-xs font-bold rounded-full font-heading">ARTIKEL PILIHAN</div>
                    </div>
                    <div class="w-full md:w-1/2 p-8 md:p-12 flex flex-col justify-center bg-white relative">
                        <div class="bg-green-light text-green-dark text-xs font-bold px-3 py-1 rounded-full w-max mb-4">Gaya Hidup</div>
                        <h2 class="text-3xl lg:text-4xl font-heading font-bold text-green-dark mb-4 leading-tight">Memulai Gaya Hidup Minim Sampah dari Dapur Kost</h2>
                        <p class="text-brown-medium mb-8 line-clamp-3">Tinggal di tempat sempit bukan halangan untuk peduli lingkungan. Simak cara mudah memilah sampah dan mengkompos meskipun kamu anak kos.</p>
                        
                        <div class="flex items-center justify-between mt-auto">
                            <div class="flex items-center gap-4 text-xs text-brown-medium font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> 10 Sep 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 4 menit baca</span>
                            </div>
                            <a href="#" class="font-heading font-bold text-terracotta hover:text-brown-dark transition-colors flex items-center gap-1">Baca Selengkapnya <span class="text-lg">&rarr;</span></a>
                        </div>
                    </div>
                </div>

                <!-- Slider Controls -->
                <div class="absolute bottom-4 left-1/2 md:left-auto md:right-12 transform -translate-x-1/2 md:translate-x-0 flex gap-2 z-20">
                    <button onclick="changeSlide(0)" class="slider-dot w-8 h-2.5 rounded-full bg-green-dark transition-all"></button>
                    <button onclick="changeSlide(1)" class="slider-dot w-2.5 h-2.5 rounded-full bg-cream-dark hover:bg-brown-medium transition-all"></button>
                </div>
            </div>
        </div>
    </section>

    <!-- ===================== ARTIKEL TERBARU ===================== -->
    <section class="py-16 bg-white reveal">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between mb-10">
                <h2 class="text-3xl font-heading font-bold text-green-dark">Artikel Terbaru</h2>
                <a href="#" class="font-heading font-bold text-terracotta hover:text-brown-dark transition-colors flex items-center gap-1">Lihat Semua Artikel <span class="text-lg">&rarr;</span></a>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Card 1 -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group">
                    <div class="h-48 relative overflow-hidden">
                        <img src="assets/event-1.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Tips Kompos">
                        <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">Tips Kompos</div>
                    </div>
                    <div class="p-6">
                        <h3 class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">5 Manfaat Kompos untuk Tanaman dan Lingkungan</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">Kompos bukan hanya menyuburkan tanaman, tapi juga membantu mengurangi sampah rumah tangga dan menjaga bumi tetap sehat.</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> 8 Sep 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 6 mnt</span>
                            </div>
                            <a href="#" class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>

                <!-- Card 2 -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group">
                    <div class="h-48 relative overflow-hidden">
                        <img src="assets/event-2.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Gaya Hidup">
                        <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">Gaya Hidup</div>
                    </div>
                    <div class="p-6">
                        <h3 class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">Cara Memilah Sampah Organik di Rumah dengan Mudah</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">Mulai dari dapur, kamu bisa memisahkan sampah organik dengan cara sederhana. Ikuti langkah-langkahnya di sini.</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> 5 Sep 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 4 mnt</span>
                            </div>
                            <a href="#" class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>

                <!-- Card 3 -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group">
                    <div class="h-48 relative overflow-hidden">
                        <img src="assets/event-3.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Tanaman">
                        <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">Tanaman & Kebun</div>
                    </div>
                    <div class="p-6">
                        <h3 class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">Tanaman yang Cocok Menggunakan Kompos</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">Tidak semua tanaman sama. Cari tahu jenis tanaman yang paling cocok dan cara menggunakannya agar hasilnya maksimal.</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> 1 Sep 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 5 mnt</span>
                            </div>
                            <a href="#" class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>

                <!-- Card 4 -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group">
                    <div class="h-48 relative overflow-hidden">
                        <img src="assets/event-4.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Sampah Organik">
                        <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">Sampah Organik</div>
                    </div>
                    <div class="p-6">
                        <h3 class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">Cara Membuat Pupuk Cair (Air Lindi) yang Aman</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">Air lindi bisa menjadi pupuk organik cair yang bermanfaat jika diolah dengan benar. Simak cara membuatnya di sini.</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> 28 Agu 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 6 mnt</span>
                            </div>
                            <a href="#" class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>

                <!-- Card 5 -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group">
                    <div class="h-48 relative overflow-hidden">
                        <img src="assets/event-5.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Gaya Hidup">
                        <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">Gaya Hidup</div>
                    </div>
                    <div class="p-6">
                        <h3 class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">Kompos di Apartemen? Bisa Banget!</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">Hunian terbatas bukan halangan. Temukan tips dan solusi mengelola sampah organik di apartemen atau kos.</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> 24 Agu 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 5 mnt</span>
                            </div>
                            <a href="#" class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>

                <!-- Card 6 -->
                <div class="bg-white rounded-3xl overflow-hidden shadow-soft border border-black/5 hover-lift group">
                    <div class="h-48 relative overflow-hidden">
                        <img src="assets/event-6.png" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Tips Kompos">
                        <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm text-green-dark px-3 py-1 text-xs font-bold rounded-full font-heading shadow-sm">Tips Kompos</div>
                    </div>
                    <div class="p-6">
                        <h3 class="font-heading font-bold text-xl text-brown-dark mb-3 group-hover:text-green-dark transition-colors line-clamp-2 leading-tight">Tanda-tanda Kompos Kamu Sudah Jadi</h3>
                        <p class="text-sm text-brown-medium mb-6 line-clamp-2">Bagaimana cara mengetahui kompos sudah matang? Kenali ciri-cirinya agar aman digunakan untuk tanaman.</p>
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-xs text-brown-medium/70 font-semibold">
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg> 20 Agu 2025</span>
                                <span class="flex items-center gap-1"><svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> 4 mnt</span>
                            </div>
                            <a href="#" class="font-heading font-bold text-terracotta text-sm hover:text-brown-dark transition-colors flex items-center gap-1">Baca <span class="text-base">&rarr;</span></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ===================== NEWSLETTER ===================== -->
    <section class="py-16 bg-cream relative overflow-hidden reveal">
        <div class="absolute -left-20 -bottom-20 w-64 h-64 bg-green-light rounded-full mix-blend-multiply opacity-70"></div>
        <div class="absolute -right-20 -top-20 w-80 h-80 bg-peach-light rounded-full mix-blend-multiply opacity-70"></div>
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="bg-white rounded-3xl p-8 md:p-12 shadow-soft border border-black/5 flex flex-col md:flex-row items-center gap-8">
                <div class="w-32 h-32 flex-shrink-0 animate-float">
                    <img src="assets/why-wormi-solusi.png" class="w-full h-full object-contain" alt="WORMI Mail">
                </div>
                <div class="flex-1 text-center md:text-left">
                    <h2 class="text-2xl md:text-3xl font-heading font-bold text-green-dark mb-3">Dapatkan tips terbaru langsung di email kamu!</h2>
                    <p class="text-brown-medium mb-6">Ikuti perjalanan WORMI untuk hidup lebih bersih dan ramah lingkungan.</p>
                    <form class="flex flex-col sm:flex-row gap-3">
                        <div class="relative flex-1">
                            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                <svg class="w-5 h-5 text-brown-medium/60" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                            </div>
                            <input type="email" placeholder="Masukkan email kamu" class="w-full pl-11 pr-4 py-3.5 border border-black/10 rounded-full focus:outline-none focus:border-green-dark focus:ring-1 focus:ring-green-dark text-brown-dark transition-all" required>
                        </div>
                        <button type="submit" class="bg-terracotta text-white px-8 py-3.5 rounded-full font-heading font-bold hover:bg-brown-dark transition-colors shadow-md">Langganan</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
    """
    
    script_injection = """
    <script>
        // Auto-slider logic
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const dots = document.querySelectorAll('.slider-dot');
        const totalSlides = slides.length;
        
        function changeSlide(index) {
            slides[currentSlide].classList.remove('opacity-100', 'z-10', 'active');
            slides[currentSlide].classList.add('opacity-0', 'z-0');
            dots[currentSlide].classList.remove('w-8', 'bg-green-dark');
            dots[currentSlide].classList.add('w-2.5', 'bg-cream-dark');
            
            currentSlide = index;
            
            slides[currentSlide].classList.add('opacity-100', 'z-10', 'active');
            slides[currentSlide].classList.remove('opacity-0', 'z-0');
            dots[currentSlide].classList.add('w-8', 'bg-green-dark');
            dots[currentSlide].classList.remove('w-2.5', 'bg-cream-dark');
        }
        
        setInterval(() => {
            let next = (currentSlide + 1) % totalSlides;
            changeSlide(next);
        }, 5000);
    </script>
    """

    # We need to insert script_injection just before the closing </body> tag
    footer_scripts = footer_scripts.replace('</body>', script_injection + '\n</body>')
    
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(head_nav + blog_content + footer_scripts)
        
if __name__ == '__main__':
    build()
