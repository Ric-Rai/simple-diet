from flask_login import current_user
from wtforms import ValidationError

from application.diets.models import Diet
from application.meals.models import Meal
from application.forms import ModelForm, IdField


class MealForm(ModelForm):
    db_model = Meal
    diet_id = IdField()

    # Override ->
    def validate_id_fields(form):
        if form.id and form.id.data:
            id_validation_result = form.validate_id()
            if not id_validation_result:
                return id_validation_result
        if form.diet_id and form.diet_id.data:
            diet_id_result = form.validate_diet_id()
            if not diet_id_result:
                return diet_id_result
        return True

    def validate_diet_id(form, field=None):
        diet = Diet.query.get(form.diet_id.data)
        if diet is None:
            return ValidationError("Invalid identifier for %s" % Diet)
        if diet.account_id is not current_user.id:
            return ValidationError("Unauthorized access")
        return True
