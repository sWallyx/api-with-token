""" Main file for the API """
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# TODO: The secret key will end up in as environment variable
app.config["SECRET_KEY"] = "thissecret"
# TODO: Find a way to use a relative path for the database
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "sqlite:////Users/mikel.sanchez/github/api-with-token/todo.db"

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

@app.route('/users', methods=['GET'])
def get_all_users():
    return ''

@app.route('/user/<user_id>', methods=['GET'])
def get_one_user():
    return ''

@app.route('/user', methods=['POST'])
def create_user():
    return ''

@app.route('/user/<user_id>', methods=['PUT'])
def promote_user():
    return ''

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user():
    return ''

if __name__ == "__main__":
    app.run(debug=True)
