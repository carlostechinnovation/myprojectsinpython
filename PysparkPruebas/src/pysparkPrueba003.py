"""Prueba 003 de PYSPARK Pandas API.
Permite procesar DataFrames distribuidos sobre Spark, es decir, multiservidor (frente a librería pandas tradicional que es monoservidor).

Para evitar el error "ShutdownHookManager: Exception while deleting Spark temp dir", abrir el VSCode como Administrador.

¿Como ejecutarlo?
    - Version monoservidor (pandas_normal): python C:\DATOS\GITHUB_REPOS\myprojectsinpython\PysparkPruebas\src\pysparkPrueba003.py --modo "1"
    - Version multiservidor (pandas_api_on_spark): cmd /k C:\apps\spark-3.4.0-bin-hadoop3\bin\spark-submit --master "local[*]" C:\DATOS\GITHUB_REPOS\myprojectsinpython\PysparkPruebas\src\pysparkPrueba003.py --modo 2
    
Manual PandasAPIonSpark: https://spark.apache.org/docs/3.2.0/api/python/user_guide/pandas_on_spark/index.html
"""
import sys
import argparse
import pyspark.pandas as ps  # distribuido multiservidor
import pandas as pd  # monoservidor
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.shell import sc

technologies = ({
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", "Hadoop", "Spark", "Python", "NA"],
    'Fee': [22000, 25000, 23000, 24000, 26000, 25000, 25000, 22000, 1500],
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '30days', '50days', '40days'],
    'Discount': [1000, 2300, 1000, 1200, 2500, None, 1400, 1600, 0]
})


def init_spark():
    # ajustes para windows: https://cwiki.apache.org/confluence/display/HADOOP2/WindowsProblems

    # os.environ['HADOOP_HOME'] = "C:\\hadoop\\"

    import os
    import sys
    print("sys.executable ->" + sys.executable)
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    print("Se detiene la instancia de SparkSession abierta por defecto.")
    spark = SparkSession.builder.getOrCreate()
    spark.stop()

    print("Se inicia una nueva sesion Spark explicitamente...")
    # Create a SparkConf object
    conf = SparkConf().setAppName("pysparkPrueba003").setMaster("local[2]")\
        .set("spark.executor.memory", "1g")\
        .set("spark.sql.warehouse.dir", "target/spark-warehouse")\
        .set("spark.local.dir", "/tmp/spark-temp")\
        .set("spark.worker.cleanup.enabled", "true")
    # .set("spark.sql.execution.arrow.pyspark.enabled", "true")\
    # .set("spark.sql.execution.arrow.pyspark.fallback.enabled", "true")\

    spark = SparkSession.builder.config(conf=conf).getOrCreate()

    # Pintar configuracion Spark aplicada
    sc = spark.sparkContext
    conf = sc.getConf()
    print("spark.app.name = ", conf.get("spark.app.name"))
    print("spark.master = ", conf.get("spark.master"))
    print("spark.executor.memory = ", conf.get("spark.executor.memory"))

    return spark, sc


def convertirDFaDistribuido(df1, pathSalidaHdfs):
    """Convierte un DF no distribuido (pandas normal) en un DF distribuido (pyspark). Éste ese puede guardar en HDFS.
    Entrada: DF no distribuido
    Salida: DF distribuido
    """
    pass


def convertirDFaNoDistribuido(df1):
    """Convierte un DF distribuido (pyspark) en un DF no distribuido (pandas normal). El DF de entrada puede leerse desde HDFS.
    Entrada: DF distribuido
    Salida: DF no distribuido
    """
    pass


def monoservidor(spark):
    """Parametros: 
        - spark: Sesion Spark previamente abierta
    Salida:
        - DataFrame en memoria local (del driver)
    """
    print("############### PANDAS (normal, MONOSERVIDOR) ###############")
    # Create pandas DataFrame
    df = pd.DataFrame(technologies)
    print(df)

    # Leer CSV desde local
    sdf = spark.read.options(inferSchema='True', header='True')\
        .csv("C:\\apps\\pandas003.csv")

    # Use groupby() to compute the sum
    df2 = df.groupby(['Courses']).sum()
    df2.head()
    return df2


def multiservidor(spark):
    """Parametros: 
        - spark: Sesion Spark previamente abierta
    Salida:
        - DataFrame en memoria distribuida (de los workers)
    """

    print("############### PYSPARK PANDAS API (multiservidor, distribuido) ###############")
    print("Creando DF distribuido en los workers (no en driver) a partir de datos locales del driver (podria leerse un CSV desde HDFS o S3)...")
    df = ps.DataFrame(technologies)
    print("Primeras filas leidas:")
    print(df.head(n=3))

    # lectura de CSV desde HDFS
    # df = ps.read_csv(pathDirHdfs + 'prueba.csv')

    print("Datos agrupados (calculado en modo distribuido):")
    df2 = df.groupby(['Courses']).sum()
    print(df2.head())
    return df2


def main(argv, miSesionSpark):
    print("############### MAIN ###############")
    import os
    os.environ["PYARROW_IGNORE_TIMEZONE"] = "1"

    # https://spark.apache.org/docs/3.0.0-preview/sql-pyspark-pandas-with-arrow.html#compatibiliy-setting-for-pyarrow--0150-and-spark-23x-24x
    os.environ["ARROW_PRE_0_15_IPC_FORMAT"] = "0"

    # Parametros de entrada
    if len(argv) < 1:
        raise Exception("Numero de parametros incorrecto. Saliendo...")

    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--modo", type=int,
                           help="Modo de ejecucion: 1 (pandas_normal), 2 (pandas_api_on_spark)")

    args = argParser.parse_args()
    print("args.modo=" + str(args.modo))

    if args.modo == 1:
        dfEnMemoriaLocal = monoservidor(miSesionSpark)

        # print("Conversión de Pandas DF a Pandas API on Spark DF...")
        # psdf = ps.from_pandas(dfEnMemoriaLocal)
        # print("DF de pandas -->" + type(psdf))

    elif args.modo == 2:
        psdf = multiservidor(miSesionSpark)

        # print("Conversión de Pandas API on Spark DF a Pandas DF ( MUCHO CUIDADO: se puede llenar la memoria del contenedor driver )...")
        # dfEnMemoriaLocal = psdf.to_pandas()
        # print("dfEnMemoriaLocal -->" + str(type(dfEnMemoriaLocal)) + " Muestra:")
        # dfEnMemoriaLocal.head(n=3)

    else:
        raise Exception(
            "El parametro MODO toma un valor incorrecto. Saliendo...")


if __name__ == '__main__':
    miSesionSpark, sc = init_spark()
    main(sys.argv, miSesionSpark)
    print("Cerrando sesion spark...")
    miSesionSpark.stop()

print("############### FIN ###############")
