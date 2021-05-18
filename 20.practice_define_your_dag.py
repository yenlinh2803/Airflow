from airflow import DAG
from datetime import datetime, timedelta

default_args= {
	"owner":"airflow",
	"email_on_failure": False,
	"email_on_retry": False,
	"email": "admin@localhost.com",
	"retries":1, #the task fail and will be retried at least one time before ending up with the staue's failure
	"retry_delay":timedelta(minutes=5) # before retried I want to wait 5 mins 
}
# add default_args to the dag object 
with DAG(dag_id="forex_data_pipeline",
	start_date=datetime(2021,1,1),
	schedule_interval="@daily",
	default_ags=default_ags,
	catchup=False) as dag:
