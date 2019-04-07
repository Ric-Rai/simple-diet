from sqlalchemy import text

from application import db


class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    edited = db.Column(db.DateTime, nullable=False)
    meals = db.relationship("Meal", backref='all_meals_in_diet', lazy=True, cascade='all, delete')
    meals_query = db.relationship("Meal", lazy="dynamic")
