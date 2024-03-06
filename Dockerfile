FROM python:3.11.8-bullseye

COPY . /usr/ota-data-task
WORKDIR /usr/ota-data-task

# Install OpenJDK-11
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;

# Install PYTHON requirements
#COPY src/ ./
RUN pip install -r requirements.txt

# START WEBAPP SERVICE
CMD [ "python", "src/pyspark/extract-load.py" ]