from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=False, nullable=False)
    # pets = db.relationship('Pet', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    pet_type = db.Column(db.String(80), unique=False, nullable=True)
    sex = db.Column(db.String(20), unique=False, nullable=True)
    color = db.Column(db.String(100), unique=False, nullable=True)
    dob = db.Column(db.String(100), unique=False, nullable=True)
    habitat_id = db.Column(db.String(100), unique=False, nullable=True)
    note = db.Column(db.String(300), unique=False, nullable=True)
    # user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    def __repr__(self):
        return '<Pet %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "pet_type": self.pet_type,
            "sex": self.sex,
            "color": self.color,
            "dob": self.dob,
            "habitat_id": self.habitat_id,
            "note": self.note,
            # "user_id": self.user_id
            }
    
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    pet_type = db.Column(db.String(100), unique=False, nullable=False)
    color = db.Column(db.String(100), unique=False, nullable=False)
    eye_color = db.Column(db.String(100), unique=False, nullable=False)
    last_seen = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=True)
    status = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return '<Posts %r>' % self.status

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "pet_type": self.pet_type,
            "color": self.color,
            "eye_color": self.eye_color,
            "last_seen": self.last_seen,
            "description": self.description,
            "status": self.status
        }
