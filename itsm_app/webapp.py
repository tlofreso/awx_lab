from flask import Flask

app = Flask(__name__)


@app.route("/")
def web_form():
    return "Let's build a new server."