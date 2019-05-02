from application import db
from application.models import Base


class Diet(Base):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    edited = db.Column(db.DateTime, nullable=False)
    meals = db.relationship("Meal", lazy=True, cascade='all, delete')
    meals_query = db.relationship("Meal", lazy="dynamic")

    @property
    def energy(self):
        energy = 0
        for meal in self.meals:
            energy += meal.energy
        return energy

    @property
    def protein(self):
        protein = 0
        for meal in self.meals:
            protein += meal.protein
        return protein

    @property
    def carb(self):
        carb = 0
        for meal in self.meals:
            carb += meal.carb
        return carb

    @property
    def fat(self):
        fat = 0
        for meal in self.meals:
            fat += meal.fat
        return fat
