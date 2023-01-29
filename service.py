#!/usr/bin/env python3
from sqlalchemy.orm import Session
from model import user
   
def listAll():
    #print(db.query(user).all())
    print(user)
    return user.query.all()
def list():
    return 
def update():
    return
    
def add():
    return 

def delete():
    return
