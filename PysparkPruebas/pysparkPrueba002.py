from pyspark.sql import SparkSession


def read_csv(spark_session, file_path):
    df = spark_session.read.format("csv").option(
        "header", "true").load(file_path)
    return df


def filter_by_column(df, column_name, column_value):
    filtered_df = df.filter(df[column_name] == column_value)
    return filtered_df
