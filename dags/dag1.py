from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from scrape_hocky import scrape_hockey_data, save_to_csv as save_hockey_to_csv
from scrape_country import scrape_country_data, save_to_csv as save_country_to_csv
import pymongo 
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 10), 
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'weekly_data_scraping_dag',
    default_args=default_args,
    description='DAG to scrape hockey and country data weekly',
    schedule_interval='0 0 * * 0',  
)

def scrape_and_save_hockey():
    hockey_data = scrape_hockey_data(pages=4)
    save_hockey_to_csv(hockey_data, 'hockey_data.csv')

def scrape_and_save_country():
    country_data = scrape_country_data()
    save_country_to_csv(country_data, 'country_data.csv')

with dag:
    scrape_and_save_hockey_task = PythonOperator(
        task_id='scrape_and_save_hockey',
        python_callable=scrape_and_save_hockey,
    )

    scrape_and_save_country_task = PythonOperator(
        task_id='scrape_and_save_country',
        python_callable=scrape_and_save_country,
    )

    scrape_and_save_hockey_task >> scrape_and_save_country_task
