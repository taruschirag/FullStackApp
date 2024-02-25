# contain database models
from config import db


# A database model reprsentaed as python class. In python code we can define different variables
class Contact(db.Model):
    # primary key is the key used to index it and it must be unique
    id = db.Column(db.Integer, primary_key=True)
    # cant make the name NULL
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
