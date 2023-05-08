import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pysparkPrueba002
import os

# Ejecutar:
# C:\DATOS\GITHUB_REPOS\myprojectsinpython\PysparkPruebas> python -m pytest

# Ejemplo: https://hangar.tech/posts/unit-testing-spark/


def test_read_csv(spark_session):

    # Get the path of the file in the 'tests' directory
    pathFicheroTest = os.path.join(os.path.dirname(
        __file__), "../recursos/fichero002.csv")
    print("file_path2="+pathFicheroTest)

    df = pysparkPrueba002.read_csv(spark_session, pathFicheroTest)
    assert df.count() == 3
    assert df.select(col("nombre")).distinct().count() == 2
