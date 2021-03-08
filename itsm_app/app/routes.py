from flask import render_template
from app import app
from app.forms import NewServer


@app.route("/")
def web_form():
    form = NewServer()
    return render_template("index.html", title="Home", form=form)
