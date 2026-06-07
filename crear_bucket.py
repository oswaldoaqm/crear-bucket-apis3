import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['nombre_bucket']
    # Proceso
    s3 = boto3.client('s3')
    response = s3.create_bucket(
        Bucket=nombre_bucket,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-1'
        }
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'body': 'Bucket creado correctamente',
        'bucket': nombre_bucket
    }