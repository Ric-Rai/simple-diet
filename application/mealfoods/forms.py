from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, HiddenField
from wtforms.validators import Length, DataRequired, NumberRange, Optional


class MealFoodForm(FlaskForm):
    meal_id = HiddenField()
    food_name = StringField("Ruoka", [Length(min=2), DataRequired()])
    amount = IntegerField("Määrä", [NumberRange(min=0)])
    energy = IntegerField("Energia", [Optional()], render_kw={"readonly": ""})
    protein = DecimalField("Proteiini", [Optional()], render_kw={"readonly": ""})
    carb = DecimalField("Hiilihydraatti", [Optional()], render_kw={"readonly": ""})
    fat = DecimalField("Rasva", [Optional()], render_kw={"readonly": ""})

    class Meta:
        csrf = False
