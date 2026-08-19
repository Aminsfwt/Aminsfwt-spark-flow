FROM image: apache/airflow:2.7.3-python3.11

USER root
RUN apt-get update \
    && apt-get install -y gcc python3-dev openjdk-11-jdk \
    && apt-get clean 

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

USER airflow

# Python deps
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

