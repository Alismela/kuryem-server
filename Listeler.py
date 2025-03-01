gitignore_content = """# Python dosyaları
*.pyc
__pycache__/

# Sanal ortamlar
venv/
env/
*.env

# Veritabanı dosyaları (örn: SQLite)
*.db

# Log dosyaları
*.log

# IDE/Editor dosyaları
.vscode/
.idea/
*.sublime-project
*.sublime-workspace

# MacOS
.DS_Store
"""

with open('.gitignore', 'w', encoding='utf-8') as f:
    f.write(gitignore_content)

print("'.gitignore' dosyası başarıyla oluşturuldu!")
