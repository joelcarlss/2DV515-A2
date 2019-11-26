from flask_restful import Resource, Api
from k_means import *
from utils import *
from json import *


class Users(Resource):
    def get(self):
        return {'res': 'hej'}  # Fetches first column that is Employee ID


blog_data, blog_names = get_data()
result = k_means(blog_data)
named_list = elements_for_names(result, blog_names)

