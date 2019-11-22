from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from flask_cors import CORS
from utils import *
from routes.route import *
from database import *

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Users, '/users')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')

