from flask_login import login_required

from application import app

from application.components import table
from application.mealfoods.models import MealFood
from application.mealfoods.forms import MealFoodForm


@app.route("/mealfoods/delete", methods=["POST"])
@login_required
def mealfoods_delete_row():
    return table.delete_row(MealFood, MealFoodForm)


@app.route("/mealfoods/edit", methods=["GET", "POST"])
@login_required
def mealfoods_edit_row():
    return table.edit_row(MealFood, MealFoodForm)


@app.route("/mealfoods/new", methods=["GET", "POST"])
@login_required
def mealfoods_new_row():
    return table.new_row(MealFood, MealFoodForm)
