from flask_login import current_user
from sqlalchemy import text

from application import db


class Overview:

    @staticmethod
    def average_meal_count():
        stmt = text("SELECT AVG(meal_count) FROM ("
                    " SELECT COUNT(*) AS meal_count FROM Meal"
                    " JOIN Diet ON Meal.diet_id = Diet.id"
                    " WHERE Diet.account_id = :user_id"
                    " GROUP BY Meal.diet_id ) AS Subquery"
                    ).params(user_id=current_user.id)
        res = db.engine.execute(stmt).fetchone()[0]
        if res is None:
            return 0
        return round(res, 2)

    @staticmethod
    def average_diet_mealfood_count():
        stmt = text("SELECT AVG(mf_count) FROM ("
                    "SELECT COUNT(*) AS mf_count"
                    " FROM Meal_food"
                    " JOIN Meal ON Meal_food.meal_id = Meal.id"
                    " JOIN Diet ON Meal.diet_id = Diet.id"
                    " WHERE Diet.account_id = :user_id"
                    " GROUP BY Meal.diet_id"
                    ") AS Subquery").params(user_id=current_user.id)
        res = db.engine.execute(stmt).fetchone()[0]
        if res is None:
            return 0
        return round(res, 2)

    @staticmethod
    def average_meal_mealfood_count():
        stmt = text("SELECT AVG(mf_count) FROM ("
                    " SELECT COUNT(*) AS mf_count FROM Meal_food"
                    " JOIN Meal ON Meal_food.meal_id = Meal.id"
                    " JOIN Diet ON Meal.diet_id = Diet.id"
                    " WHERE Diet.account_id = :user_id"
                    " GROUP BY Meal_food.meal_id "
                    ") AS Subquery").params(user_id=current_user.id)
        res = db.engine.execute(stmt).fetchone()[0]
        if res is None:
            return 0
        return round(res, 2)

    @staticmethod
    def user_food_count():
        stmt = text("SELECT COUNT(Food.id) FROM Food "
                    "WHERE Food.account_id = :user_id").params(user_id=current_user.id)
        res = db.engine.execute(stmt).fetchone()
        if res is None:
            return 0
        return res[0]

    @staticmethod
    def most_used_food():
        stmt = text("SELECT Food.name, SUM(Meal_food.amount) AS total FROM Meal_food"
                    " JOIN Food ON Meal_food.food_id = Food.id"
                    " WHERE Food.account_id = :user_id"
                    " GROUP BY Food.name"
                    " ORDER BY total DESC"
                    " LIMIT 1").params(user_id=current_user.id)
        res = db.engine.execute(stmt).fetchone()
        if res is None:
            return 0
        return res[0]
