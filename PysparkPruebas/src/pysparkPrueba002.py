from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


def read_csv(spark_session, file_path)->DataFrame:
    """Lee una ruta en local y carga un DataFrame (en memoria distribuida)

    Args:
        spark_session (_type_): sesion spark ya iniciada.
        file_path (_type_): path absoluto al fichero de entrada

    Returns:
        _type_: DataFrame con el contenido del fichero
    """
    df = spark_session.read.format("csv").option("header", "true").option("inferSchema", "true").load(file_path)
    print(str(type(df)))
    # df = df.toPandas()
    return df


def filter_by_column(df, column_name, column_value)->DataFrame:
    filtered_df = df.filter(df[column_name] == column_value)
    return filtered_df
