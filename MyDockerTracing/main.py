import docker
import dotenv
import os
import requests
import json

"""
OBTIENE LA LISTA DE LOS PAQUETES DOCKER MAS USADOS EN EL ULTIMO MES, ORDENADOS POR EL NUMERO DE PULLS (En la web no ofrecen esa ordenacion)
Ademas, sirve como ejemplo de cómo conectarse a la API de DockerHub.
Y para cargar variables de contexto usando python-dotenv

Requiere tener instalado el cliente Docker Desktop en local y tambien hacer esto: en el fichero ~/.docker/config.json change credsStore to credStore
(ver https://stackoverflow.com/questions/67642620/docker-credential-desktop-not-installed-or-not-available-in-path )
"""

print(" Se leen variables secretas desde fichero protegido...")
PATH_FICHERO_CLAVES = "C:/DATOS/CLAVES_NOBORRAR/MyDockerTracing_claves.env"
# cargando variables de entorno
dotenv.load_dotenv(PATH_FICHERO_CLAVES)
miusuario = os.getenv('miusuario')
miclave = os.getenv('miclave')
miemail = os.getenv('miemail')
print("USUARIO: " + miusuario)

print("Conexion a cliente Docker Desktop...")
client = docker.from_env()
loginResponse = client.login(username=miusuario, password=miclave,
                             email=miemail, registry='https://index.docker.io/v1/')

print(loginResponse)
estado = loginResponse.get("Status")

if "Succeed" not in estado:
    print("ERROR en la conexion. Saliendo...")
    exit

print("Resumen de MIS repositorios:")
urlMisRepositorios = "https://hub.docker.com/v2/namespaces/"+miusuario+"/repositories/"
params = dict()  # ejemplo: {"id": [1, 2, 3], "userId":1}
resp = requests.get(url=urlMisRepositorios, params=params)
data = resp.json()  # Respuesta en un DICT
print(data)
