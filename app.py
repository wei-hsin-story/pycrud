#!/usr/bin/env python3

import socket

from fastapi.encoders import jsonable_encoder
import json
from model import *

ip = socket.gethostbyname(socket.gethostname())

class User(Resource):

    @app.route('/user/<string:id>', methods=['GET'])
    def get(id):
        print(id)
        return {
            'message': 'List user successfully',
            'data': id
        }

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        return {
            'message': 'Insert user successfully',
            'data': json_data
        }

    def put(self):
        json_data = request.get_json(force=True)
        print(json_data)
        return {
            'message': 'Update user successfully',
            'data': json_data
        }


    @app.route('/user/<string:id>', methods=['DELETE'])
    def delete(id):
        print(id)
        return {
            'message': 'Delete user successfully',
            'data': id
        }


class Users(Resource):
    def get(self):
        rows = user.query.all()
        data = jsonable_encoder(rows)
        
        for r in rows:
            print (r.id)
        
       # data = row2dict(result)
        return{
            'message': 'List all users successfully',
            'data': data
        }


def row2dict(rows):
    for ret in row:
        retList.append(ret.__dict__)
        pass
    return d

# User Operation
api.add_resource(Users, '/users')
api.add_resource(User, '/user')

if __name__ == '__main__':
    print(db)
    app.run(debug=True, port=5000,host="172.28.88.56")

