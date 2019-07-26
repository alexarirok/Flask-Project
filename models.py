from app import db, login_manager  
from flask_login import UserMixin  

@login_manager.user_loader
def load_user(user_id):
    return User.query.get((user_id))

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))


    def __repr__(self):
        return f"{self.email}"

    def self_to_db(self):
        db.session.add(self)
        db.session.commit()

class Parcel(db.Model):
    __tablename__ = "parcel"
    id = db.Column(db.Integer, primary_key = True)
    parcel_name = db.Column(db.String(100))
    parcel_number = db.Column(db.String(100), unique = True)
    pickup_destination = db.Column(db.String(100))
    delivery_destination = db.Column(db.String(100))

    def __init__(self, parcel_name, parcel_number, parcel_destination, delivery_destination):
        self.parcel_name = parcel_name
        self.parcel_number = parcel_number
        self.pickup_destination = pickup_destination
        self.delivery_destination = delivery_destination

    def __repr__(self):
        return f"{self.parcelname}"

    def self_to_db(self):
        db.session.add(self)
        db.session.commit()
