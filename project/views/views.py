from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

main = Blueprint("main", __name__, template_folder="templates", static_folder="static")


@main.route("/")
@login_required
def index():
    try:
        print("this happens first")
        return render_template("index.html") 
    except Exception as e:
        abort(500)


@main.route("/profile")
@login_required
def profile():
    try:
        return render_template("profile.html", name=current_user.name)
    except Exception as e:
        abort(500)