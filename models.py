from app import db, login_manager  
from flask_login import UserMixin  

@login_manager.user_loader
def load_user(user_id):
    return User.query.get((user_id))

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(40), unique = True)
    password = db.Column(db.String(40))


    def __repr__(self):
        return f"{self.email}"

    def self_to_db(self):
        db.session.add(self)
        db.session.commit()

class Order(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key = True)
    parcel_name = db.Column(db.String(100))
    parcel_number = db.Column(db.String(100), unique = True)
    

    
    def __repr__(self):
        return f"{self.parcel_name}"

    def self_to_db(self):
        db.session.add(self)
        db.session.commit()
