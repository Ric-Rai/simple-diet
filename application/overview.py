from flask_login import current_user
from sqlalchemy import text

from application import db


class Overview:

    @staticmethod
    def average_meal_count():
        stmt = text("SELECT AVG(meal_count) FROM ("
                    " SELECT COUNT(*) AS meal_count FROM Meal"
                    " GROUP BY Meal.diet_id )"
                    )
        return round(db.engine.execute(stmt).fetchone()[0], 2)

    @staticmethod
    def average_diet_mealfood_count():
        stmt = text("SELECT (SELECT COUNT(*) FROM Meal_food) /"
                    " (SELECT COUNT(*) AS diet_count FROM Diet)"
                    )
        return round(db.engine.execute(stmt).fetchone()[0], 2)

    @staticmethod
    def average_meal_mealfood_count():
        stmt = text("SELECT AVG(mf_count) FROM ("
                    " SELECT COUNT(*) AS mf_count FROM Meal_food"
                    " GROUP BY Meal_food.meal_id )"
                    )
        return round(db.engine.execute(stmt).fetchone()[0], 2)

    @staticmethod
    def user_food_count():
        stmt = text("SELECT COUNT(Food.id) FROM Food "
                    "WHERE Food.account_id = :user_id").params(user_id=current_user.id)
        return db.engine.execute(stmt).fetchone()[0]

    @staticmethod
    def most_used_food():
        stmt = text("SELECT Food.name, SUM(Meal_food.amount) AS total FROM Meal_food"
                    " JOIN Food ON Meal_food.food_id = Food.id"
                    " GROUP BY Food.name"
                    " ORDER BY total DESC"
                    " LIMIT 1")
        return db.engine.execute(stmt).fetchone()[0]
