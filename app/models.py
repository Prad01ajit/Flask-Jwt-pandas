from app import db


class Users(db.Model):
    __tablename__ = 'user-account'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50))
    name = db.Column(db.String(50))
    password = db.Column(db.String(100))