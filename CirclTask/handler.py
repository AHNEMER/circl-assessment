import json
import boto3
import os
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
bucket_name = os.environ['S3_BUCKET_NAME']
#jsjsjsjsjs

def uploadCustomer(event, context):
    try:
        # Parse the JSON body from the incoming event
        body = json.loads(event['body'])
        name = body['name']
        email = body['email']

        # Create a unique key for the S3 object
        key = f"{name}.json"

        # convert data to json to store in S3
        data = {
            'name': name,
            'email': email
        }

        # Upload data to S3
        s3.put_object(Bucket=bucket_name, Key=key, Body=json.dumps(data))
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Customer uploaded successfully'})
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


def getCustomers(event, context):
    try:
        # List all objects in the S3 bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        # Collect customer data from S3 objects
        customers = []
        if 'Contents' in response:
            for obj in response['Contents']:
                key = obj['Key']
                obj_data = s3.get_object(Bucket=bucket_name, Key=key)
                customer = json.loads(obj_data['Body'].read())
                customers.append(customer)

        return {
            'statusCode': 200,
            'body': json.dumps(customers)
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
