init-airflow:
	mkdir -p airflow_home
	AIRFLOW_HOME=./airflow_home airflow db init

run-airflow:
	AIRFLOW_HOME=./airflow_home airflow webserver -p 8080 & 
	AIRFLOW_HOME=./airflow_home airflow scheduler &
