"""
@Author Marco A. Gallegos
@Date   2020/10/09
@Update 2020/10/09
@Description
    Main Api file
"""
from config.config import APP_CONFIG
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import (get_jwt_identity, jwt_required, JWTManager)
import os
from config.config import APP_CONFIG

# controladores
import controllers

app = Flask(APP_CONFIG['APP_NAME'])
CORS(app, resources={r"/*": {"origins": "*"}})

# Setup the Flask-JWT-Extended extension
# TODO use .env secret
app.config["JWT_SECRET_KEY"] = APP_CONFIG["APP_KEY"]
jwt = JWTManager(app)


# se pueden agregar rutas nativas de flask que regresen json
# @app.route("/users/login", methods=["GET"])

# Setup the flask restful api
api = Api(app)

# rutas resource de flask restful
# api.add_resource(controllers.HelloWorld, '/hello')
api.add_resource(controllers.UserController, '/users')
api.add_resource(controllers.LoginController, '/users/login')


if __name__ == '__main__':
    host = os.getenv('APP_HOST') if os.getenv('APP_HOST') else '0.0.0.0'
    port = 5000
    app.run(debug=True, host=host, port=port)
