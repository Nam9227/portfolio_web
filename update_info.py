import os
import glob

directory = r"d:\CS_AI\portfolio_web"
html_files = glob.glob(os.path.join(directory, "*.html"))

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace footer
    content = content.replace("Bản quyền thuộc về Học viên.", "Bản quyền thuộc về Nguyễn Văn Nam (25021905).")
    
    # In index.html specifically
    if "index.html" in filepath:
        content = content.replace(
            '<h1 class="glitch-effect">Xin chào, tôi là <span class="highlight">Học viên</span></h1>',
            '<h1 class="glitch-effect">Xin chào, tôi là <span class="highlight">Nguyễn Văn Nam</span></h1>'
        )
        content = content.replace(
            '<p class="subtitle">Sinh viên ngành Công nghệ | Đam mê Trí tuệ nhân tạo & Công nghệ số</p>',
            '<p class="subtitle">Sinh viên ngành Khoa học Máy tính | Trường Đại học Công nghệ (UET)<br>Mã sinh viên: 25021905</p>'
        )
        content = content.replace(
            '<title>Portfolio Cá Nhân - Nhập môn Công nghệ số & AI</title>',
            '<title>Portfolio - Nguyễn Văn Nam (25021905)</title>'
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated name, id, and major across all HTML files.")
