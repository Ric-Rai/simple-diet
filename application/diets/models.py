from sqlalchemy import text

from application import db


class Diet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    edited = db.Column(db.DateTime, nullable=False)
    meals = db.relationship("Meal", backref='meals', lazy=True)
