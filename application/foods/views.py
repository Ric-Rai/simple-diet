import os

from flask import render_template, jsonify
from flask_login import login_required, current_user
from sqlalchemy import or_
from sqlalchemy.orm import load_only

from application import app

from application.components import table
from application.foods.models import Food
from application.foods.forms import FoodForm


@app.route("/foods/view")
@login_required
def foods_view():
    if os.environ.get("HEROKU"):
        foods = Food.query.filter(or_(Food.account_id == current_user.id, Food.account_id.is_(None))) \
            .order_by(Food.account_id.asc(), Food.name)
    else:
        foods = Food.query.filter(or_(Food.account_id == current_user.id, Food.account_id.is_(None))) \
            .order_by(Food.account_id.desc(), Food.name)
    return render_template("components/table.html", rows=foods, css_class="foods", url="foods", form=FoodForm())


@app.route("/foods/delete", methods=["POST"])
@login_required
def foods_delete_row():
    return table.delete_row(Food, FoodForm)


@app.route("/foods/edit", methods=["GET", "POST"])
@login_required
def foods_edit_row():
    return table.edit_row(Food, FoodForm)


@app.route("/foods/new", methods=["GET", "POST"])
@login_required
def foods_new_row():
    return table.new_row(Food, FoodForm)


@app.route("/foods/list")
@login_required
def foods_list():
    foods = Food.query.filter(or_(Food.account_id == current_user.id, Food.account_id.is_(None)))\
        .options(load_only("name"))
    return jsonify([food.name for food in foods])
