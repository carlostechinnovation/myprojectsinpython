import pytest
from pyspark.sql import SparkSession


@pytest.fixture  # (scope="session")
def spark_session():
    spark = SparkSession.builder.appName(
        "MisPruebasSpark").master("local[*]").getOrCreate()
    yield spark
    spark.stop()
