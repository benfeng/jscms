__author__ = 'fengbq@live.com'

from flask_restful  import Resource, Api
from webapp import app
from webapp.resource.sercurity  import Sercurity

# api
api=Api(app)
baseApiUrl="/api"

class HelloWorld(Resource):
    def get(self):
        return {"success":True}

api.add_resource(Sercurity,baseApiUrl+ '/a')

