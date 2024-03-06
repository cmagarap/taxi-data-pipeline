from __init__ import spark
from pyspark.sql.functions import sum, month, year, round
from pyspark.sql.types import DateType
import plotly.express as px
import os
import logging

logging.basicConfig(level=logging.INFO)

logging.info('Connecting to MySQL...')
trip_data = spark.read \
    .format('jdbc') \
    .option('url', 'jdbc:mysql://localhost:3306/taxidb?useSSL=false') \
    .option('dbtable', 'trip') \
    .option('user', 'user') \
    .option('password', 'user123') \
    .load()

filtered_data = trip_data.filter(year('tpep_pickup_datetime') == 2023) \
    .filter(month('tpep_pickup_datetime') == 12).orderBy('tpep_pickup_datetime')

aggregate_data = filtered_data.groupby(
        filtered_data['tpep_pickup_datetime'].cast(DateType()).alias('tpep_pickup_date')
    ).agg(round(sum('total_amount'), 2).alias('total_amount')) \
    .orderBy('tpep_pickup_date')

# Convert Pyspark DataFrame to Pandas
aggregate_data_pd = aggregate_data.toPandas()
aggregate_data_pd.rename(columns={'total_amount': 'Amount', 'tpep_pickup_date': 'Date'}, inplace=True)

logging.info('Generating Data Figure...')
# Line Chart
fig = px.line(aggregate_data_pd, x='Date', y='Amount',
              title='TCL Trip Total Amount Earned per day for December 2023', markers=True)
fig.show()
logging.info('Figure generated!')

if not os.path.exists('figures'):
    os.mkdir('figures')

logging.info('Saving Data Figure as HTML file...')
# Save the Figure into an HTML File
fig.write_html('figures/line-fig.html')
logging.info('Figure saved!')
