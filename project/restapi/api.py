from flask_restful import Api

from restapi import app
from restapi.resources import DeleteFile, HelloWorld, ListBuckets, ListFiles, UploadFile


api = Api(app)
api.add_resource(HelloWorld, "/api")
api.add_resource(ListBuckets, "/api/buckets")
api.add_resource(ListFiles, "/api/<string:bucket>/<string:user>")
api.add_resource(UploadFile, "/api/upload")
api.add_resource(DeleteFile, "/api/delete")
