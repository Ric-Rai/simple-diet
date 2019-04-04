from application import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    diet_id = db.Column(db.Integer, db.ForeignKey('diet.id'), nullable=False)
    order_num = db.Column(db.Integer, nullable=False)
    mealfoods = db.relationship("MealFood", backref='mealfoods', lazy=False)
