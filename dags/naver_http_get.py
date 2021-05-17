from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

from datetime import datetime, timedelta
import requests
from requests import status_codes


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 5, 16),
    "email": ["nara03050@gmail.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

class NaverServerSensor(BaseSensorOperator):

    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(NaverServerSensor, self).__init__(*args, **kwargs)
          
    def poke(self, context):
        response = requests.get(url="https://naver.com", verify=False)
        status_code = response.status_code
        print("status code = " + str(status_code))
        if status_code == 200:
            return True            
        return False


with DAG("naver_sensor_dag", default_args=default_args, schedule_interval="5 4 * * *", catchup=False) as sensor_dag:
    task_1 = SimpleHttpOperator(
        dag=sensor_dag,
        task_id='get_naver_with_sensor',
        http_conn_id="http_naver",
        endpoint="/",
        method="get"
        )
    sensor = NaverServerSensor(
        dag=sensor_dag,
        task_id="sensor_naver"
    )

sensor >> task_1
