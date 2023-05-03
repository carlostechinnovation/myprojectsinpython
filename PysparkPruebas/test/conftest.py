import pytest
from pyspark.sql import SparkSession


@pytest.fixture
def spark_session():
    spark = SparkSession.builder.appName(
        "MisPruebasSpark").master("local[*]").getOrCreate()
    yield spark
    spark.stop()
