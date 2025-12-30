from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("WeatherStream") \
    .getOrCreate()

schema = StructType([
    StructField("location", StructType([
        StructField("name", StringType()),
        StructField("country", StringType())
    ])),
    StructField("current", StructType([
        StructField("temp_c", FloatType()),
        StructField("humidity", IntegerType()),
        StructField("wind_kph", FloatType()),
        StructField("pressure_mb", FloatType()),
    ]))
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "weather_topic") \
    .load()

weather = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.location.name", "data.current.temp_c", "data.current.humidity", "data.current.wind_kph")

query = weather.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
