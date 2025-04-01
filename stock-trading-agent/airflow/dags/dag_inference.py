# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime
# from src.trading_agent.models.inference import run_inference

# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2023, 10, 1),
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# dag = DAG(
#     'dag_inference',
#     default_args=default_args,
#     description='DAG for live inference',
#     schedule_interval='@hourly',
# )

# run_inference_task = PythonOperator(
#     task_id='run_inference',
#     python_callable=run_inference,
#     dag=dag,
# )

# run_inference_task