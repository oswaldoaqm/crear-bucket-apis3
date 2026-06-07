import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['nombre_bucket']
    nombre_directorio = event['body']['nombre_directorio']
    # En S3 un directorio es un objeto vacío que termina en "/"
    if not nombre_directorio.endswith('/'):
        nombre_directorio = nombre_directorio + '/'
    # Proceso
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=nombre_bucket,
        Key=nombre_directorio,
        Body=''
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'body': 'Directorio creado correctamente',
        'bucket': nombre_bucket,
        'directorio': nombre_directorio
    }