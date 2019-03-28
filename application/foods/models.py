from application import db


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
#   account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
#   created = db.Column(db.DateTime, default=db.func.current_timestamp())

    name = db.Column(db.String(100), unique=True, nullable=False)
    energy = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Numeric(scale=2), nullable=False)
    carb = db.Column(db.Numeric(scale=2), nullable=False)
    fat = db.Column(db.Numeric(scale=2), nullable=False)

    def __init__(self, name, energy, protein, carb, fat):
        self.name = name
        self.energy = energy
        self.protein = protein
        self.carb = carb
        self.fat = fat

#    meals = db.relationship("Meal", backref='meal', lazy=True)
