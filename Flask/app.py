from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, good evening!"

@app.route('/api/data')
def get_data():
    sample_data = {"message": "This is a sample API response", "status": "success"}
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
