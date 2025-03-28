from flask import Flask, request, jsonify
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import google.auth.crypt
import google.auth.jwt
import requests
import json
import os
import base64

app = Flask(__name__)

# 🌐 Google'ın doğrulama URL'si
GOOGLE_API_URL = "https://playintegrity.googleapis.com/v1/integrityTokens:decode"

# 🔐 Ortam değişkeninden base64 olarak şifrelenmiş JSON key'i al
json_key_base64 = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "").strip()
if not json_key_base64:
    raise Exception("❌ GOOGLE_SERVICE_ACCOUNT_JSON ortam değişkeni boş geldi!")

# 🔓 Base64 çözümle
try:
    decoded_str = base64.b64decode(json_key_base64).decode("utf-8")
except Exception as e:
    raise Exception(f"🧨 Base64 çözümleme başarısız: {e}")

# 📄 JSON çözümle
try:
    json_key_dict = json.loads(decoded_str)
except json.JSONDecodeError as e:
    raise Exception(f"❌ JSON decode hatası: {e}")

# 🎫 Kimlik bilgilerini oluştur
credentials = service_account.Credentials.from_service_account_info(
    json_key_dict,
    scopes=["https://www.googleapis.com/auth/playintegrity"]
)

@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    integrity_token = data.get("token")

    if not integrity_token:
        return jsonify({"error": "Token eksik"}), 400

    # 🔑 Erişim token’ı oluştur
    authed_session = Request()
    credentials.refresh(authed_session)
    access_token = credentials.token

    # 📡 Google'a doğrulama isteği gönder
    response = requests.post(
        GOOGLE_API_URL,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        json={"integrityToken": integrity_token}
    )

    if response.status_code != 200:
        print("❌ Doğrulama başarısız:", response.text)
        return jsonify({"is_premium": False, "error": "Doğrulama başarısız"}), 401

    decoded = response.json()
    print("✅ Doğrulanan yanıt:", json.dumps(decoded, indent=2))

    # 🏷️ Lisans kontrolü
    license_status = decoded.get("accountDetails", {}).get("appLicensingVerdict", "UNLICENSED")
    is_premium = license_status == "LICENSED"

    return jsonify({"is_premium": is_premium})
@app.route('/')
def home():
    return "🚀 Kuryem API çalışıyor!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
