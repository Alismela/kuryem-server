from jinja2 import Template

# Jinja2 HTML Şablonu
template_str = """ 
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Pizza V Kurye Takip</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background-color: #f4f4f4; }
        h1 { text-align: center; color: #333; }
        table { width: 100%; max-width: 800px; margin: 20px auto; border-collapse: collapse; background: white; }
        th, td { padding: 10px; border: 1px solid #ddd; text-align: center; }
        th { background: #4CAF50; color: white; }
        tr:nth-child(even) { background: #f2f2f2; }
    </style>
</head>
<body>

<h1>Pizza V Kurye Takip Sistemi</h1>

<h3>1-15 Arası Kazanç: {{ kazanc_1_15 }} TL</h3>
<h3>16-31 Arası Kazanç: {{ kazanc_16_31 }} TL</h3>
<h2>Toplam Kazanç: {{ kazanc_1_15 + kazanc_16_31 }} TL</h2>

<table>
    <tr>
        <th>Tarih</th>
        <th>Çalışma Saati</th>
        <th>Paket Sayısı</th>
        <th>Toplam Kazanç</th>
    </tr>
    {% for row in calisma %}
    <tr>
        <td>{{ row['tarih'] }}</td>
        <td>{{ row['saat'] }}</td>
        <td>{{ row['paket'] }}</td>
        <td>{{ row['saat'] * row['saatlik_ucret'] + row['paket'] * row['paket_ucret'] }} TL</td>
    </tr>
    {% endfor %}
</table>

</body>
</html>
"""

# Jinja2 şablonunu oluştur
template = Template(template_str)

# Örnek veri
data = {
    "kazanc_1_15": 5000,
    "kazanc_16_31": 6000,
    "calisma": [
        {"tarih": "2025-02-10", "saat": 8, "paket": 20, "saatlik_ucret": 50, "paket_ucret": 10},
        {"tarih": "2025-02-11", "saat": 7, "paket": 15, "saatlik_ucret": 50, "paket_ucret": 10},
    ]
}

# Şablonu verilerle işleyerek HTML çıktısı al
html_output = template.render(data)

# HTML dosyasına kaydet
with open("pizza_v_kurye_takip.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("✅ HTML dosyası oluşturuldu: pizza_v_kurye_takip.html")
