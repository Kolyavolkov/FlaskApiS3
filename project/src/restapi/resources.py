import boto3
from flask import jsonify, request
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
        my_bucket = boto3.resource("s3").Bucket(bucketname)
        all_files = [object.key for object in my_bucket.objects.all()]
        if filename in all_files:
            my_bucket.Object(filename).delete()
            return {"Object": "Deleted"}
        else:
            return {"Object": "Not Found"}


class UploadFile(Resource):
    def upload(self):
        pass
