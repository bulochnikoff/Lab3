import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from api import api   # импортируем настроенный API из папки api

load_dotenv()

app = Flask(__name__)

# Подключаем flask-restx к приложению
api.init_app(app)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)