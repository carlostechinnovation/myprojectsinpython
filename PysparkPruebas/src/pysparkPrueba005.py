"""Operaciones basicas con DATAFRAMES en PYSPARK.
¿Como ejecutarlo?
cmd /k C:\apps\spark-3.4.0-bin-hadoop3\bin\spark-submit --master "local[*]" C:\DATOS\GITHUB_REPOS\myprojectsinpython\PysparkPruebas\src\pysparkPrueba005.py
"""

from pyspark.sql import SparkSession
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql import Column
from pyspark.sql.functions import upper
from pyspark.sql.functions import pandas_udf
import os
from pyspark.sql.functions import expr


def pandas_filter_func(iterator):
    for pandas_df in iterator:
        yield pandas_df[pandas_df.a == 1]

def plus_mean(pandas_df):
    return pandas_df.assign(v1=pandas_df.v1 - pandas_df.v1.mean())

def main():
    spark = SparkSession.builder.getOrCreate()
    
    # Nivel de log
    spark.sparkContext.setLogLevel("WARN")
    
    # #Con datos brutos
    # df = spark.createDataFrame([
    #     Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    #     Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    #     Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
    # ])
    # df

    # #Con schema explicito
    # df = spark.createDataFrame([
    #     (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    #     (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    #     (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
    # ], schema='a long, b double, c string, d date, e timestamp')
    # df

    # Desde un PANDAS DF
    pandas_df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [2., 3., 4.],
        'c': ['string1', 'string2', 'string3'],
        'd': [date(2000, 1, 1), date(2000, 2, 1), date(2000, 3, 1)],
        'e': [datetime(2000, 1, 1, 12, 0), datetime(2000, 1, 2, 12, 0), datetime(2000, 1, 3, 12, 0)]
    })
    df = spark.createDataFrame(pandas_df)
    df.show()
    df.printSchema()
    
    print("==================== VISTAS =================")
    spark.conf.set('spark.sql.repl.eagerEval.enabled', True)
    df.show(1, vertical=True)
    df.select("a", "b", "c").describe().show()
    
    print("Conversion a pandas (si son pocas filas):")
    df.toPandas()
    
    print("Seleccion y acceso a datos: es LAZILY EVALUATED")
    df.select(df.c).show()
    df.withColumn('upper_c', upper(df.c)).show()
    
    print("Funciones (UDF):")
    df.select(pandas_plus_one(df.a)).show()
    df.mapInPandas(pandas_filter_func, schema=df.schema).show()

    print("Agrupacion de datos:")
    df = spark.createDataFrame([
    ['red', 'banana', 1, 10], ['blue', 'banana', 2, 20], ['red', 'carrot', 3, 30],
    ['blue', 'grape', 4, 40], ['red', 'carrot', 5, 50], ['black', 'carrot', 6, 60],
    ['red', 'banana', 7, 70], ['red', 'grape', 8, 80]], schema=['color', 'fruit', 'v1', 'v2'])
    df.groupby('color').avg().show()
    
    df.groupby('color').applyInPandas(plus_mean, schema=df.schema).show()

    df1 = spark.createDataFrame(
    [(20000101, 1, 1.0), (20000101, 2, 2.0), (20000102, 1, 3.0), (20000102, 2, 4.0)],
    ('time', 'id', 'v1'))

    df2 = spark.createDataFrame(
        [(20000101, 1, 'x'), (20000101, 2, 'y')],
        ('time', 'id', 'v2'))

    def merge_ordered(l, r):
        return pd.merge_ordered(l, r)

    df1.groupby('id').cogroup(df2.groupby('id')).applyInPandas(
        merge_ordered, schema='time int, id int, v1 double, v2 string').show()

    print("Operaciones con CSVs:")
    
    pathSalida="tests/recursos/pruebaSalida.csv"
    if os.path.exists(pathSalida):
        os.remove(pathSalida)
        df.write.csv(pathSalida, header=True)
    
    if os.path.exists(pathSalida):
        spark.read.csv(pathSalida, header=True).show()
    else:
        print("ERROR El fichero de salida no se escribio, asi que ahora no se puede leer")

    print("================ SPARK SQL =============")
    df.createOrReplaceTempView("tableA")
    spark.sql("SELECT count(*) from tableA").show()
    
    spark.udf.register("add_one", add_one)  #Funcion
    spark.sql("SELECT add_one(v1) FROM tableA").show()

    df.selectExpr('add_one(v1)').show()
    df.select(expr('count(*)') > 0).show()
    
    print("Cerrando sesion Spark...")
    spark.stop()


if __name__ == '__main__':
    main()
    

@pandas_udf('long')
def pandas_plus_one(series: pd.Series) -> pd.Series:
    # Simply plus one by using pandas Series.
    return series + 1

@pandas_udf("integer")
def add_one(s: pd.Series) -> pd.Series:
    return s + 1
