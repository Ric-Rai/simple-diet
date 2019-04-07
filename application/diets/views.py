from flask import render_template
from flask_login import login_required, current_user

from application import app

from application.components import table
from application.diets.models import Diet
from application.diets.forms import DietForm
from application.mealfoods.forms import MealFoodForm


@app.route("/diets/view")
@login_required
def diets_view():
    diets = Diet.query.filter(Diet.account_id == current_user.id).order_by(Diet.edited)
    return table.render_table(rows=diets, form=DietForm(), headers=True, css_class='diets', url='diets', anchors=True)


@app.route("/diets/delete/<diet_id>", methods=["POST"])
@login_required
def diets_delete_row(diet_id):
    return table.delete_row(diet_id, Diet)


@app.route("/diets/input-row/<diet_id>", methods=["GET", "POST"])
@login_required
def diets_render_input_row(diet_id):
    return table.edit_row(diet_id, Diet, DietForm, anchors=True)


@app.route("/diets/input-row", methods=["GET", "POST"])
@login_required
def diets_edit_row():
    return table.new_row(Diet, DietForm, anchors=True)


@app.route("/diets/<diet_id>", methods=["GET"])
@login_required
def diet_view(diet_id):
    diet = Diet.query.get(diet_id)
    headers = ("Ruoka", "Määrä", "Energia", "Proteiini", "Hiilihydraatti", "Rasva")
    url = "diets/" + str(diet_id) + "/meals"
    return render_template("diets/view.html", form=MealFoodForm(), meals=diet.meals, url=url, headers=headers)
