import sqlite3

def create_db():
    conn = sqlite3.connect("kurye_takip.db")  # Veritabanı adı
    c = conn.cursor()

    # Calisma tablosu oluşturma
    c.execute('''CREATE TABLE IF NOT EXISTS calisma (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tarih TEXT,
                    saat INTEGER,
                    paket INTEGER,
                    saatlik_ucret INTEGER,
                    paket_ucret INTEGER)''')

    conn.commit()
    conn.close()
    print("Tablo oluşturuldu!")

if __name__ == "__main__":
    create_db()
