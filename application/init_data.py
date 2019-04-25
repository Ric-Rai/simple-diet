from random import randint

from sqlalchemy import text, func

from application import db
from application.diets.models import Diet
from application.foods.models import Food
from application.mealfoods.models import MealFood


def food_init_values():
    stmt = text("INSERT INTO Food (name, energy, protein, carb, fat, account_id) VALUES "
                "('Avokado', 198, 2.6, 0.8, 2.6, null),"
                "('Banaani', 87, 1.1, 18.3, 1.1, null),"
                "('Digestive', 474, 7.3, 68.0, 7.3, null),"
                "('Feta', 261, 18.2, 0.5, 18.2, null),"
                "('Hedelmä', 32, 0.0, 6.6, 0.0, null),"
                "('Hera', 410, 92.0, 0.0, 92.0, null),"
                "('Homejuusto', 340, 18.0, 0.0, 18.0, null),"
                "('Juusto', 370, 25.0, 0.0, 25.0, null),"
                "('Kaakaojauhe', 378, 20.0, 11.0, 20.0, null),"
                "('Kaakaomassa', 657, 13.0, 26.0, 13.0, null),"
                "('Kaakaovoi', 581, 0.0, 0.0, 0.0, null),"
                "('Kasvikset', 61, 2.5, 8.9, 2.5, null),"
                "('Kasvispiirakka', 304, 8.4, 34.0, 8.4, null),"
                "('Kaurajauhe', 370, 12.0, 56.0, 12.0, null),"
                "('Kermarahka', 141, 8.8, 3.7, 8.8, null),"
                "('Ketsuppi', 64, 1.4, 11.9, 1.4, null),"
                "('Kikherne keitetty', 133, 8.4, 17.6, 8.4, null),"
                "('Kookosmaito', 166, 1.0, 2.0, 1.0, null),"
                "('Kookosrasva', 900, 0.0, 0.0, 0.0, null),"
                "('Kuohukerma', 340, 2.0, 3.0, 2.0, null),"
                "('Kvinoa', 355, 13.0, 57.0, 13.0, null),"
                "('Leipäjuusto', 272, 18.0, 2.5, 18.0, null),"
                "('Maitojauhe', 437, 37.0, 38.0, 37.0, null),"
                "('Maitorahka', 68, 12.0, 4.0, 12.0, null),"
                "('Mannasuurimo', 350, 12.0, 70.0, 12.0, null),"
                "('Mansikka', 47, 0.5, 8.4, 0.5, null),"
                "('Mantelijauho', 616, 21.0, 8.8, 21.0, null),"
                "('Mantelivoi', 650, 25.0, 6.5, 25.0, null),"
                "('Mehukeitto', 8, 0.0, 2.0, 0.0, null),"
                "('Mozzarella', 248, 18.0, 1.5, 18.0, 1),"
                "('Nuudeli', 347, 10.2, 66.4, 10.2, 1),"
                "('Oliivi', 125, 0.5, 0.5, 0.5, 1),"
                "('Piimä', 55, 3.2, 4.4, 3.2, 1),"
                "('Pikakaurahiutale', 362, 14.0, 54.0, 14.0, 1),"
                "('Pinaattiohukainen', 197, 5.9, 29.0, 5.9, 1),"
                "('Porkkana', 33, 0.6, 5.6, 0.6, 1),"
                "('Psyllium', 378, 0.0, 89.0, 0.0, 1),"
                "('Remoulade', 600, 0.6, 5.0, 0.6, 1),"
                "('Riisi', 366, 8.1, 79.0, 8.1, 1),"
                "('Riisimuro', 383, 6.0, 87.0, 6.0, 1),"
                "('Rouhe', 336, 50.0, 40.4, 50.0, 1),"
                "('Ruisleipä', 241, 9.5, 40.0, 9.5, 1),"
                "('Sipuli', 30, 1.3, 4.8, 1.3, 1),"
                "('Soijamaito', 45, 3.2, 3.9, 3.2, 1),"
                "('Soijapapuhiutale', 390, 39.0, 13.0, 39.0, 1),"
                "('Soijaproteiini', 400, 90.0, 0.0, 90.0, 1),"
                "('Suklaa-sirut', 604, 13.0, 18.0, 13.0, 1),"
                "('Sulatejuusto', 166, 22.0, 6.0, 22.0, 1),"
                "('Tahini', 647, 22.2, 2.6, 22.2, 1),"
                "('Tofu', 117, 12.0, 1.0, 12.0, 1),"
                "('Vehnäjauho', 358, 12.0, 70.0, 12.0, 1),"
                "('Vesi', 0, 0.0, 0.0, 0.0, 1),"
                "('Voi', 720, 0.0, 0.0, 0.0, 1)")
    db.engine.execute(stmt)


def diet_init_values():
    stmt = text("INSERT INTO Diet (account_id, name, edited) VALUES "
                "(1, 'Ruokavalio', '2019-01-01 00:00:00.000'),"
                "(1, 'Dieetti', '2019-01-01 00:00:00.000')")
    db.engine.execute(stmt)


def meal_init_values():
    stmt = text("INSERT INTO Meal (diet_id, order_num) VALUES "
                "(1, 1),"
                "(1, 2),"
                "(1, 3),"
                "(1, 4),"
                "(1, 5),"
                "(1, 6),"
                "(2, 1),"
                "(2, 2),"
                "(2, 3),"
                "(2, 4),"
                "(2, 5),"
                "(2, 6)")
    db.engine.execute(stmt)


def mealfood_init_values():
    diet1 = Diet.query.get(1)
    for meal in diet1.meals:
        foods = Food.query.order_by(func.random()).limit(randint(3, 5))
        for food in foods:
            mf = MealFood(_food_name=food.name, meal_id=meal.id, food_id=food.id, amount=randint(50, 300))
            meal.mealfoods.append(mf)
    diet2 = Diet.query.get(2)
    for meal in diet2.meals:
        foods = Food.query.order_by(func.random()).limit(randint(3, 5))
        for food in foods:
            mf = MealFood(_food_name=food.name, meal_id=meal.id, food_id=food.id, amount=randint(50, 300))
            meal.mealfoods.append(mf)
    db.session.commit()
