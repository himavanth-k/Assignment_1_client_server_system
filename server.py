from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/send', methods=['POST'])
def send_message():
    content = request.json.get('content')
    if content:
        messages.append(content)
        return jsonify({"message": "Message sent successfully!"}), 200
    else:
        return jsonify({"error": "Invalid message content!"}), 400

@app.route('/receive', methods=['GET'])
def receive_messages():
    return jsonify({"messages": messages}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
