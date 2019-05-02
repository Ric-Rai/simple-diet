from flask_login import current_user
from wtforms import StringField, DateTimeField
from wtforms.validators import Length, DataRequired, ValidationError

from application.diets.models import Diet
from application.forms import ModelForm


class DietForm(ModelForm):
    db_model = Diet
    name = StringField(None, [Length(min=2), DataRequired(message="Ruokavalion nimi puuttuu")])
    edited = DateTimeField(None, format='%d.%m.%Y %H:%M', render_kw={"readonly": "", "current-time": ""})
    heading = "Ruokavaliot"
    headers = ("Nimi", "Luotu")

    @staticmethod
    def validate_name(form, field):
        diet = current_user.diets.filter_by(name=field.data).first()
        error = ValidationError("Tämän niminen ruokavalio on jo tallennettu taulukkoon. "
                                "Ruokavalioiden nimien tulee olla uniikkeja.")
        if diet is not None:
            if not form.id:
                raise error
            if diet.id is not form.id.data:
                raise error
