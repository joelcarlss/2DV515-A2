import csv
from database import mycursor
from model import *
import json


# Returns arrays with objects
def query_db(query, args=(), one=False):
    mycursor.execute(query, args)
    r = [dict((mycursor.description[i][0], value)
              for i, value in enumerate(row)) for row in mycursor.fetchall()]
    return (r[0] if r else None) if one else r


def get_rating_from_db(uid):
    other = query_db("select * from ratings WHERE NOT userId = %s", (uid,))
    selected = query_db("select * from ratings WHERE userId = %s;", (uid,))
    return selected, other