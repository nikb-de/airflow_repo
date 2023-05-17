from airflow import DAG 
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime 

def _check():
    print("checking my data")

dag = DAG('wrong_dag', schedule_interval='@daily', catchup=False)

task_1 = PythonOperator(
        task_id='task_1',
        python_callable=_check,
        dag=dag
)

task_2 = BashOperator(
        task_id = 'task_2',
        bash_command='echo "hello here"',
        dag=dag
)
