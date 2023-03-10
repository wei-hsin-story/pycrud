import datetime
import uuid
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from service import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@172.28.88.56:5432/postgres'

db = SQLAlchemy(app)
api = Api(app)



# db model , as table structure defined fields about talbe schema
class user(db.Model):
    __tablename__ = 'users'
    def gen_id(self):
        return uuid.uuid4().hex

    #id = db.Column(db.String(),primary_key=True,default=gen_id)
    id = db.Column(db.String(),primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    create_time = db.Column(db.DateTime,default=datetime.datetime.now)

    def __init__(self, username, password):
        self.id = self.gen_id()
        self.username=username
        self.password=password
        #self.create_time=create_time
