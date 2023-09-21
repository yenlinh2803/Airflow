import datetime as dt 

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import pendulum
import logging
from airflow.operators.python import PythonOperator


# execution_ds = str("{{ ds }}")
# execution_ts = str("{{ ts }}")
# execution_ts = execution_ts[0:19]
# ts_nodash_date = str("{{ ts_nodash }}")
# logging.info(f"execution_ds = {execution_ds}, execution_ts={execution_ts}, ts_nodash_str={ts_nodash_date}")
# business_date = dt.datetime.strptime(execution_ts, "%Y-%m-%dT%H:%M:%S") + dt.timedelta(hours=7)
# logging.info(f"business_date = {business_date}")
# file_business_date_format = dt.datetime.strftime(business_date, "%Y-%m-%d %H:%M:%S.%f")
# logging.info(f"file_business_date_format = {file_business_date_format}")
# file_business_date_format = dt.datetime.strptime(business_date, "%Y-%m-%d %H:%M:%S.%f") + dt.timedelta(hours=6)
# logging.info(f"file_business_date_format = {file_business_date_format}")
# file_business_date_format = dt.datetime.strftime(file_business_date_format, "%Y-%m-%d %H:%M:%S.%f")
# logging.info(f"file_business_date_format = {file_business_date_format}")

# execution_ds: 2022-12-15\n        execution_ts: 2022-12-15T11:39:03.081873+00:00\n        ts_nodash: 20221215T113903

def generate_business_date(execution_ts):
    logging.info(f"execution_ts = {execution_ts}")
    business_date = pendulum.parse(execution_ts) + dt.timedelta(hours=7)
    logging.info(f"business_date = {business_date}")
    file_business_date = dt.datetime.strftime(business_date, "%Y-%m-%d")
    logging.info(f"file_business_date = {file_business_date}")
    file_business_date_nodash = file_business_date.replace("-","")
    logging.info(f"file_business_date_nodash = {file_business_date_nodash}")


with DAG(
  dag_id="example",
  schedule_interval=None,
  start_date=dt.datetime(year=2022, month=8, day=31)
) as dag:
    generate_product_code_task = PythonOperator(
            task_id=f"generate_business_date",
            python_callable=generate_business_date,
            op_kwargs={
                "execution_ts": "{{ ts }}",
            },
        )

generate_product_code_task