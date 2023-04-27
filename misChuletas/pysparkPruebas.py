import pyspark
from pyspark.sql import SparkSession
import os


def init_spark():
    # ajustes para windows: https://cwiki.apache.org/confluence/display/HADOOP2/WindowsProblems
    from pyspark.shell import sc
    # os.environ['HADOOP_HOME'] = "C:\\hadoop\\"

    spark = SparkSession.builder.master(
        "local[*]").appName("HelloWorld").getOrCreate()
    sc = spark.sparkContext
    return spark, sc


def main():
    miSesionSpark, sc = init_spark()

    textFile = miSesionSpark.read.text("C:\\apps\\prueba.txt")
    numeroFilas = textFile.count()
    print("El fichero tiene "+str(numeroFilas)+" filas")

    # nums = sc.parallelize([1, 2, 3, 4])
    # print(nums.map(lambda x: x*x).collect())


if __name__ == '__main__':
    main()
