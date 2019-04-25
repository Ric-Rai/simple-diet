from collections import OrderedDict

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
    if Food.cache:
        foods = sorted(Food.cache.values(), key=lambda v: v.name)
        foods = sorted(foods, key=lambda v: v.account_id is None)
    else:
        foods = Food.query.filter(or_(Food.account_id == current_user.id, Food.account_id.is_(None)))\
                .order_by(Food.account_id.desc(), Food.name)
        Food.to_cache(foods)

    return render_template("components/table.html", rows=foods, headers=True, css_class="foods", url="foods", form=FoodForm())


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
