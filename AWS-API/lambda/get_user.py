import json
import boto3
import decimal
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

# Helper class to convert Decimal to int/float for JSON serialization
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj) if obj % 1 else int(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        # Get user_id from path parameters
        user_id = event['pathParameters']['user_id']
        
        # Query DynamoDB
        response = table.query(
            KeyConditionExpression=Key('user_id').eq(user_id)
        )
        
        # Check if user exists
        if not response['Items']:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'User not found'})
            }
        
        # Return found user with custom JSON encoder for Decimal
        return {
            'statusCode': 200,
            'body': json.dumps(response['Items'][0], cls=DecimalEncoder)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }