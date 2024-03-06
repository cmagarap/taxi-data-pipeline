from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master('local') \
    .appName('taxiTripsETL') \
    .config('spark.executor.memory', '5g') \
    .config('spark.cores.max', '6') \
    .config('spark.jars', 'src/pyspark/mysql-connector-java-8.0.13.jar') \
    .config('spark.driver.extraClassPath', 'src/pyspark/mysql-connector-java-8.0.13.jar') \
    .getOrCreate()
