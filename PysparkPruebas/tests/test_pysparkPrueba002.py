import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import src.pysparkPrueba002 as psp002
import os
import pyspark.pandas as ps  # distribuido multiservidor
import pandas as pd  # monoservidor


# Ejecutar:
# C:\DATOS\GITHUB_REPOS\myprojectsinpython\PysparkPruebas> python -m pytest

# Ejemplo: https://hangar.tech/posts/unit-testing-spark/

# para debuguear desde remoto: https://code.visualstudio.com/docs/python/debugging#_debugging-by-attaching-over-a-network-connection


def test_read_csv(spark_session):

    # Get the path of the file in the 'tests' directory
    pathFicheroTest = os.path.join(os.path.dirname(__file__), "recursos/fichero002.csv")
    print("file_path2="+pathFicheroTest)

    df = psp002.read_csv(spark_session, pathFicheroTest)
    
    # assert "pyspark.sql.dataframe.DataFrame" == str(type(df))
    assert df.count() == 3
    asdfasf=df.select(col("nombre"))
    assert df.select(col("nombre")).distinct().count() == 2
    
    print("Numero de palabras...")
    pathFicheroTest2 = os.path.join(os.path.dirname(__file__), "recursos/prueba.txt")
    df2 = psp002.read_csv(spark_session, pathFicheroTest2)
    
    df2.createOrReplaceTempView("parquetFile")
    tuesdaycrimes = spark_session.sql("SELECT LENGTH(CAMPO) - LENGTH(REPLACE(CAMPO, ' ', ''))+1 FROM parquetFile")
    print(tuesdaycrimes.show())
