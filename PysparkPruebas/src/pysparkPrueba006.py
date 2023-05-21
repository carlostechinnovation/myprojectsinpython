"""Operaciones basicas con PANDAS API en PYSPARK.
¿Como ejecutarlo?
cmd /k C:\apps\spark-3.4.0-bin-hadoop3\bin\spark-submit --master "local[*]" C:\DATOS\GITHUB_REPOS\myprojectsinpython\PysparkPruebas\src\pysparkPrueba006.py

Mas info: https://spark.apache.org/docs/latest/api/python/getting_started/quickstart_ps.html
"""
import pandas as pd
import numpy as np
import pyspark.pandas as ps
from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.getOrCreate()
    
    # Nivel de log
    spark.sparkContext.setLogLevel("WARN")
    
    s = ps.Series([1, 3, 5, np.nan, 6, 8])
    s
    
    psdf = ps.DataFrame(
    {'a': [1, 2, 3, 4, 5, 6],
     'b': [100, 200, 300, 400, 500, 600],
     'c': ["one", "two", "three", "four", "five", "six"]},
    index=[10, 20, 30, 40, 50, 60])
    psdf
    
    dates = pd.date_range('20130101', periods=6)
    dates
    pdf = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    pdf
    psdf = ps.from_pandas(pdf)
    type(psdf)
    psdf
    
    print("Se crean Dataframes DISTRIBUIDOS...")
    sdf = spark.createDataFrame(pdf)
    sdf.show()
    
    print("Conversion a Pandas API")
    psdf = sdf.pandas_api()
    psdf
    psdf.dtypes
    psdf.head()
    # The natural order can be preserved by setting compute.ordered_head option but it causes a performance overhead with sorting internally.
    
    print("Missing data:")
    pdf1 = pdf.reindex(index=dates[0:4], columns=list(pdf.columns) + ['E'])
    pdf1.loc[dates[0]:dates[1], 'E'] = 1
    psdf1 = ps.from_pandas(pdf1)
    psdf1
    psdf1.dropna(how='any')
    psdf1.fillna(value=5)

    print("Operaciones:")
    psdf.mean()
    
    print("Configuraciones de SparK...")
    prev = spark.conf.get("spark.sql.execution.arrow.pyspark.enabled")  # Keep its default value.
    ps.set_option("compute.default_index_type", "distributed")  # Use default index prevent overhead.
    import warnings
    warnings.filterwarnings("ignore")  # Ignore warnings coming from Arrow optimizations.
    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", True)
    # %timeit ps.range(300000).to_pandas()
    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", False)
    # %timeit ps.range(300000).to_pandas()
    ps.reset_option("compute.default_index_type")
    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", prev)  # Set its default value back.
        
    print("Cerrando sesion Spark...")
    spark.stop()

if __name__ == '__main__':
    main()
    