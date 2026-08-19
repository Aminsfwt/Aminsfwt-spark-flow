
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.python import PythonOperator


def hello_spark():
    print("Hello from Spark Airflow DAG!")

default_args = {
    'owner': 'spark airflow project',
    'catch_up': False,
    'start_date': '2026-08-19',
    'retries': '2'
}



with DAG(
    dag_id='spark_airflow_dag',
    default_args=default_args,
    schedule='* 10 * * *',  # Run every day at 10:00 AM
    description='A DAG to run Spark jobs using Airflow',
    tags=['spark', 'airflow'],
) as dag:
    
    py_spark_task = PythonOperator(
        task_id='py_spark_task',
        python_callable=hello_spark,  # Replace with your Python function
    )

    spark_submit_task = SparkSubmitOperator(
        task_id='spark_submit_task',
        application='/opt/airflow/dags/spark_job.py',  # Path to your Spark job script
        conn_id='spark_default',  # Connection ID for Spark
        verbose=True,
    )

    spark_submit_task >> py_spark_task
