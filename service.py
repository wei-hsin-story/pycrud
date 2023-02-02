#!/usr/bin/env python3
import logging
from model import *

logging.getLogger().setLevel(logging.INFO)

class UserORM():
    def listAll():
        return user.query.all()
    def list(id):
        return user.query.filter_by(id=id).first()
    def update(user_data):
        u = user.query.filter_by(id=user_data['id']).first()
        u.username = user_data['username']
        u.password = user_data['password']
        try:
            db.session.commit()
        except Exception as e:
            print(e)
    
    def add(user):
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
        return  user.query.filter_by(id=user.id).first()
    def delete(id):
        u = user.query.filter_by(id=id).first()
        try:
            db.session.delete(u)
            db.session.commit()
        except Exception as e:
            print(e)
        return u
