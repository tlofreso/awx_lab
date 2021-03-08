from flask import render_template, redirect
from app import app
from app.forms import NewServer


@app.route("/", methods=["GET", "POST"])
def web_form():
    form = NewServer()
    if form.validate_on_submit():
        name = form.name.data
        region = form.region.data
        size = form.size.data
        image = form.image.data

        payload = {"name": name, "region": region, "size": size, "image": image}

        print(payload)

        return redirect("/")

    return render_template("index.html", title="Home", form=form)
