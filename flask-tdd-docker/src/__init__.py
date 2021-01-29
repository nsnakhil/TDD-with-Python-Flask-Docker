# src/__init__.py

import flask
import flask_restx

from flask import Flask, jsonify
from flask_restx import Resource, Api

# intsantiate the app

app = Flask(__name__)

api= Api(app)

# set config
app.config.from_object('src.config.DevelopmentConfig')  # new



class Ping(Resource):
    def get(self):
        return {
                'status': 'success',
                'message': 'pong!'

             }

api.add_resource(Ping, '/ping')