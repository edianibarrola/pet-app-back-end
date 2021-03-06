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

class Habitat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    pet_in_habitat_id = db.Column(db.String(80), unique=False, nullable=True)
    info = db.Column(db.String(250), unique=False, nullable=True)
    habitat_location = db.Column(db.String(100), unique=False, nullable=True)
    habitat_supplies = db.Column(db.String(100), unique=False, nullable=True)
    habitat_equipment = db.Column(db.String(100), unique=False, nullable=True)
    
    
    
    def __repr__(self):
        return '<Habitat %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "pet_in_habitat_id": self.pet_in_habitat_id,
            "info": self.info,
            "habitat_location": self.habitat_location,
            "habitat_supplies": self.habitat_supplies,
            "habitat_equipment": self.habitat_equipment,
            
            }

class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    all_day = db.Column(db.Boolean, unique=False, default=False, nullable=True )
    habitat_id = db.Column(db.String(80), unique=False, nullable=True)
    notes = db.Column(db.String(250), unique=False, nullable=True)
    pets = db.Column(db.String(100), unique=False, nullable=True)
    start_date = db.Column(db.String(100), unique=False, nullable=False)
    end_date = db.Column(db.String(100), unique=False, nullable=False)
    title = db.Column(db.String(100), unique=False, nullable=False)
    
    
    
    def __repr__(self):
        return '<Calendar %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "allDay": self.all_day,
            "habitatId": self.habitat_id,
            "notes": self.notes,
            "pets": self.pets,
            "startDate": self.start_date,
            "endDate": self.end_date,
            "title": self.title
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
    post_picture = db.Column(db.String(500), unique=False, nullable=True)

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
            "status": self.status,
            "post_picture": self.post_picture
        }
