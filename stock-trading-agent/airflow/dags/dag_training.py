# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime
# from src.trading_agent.pipelines.training_pipeline import run_training

# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': datetime(2023, 1, 1),
#     'retries': 1,
# }

# dag = DAG(
#     'dag_training',
#     default_args=default_args,
#     description='A DAG for training the stock trading model',
#     schedule_interval='@daily',
# )

# train_model = PythonOperator(
#     task_id='train_model',
#     python_callable=run_training,
#     dag=dag,
# )

# train_model