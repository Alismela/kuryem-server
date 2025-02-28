from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("kurye_takip.db")
    conn.row_factory = sqlite3.Row
    return conn


# 1-15 aras?nda kazanc? hesaplayan fonksiyon
def get_aylik_kazanc_1_15():
    conn = get_db_connection()
    cursor = conn.cursor()
    ay_baslangic = datetime.datetime.now().replace(day=1).strftime('%d-%m-%Y')
    ay_ortasi = (datetime.datetime.now().replace(day=15)).strftime('%d-%m-%Y')

    cursor.execute('''
        SELECT SUM(saat * saatlik_ucret + paket * paket_ucret) as toplam_kazanc
        FROM calisma
        WHERE tarih >= ? AND tarih <= ?''', (ay_baslangic, ay_ortasi))
    sonuc = cursor.fetchone()
    conn.close()
    return sonuc['toplam_kazanc'] if sonuc['toplam_kazanc'] else 0


# 16-31 aras?nda kazanc? hesaplayan fonksiyon
import calendar
import datetime


def get_aylik_kazanc_16_31():
    # ?u anki tarihin y?l? ve ay?
    yil = datetime.datetime.now().year
    ay = datetime.datetime.now().month

    # Ay?n 16's?
    ay_baslangic = datetime.datetime(yil, ay, 16).strftime('%d-%m-%Y')

    # Ay?n son g?n?
    son_gun = calendar.monthrange(yil, ay)[1]  # Ay?n ka? g?n s?rd???n? al?r
    ay_son = datetime.datetime(yil, ay, son_gun).strftime('%d-%m-%Y')

    # Veritaban? sorgusunu yap
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT SUM(saat * saatlik_ucret + paket * paket_ucret) as toplam_kazanc 
        FROM calisma WHERE tarih >= ? AND tarih <= ?''', (ay_baslangic, ay_son))
    sonuc = cursor.fetchone()
    conn.close()

    return sonuc['toplam_kazanc'] if sonuc['toplam_kazanc'] else 0


@app.route('/')
def index():
    conn = get_db_connection()
    calisma = conn.execute('SELECT * FROM calisma ORDER BY tarih DESC').fetchall()
    conn.close()

    kazanc_1_15 = get_aylik_kazanc_1_15()
    kazanc_16_31 = get_aylik_kazanc_16_31()

    return render_template('index.html',
                           calisma=calisma,
                           kazanc_1_15=kazanc_1_15,
                           kazanc_16_31=kazanc_16_31)


@app.route('/add', methods=['POST'])
def add():
    tarih = request.form['tarih']
    saat = int(request.form['saat'])
    paket = int(request.form['paket'])
    saatlik_ucret = int(request.form['saatlik_ucret'])
    paket_ucret = int(request.form['paket_ucret'])

    conn = get_db_connection()
    conn.execute('INSERT INTO calisma (tarih, saat, paket, saatlik_ucret, paket_ucret) VALUES (?, ?, ?, ?, ?)',
                 (tarih, saat, paket, saatlik_ucret, paket_ucret))
    conn.commit()
    conn.close()
    return redirect('/')


# Kayd? Silme
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM calisma WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')


# Kayd? G?ncelleme
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()

    if request.method == 'POST':
        tarih = request.form['tarih']
        saat = int(request.form['saat'])
        paket = int(request.form['paket'])
        saatlik_ucret = int(request.form['saatlik_ucret'])
        paket_ucret = int(request.form['paket_ucret'])

        conn.execute('''
            UPDATE calisma 
            SET tarih = ?, saat = ?, paket = ?, saatlik_ucret = ?, paket_ucret = ? 
            WHERE id = ?''',
                     (tarih, saat, paket, saatlik_ucret, paket_ucret, id))
        conn.commit()
        conn.close()
        return redirect('/')

    row = conn.execute('SELECT * FROM calisma WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', row=row)


if __name__ == '__main__':
    app.run(debug=True)
