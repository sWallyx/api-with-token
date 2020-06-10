from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/mikel.sanchez/github/api-with-token/todo.db'

db = SQLAlchemy(app)

# We define the tables fort our database, in this case, two tables
# User table and Todo table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

if __name__ == '__main__':
    app.run(debug=True)