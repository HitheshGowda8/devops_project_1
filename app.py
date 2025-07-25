from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
        return "Hey I am Hithesh Gowda"

@app.route("/phone")
def lwphone():
        return "1234567890"

app.run(host="0.0.0.0", port=5001)


