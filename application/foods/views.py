from flask import render_template
from flask_login import login_required, current_user
from sqlalchemy import or_

from application import app

from application.components import table
from application.foods.models import Food
from application.foods.forms import FoodForm


@app.route("/foods/view")
@login_required
def foods_view():
    foods = Food.query.filter(or_(Food.account_id == current_user.id, Food.account_id.is_(None)))\
                .order_by(Food.account_id.desc(), Food.name)
    headers = ("Nimi", "Energia (kcal", "Proteiini", "Hiilihydraatti", "Rasva", "Toiminnot")
#   Not working in Heroku ->
#   heading = "Ruokataulukko, omia ruokia yhteensä: " + str(Food.count_foods_of_user(current_user.id))
    return render_template("components/table.html", rows=foods, headers=headers, table_type="foods", heading=heading)


@app.route("/foods/delete/<food_id>", methods=["POST"])
@login_required
def foods_delete_row(food_id):
    return table.delete_row(food_id, Food)


@app.route("/foods/row/<food_id>")
@login_required
def foods_render_row(food_id):
    return table.render_row(food_id, Food)


@app.route("/foods/input-row/<food_id>", methods=["GET", "POST"])
@login_required
def foods_render_input_row(food_id):
    return table.render_input_row(food_id, Food, FoodForm)


@app.route("/foods/input-row", methods=["GET", "POST"])
@login_required
def foods_render_new_input_row():
    return table.render_new_input_row(Food, FoodForm)
