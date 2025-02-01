from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("base.html", title="Home")

@main.route("/skill")
def skill():
    return render_template("skill.html", title="Skills")

@main.route("/about")
def about():
    return render_template("about.html", title="About")

@main.route("/connect")
def connect():
    return render_template("connect.html", title="Connect")
