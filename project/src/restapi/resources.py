import boto3
from flask import jsonify
from flask.wrappers import Response
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


class ListFiles(Resource):
    def get(self, bucketname, username):
        my_bucket = boto3.resource("s3").Bucket(bucketname)
        all_files = list(my_bucket.objects.filter(Prefix=username))
        response = jsonify([object.key for object in all_files])
        response.status_code = 200
        return response


class DeleteFile(Resource):
    def post(self, bucketname, filename):
        key = filename
        my_bucket = boto3.resource("s3").Bucket(bucketname)
        my_bucket.Object(key).delete()
        return {"Object": "deleted"}


class UploadFile(Resource):
    def upload(self):
        pass
