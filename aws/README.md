# AWS

```python
import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client("s3")
    
    if event:
        file_name = event.get("Records")[0].get("s3").get("object").get("key")
        bucket = event.get("Records")[0].get("s3").get("bucket").get("name")
        
        file_object = s3.get_object(Bucket=bucket, Key=file_name)
        contents = file_object['Body'].read()
        print(contents)
    
    return {
        'statusCode': 200,
        'body': json.dumps('')
    }

```