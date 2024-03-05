import pandas as pd
import sqlite3
import plotly.express as px

conn = sqlite3.connect('taxidb.sqlite')

trip_data = pd.read_sql('SELECT * FROM trip', conn)
trip_data['tpep_pickup_datetime'] = pd.to_datetime(trip_data['tpep_pickup_datetime'], format='%Y-%m-%d %H:%M:%S')

filtered_data = trip_data[trip_data['tpep_pickup_datetime'].dt.strftime('%Y-%m') == '2023-12']
filtered_data = filtered_data.sort_values(by='tpep_pickup_datetime')

aggregate_data = filtered_data.groupby(filtered_data['tpep_pickup_datetime'].dt.date)['total_amount'].sum()
aggregate_data = aggregate_data.to_frame()

print(aggregate_data.info())
aggregate_data.rename(columns={'total_amount': 'Amount', 'tpep_pickup_date': 'Date'}, inplace=True)
print(aggregate_data.head(32))
print(type(aggregate_data))

# Line Chart
fig = px.line(aggregate_data, title='TCL Trip Total Amount Earned per day for December 2023', markers=True)
fig.show()
