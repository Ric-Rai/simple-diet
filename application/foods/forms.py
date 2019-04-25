from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import Length, DataRequired, NumberRange, ValidationError

from application import app
from application.foods.models import Food
from application.forms import ModelForm


class FoodForm(ModelForm):
    db_model = Food
    name = StringField(None, [Length(min=2), DataRequired()])
    energy = IntegerField(None, [NumberRange(min=0, max=1000)], default=0)
    protein = DecimalField(None, [NumberRange(min=0, max=100)], default=0)
    carb = DecimalField(None, [NumberRange(min=0, max=100)], default=0)
    fat = DecimalField(None, [NumberRange(min=0, max=100)], default=0)
    headers = ("Nimi", "Energia (kcal)", "Proteiini", "Hiilihydraatti", "Rasva")

    @staticmethod
    def validate_name(form, field):
        app.logger.info("validating food name")
        error = ValidationError("Tämän niminen ruoka on jo tallennettu taulukkoon. "
                                "Ruokien nimien tulee olla uniikkeja.")

        for food in Food.cache.values():
            if food.name == field.data:
                if not form.id:
                    raise error
                if food.id is not form.id.data:
                    raise error
