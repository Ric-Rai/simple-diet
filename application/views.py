from flask import render_template
from flask_login import login_required

from application import app
from application.overview import Overview


@app.route("/")
def index():
    return render_template("index.html")


@login_required
@app.route("/overview")
def overview():
    return render_template("overview.html", overview=Overview())
