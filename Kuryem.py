from flask import Flask, request, jsonify
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import google.auth.crypt
import google.auth.jwt
import requests
import json

app = Flask(__name__)

# 📁 İndirdiğin JSON key dosyasının yolu (aynı klasördeyse sadece dosya adı yeterli)
SERVICE_ACCOUNT_FILE = r"C:\Users\Alismela\Desktop\Kuryem\kuryem-app-cloud-4b93ea15e57d.json"


# Google'ın doğrulama URL'si
GOOGLE_API_URL = "https://playintegrity.googleapis.com/v1/integrityTokens:decode"

# Kimlik bilgilerini al
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/playintegrity"]
)

@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    integrity_token = data.get("token")

    if not integrity_token:
        return jsonify({"error": "Token eksik"}), 400

    # 🧠 JWT imzalı erişim token'ı oluştur
    authed_session = Request()
    credentials.refresh(authed_session)
    access_token = credentials.token

    # Google'a token'ı doğrulama isteği gönder
    response = requests.post(
        GOOGLE_API_URL,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        },
        json={"integrityToken": integrity_token}
    )

    if response.status_code != 200:
        print("Doğrulama başarısız:", response.text)
        return jsonify({"is_premium": False, "error": "Doğrulama başarısız"}), 401

    decoded = response.json()
    print("Doğrulanan yanıt:", json.dumps(decoded, indent=2))

    # 🎯 Örnek olarak sadece lisans kontrolüne göre premium belirleyelim
    license_status = decoded.get("accountDetails", {}).get("appLicensingVerdict", "UNLICENSED")

    is_premium = license_status == "LICENSED"
    return jsonify({"is_premium": is_premium})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
