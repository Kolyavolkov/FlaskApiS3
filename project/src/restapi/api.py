from restapi import app
from flask_restful import Api
from restapi.resources import HelloWorld, ListBuckets, ListFiles


api = Api(app)
api.add_resource(HelloWorld, "/api")
api.add_resource(ListBuckets, "/api/buckets")
api.add_resource(ListFiles, "/api/<string:bucketname>/<string:username>")
