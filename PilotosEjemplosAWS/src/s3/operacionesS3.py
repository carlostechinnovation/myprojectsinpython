import logging
import os
from botocore.exceptions import ClientError
import boto3

"""
Ejemplos sacados de aqui: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html#
Configuracion: https://github.com/awslabs/aws-shell
"""


def listarBuckets():
    # Retrieve the list of existing buckets
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)


def subir_fichero(file_name, bucket, prefijo, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(
            file_name, bucket, prefijo + object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == '__main__':
    listarBuckets()

    # subimos este mismo script que estamos ejecutando, por ejemplo
    file_name = os.path.realpath(__file__)
    bucket = "bucket-pruebapiloto"
    # es la ruta de subdirectorios dentro del bucket de S3
    prefijo = "proyecto1/datos/raw/"
    if subir_fichero(file_name, bucket, prefijo, object_name=None):
        print("Fichero subido BIEN hacia S3")
    else:
        print("Fichero subido MAL hacia S3")
