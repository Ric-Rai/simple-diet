from flask_login import login_required

from application import app, db
from flask import render_template, request, Response

from application.foods.models import Food
from application.foods.forms import FoodForm



@app.route("/foods/view")
@login_required
def foods_view():
    foods = Food.query.all()

    def to_dict(row):
        return dict((col, getattr(row, col)) for col in row.__table__.columns.keys())

    return render_template("foods/table.html", rows=map(to_dict, foods))


@app.route("/foods/delete/<food_id>", methods=["POST"])
@login_required
def foods_delete(food_id):
    food = Food.query.get(food_id)

    if food is not None:
        db.session().delete(food)
        db.session().commit()
        return Response("", status=200, mimetype='text/plain')

    return Response("", status=404, mimetype='text/plain')


@app.route("/foods/row/<food_id>")
@login_required
def foods_row(food_id):
    food = Food.query.get(food_id)

    if food is None:
        return Response("", status=404, mimetype='text/plain')

    row_dict = dict((col, getattr(food, col)) for col in food.__table__.columns.keys())
    return render_template("foods/row.html", row_dict=row_dict)


@app.route("/foods/input-row/<food_id>", methods=["GET", "POST"])
@login_required
def foods_input_row(food_id):
    food = Food.query.get(food_id)

    if food is None:
        return Response("", status=404, mimetype='text/plain')

    if request.method == "GET":
        row_dict = dict((col, getattr(food, col)) for col in food.__table__.columns.keys())
        return render_template("foods/input-row.html", row_dict=row_dict, form=FoodForm())

    form = FoodForm(request.form)

    if not form.validate():

        return render_template("foods/input-row.html", form=form), 422

    food.name = form.name.data
    food.energy = form.energy.data
    food.protein = form.protein.data
    food.carb = form.carb.data
    food.fat = form.fat.data

    db.session().add(food)
    db.session().commit()

    food = Food.query.get(food_id)
    row_dict = dict((col, getattr(food, col)) for col in food.__table__.columns.keys())
    return render_template("foods/row.html", row_dict=row_dict)


@app.route("/foods/input-row", methods=["GET", "POST"])
@login_required
def foods_input_form():
    if request.method == "GET":
        return render_template("foods/input-row.html", form=FoodForm(), row_id="")

    form = FoodForm(request.form)

    if not form.validate():
        return render_template("foods/input-row.html", form=form), 422

    food = Food(form.name.data, form.energy.data, form.protein.data, form.carb.data, form.fat.data)
    db.session().add(food)
    db.session().commit()

    row_dict = dict((col, getattr(food, col)) for col in food.__table__.columns.keys())
    return render_template("foods/row.html", row_dict=row_dict)

