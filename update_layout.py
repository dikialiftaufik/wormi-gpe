import os
import re
import glob

def get_active_page(filename):
    if filename == 'index.html':
        return 'Beranda'
    elif 'produk' in filename or 'bioaktivator' in filename or 'refillpack' in filename:
        return 'Produk'
    elif filename == 'eco-events.html':
        return 'Eco Events'
    elif 'blog' in filename or 'artikel' in filename:
        return 'Blog'
    return None

def build_desktop_menu(active_page):
    links = [
        ('index.html', 'Beranda'),
        ('produk.html', 'Produk'),
        ('eco-events.html', 'Eco Events'),
        ('blog.html', 'Blog')
    ]
    html = '<div class="hidden md:flex items-center space-x-8">\n'
    for href, label in links:
        if active_page == label:
            cls = 'font-heading font-bold text-brown-dark border-b-2 border-terracotta pb-1'
        else:
            cls = 'font-heading font-semibold text-brown-medium hover:text-brown-dark transition-colors'
        html += f'                    <a href="{href}" class="{cls}">{label}</a>\n'
    html += '                </div>'
    return html

def build_footer_links():
    return '''<div class="flex flex-wrap justify-center gap-x-8 gap-y-4 text-sm font-heading font-semibold">
                    <a href="index.html" class="hover:text-terracotta transition-colors">Beranda</a>
                    <a href="produk.html" class="hover:text-terracotta transition-colors">Produk</a>
                    <a href="eco-events.html" class="hover:text-terracotta transition-colors">Eco Events</a>
                    <a href="blog.html" class="hover:text-terracotta transition-colors">Blog</a>
                </div>'''

def update_files():
    # We will use simple regex replacement for the desktop menu and footer links.
    files = glob.glob('*.html')
    
    desktop_menu_pattern = re.compile(r'<div class="hidden md:flex items-center space-x-8">.*?</div>', re.DOTALL)
    
    # Let's check if some files use gap-6 or space-x-8
    # checkout.html has `<div class="hidden md:flex items-center space-x-8">`
    # produk.html has space-x-8
    
    footer_links_pattern = re.compile(r'<div class="flex flex-wrap justify-center gap-x-8 gap-y-4 text-sm font-heading font-semibold">.*?</div>', re.DOTALL)
    
    # Wait! the user also wants to update the full footer of checkout.html to match index.html
    # Let's get the full footer from index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        index_content = f.read()
        
    full_footer_match = re.search(r'(<footer class="bg-green-dark text-white relative pt-20 pb-8 mt-16 md:mt-24">.*?</footer\s*>)', index_content, re.DOTALL)
    if full_footer_match:
        full_footer = full_footer_match.group(1)
        # Update the footer links inside this full footer
        full_footer = footer_links_pattern.sub(build_footer_links(), full_footer)
    else:
        print("Could not find full footer in index.html")
        return

    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        active_page = get_active_page(filename)
        
        # 1. Update Desktop Menu
        new_desktop_menu = build_desktop_menu(active_page)
        content = desktop_menu_pattern.sub(new_desktop_menu, content)
        
        # 2. Update Footer Links
        content = footer_links_pattern.sub(build_footer_links(), content)
        
        # 3. If checkout.html, replace the entire footer
        if filename == 'checkout.html':
            checkout_footer_pattern = re.compile(r'<footer .*?</footer\s*>', re.DOTALL)
            content = checkout_footer_pattern.sub(full_footer, content)
            
        # 4. Handle mobile menu links if any (the ID is usually mobile-menu)
        # But this might be too brittle, let's see if we can find it
        mobile_menu_links_pattern = re.compile(r'(<div class="px-2 pt-2 pb-3 space-y-1">).*?(</div>\s*</div>\s*</nav>)', re.DOTALL)
        if mobile_menu_links_pattern.search(content):
            mobile_links = [
                ('index.html', 'Beranda'),
                ('produk.html', 'Produk'),
                ('eco-events.html', 'Eco Events'),
                ('blog.html', 'Blog')
            ]
            m_html = ''
            for href, label in mobile_links:
                if active_page == label:
                    m_cls = 'block px-3 py-2 rounded-md text-base font-bold font-heading text-terracotta bg-terracotta/10'
                else:
                    m_cls = 'block px-3 py-2 rounded-md text-base font-semibold font-heading text-brown-dark hover:bg-cream-dark/50 hover:text-terracotta transition-colors'
                m_html += f'                        <a href="{href}" class="{m_cls}">{label}</a>\n'
            
            content = mobile_menu_links_pattern.sub(r'\1\n' + m_html + r'                    \2', content)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

if __name__ == '__main__':
    update_files()
