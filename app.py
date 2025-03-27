from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
conversation_history = []

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    # System prompt'u tanımla
    system_prompt = {
        "role": "system",
        "content": (
        "Sen Türkçe konuşan, sade ve samimi bir asistanısın. "
        "Cevaplarını kısa, net, sıcak ve profesyonel ver. "
        "Kullanıcının verdiği mesajlardan şu verileri anlamaya çalış:\n"
        "- Tarih\n"
        "- Paket sayısı\n"
        "- Çalışma süresi\n"
        "- Paket başı ücret\n"
        "- Saatlik ücret\n"
        "Bu bilgileri düzgünce ayrıştır ve net özet ver. Gereksiz uzatma, sayı vermek için varsayım yapma. "
        "Kısa ve güven verici ol."

        )
    }

    # Konuşma geçmişine eklemeden önce prompt'u en başa koy
    full_messages = [system_prompt] + conversation_history + [{"role": "user", "content": user_input}]

    response = requests.post('http://localhost:11434/api/chat', json={
        "model": "mistral",
        "messages": full_messages,
        "stream": False
    })

    reply = response.json()["message"]["content"]

    # Hafızayı güncelle
    conversation_history.append({"role": "user", "content": user_input})
    conversation_history.append({"role": "assistant", "content": reply})

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
