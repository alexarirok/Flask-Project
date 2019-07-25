from db import db    


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.username}"

    def self_to_db(self):
        db.session.add(self)
        db.session.commit()

class Parcel(db.Model):
    __tablename__ = "parcels"
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
