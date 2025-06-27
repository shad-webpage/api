from flask import Flask, jsonify, request

app = Flask(__name__)

# Route اصلی برای تست
@app.route('/')
def home():
    return jsonify({
        "message": "سلام! به API من خوش آمدید!",
        "status": "فعال",
        "routes": {
            "home": "/",
            "test": "/test",
            "echo": "/echo",
            "data": "/data"
        }
    })

# Route تستی
@app.route('/test')
def test():
    return jsonify({"message": "سرور به درستی کار می‌کند!", "success": True})

# Route برای echo کردن داده ورودی
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not data:
        return jsonify({"error": "داده‌ای دریافت نشد"}), 400
    return jsonify({"received_data": data, "message": "داده شما دریافت شد"})

# Route برای دریافت داده نمونه
@app.route('/data')
def get_data():
    sample_data = {
        "users": [
            {"id": 1, "name": "علی"},
            {"id": 2, "name": "رضا"},
            {"id": 3, "name": "سارا"}
        ],
        "products": [
            {"id": 101, "name": "ماوس", "price": 150000},
            {"id": 102, "name": "کیبورد", "price": 300000}
        ]
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
