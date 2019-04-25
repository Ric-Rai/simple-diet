from flask import Flask
from sqlalchemy import event

app = Flask(__name__, static_url_path='/static')

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///diets.db"
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)

from application import views

from application.foods import models
from application.foods import views
from application.foods.models import Food

from application.auth import models
from application.auth import views

from application.diets import models
from application.diets import views
from application.diets.models import Diet

from application.meals import models
from application.meals import views
from application.meals.models import Meal

from application.mealfoods import models
from application.mealfoods import views
from application.mealfoods.models import MealFood

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@event.listens_for(User.__table__, 'after_create')
def user_init_values(*args, **kwargs):
    db.session.add(User('test', 'test', 'Testaaja', 'test@test.test'))
    db.session.commit()


from application.init_data import *


@event.listens_for(Food.__table__, 'after_create')
def food_init(*args, **kwargs):
    food_init_values()


@event.listens_for(Diet.__table__, 'after_create')
def diet_init(*args, **kwargs):
    diet_init_values()


@event.listens_for(Meal.__table__, 'after_create')
def meal_init(*args, **kwargs):
    meal_init_values()


@event.listens_for(MealFood.__table__, 'after_create')
def mealfood_init(*args, **kwargs):
    mealfood_init_values()


try:
    db.create_all()
except:
    pass
