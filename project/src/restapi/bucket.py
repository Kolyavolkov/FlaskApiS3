import boto3
from flask import session


def get_bucket():
    if "bucket" in session:
        bucket = session["bucket"]
    else:
        bucket = S3_BUCKET

    return boto3.resource("s3").Bucket(bucket)


def get_buckets_list():
    client = boto3.client("s3")
    return client.list_buckets().get("Buckets")
