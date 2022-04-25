"""
@Author Marco A. Gallegos
@Date 2020/10/09
@Description
    controlador de ejemplo para tener un endpoint que siempre responda
"""
from flask_restful import Resource
from flask_jwt_extended import jwt_required


class HelloWorld(Resource):

    @jwt_required()
    def get(self):
        return {'hello': 'world'}