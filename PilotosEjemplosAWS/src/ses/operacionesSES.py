"""
EJEMPLOS: https://www.learnaws.org/2020/12/18/aws-ses-boto3-guide/
"""
import boto3
from email import encoders
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def verify_email_identity(destino, region):
    """Los emails de DESTINO deben ser verificados OBLIGATORIAMENTE
    """
    print("Verificando email destino " + destino + " ...")
    ses_client = boto3.client("ses", region_name=region)
    response = ses_client.verify_email_identity(EmailAddress=destino)
    print(response)


def send_email_with_ses(sender_email, recipient_email, subject, body_text):
    # Create an AWS SES client
    ses_client = boto3.client('ses')

    # Send the email
    response = ses_client.send_email(
        Source=sender_email,
        Destination={'ToAddresses': [recipient_email]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body_text}}
        }
    )

    # Return the response
    return response


def send_html_email(origen, destinos, region):
    print("ENVIO TIPO 1 (html)....")

    ses_client = boto3.client("ses", region_name=region)
    CHARSET = "UTF-8"
    HTML_EMAIL_CONTENT = """
        <html>
            <head></head>
            <h1 style='text-align:center'>Hola soy Carlos</h1>
            <p>Hola mundo</p>
            </body>
        </html>
    """

    response = ses_client.send_email(
        Destination={
            "ToAddresses": destinos,
        },
        Message={
            "Body": {
                "Html": {
                    "Charset": CHARSET,
                    "Data": HTML_EMAIL_CONTENT,
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Prueba de Carlos desde AWS SES. Hola!! :-)",
            },
        },
        Source=origen,
    )


def send_email_with_attachment(origen, destinos, region):
    print("ENVIO TIPO 2 (adjuntos)....")
    msg = MIMEMultipart()
    msg["Subject"] = "This is an email with an attachment!"
    msg["From"] = origen
    msg["To"] = destinos

    # Set message body
    body = MIMEText("Hello, world!", "plain")
    msg.attach(body)

    # subimos este mismo script que estamos ejecutando, por ejemplo
    file_name = "ejemplo.txt"

    with open(file_name, "rb") as attachment:
        part = MIMEApplication(attachment.read())
        part.add_header("Content-Disposition",
                        "attachment",
                        filename=file_name)
    msg.attach(part)

    # Convert message to string and send
    ses_client = boto3.client("ses", region_name=region)
    response = ses_client.send_raw_email(
        Source=origen,
        Destinations=destinos,
        RawMessage={"Data": msg.as_string()}
    )

    print(response)


if __name__ == '__main__':

    boto3.set_stream_logger('botocore', level='INFO')

    origen = "carlosandresgarcia1986@gmail.com"
    destinos = ["carlosandresgarcia1986@hotmail.com",
                # "luisandresgarcia@gmail.com",
                # "fcacereslau@hotmail.com",
                ]
    region = "eu-north-1"

    # ANTES DE ENVIAR, hay que verificar ORIGEN y DESTINOS
    verify_email_identity(origen, region)
    for destino in destinos:
        verify_email_identity(destino, region)

    # EMAILS de VARIOS TIPOS:
    # response = send_email_with_ses(
    #     origen, destinos, "Mi asunto de pruebas", "Hola, esto es una prueba.")
    # print(response)

    send_html_email(origen, destinos, region)

    # send_email_with_attachment(origen, destinos, region)
