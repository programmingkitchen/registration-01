from registrationapp import db
from werkzeug.security import generate_password_hash,check_password_hash


class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique=True, index=True)
    passwordHash = db.Column(db.String(128))

    def __init__(self, name, password):
        self.name = name
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.passwordHash, password)

    def genPassword(self, password):
        return generate_password_hash(password)
