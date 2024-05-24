import json
import boto3
import os

def lambda_handler(event, context):
    # Get the S3 bucket name from an environment variable or event
    bucket_name =  'test125151262'
    # Alternatively, you could get the bucket name from the event parameter
    # bucket_name = event['bucket_name']

    # Create a Boto3 client for S3
    s3_client = boto3.client('s3')

    # List the objects in the specified S3 bucket
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            files = [item['Key'] for item in response['Contents']]
            return {
                'statusCode': 200,
                'body': json.dumps(files)
            }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps([])  # No files found
            }
            
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error listing files: {str(e)}")
        }

