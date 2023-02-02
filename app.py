#!/usr/bin/env python3

import socket

from fastapi.encoders import jsonable_encoder
import json
import logging
from common import *
from service import *

# init logging object and set the Info type to dump related message 
logging.getLogger().setLevel(logging.INFO)
ip = socket.gethostbyname(socket.gethostname())


# trigger specify class to process from entry request 
class User(Resource):

# categorize the CRUD request (get,put,post,delete)
    @app.route('/user/<string:id>', methods=['GET'])
    def get(id):
        u = UserORM.list(id)
        data = jsonable_encoder(u)
        return {
            'message': 'List user successfully',
            'data': data
        }

    def post(self):
        json_data = request.get_json(force=True)
        hashpwd = hashing(json_data['password'])
        usr = user(json_data['username'],hashpwd)
        u = UserORM.add(usr)
        data = jsonable_encoder(u)
        return {
            'message': 'Insert user successfully',
            'data': data
        }

    def put(self):
        json_data = request.get_json(force=True)
        json_data['password'] = hashing(json_data['password'])
        UserORM.update(json_data)
        return {
            'message': 'Update user successfully',
            'data': json_data
        }


    @app.route('/user/<string:id>', methods=['DELETE'])
    def delete(id):
        usr = UserORM.delete(id)
        u = jsonable_encoder(usr)
        if usr is None:
            return {
                'message': 'No found', 
                'data': u
            }
        return {
            'message': 'Delete user successfully',
            'data': u
        }


class Users(Resource):
    def get(self):
	# ORM method , use object to handle db operation
        users = UserORM.listAll()
        #users = user.query.all()
	# use fastapi.encoders class to convert data structure from dict to json
        users = jsonable_encoder(users)
        
        return{
            'message': 'List all users successfully',
            'data': users
        }


# controller entry 
api.add_resource(Users, '/users')
api.add_resource(User, '/user')

if __name__ == '__main__':
    print(db)
    app.run(debug=True, port=5000,host=ip)

