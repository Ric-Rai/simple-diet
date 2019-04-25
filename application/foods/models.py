from application import db
from application.models import Base


class Food(Base):
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    name = db.Column(db.String(100), nullable=False)
    energy = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Numeric(scale=2), nullable=False)
    carb = db.Column(db.Numeric(scale=2), nullable=False)
    fat = db.Column(db.Numeric(scale=2), nullable=False)
    cache = dict()

    # def before_delete(self):
    #     from application.mealfoods.models import MealFood
    #     mealfoods = MealFood.query.filter_by(food_id=self.id).all()
    #     for mealfood in mealfoods:
    #         mealfood.food_id = None
    #         db.session.add(mealfood)
    #     db.session.commit()
