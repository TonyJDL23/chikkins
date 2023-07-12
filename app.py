from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/sal")
def sal():
    return jsonify({"message": "pong!"})


if __name__ == "__main__":
    app.run(debug=True, port=4000)
