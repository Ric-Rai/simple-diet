from wtforms import StringField, DateTimeField
from wtforms.validators import Length, DataRequired, ValidationError

from application import app
from application.diets.models import Diet
from application.forms import ModelForm


class DietForm(ModelForm):
    db_model = Diet
    name = StringField("Nimi", [Length(min=2), DataRequired()])
    edited = DateTimeField("Muokattu", format='%Y-%m-%d-%H-%M', render_kw={"readonly": "", "current-time": ""})
    headers = ("Nimi", "Muokattu")

    @staticmethod
    def validate_name(form, field):
        app.logger.info("validating diet name")
        error = ValidationError("Tämän niminen ruokavalio on jo tallennettu taulukkoon. "
                                "Ruokavalioiden nimien tulee olla uniikkeja.")

        for diet in Diet.cache.values():
            if diet.name == field.data:
                if not form.id:
                    raise error
                if diet.id is not form.id.data:
                    raise error
