from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# POST Method
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"
    
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [char for char in data if char.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

    # Query parameters
    is_number = request.args.get('isNumber') == 'true'
    is_alphabet = request.args.get('isAlphabet') == 'true'
    is_highest_lowercase_alphabet = request.args.get('isHighestLowercaseAlphabet') == 'true'
    
    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers if is_number or not (is_alphabet or is_highest_lowercase_alphabet) else [],
        "alphabets": alphabets if is_alphabet or not (is_number or is_highest_lowercase_alphabet) else [],
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if (is_highest_lowercase_alphabet or not (is_number or is_alphabet)) and highest_lowercase_alphabet else []
    }

    return jsonify(response)

# GET Method
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
