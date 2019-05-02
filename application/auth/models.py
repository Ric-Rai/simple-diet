from application import db


class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    foods = db.relationship("Food", backref='account', lazy='dynamic')
    diets = db.relationship("Diet", backref='account', lazy='dynamic')

    username = db.Column(db.String(144), nullable=False, unique=True, index=True)
    password = db.Column(db.String(144), nullable=False)
    name = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __init_subclass__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
