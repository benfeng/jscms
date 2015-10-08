__author__ = 'fengbq@live.com'

from flask_restful  import Resource
from pymongo import MongoClient
import webapp.lib.const
client = MongoClient("mongodb://localhost:27017")
db = client.primer

class Sercurity(Resource):
    def get(self):
        db.test.insert({
            "code":"003",
            "name":"ss",
            "isAdmin":False
        })
        a= db.test.find()
        print(db.test.find())
        # return db.test.find()
        return {"success":True}


