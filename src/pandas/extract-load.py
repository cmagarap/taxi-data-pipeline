import logging
import pandas as pd
import sqlite3

logging.basicConfig(level=logging.INFO)

raw_data = pd.read_parquet('../../dataset/yellow_tripdata_2023-12.parquet')
filtered_data = raw_data.loc[raw_data['passenger_count'] > 0]

conn = sqlite3.connect('taxidb.sqlite')

with open('../../sql/sqlite-DDL.sql', 'r') as file:
    query = file.read()

conn.execute(query)

logging.info('WRITING DATA...')
filtered_data.to_sql('trip', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
