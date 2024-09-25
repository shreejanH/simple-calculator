from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    x = data.get('x')
    y = data.get('y')

    if operation == 'add':
        result = x + y
    elif operation == 'subtract':
        result = x - y
    elif operation == 'multiply':
        result = x * y
    elif operation == 'divide':
        if y != 0:
            result = x / y
        else:
            return jsonify({"error": "Division by zero"}), 400
    else:
        return jsonify({"error": "Invalid operation"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Changed to port 80
