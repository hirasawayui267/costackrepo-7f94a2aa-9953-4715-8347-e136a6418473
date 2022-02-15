# create your main function here
# run the necessary operaitons and return
import json
import boto3
import os 
def entropy_main(event, context):
    print(event)
    print(os.getenv("User_id"))
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('perseus-random')
    print(my_bucket)
    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object)

    # file format --> file will be put into s3 --> first read the file and do some analysis
    # 
    return {"response": "退款成功 hellp" }