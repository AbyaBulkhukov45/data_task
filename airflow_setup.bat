@echo off
REM === Установка переменных среды ===
set AIRFLOW_HOME=%TEMP%\airflow_home
set AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=sqlite:///%TEMP%\airflow_home\airflow.db

REM === Создание папки, если не существует ===
if not exist "%AIRFLOW_HOME%" (
    mkdir "%AIRFLOW_HOME%"
)

REM === Очистка старой базы, если была ===
del "%AIRFLOW_HOME%\airflow.db" >nul 2>&1

REM === Инициализация базы данных Airflow ===
echo Инициализация базы Airflow...
airflow db init

pause