from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import Length, Email, EqualTo, Regexp, DataRequired, ValidationError

from application.auth.models import User


class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [Length(min=2), DataRequired()], description="👤:")
    password = PasswordField("Salasana", [Length(min=4), DataRequired()], description="🔑")

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    name = StringField("Nimi", [Regexp('[^\d]+\s[^\d]+', message='Nimen tulee olla muotoa Etunimi Sukunimi')],
                       description="🏷: Etunimi Sukunimi")

    email = StringField("Sähköposti", [Email(message='Sähköpostin tulee olla muotoa tunnus@verkkotunnus.esim')],
                        description="@: tunnus@verkkotunnus.esim")

    username = StringField("Käyttäjätunnus", [Length(min=2, message="Käyttätunnuksen tulee olla vähintään 2 merkkiä "
                                                                    "pitkä"),
                                              DataRequired(message="Käyttätunnus puuttuu")],
                           description="👤: Vähintään kaksi merkkiä pitkä")

    password = PasswordField("Salasana", [EqualTo('confirm', message='Salasanat eivät täsmää'),
                                          Length(min=6, message="Salasanan tulee olla vähintään 6 merkkiä pitkä"),
                                          DataRequired(message="Salasana puuttuu")],
                             description="🔑: Vähintään kuusi merkkiä pitkä")

    confirm = PasswordField("Toista salasana", description="🔑:  ")

    @staticmethod
    def validate_username(form, field):
        username = User.query.filter_by(username=field.data).first()
        error = ValidationError("Käyttäjätunnus on varattu")
        if username is not None:
            raise error

    class Meta:
        csrf = False
