"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator
from datetime import datetime, timedelta


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2015, 6, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG("simple-http", default_args=default_args, schedule_interval=timedelta(1)) as http:
    task_1 = SimpleHttpOperator(
        dag=http,
        task_id='get_naver_1',
        endpoint='/',
        method="get"
        )

    task_2 = SimpleHttpOperator(
        task_id='get_naver_2',
        endpoint='/',
        method="get",
        dag=http
        )

task_1 >> task_2
