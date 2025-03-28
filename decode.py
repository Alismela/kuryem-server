import json
import base64

# 1. JSON içeriğini sözlük olarak yaz
json_data = {

}

# 2. JSON'u stringe çevir
json_string = json.dumps(json_data, separators=(',', ':'))

# 3. Base64'e çevir
encoded = base64.b64encode(json_string.encode('utf-8')).decode('utf-8')

# 4. Sonucu yazdır veya dosyaya kaydet
print("Base64 Şifreli JSON:")
print(encoded)

# (Opsiyonel) Dosyaya yaz
with open("encoded_json.txt", "w", encoding="utf-8") as f:
    f.write(encoded)
