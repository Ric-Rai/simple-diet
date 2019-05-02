from flask_login import current_user
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import Length, DataRequired, NumberRange, ValidationError

from application.foods.models import Food
from application.forms import ModelForm


class FoodForm(ModelForm):
    energy_msg = "Ruoan energiamäärän sataa grammaa kohden tulee olla kokonaisluku väliltä 0-1000. Puhtaalla rasvalla "\
                 "on korkein mahdollinen ruoan energiapitoisuus, joka on noin 920 kcal / 100 g."
    macro_msg = "Makroravinteen määrän sataa grammaa kohden tulee olla kokonaisluku väliltä 0-100"
    db_model = Food
    name = StringField(None, [Length(min=2), DataRequired(message="Ruoan nimi puuttuu")])
    energy = IntegerField(None, [NumberRange(min=0, max=1000, message=energy_msg)], default=0)
    protein = DecimalField(None, [NumberRange(min=0, max=100, message=macro_msg)], default=0)
    carb = DecimalField(None, [NumberRange(min=0, max=100, message=macro_msg)], default=0)
    fat = DecimalField(None, [NumberRange(min=0, max=100, message=macro_msg)], default=0)
    heading = "Ruokataulukko"
    headers = ("Nimi", "Energia (kcal)", "Proteiini (g)", "Hiilihydraatti (g)", "Rasva (g)")

    @staticmethod
    def validate_name(form, field):
        food = current_user.foods.filter_by(name=field.data).first()
        error = ValidationError("Tämän niminen ruoka on jo tallennettu taulukkoon. "
                                "Ruokien nimien tulee olla uniikkeja.")
        if food is not None:
            if not form.id:
                raise error
            if food.id is not form.id.data:
                raise error
