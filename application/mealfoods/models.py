from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.orm import relationship

from application import db, app
from application.models import Base
from application.foods.models import Food


class MealFood(Base):
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id', ondelete="SET NULL"))
    _food_name = db.Column(db.String(100), nullable=False)
    food = relationship("Food", lazy=True, uselist=False)
    meal = relationship("Meal", lazy=True, uselist=False)
    amount = db.Column(db.Integer, nullable=False)
    order_num = db.Column(db.Integer)
    cache = dict()

    @property
    def account_id(self):
        return self.meal.account_id

    @account_id.setter
    def account_id(self, value):
        pass

    @property
    def food_name(self):
        return self._food_name

    @food_name.setter
    def food_name(self, food_name):
        self._food_name = food_name
        self.food_id = db.session.query(Food.id).filter_by(name=food_name).scalar()

    @property
    def energy(self):
        return round(self.amount * (self.food.energy / 100))

    @property
    def protein(self):
        return round(self.amount * (self.food.protein / 100), 2)

    @property
    def carb(self):
        return round(self.amount * (self.food.carb / 100), 2)

    @property
    def fat(self):
        return round(self.amount * (self.food.fat / 100), 2)
