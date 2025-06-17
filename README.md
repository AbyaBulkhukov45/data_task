# Breast Cancer Diagnosis Pipeline (Airflow)

## 📌 Цель проекта

Автоматизировать ETL-процесс для задачи диагностики рака груди с использованием пайплайна на Apache Airflow и Python.

## 🧠 Задача ML

Классификация (бинарная): определить, является ли опухоль злокачественной или доброкачественной.

Модель: `LogisticRegression`

## 📦 Структура проекта

```
├── dags/                 # DAG-файл для Airflow
│   └── pipeline_dag.py
├── etl/                  # Шаги пайплайна
│   ├── load.py
│   ├── preprocess.py
│   ├── train.py
│   ├── metrics.py
│   └── upload.py
├── data/
│   ├── raw/
│   └── processed/
├── results/              # Модель и метрики
├── logs/                 # Логи
```

## 🔁 Описание шагов пайплайна

1. **load.py** — загружает исходные данные
2. **preprocess.py** — чистит и нормализует
3. **train.py** — обучает модель
4. **metrics.py** — считает accuracy, precision, recall, F1
5. **upload.py** — сохраняет модель и метрики

## 🛠 Оркестрация (Airflow DAG)

- Название DAG: `breast_cancer_pipeline`
- Задачи: `load_data → preprocess_data → train_model → calculate_metrics → upload_results`

Команда для локального запуска:

```bash
airflow tasks test load_data 2025-06-17
```

## ☁️ Хранилище

Результаты сохраняются в `results/`. Поддерживается выгрузка на S3 (если подключить доступ).

## ⚠️ Анализ отказов

- Проблемы загрузки данных — перехватываются `try-except`
- Плохой формат CSV — валидация и логирование
- Ошибка модели — логируется, пайплайн не падает целиком
- Airflow настроен с `retries`, `timeout`

## 🧠 Идеи по улучшению

- Визуализация метрик
- Интеграция с облаком (S3, GDrive)
- Поддержка CI/CD через GitHub Actions

## 📜 Инструкция по запуску

```bash
pip install -r requirements.txt
airflow db init
airflow scheduler
airflow webserver
```

Затем в UI запустить DAG `breast_cancer_pipeline`.

