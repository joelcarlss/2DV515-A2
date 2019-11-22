from flask_restful import Resource, Api
from database import *
from model.pearson import *
from model.euclidean import *
from utils import *
from json import *


class Users(Resource):
    def get(self):
        result = query_db("select * from users")
        return {'res': result}  # Fetches first column that is Employee ID






