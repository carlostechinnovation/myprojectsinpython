"""Prueba 003 de PYSPARK Pandas API.
cmd /k C:\apps\spark-3.4.0-bin-hadoop3\bin\spark-submit --master "local[*]" C:\DATOS\GITHUB_REPOS\myprojectsinpython\PysparkPruebas\src\pysparkPrueba001.py
"""

import pyspark
from pyspark.sql import SparkSession
import os

def init_spark():
    # ajustes para windows: https://cwiki.apache.org/confluence/display/HADOOP2/WindowsProblems
    from pyspark.shell import sc
    # os.environ['HADOOP_HOME'] = "C:\\hadoop\\"

    import os
    import sys
    print("sys.executable ->" + sys.executable)
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    spark = SparkSession.builder.master(
        "local[2]").appName("HelloWorld").getOrCreate()
    sc = spark.sparkContext
    return spark, sc


def lecturaEscrituraFicheroLocal(miSesionSpark, misparkContext):
    print("lecturaEscrituraFicheroLocal...")
    textFile = miSesionSpark.read.text("C:\\apps\\prueba.txt")
    numeroFilas = textFile.count()
    print("El fichero tiene "+str(numeroFilas)+" filas")

    nums = misparkContext.parallelize([1, 2, 3, 4])
    print(nums.map(lambda x: x*x).collect())
    

def streamingLeyendoSocket(miSesionSpark):
    print("streamingLeyendoSocket...")
    df = miSesionSpark.readStream    .format("socket")    .option(
        "host", "localhost")    .option("port", "9090")    .load()

    df.printSchema()

    # Escribir el Dataframe en real-time a kafka, base de datos, etc
    # query = count.writeStream.format("console").outputMode("complete").start().awaitTermination()


def streamingLeyendoKafka(miSesionSpark):
    print("streamingLeyendoKafka...")
    #  From starting
    df = miSesionSpark.readStream.format("kafka").option("kafka.bootstrap.servers", "192.168.1.100:9092").option("subscribe", "json_topic").option("startingOffsets", "earliest").load()

    # writes message to another topic in Kafka using writeStream()
    # df.selectExpr("CAST(id AS STRING) AS key", "to_json(struct(*)) AS value")
    #    .writeStream
    #    .format("kafka")
    #    .outputMode("append")
    #    .option("kafka.bootstrap.servers", "192.168.1.100:9092")
    #    .option("topic", "json_data_topic")
    #    .start()
    #    .awaitTermination()


def main():

    print("Pyspark pruebas - INICIO")
    # Previamente (en WINDOWS):
    # Ejecutar en terminal: C:\apps\spark-3.4.0-bin-hadoop3\bin\pyspark
    # Web:  http://DESKTOP-K5O3F28:4040
    # Configurar Spark History Server: spark-defaults.conf
    # Iniciar Spark History Server: C:\apps\spark-3.4.0-bin-hadoop3\bin\spark-class.cmd org.apache.spark.deploy.history.HistoryServer
    # https://stackoverflow.com/questions/41825871/exception-while-deleting-spark-temp-dir-in-windows-7-64-bit

    miSesionSpark, sc = init_spark()
    lecturaEscrituraFicheroLocal(miSesionSpark, sc)
    # streamingLeyendoSocket(miSesionSpark)
    # streamingLeyendoKafka(miSesionSpark)
    
    miSesionSpark.stop()
    print("Pyspark pruebas - FIN")


if __name__ == '__main__':
    main()
