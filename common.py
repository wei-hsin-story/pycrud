#!/usr/bin/env python3

from werkzeug.security import generate_password_hash,check_password_hash

def hashing(pwd):
    return generate_password_hash(pwd)

def checkpwd(pwdhash,pwd):
    return check_password_hash(pwdhash,pwd)
    
