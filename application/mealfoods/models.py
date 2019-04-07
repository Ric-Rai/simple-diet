from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from application import db
from application.foods.models import Food


class MealFood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    _food_name = db.Column(db.String(100), nullable=False)
    food = relationship("Food", backref='food', lazy=True, uselist=False)
    amount = db.Column(db.Integer, nullable=False)
    order_num = db.Column(db.Integer)

    @hybrid_property
    def food_name(self):
        return self._food_name

    @food_name.setter
    def food_name(self, food_name):
        self._food_name = food_name
        self.food_id = db.session.query(Food.id).filter_by(name=food_name).scalar()

        # TODO: Make more efficient

    @hybrid_property
    def energy(self):
        return self.amount * self.food.energy

    @energy.setter
    def energy(self, energy):
        pass

    @hybrid_property
    def protein(self):
        return self.amount * self.food.protein

    @protein.setter
    def protein(self, protein):
        pass

    @hybrid_property
    def carb(self):
        return self.amount * self.food.carb

    @carb.setter
    def carb(self, carb):
        pass

    @hybrid_property
    def fat(self):
        return self.amount * self.food.fat

    @fat.setter
    def fat(self, fat):
        pass
