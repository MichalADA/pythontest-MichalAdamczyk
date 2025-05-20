import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):
    try:
        # Parsowanie treści żądania
        body = json.loads(event['body'])
        
        # Sprawdzenie czy wymagane pola są obecne
        if 'first_name' not in body or 'age' not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Missing required fields: first_name and age'})
            }
        
        # Generowanie unikalnego ID użytkownika
        user_id = str(uuid.uuid4())
        
        # Tworzenie nowego rekordu
        item = {
            'user_id': user_id,
            'first_name': body['first_name'],
            'age': body['age']
        }
        
        # Zapisanie do DynamoDB
        table.put_item(Item=item)
        
        # Zwrócenie odpowiedzi z ID użytkownika
        return {
            'statusCode': 201,
            'body': json.dumps({'user_id': user_id})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)})
        }