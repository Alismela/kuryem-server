import os
import json
import base64

json_key_base64 = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
print("GELEN ŞİFRELİ JSON:", json_key_base64[:100])  # İlk 100 karakteri yaz

# Eğer None veya boş ise:
if not json_key_base64:
    raise Exception("🚫 Ortam değişkeni boş gelmiş!")

# Base64 çöz
try:
    json_key_str = base64.b64decode(json_key_base64).decode('utf-8')
except Exception as e:
    raise Exception(f"🧨 Base64 decode edilemedi: {e}")

print("ÇÖZÜLEN JSON:", json_key_str[:100])  # İlk 100 karakteri göster

# JSON parse
try:
    json_key_dict = json.loads(json_key_str)
except Exception as e:
    raise Exception(f"❌ JSON decode hatası: {e}")
