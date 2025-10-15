from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3

def upload_test():
    s3 = boto3.client("s3")
    s3.put_object(Bucket="redapi-test", Key="test_upload.txt", Body="Hello Airflow!")

with DAG(
    "test_s3_upload",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    upload = PythonOperator(
        task_id="upload_test_file",
        python_callable=upload_test
    )
