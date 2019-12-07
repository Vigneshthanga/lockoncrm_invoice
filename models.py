#from app import db
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import bcrypt
from sqlalchemy.orm import sessionmaker, relationship, scoped_session

import datetime as dt

db= SQLAlchemy()

class Artist(db.Model):
    __tablename__ = "artists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return "{}".format(self.name)


class Album(db.Model):
    """"""
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    release_date = db.Column(db.String(50))
    publisher = db.Column(db.String(50))
    status = db.Column(db.Enum('Sent', 'Paid','Cancel', 'Pending'))

    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"))
    artist = db.relationship("Artist", backref=db.backref(
        "albums", order_by=id), lazy=True)
