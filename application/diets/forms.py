from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField
from wtforms.validators import Length, DataRequired


class DietForm(FlaskForm):
    name = StringField("Nimi", [Length(min=2), DataRequired()])
    edited = DateTimeField("Muokattu", format='%Y-%m-%d-%H-%M', render_kw={"readonly": "", "current-time": ""})
    headers = ("Nimi", "Muokattu")

    class Meta:
        csrf = False
