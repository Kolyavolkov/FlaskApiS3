from flask import jsonify
from flask_restful import Resource
from restapi.bucket import get_bucket, get_buckets_list


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


class ListBuckets(Resource):
    def get(self):
        response = jsonify(get_buckets_list())
        response.status_code = 200
        return response
