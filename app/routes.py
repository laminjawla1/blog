from app import app
from .posts import posts
from .forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route("/")
def index():
    user = {"username": "sage"}
    return render_template("index.html", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested by {form.username.data}, remember_me={form.remember_me.data}")
        return redirect(url_for("index"))
    return render_template("login.html", form=form, title="Sign In")