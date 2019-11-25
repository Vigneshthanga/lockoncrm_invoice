# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ranjani:SRbravard@94@localhost:5432/sample'
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)