import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ubf_donors')

def lambda_handler(event, context):
    # TODO implement
    table.put_item(Item=event)
    return {
        "code": 200,
        "message": "Response ok"
    }
