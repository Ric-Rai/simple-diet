from flask import render_template, request, Response, abort
from flask_login import login_required

from application import app, db

from application.diets.models import Diet
from application.mealfoods.forms import MealFoodForm
from application.meals.forms import MealForm
from application.meals.models import Meal


@app.route("/meals/delete", methods=["POST"])
@login_required
def meals_delete_row():
    form = MealForm(request.form)
    if not form.validate_id_fields():
        abort(401)
    meal = Meal.query.get(form.id.data)
    db.session.delete(meal)
    i = 1
    for meal in meal.diet.meals_query.order_by(Meal.order_num).all():
        meal.order_num = i
        i += 1
    db.session.commit()
    return Response("", status=200, mimetype='text/plain')


@app.route("/meals/new", methods=["GET"])
@login_required
def meals_new_row():
    form = MealForm(request.args)
    if not form.validate_id_fields():
        abort(401)
    diet = Diet.query.get(form.diet_id.data)
    meal = Meal()
    meal.order_num = diet.meals_query.count() + 1
    diet.meals.append(meal)
    db.session.commit()
    url = "meals/" + str(meal.id) + "/foods"
    return render_template("meals/meal-row.html", meal=meal, form=MealFoodForm(), url=url)
