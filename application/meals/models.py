from application import db, app
from application.models import Base


class Meal(Base):
    diet_id = db.Column(db.Integer, db.ForeignKey('diet.id'), nullable=False)
    order_num = db.Column(db.Integer, nullable=False)
    mealfoods = db.relationship("MealFood", lazy=True, cascade='all, delete')
    diet = db.relationship("Diet", lazy=True)
    cache = dict()

    @property
    def account_id(self):
        return self.diet.account_id

    @account_id.setter
    def account_id(self, value):
        pass
    
    @property
    def energy(self):
        energy = 0
        for mealfood in self.mealfoods:
            if mealfood.food_id is None:
                continue
            energy += mealfood.energy
        return energy
    
    @property
    def protein(self):
        protein = 0
        for mealfood in self.mealfoods:
            if mealfood.food_id is None:
                continue
            protein += mealfood.protein
        return protein
    
    @property
    def carb(self):
        carb = 0
        for mealfood in self.mealfoods:
            if mealfood.food_id is None:
                continue
            carb += mealfood.carb
        return carb
    
    @property
    def fat(self):
        fat = 0
        for mealfood in self.mealfoods:
            if mealfood.food_id is None:
                continue
            fat += mealfood.fat
        return fat
