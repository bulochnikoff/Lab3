import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

from api.v1.sensors import bp as sensors_bp
app.register_blueprint(sensors_bp)
# Глобальный обработчик ошибок 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Invalid input", "details": str(error.description)}), 400
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)