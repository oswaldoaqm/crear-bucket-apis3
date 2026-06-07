import boto3
import base64

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket    = event['body']['nombre_bucket']
    nombre_directorio = event['body']['nombre_directorio']
    nombre_archivo   = event['body']['nombre_archivo']
    contenido_base64 = event['body']['contenido_base64']
    content_type     = event['body'].get('content_type', 'application/octet-stream')
    # Aseguramos que el directorio termine en "/"
    if not nombre_directorio.endswith('/'):
        nombre_directorio = nombre_directorio + '/'
    # Construimos la ruta completa: directorio/archivo
    key = nombre_directorio + nombre_archivo
    # Decodificamos el contenido base64
    contenido = base64.b64decode(contenido_base64)
    # Proceso
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=nombre_bucket,
        Key=key,
        Body=contenido,
        ContentType=content_type
    )
    # Salida (json)
    return {
        'statusCode': 200,
        'body': 'Archivo subido correctamente',
        'bucket': nombre_bucket,
        'ruta': key
    }