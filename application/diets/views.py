from flask import render_template
from flask_login import login_required, current_user

from application import app

from application.components import table
from application.diets.models import Diet
from application.diets.forms import DietForm


@app.route("/diets/view")
@login_required
def diets_view():
    diets = Diet.query.filter(Diet.account_id == current_user.id).order_by(Diet.edited)
    headers = ("Nimi", "Muokattu", "Toiminnot")
    return table.render_table(diets, headers, table_type="diets", anchors=True)


@app.route("/diets/delete/<diet_id>", methods=["POST"])
@login_required
def diets_delete_row(diet_id):
    return table.delete_row(diet_id, Diet)


@app.route("/diets/row/<diet_id>")
@login_required
def diets_render_row(diet_id):
    return table.render_row(diet_id, Diet, anchors=True)


@app.route("/diets/input-row/<diet_id>", methods=["GET", "POST"])
@login_required
def diets_render_input_row(diet_id):
    return table.render_input_row(diet_id, Diet, DietForm)


@app.route("/diets/input-row", methods=["GET", "POST"])
@login_required
def diets_render_new_input_row():
    return table.render_new_input_row(Diet, DietForm, anchors=True)


@app.route("/diets/<diet_id>", methods=["GET"])
@login_required
def diet_view(diet_id):
    diet = Diet.query.get(diet_id)
#   headers = ("Nimi", "Muokattu", "Toiminnot")
    return render_template("diets/view.html", meals=diet.meals, table_type="meals")
