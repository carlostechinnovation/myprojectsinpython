# Proyectos piloto en PYTHON

Proyectos piloto que SÍ funcionan.
Son pruebas funcionales (solucionan necesidades de usuarios) o técnicas (probar librerías). 

Lenguaje de programación: Python.

Cliente comercial: uso personal.

## PilotosEjemplosAWS v.0.1

Ejemplos de uso de los servicios de Amazon AWS: S3, EC2, codedeploy, IAM, SES...

## PythonBasicoChuleta v.0.1

Mis apuntes sobre un cursillo online de operaciones básicas en Python.

## MyDockerTracking v.0.1

Objetivo: ver cuáles son las imágenes Docker más utilizadas recientemente, ya que el buscador oficial de Dockerhub no permite ordenar por fecha (https://hub.docker.com/search).

## YoutubeUtils v.0.1

Lectura masiva y guardado del contenido de una lista de vídeos en Youtube.

Guarda vídeo+audio o solo audio.

## PysparkPruebas v.0.1

POC que usa la librería pyspark de Python sobre procesamiento distribuido con Apache Spark <img src="PysparkPruebas\resources\spark.png" alt="Apache Spark" width="60"/>

Para construir el paquete, he seguido el manual: https://packaging.python.org/en/latest/tutorials/packaging-projects/
Se construye con: py -m build

Manual útil sobre operaciones básicas con Pyspark, comparadas con DataFrames monoservidor: https://towardsdatascience.com/run-pandas-as-fast-as-spark-f5eefe780c45

Si en Windows no se reconoce el comando python3, hacer esto:

```
cd C:\apps\python3_symb_link
mklink python3.exe C:\Users\casa\AppData\Local\Programs\Python\Python37\python.exe
```

