# Contain the main configurations of the application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# send or request to this backend from a different URL. Since frontend is a different server we need this to deal with this error.
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This stores a file named mydatabase.db in the local machine which is going ot be a sqlite database.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

# Not track all the modificaitons made to the database. But we can monitor it if we want
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create an instance of the database

db = SQLAlchemy(app)
