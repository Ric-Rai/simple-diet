from flask import render_template, abort
from flask_login import login_required, current_user

from application import app

from application.components import table
from application.diets.models import Diet
from application.diets.forms import DietForm
from application.mealfoods.forms import MealFoodForm


@app.route("/diets/view")
@login_required
def diets_view():
    diets = current_user.diets.order_by(Diet.edited.desc())
    return table.render_table(rows=diets, form=DietForm(), headers=True, css_class='diets', url='diets', anchors=True)


@app.route("/diets/delete", methods=["POST"])
@login_required
def diets_delete_row():
    return table.delete_row(Diet, DietForm)


@app.route("/diets/edit", methods=["GET", "POST"])
@login_required
def diets_edit_row():
    return table.edit_row(Diet, DietForm, anchors=True)


@app.route("/diets/new", methods=["GET", "POST"])
@login_required
def diets_new_row():
    return table.new_row(Diet, DietForm, anchors=True)


@app.route("/diets/<diet_id>", methods=["GET"])
@login_required
def diet_view(diet_id):
    form = DietForm()
    form.id.data = diet_id
    if not form.validate_id():
        abort(422)
    diet = Diet.query.get(diet_id)
    url = "diets/" + str(diet_id) + "/meals"
    return render_template("diets/view.html", form=MealFoodForm(), diet=diet, url=url,
                           add_url='/meals/new?diet_id=%s' % diet_id)
