from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
        return "Hello there I am Hithesh gowda"

@app.route("/phone")
def lwphone():
        return "123456789"

app.run(host="0.0.0.0", port=5001)


