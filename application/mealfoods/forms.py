from flask_login import current_user
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import Length, DataRequired, NumberRange, Optional, ValidationError

from application.mealfoods.models import MealFood
from application.meals.models import Meal
from application.forms import IdField, ModelForm


class MealFoodForm(ModelForm):
    db_model = MealFood
    meal_id = IdField()
    food_name = StringField(None, [Length(min=2), DataRequired()])
    amount = IntegerField(None, [NumberRange(min=0)])
    energy = IntegerField(None, [Optional()], render_kw={"readonly": ""})
    protein = DecimalField(None, [Optional()], render_kw={"readonly": ""})
    carb = DecimalField(None, [Optional()], render_kw={"readonly": ""})
    fat = DecimalField(None, [Optional()], render_kw={"readonly": ""})

    # Override ->
    def populate_obj(self, obj):
        for name, field in self._fields.items():
            if field.render_kw and "readonly" in field.render_kw.keys():
                continue
            field.populate_obj(obj, name)

    # Override ->
    def validate_id_fields(form):
        if form.id and form.id.data:
            id_validation_result = form.validate_id()
            if not id_validation_result:
                return id_validation_result
        if form.meal_id and form.meal_id.data:
            meal_id_result = form.validate_meal_id()
            if not meal_id_result:
                return meal_id_result
        return True

    def validate_meal_id(form, field=None):
        meal = Meal.query.get(form.meal_id.data)
        if meal is None:
            return ValidationError("Invalid identifier for %s" % Meal)
        if meal.account_id is not current_user.id:
            return ValidationError("Unauthorized access")
        return True
