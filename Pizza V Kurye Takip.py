from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_FILE = 'kazanc_data.db'

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS calisma (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarih TEXT,
                saat INTEGER,
                paket INTEGER,
                paket_basi_ucret REAL,
                saatlik_ucret REAL,
                toplam_kazanc INTEGER,
                ay TEXT
            )
        ''')
        conn.commit()

init_db()

def safe_int(value):
    try:
        return int(round(float(value)))
    except (ValueError, TypeError):
        return 0

# Geçen ayı hesaplayan fonksiyon
def get_last_month():
    now = datetime.now()
    year = now.year
    month = now.month
    if month == 1:
        last_month = 12
        last_year = year - 1
    else:
        last_month = month - 1
        last_year = year
    return f"{last_month:02d}-{last_year}"

# Ay numarasını Türkçe isme çeviren fonksiyon
def get_month_name(month_number):
    month_names = {
        "01": "Ocak",
        "02": "Şubat",
        "03": "Mart",
        "04": "Nisan",
        "05": "Mayıs",
        "06": "Haziran",
        "07": "Temmuz",
        "08": "Ağustos",
        "09": "Eylül",
        "10": "Ekim",
        "11": "Kasım",
        "12": "Aralık"
    }
    return month_names.get(month_number, "")

@app.route('/')
def index():
    # Güncel ay "MM-YYYY" formatında
    current_month = datetime.now().strftime("%m-%Y")
    # Güncel ayın ismi
    current_month_name = get_month_name(datetime.now().strftime("%m"))
    # Geçen ay
    last_month = get_last_month()

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        # Güncel ayın kayıtları
        cursor.execute("""
            SELECT id, tarih, saat, paket, paket_basi_ucret, saatlik_ucret, toplam_kazanc, ay 
            FROM calisma 
            WHERE ay = ? 
            ORDER BY tarih DESC
        """, (current_month,))
        current_records = cursor.fetchall()

        # Geçtiğimiz ayın kayıtları
        cursor.execute("""
            SELECT id, tarih, saat, paket, paket_basi_ucret, saatlik_ucret, toplam_kazanc, ay 
            FROM calisma 
            WHERE ay = ? 
            ORDER BY tarih DESC
        """, (last_month,))
        last_month_records = cursor.fetchall()

    # Güncel ay kazanç hesaplamaları
    total_income = sum(safe_int(row[6]) for row in current_records) if current_records else 0
    total_income_1_15 = sum(safe_int(row[6]) for row in current_records if int(row[1].split('/')[0]) <= 15) if current_records else 0
    total_income_15_31 = sum(safe_int(row[6]) for row in current_records if int(row[1].split('/')[0]) > 15) if current_records else 0

    # Geçtiğimiz ayın toplam kazancı ve ismi
    last_month_income = sum(safe_int(row[6]) for row in last_month_records) if last_month_records else 0
    last_month_name = get_month_name(last_month.split('-')[0])

    return render_template(
        'index.html',
        current_records=current_records,
        last_month_records=last_month_records,
        total_income=total_income,
        total_income_1_15=total_income_1_15,
        total_income_15_31=total_income_15_31,
        current_month_name=current_month_name,
        last_month_income=last_month_income,
        last_month_name=last_month_name
    )

@app.route('/add', methods=['POST'])
def add_data():
    tarih = request.form['tarih']  # YYYY-MM-DD format
    try:
        saat = int(request.form['saat'])
    except ValueError:
        saat = 0
    try:
        paket = int(request.form['paket'])
    except ValueError:
        paket = 0
    try:
        paket_basi_ucret = float(request.form['paket_basi_ucret'])
    except ValueError:
        paket_basi_ucret = 0.0
    try:
        saatlik_ucret = float(request.form['saatlik_ucret'])
    except ValueError:
        saatlik_ucret = 0.0

    toplam_kazanc = int(round((paket * paket_basi_ucret) + (saat * saatlik_ucret)))

    # Tarih formatı
    try:
        dt = datetime.strptime(tarih, '%Y-%m-%d')
        formatted_tarih = dt.strftime('%d/%m/%Y')
        ay_yil = dt.strftime('%m-%Y')
    except ValueError:
        return "Hatalı tarih formatı!", 400

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO calisma (tarih, saat, paket, paket_basi_ucret, saatlik_ucret, toplam_kazanc, ay)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (formatted_tarih, saat, paket, paket_basi_ucret, saatlik_ucret, toplam_kazanc, ay_yil))
        conn.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_data(id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM calisma WHERE id = ?", (id,))
        conn.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_data(id):
    if request.method == 'POST':
        tarih = request.form['tarih']
        try:
            saat = int(request.form['saat'])
        except ValueError:
            saat = 0
        try:
            paket = int(request.form['paket'])
        except ValueError:
            paket = 0
        try:
            paket_basi_ucret = float(request.form['paket_basi_ucret'])
        except ValueError:
            paket_basi_ucret = 0.0
        try:
            saatlik_ucret = float(request.form['saatlik_ucret'])
        except ValueError:
            saatlik_ucret = 0.0

        toplam_kazanc = int(round((paket * paket_basi_ucret) + (saat * saatlik_ucret)))

        try:
            dt = datetime.strptime(tarih, '%Y-%m-%d')
            formatted_tarih = dt.strftime('%d/%m/%Y')
            ay_yil = dt.strftime('%m-%Y')
        except ValueError:
            return "Hatalı tarih formatı!", 400

        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE calisma 
                SET tarih = ?, saat = ?, paket = ?, paket_basi_ucret = ?, saatlik_ucret = ?, toplam_kazanc = ?, ay = ? 
                WHERE id = ?
            """, (formatted_tarih, saat, paket, paket_basi_ucret, saatlik_ucret, toplam_kazanc, ay_yil, id))
            conn.commit()
        return redirect(url_for('index'))

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, tarih, saat, paket, paket_basi_ucret, saatlik_ucret, toplam_kazanc, ay 
            FROM calisma 
            WHERE id = ?
        """, (id,))
        record = cursor.fetchone()
    return render_template('edit.html', record=record)

@app.route('/gecmis/<ay>')
def gecmis_veriler(ay):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, tarih, saat, paket, paket_basi_ucret, saatlik_ucret, toplam_kazanc, ay 
            FROM calisma 
            WHERE ay = ?
        """, (ay,))
        records = cursor.fetchall()

    def safe_int(value):
        try:
            return int(round(float(value)))
        except (ValueError, TypeError):
            return 0

    total_income = sum(safe_int(row[6]) for row in records) if records else 0
    total_income_1_15 = sum(safe_int(row[6]) for row in records if int(row[1].split('/')[0]) <= 15) if records else 0
    total_income_15_31 = sum(safe_int(row[6]) for row in records if int(row[1].split('/')[0]) > 15) if records else 0

    return render_template('gecmis.html', records=records, ay=ay,
                           total_income=total_income,
                           total_income_1_15=total_income_1_15,
                           total_income_15_31=total_income_15_31)

if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import Flask

app = Flask(__name__)
DB_FILE = 'kazanc_data.db'

# Uygulamanızın diğer kodları burada yer alır.

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
