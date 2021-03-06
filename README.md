# FlaskApiS3
simple flask api to interact with S3Bucket
# Project Description
Api provides access to your S3buckets in two ways: 
- with command line through API
- with web-interface app

You can list, upload and delete files by your username.

# AWS folder
Here is the AWS template to create your stack with FlaskApiS3 installed.
To create this stack go to your AWS Management Console -> Cloudformation -> Create stack
Than you'll have to fill some neccessary fields with your data and provide a key-pair.
When stack is created, you'll get LoadBalancers DNS in outputs.
App now is available by this DNS name.

# Project folder contains the api itself

CURL commands to use API :
```bash
curl load.balancers.dns/health
#returns healthcheck status

curl load.balancers.dns/api
#returns "Hello world"

curl load.balancers.dns./api/buckets
#returns list of available buckets

curl load.balancers.dns/api/<string:bucket>/<string:user>
#returns all files accessable for <user> in <bucket>

curl -X POST -F file=filename -F bucket=bucketname load.balancers.dns/api/delete
#deletes file

curl -X POST -F file=@path/to/file -F bucket=bucketname -F user=username load.balancers.dns/api/upload
#uploads file with username tag
```

