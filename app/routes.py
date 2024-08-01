from flask import render_template # type: ignore
from app import app
from .posts import posts


@app.route("/")
def hello_world():
    user = {"username": "ljawla"}
    return render_template("index.html", user=user, posts=posts)