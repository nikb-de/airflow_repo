from airflow import DAG 
from airflow.operators.bash import BashOperator 


from datetime import datetime, timedelta 

dag = DAG('dag_different_start_dates', start_date=datetime(2021, 1, 1), schedule_interval='@daily', catchup=False)

task_1 = BashOperator(
        task_id='bash_cmd_1', 
        bash_command='echo "123"',
        start_date=datetime(2023, 1, 2),
        dag=dag
)

task_2 = BashOperator(
        task_id = 'bash_cmd_2',
        bash_command='echo "345"',
        start_date=datetime(2024, 1, 1),
        dag = dag
)
