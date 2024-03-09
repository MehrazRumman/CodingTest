from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scrape_bikroyJobs import scrape_job_details, save_to_csv
import selenium 


dag = DAG(
    'bikroy_job_scraping',
    start_date=datetime(2024, 4, 1),  
    schedule_interval='0 0 1 * *',  
    catchup=False  
)


scrape_task = PythonOperator(
    task_id='scrape_job_postings',
    python_callable=scrape_job_details,
    op_kwargs={'url': 'https://bikroy.com/'},
    dag=dag
)

save_to_csv_task = PythonOperator(
    task_id='save_to_csv',
    python_callable=save_to_csv,
    op_kwargs={'data': '{{ task_instance.xcom_pull(task_ids="scrape_job_postings") }}', 'filename': 'job_details.csv'},
    dag=dag
)



scrape_task >> save_to_csv_task 
