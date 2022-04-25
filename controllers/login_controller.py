"""
@Author Marco A. Gallegos
@Date 2020/10/09
@Description
    login controller this controller makes the login function
"""
from flask_restful import Resource, reqparse
from flask import jsonify
from repository.mongorepository.main_repository import get_user, verify_password

from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, create_refresh_token
)


class LoginController(Resource):
    """This controlLer handles the login and user authorization considering a JWT token.
    this token is encrypted so consider use the same password in every microservice.
    """

    parser = reqparse.RequestParser()
    parser.add_argument('email', help='the name field is required', required=True)
    parser.add_argument('password', help='the name field is required', required=True)

    @jwt_required()
    def get(self):
        """this method returns the jwt identy, in this project jwt identity conatians user data."""
        current_user = get_jwt_identity()
        return current_user, 200
    
    def post(self):
        """this method check user data and returns a jwt token with user data in the payload."""
        data = self.parser.parse_args()
        user = get_user(data['email'])
        user["_id"] = str(user["_id"])
        # print(user)
        serialized_user = user.copy()
        serialized_user.pop('password')

        if user:
            coincide_password = verify_password(data['password'], user['password'])
            if coincide_password:
                access_token = create_access_token(identity=serialized_user)
                refresh_token = create_refresh_token(identity=serialized_user)
                return {
                    'message': f"Logged in as {user['name']}",
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
        return {'message': 'Wrong credentials'}
