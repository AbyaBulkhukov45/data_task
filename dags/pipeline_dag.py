from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'pavel',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 6, 17),
}

with DAG(
    dag_id='breast_cancer_pipeline',
    default_args=default_args,
    description='ETL and ML pipeline for breast cancer diagnosis',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    load_data = BashOperator(
        task_id='load_data',
        bash_command=(
            'python etl/load.py '
            '--url https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data '
            '--output data/raw/breast_cancer.csv'
        ),
    )

    preprocess_data = BashOperator(
        task_id='preprocess_data',
        bash_command=(
            'python etl/preprocess.py '
            '--input data/raw/breast_cancer.csv '
            '--output data/processed/data_clean.csv'
        ),
    )

    train_model = BashOperator(
        task_id='train_model',
        bash_command=(
            'python etl/train.py '
            '--input data/processed/data_clean.csv '
            '--output results/model.pkl'
        ),
    )

    calculate_metrics = BashOperator(
        task_id='calculate_metrics',
        bash_command=(
            'python etl/metrics.py '
            '--data data/processed/data_clean.csv '
            '--model results/model.pkl '
            '--output results/metrics.json'
        ),
    )

    upload_results = BashOperator(
        task_id='upload_results',
        bash_command=(
            'python etl/upload.py '
            '--source results/ '
            '--dest s3://my-bucket/'
        ),
    )

    load_data >> preprocess_data >> train_model >> calculate_metrics >> upload_results
