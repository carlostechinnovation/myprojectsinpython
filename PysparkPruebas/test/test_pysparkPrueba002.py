import pytest
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pysparkPrueba002

# Ejecutar:
# C:\DATOS\GITHUB_REPOS\myprojectsinpython\PysparkPruebas> python -m pytest


def test_read_csv(spark_session):
    file_path = "C:\\apps\\fichero002.csv"
    df = pysparkPrueba002.read_csv(spark_session, file_path)
    assert df.count() == 3
    assert df.select(col("nombre")).distinct().count() == 2
