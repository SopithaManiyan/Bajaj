from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/process', methods=['POST'])
def process_data():
    input_data = request.json.get('input_data', [])
    num_list = [item for item in input_data if item.isdigit()]
    alpha_list = [item for item in input_data if item.isalpha()]
    max_lower = max([char for char in alpha_list if char.islower()], default='', key=lambda x: ord(x))

    response = {
        "status": "success",
        "user_info": {
            "user_id": "your_username_date_of_birth",
            "email": "your_email@example.com",
            "roll_number": "your_roll_number",
        },
        "output": {
            "numbers": num_list,
            "alphabets": alpha_list,
            "max_lowercase": max_lower
        }
    }
    return jsonify(response)

@app.route('/code', methods=['GET'])
def get_code():
    return jsonify({"code": 12345})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
