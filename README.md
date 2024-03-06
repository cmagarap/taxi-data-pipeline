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
2. Install [Java 11](https://www.oracle.com/ph/java/technologies/javase/jdk11-archive-downloads.html) depending on you Operating System. You may use [Homebrew](https://formulae.brew.sh/formula/openjdk@11) for Mac.
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
2. Both the extract-load.py and aggregate-visualize.py file will be run when the docker container is built from docker-compose. 
3. An interactive graph will open in your default web browser and an HTML file is saved in the figures folder in the Docker container.


## Discussion
I created three solutions in order to make sure that I cover more scenarios. The easiest one is the Pandas solution because I just used SQLite and Pandas for that. There was no Java and server database dependencies and I have experience in using the Pandas library.

The second solution I did was using Pyspark. For me, this is the mid-tier of difficulty among the three because it depends on Java and MySQL on local machine to run. The challenge I faced here was looking for the right mysql jdbc connector and connecting it to the MySQL on my local machine. Because I am not used to local Pyspark setups, I looked for a lot of discussions online on how to properly implement this and I succeeded.

The Docker solution was the most difficult for me. First, because of some images from docker hub depends on Linux x86 architecture and the machine I am using is Mac arm64. I spent a lot of time on this, I tried turning on Rosetta (the emulation software on my Mac) but the image I initially used did not work. So I tried to use the Python image python:3.11.8-bullseye and the setup worked. I also included Java installation in the Dockerfile because of Pyspark. Another challenge I faced on Docker is the connection of MySQL container to the Python container. The jdbc driver did not work at first but when I configured the right file paths, I got connected to MySQL. I really tried on this solution because I wanted to make the project setup easier but the configuration of Docker took a lot of time from me.

Lastly, I forgot to create a view for the aggregated data. I don't think I will make it to the deadline of this test if I added it at the last minute.

## Output
![Line Chart](https://raw.githubusercontent.com/cmagarap/ota-data-task/main/figures/Screenshot.png)