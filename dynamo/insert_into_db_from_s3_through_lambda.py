import json
import boto3
from decimal import Decimal

def lambda_handler(event, context):
    # S3 settings
    s3_bucket = 'customerstocks'
    s3_key = 'CustStocks.txt' 
    
    # DynamoDB settings
    dynamodb_table = 'CustomerStocks'
    
    # Connect to S3
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket=s3_bucket, Key=s3_key)
    data = s3_object['Body'].read().decode('utf-8')
    
    # Connect to DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(dynamodb_table)
    
    # Process and insert data
    for line in data.split('\n'):
        if line.strip():  # Skip empty lines
            customer_id, stock_value1, stock_value2 = line.split()
            table.put_item(
                Item={
                    'CustomerID': customer_id,
                    'StockValue1': Decimal(stock_value1),
                    'StockValue2': Decimal(stock_value2)
                }
            )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data inserted successfully')
    }