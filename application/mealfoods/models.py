from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from application import db


class MealFood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'))
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    food = relationship("Food", backref='food', lazy=False, uselist=False)
    amount = db.Column(db.Integer, nullable=False)
    order_num = db.Column(db.Integer, nullable=False)
    # __table_args__ = (UniqueConstraint('meal_id', 'food_id'),)

    @hybrid_property
    def energy(self):
        return self.amount * self.food.energy
