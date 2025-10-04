from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! This is my simple Flask web service on Render."

@app.route('/add', methods=['GET'])
def add_numbers():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify({'error': 'Please provide a and b in the URL like /add?a=2&b=3'})
    return jsonify({'result': a + b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
