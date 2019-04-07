from flask import render_template, request, Response, abort
from flask_login import login_required, current_user

from application import app, db

from application.diets.models import Diet
from application.mealfoods.forms import MealFoodForm
from application.meals.models import Meal


@app.route("/meals/delete/<meal_id>", methods=["POST"])
@login_required
def meals_delete_row(meal_id):
    Meal.query.filter(Meal.id == meal_id).delete()
    db.session.commit()
    return Response("", status=200, mimetype='text/plain')


@app.route("/diets/<diet_id>/meals/input-row", methods=["GET"])
@login_required
def meals_new_row(diet_id):
    diet = Diet.query.get(diet_id)
    meal = Meal()
    meal.order_num = diet.meals_query.count() + 1
    diet.meals.append(meal)
    db.session.commit()
    url = "meals/" + str(meal.id) + "/foods"
    return render_template("meals/meal-row.html", meal=meal, form=MealFoodForm(), url=url)
