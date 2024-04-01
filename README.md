# TLC Taxi Trip Data Pipeline
The main objective of this data pipeline project is to extract data from nyc.gov website, load the data into an SQL database, and perform aggregations on the data so that it can be used for visualizing the daily amount earned from taxi trips on December 2023. I created 3 solutions -- using Pandas, Pyspark, and Docker to achieve this.

## Folder Structure
```
├── dataset
│   └── yellow_tripdata_2023-12.parquet
├── figures -- folder for graph/chart
│   └── line-fig.html
├── sql -- folder for all SQL files
│   ├── CREATE.sql -- used for creating table in Docker MySQL
│   ├── CREATE-TABLE.sql -- DDL for trip table in MySQL
│   ├── Dockerfile -- Docker configuration file for MySQL
│   └── sqlite-DDL.sql -- DDL for trip table in SQLite
├── src -- contains all Python scripts
│   ├── pandas -- folder for the Pandas solution
│       ├── aggregate-visualize.py
│       ├── extract-load.py
│       └── taxidb.sqlite
│   └── pyspark -- folder for the Pyspark solution
│       ├── __init__.py
│       ├── aggregate-visualize.py
│       ├── extract-load.py
│       └── mysql-connector-java-8.0.13.jar
├── docker-compose.yml -- Docker compose file for MySQL and Python containers
├── Dockerfile -- Docker configuration file 
├── README.md
└── requirements.txt -- Python requirements file
    

```

## Setup Instructions
### Pandas
1. Clone or download this repository.
2. Install [Python 3](https://www.python.org/downloads/).
3. Install Python libraries:
`pip3 install -r requirements.txt`

### Pyspark
1. Clone or download this repository.
2. Install [Java 11](https://www.oracle.com/ph/java/technologies/javase/jdk11-archive-downloads.html) depending on your Operating System. You may use [Homebrew](https://formulae.brew.sh/formula/openjdk@11) for Mac.
3. Install [Python 3](https://www.python.org/downloads/).
4. Install Python libraries:
`pip3 install -r requirements.txt`
5. Install [MySQL](https://dev.mysql.com/downloads/installer/). You may use [Homebrew](https://formulae.brew.sh/formula/mysql) for Mac.
6. Create a root MySQL User:
```
CREATE USER 'user'@'localhost' IDENTIFIED BY 'user123'; 
GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

7. Run SQL scripts for creating database and table:
```
mysql -u user -p -e "CREATE DATABASE taxidb";
mysql -u user -p taxidb < sql/CREATE-TABLE.sql
```

### Docker
1. Install [Docker](https://www.docker.com/products/docker-desktop/).


## Execution Instructions
### Pandas
1. From the root folder (ota-data-task), execute the Python script for data extraction and load:
```
python3 src/pandas/extract-load.py
```
2. Execute the Python script for aggregating and producing graph visualization:
```
python3 src/pandas/aggregate-visualize.py
```
3. An interactive graph will open in your default web browser and an HTML file is saved in the figures folder.


### Pyspark
1. From the root folder (ota-data-task), execute the Python script for data extraction and load:
```
python3 src/pyspark/extract-load.py
```
2. Execute the Python script for aggregating and producing graph visualization:
```
python3 src/pyspark/aggregate-visualize.py
```
3. An interactive graph will open in your default web browser and an HTML file is saved in the figures folder.


### Docker
1. From the root folder (ota-data-task), execute the command:
```
docker-compose up
```
2. Both the extract-load.py and aggregate-visualize.py file will run when the docker container is built from docker-compose. 
3. An interactive graph will open in your default web browser and an HTML file is saved in the figures folder in the Docker container.



## Output
#### Visualization:
![Line Chart](https://raw.githubusercontent.com/cmagarap/ota-data-task/main/figures/Screenshot.png)

#### The loaded table in MySQL:
![Trip Table](https://raw.githubusercontent.com/cmagarap/ota-data-task/main/figures/Screenshot-table.png)


#### The aggregate table:
![Aggregate Table](https://raw.githubusercontent.com/cmagarap/ota-data-task/main/figures/Screenshot-agg.png)
