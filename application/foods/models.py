from sqlalchemy import text

from application import db


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)
    mealfood = db.relationship("MealFood", backref='mealfood', lazy=True)

    name = db.Column(db.String(100), unique=True, nullable=False)
    energy = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Numeric(scale=2), nullable=False)
    carb = db.Column(db.Numeric(scale=2), nullable=False)
    fat = db.Column(db.Numeric(scale=2), nullable=False)

    @staticmethod
    def count_foods_of_user(user_id):
        stmt = text("SELECT COUNT(Food.id) FROM Food "
                    "WHERE Food.account_id = :user_id").params(user_id=user_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])

        return response
