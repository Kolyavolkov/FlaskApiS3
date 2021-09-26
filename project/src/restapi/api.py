from restapi import app
from flask_restful import Api
from restapi.resources import HelloWorld, ListBuckets


api = Api(app)
api.add_resource(HelloWorld, "/api")
api.add_resource(ListBuckets, "/api/buckets")
