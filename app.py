from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

@app.route('/api/user', methods=['GET'])
def api_get_user():
    print("api_get_user")
    return jsonify({"user1": "John", "user2": "Jane"})

@app.route('/api/user', methods=['POST'])
def api_post_user():
    print("api_post_user")
    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)