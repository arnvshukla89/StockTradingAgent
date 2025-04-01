# from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
# from datetime import datetime
# from src.trading_agent.data_ingestion.real_time_stream import ingest_real_time_data

# default_args = {
#     'owner': 'trading_agent',
#     'depends_on_past': False,
#     'start_date': datetime(2023, 10, 1),
#     'retries': 1,
# }

# dag = DAG(
#     'real_time_data_ingestion',
#     default_args=default_args,
#     description='A DAG for real-time data ingestion from WebSocket',
#     schedule_interval='@every 1 minute',
# )

# ingest_data_task = PythonOperator(
#     task_id='ingest_real_time_data',
#     python_callable=ingest_real_time_data,
#     dag=dag,
# )

# ingest_data_task