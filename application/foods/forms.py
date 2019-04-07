from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import Length, DataRequired, NumberRange


class FoodForm(FlaskForm):
    name = StringField("Nimi", [Length(min=2), DataRequired()])
    energy = IntegerField("Energia", [NumberRange(min=0, max=1000)])
    protein = DecimalField("Proteiini", [NumberRange(min=0, max=100)])
    carb = DecimalField("Hiilihydraatti", [NumberRange(min=0, max=100)])
    fat = DecimalField("Rasva", [NumberRange(min=0, max=100)])

    headers = ("Nimi", "Energia (kcal", "Proteiini", "Hiilihydraatti", "Rasva")

    # TODO: don't allow foods with same name

    class Meta:
        csrf = False
