import os
import secrets

import boto3
from flask import jsonify, request
from flask_restful import Resource

from restapi.bucket import get_buckets_list


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


class ListBuckets(Resource):
    def get(self):
        response = jsonify(get_buckets_list())
        response.status_code = 200
        return response


class ListFiles(Resource):
    def get(self, bucket, user):
        my_bucket = boto3.resource("s3").Bucket(bucket)
        all_files = list(my_bucket.objects.filter(Prefix=user))
        response = jsonify([object.key for object in all_files])
        response.status_code = 200
        return response


class DeleteFile(Resource):
    def post(self):
        file = request.form["file"]
        bucket = request.form["bucket"]
        my_bucket = boto3.resource("s3").Bucket(bucket)
        all_files = [object.key for object in my_bucket.objects.all()]
        if file in all_files:
            my_bucket.Object(file).delete()
            return {"Object": "Deleted"}
        else:
            return {"Object": "Not Found"}


class UploadFile(Resource):
    def post(self):
        file = request.files["file"]
        bucket = request.form["bucket"]
        user = request.form["user"]
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(file.filename)
        file.filename = f"{user}.{random_hex}{f_ext}"
        my_bucket = boto3.resource("s3").Bucket(bucket)
        my_bucket.Object(file.filename).put(Body=file)
        response = jsonify(file.filename)
        response.status_code = 200
        return response
