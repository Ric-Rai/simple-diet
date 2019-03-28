from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from wtforms.validators import Length, Email, EqualTo, Regexp, DataRequired


class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [Length(min=2), DataRequired()], description="👤:")
    password = PasswordField("Salasana", [Length(min=4), DataRequired()], description="🔑")

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    name = StringField("Nimi", [Regexp('[^\d\W]+\s[^\d\W]+', message='Invalid name')],
                       description="🏷: Etunimi Sukunimi")
    email = StringField("Sähköposti", [Email(message='Invalid email')],
                        description="@: tunnus@verkkotunnus.esim")
    username = StringField("Käyttäjätunnus", [Length(min=2), DataRequired()],
                           description="👤: Vähintään kaksi merkkiä pitkä")
    password = PasswordField("Salasana", [EqualTo('confirm', message='Password mismatch'), Length(min=6), DataRequired()],
                             description="🔑: Vähintään neljä merkkiä pitkä")
    confirm = PasswordField("Toista salasana", description="🔑:  ")

    class Meta:
        csrf = False
