from airflow import DAG
from datetime import datetime
import os 
import sys

# fix of typical error with airflow when not running in root directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'Manuel Andersen',
    'start_date': datetime(2024, 7, 31)
}

file_postfix = datetime.now().strftime('%Y%m%d')

dag = DAG(
    dag_id = 'etl_reddit_pipeline',
    default_args = default_args,
    schedule_interval = '@daily',
    catchup = False, 
    tags = ['reddit', 'etl', 'pipeline'] # this is optional, so why do we need it? and what it does?
)

# extraction from reddit 

# upload to s3