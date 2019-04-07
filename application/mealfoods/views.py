from flask import render_template, request, abort
from flask_login import login_required, current_user

from application import app, db

from application.components import table
from application.mealfoods.models import MealFood
from application.mealfoods.forms import MealFoodForm
from application.meals.models import Meal


@app.route("/meals/<meal_id>/foods/delete/<mealfood_id>", methods=["POST"])
@login_required
def mealfoods_delete_row(meal_id, mealfood_id):
    return table.delete_row(mealfood_id, MealFood)


@app.route("/meals/<meal_id>/foods/input-row/<mealfood_id>", methods=["GET", "POST"])
@login_required
def mealfoods_edit_row(meal_id, mealfood_id):
    return table.edit_row(mealfood_id, MealFood, MealFoodForm)


@app.route("/meals/<meal_id>/foods/input-row", methods=["GET", "POST"])
@login_required
def mealfoods_new_row(meal_id):
    form = MealFoodForm()
    form.meal_id.data = meal_id
    return table.new_row(MealFood, MealFoodForm, initial_form=form)


def check_rights(meal_id):
    meal_account_id = db.session.query(Meal.account_id).filter_by(id=meal_id).scalar()
    if meal_account_id is not current_user.id:
        abort(401)
