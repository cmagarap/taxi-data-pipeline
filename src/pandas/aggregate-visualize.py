import pandas as pd
import sqlite3
import plotly.express as px
import os
import logging

logging.basicConfig(level=logging.INFO)

conn = sqlite3.connect('src/pandas/taxidb.sqlite')

trip_data = pd.read_sql('SELECT * FROM trip', conn)
trip_data['tpep_pickup_datetime'] = pd.to_datetime(trip_data['tpep_pickup_datetime'], format='%Y-%m-%d %H:%M:%S')

filtered_data = trip_data[trip_data['tpep_pickup_datetime'].dt.strftime('%Y-%m') == '2023-12']
filtered_data = filtered_data.sort_values(by='tpep_pickup_datetime')

aggregate_data = filtered_data.groupby(filtered_data['tpep_pickup_datetime'].dt.date)['total_amount'].sum()
aggregate_data = aggregate_data.to_frame()

aggregate_data.rename(columns={'total_amount': 'Amount', 'tpep_pickup_date': 'Date'}, inplace=True)

logging.info('Generating Data Figure...')
# Line Chart
fig = px.line(aggregate_data, title='TCL Trip Total Amount Earned per day for December 2023', markers=True)
fig.show()
logging.info('Figure generated!')

if not os.path.exists('figures'):
    os.mkdir('figures')

logging.info('Saving Data Figure as HTML file...')
# Save the Figure into an HTML File
fig.write_html('figures/line-fig1.html')
logging.info('Figure saved!')
