install:
	pip install -r requirements.txt

init-airflow:
	airflow db init

run-airflow:
	airflow webserver --port 8080 & airflow scheduler

trigger:
	airflow dags trigger breast_cancer_pipeline

test-task:
	airflow tasks test breast_cancer_pipeline preprocess_data 2025-06-17