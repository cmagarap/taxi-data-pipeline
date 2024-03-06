from __init__ import spark
import logging

logging.basicConfig(level=logging.INFO)

raw_data = spark.read.parquet('dataset/yellow_tripdata_2023-12.parquet')

filtered_data = raw_data.filter(raw_data.passenger_count > 0)


logging.info('WRITING DATA...')
filtered_data.write \
    .format('jdbc') \
    .option('url', 'jdbc:mysql://localhost:3306/taxidb?useSSL=false') \
    .option('dbtable', 'trip') \
    .option('user', 'root') \
    .option('password', 'root') \
    .mode('overwrite') \
    .save()
logging.info('Data successfully loaded into MySQL')
