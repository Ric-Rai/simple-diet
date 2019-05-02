from flask import render_template
from flask_login import login_required, current_user

from application import app
from application.overview import Overview


@app.route("/")
def index():
    if current_user.is_authenticated:
        return overview()
    return render_template("index.html")


@app.route("/overview")
@login_required
def overview():
    return render_template("overview.html", overview=Overview())
