from jinja2 import Template

template_str = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pizza V Kurye Takip Sistemi</title>
    <style>
        /* Genel stil ayarları */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        h1, h2 {
            color: #333;
            text-align: center;
        }

        table {
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
            background-color: #fff;
        }

        table, th, td {
            border: 1px solid #ddd;
        }

        th, td {
            padding: 10px;
            text-align: center;
        }

        th {
            background-color: #4CAF50;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        tr:hover {
            background-color: #ddd;
        }

        form {
            margin: 20px auto;
            width: 80%;
            max-width: 500px;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        form input[type="text"], form input[type="number"] {
            width: calc(100% - 20px);
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        form input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        form input[type="submit"]:hover {
            background-color: #45a049;
        }

        a {
            color: #4CAF50;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Pizza V Kurye Takip Sistemi</h1>

    <!-- 1-15 arası kazanç -->
    <h2>1-15 Arası Kazanç: {{ kazanc_1_15 }} TL</h2>

    <!-- 16-31 arası kazanç -->
    <h2>16-31 Arası Kazanç: {{ kazanc_16_31 }} TL</h2>

    <!-- Toplam kazanç -->
    <h2>Toplam Kazanç: {{ kazanc_1_15 + kazanc_16_31 }} TL</h2>

    <table>
        <tr>
            <th>Tarih</th>
            <th>Çalışma Saati</th>
            <th>Paket Sayısı</th>
            <th>Toplam Kazanç</th>
            <th>İşlemler</th>
        </tr>
        {% for row in calisma %}
        <tr>
            <td>{{ row['tarih'] }}</td>
            <td>{{ row['saat'] }}</td>
            <td>{{ row['paket'] }}</td>
            <td>{{ row['saat'] * row['saatlik_ucret'] + row['paket'] * row['paket_ucret'] }}</td>
            <td>
                <form action="/delete/{{ row['id'] }}" method="post" style="display:inline;">
                    <input type="submit" value="Sil">
                </form>
                <a href="/edit/{{ row['id'] }}">Düzenle</a>
            </td>
        </tr>
        {% endfor %}
    </table>

    <h2>Yeni Kayıt Ekle</h2>
    <form action="/add" method="post">
        <label for="tarih">Tarih:</label>
        <input type="text" name="tarih" required><br>

        <label for="saat">Çalışma Saati:</label>
        <input type="number" name="saat" required><br>

        <label for="paket">Paket Sayısı:</label>
        <input type="number" name="paket" required><br>

        <label for="saatlik_ucret">Saatlik Ücret:</label>
        <input type="number" name="saatlik_ucret" required><br>

        <label for="paket_ucret">Paket Başı Ücret:</label>
        <input type="number" name="paket_ucret" required><br>

        <input type="submit" value="Ekle">
    </form>
</body>
</html>
"""

# Örnek veri
data = {
    "kazanc_1_15": 5000,
    "kazanc_16_31": 6000,
    "calisma": [
        {"id": 1, "tarih": "2025-02-10", "saat": 8, "paket": 20, "saatlik_ucret": 50, "paket_ucret": 10},
        {"id": 2, "tarih": "2025-02-11", "saat": 7, "paket": 15, "saatlik_ucret": 50, "paket_ucret": 10},
    ]
}

# Şablonu verilerle işleyerek HTML çıktısı al
template = Template(template_str)
html_output = template.render(data)

# HTML dosyasına kaydet
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_output)
