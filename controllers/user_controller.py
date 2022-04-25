"""
@Author Marco A. Gallegos
@Date 2020/10/09
@Description
    user controller
"""
from flask import request
from flask_restful import Resource, reqparse
import pendulum
from repository.mongorepository.main_repository import get_user, generate_hash, store_user


class UserController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', help='the name field is required', required=True)
    parser.add_argument('email', help='the name field is required', required=True)
    parser.add_argument('password', help='the name field is required', required=True)
    parser.add_argument('age', help='the age field is required', required=True)

    def get(self):
        existing_user = get_user(request.args.get('email'))
        existing_user.pop("password")
        existing_user["_id"] = str(existing_user["_id"])
        return existing_user
    
    def post(self):
        data = self.parser.parse_args()

        existing_user = get_user(data['email'])

        print(existing_user)

        if existing_user:
            return {'message': 'User already exists'}

        user = {
            "name": data['name'],
            # "lastname": data['lastname'],
            "age": data['age'],
            "email": data['email'],
            "password": generate_hash(data['password'])
        }

        new_user = store_user(user)
        user.pop("password")
        user.pop("_id")

        return user
