from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message":"Hello, World!"})

@app.route("/message")
def message():
    return jsonify({"message":"This is a message!"})

@app.route("/about")
def about():
    return jsonify({"message":"This is the about page!"})

if __name__ == "__main__":
    app.run(debug=False)