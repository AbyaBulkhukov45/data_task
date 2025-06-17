from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parents[1]

# Пути
DATA_RAW      = BASE_DIR / "data" / "raw"
DATA_PROCESSED= BASE_DIR / "data" / "processed"
RESULTS_DIR   = BASE_DIR / "results"

# Файлы
RAW_CSV       = DATA_RAW / "breast_cancer.csv"
CLEAN_CSV     = DATA_PROCESSED / "clean.csv"
MODEL_PKL     = RESULTS_DIR / "model.pkl"
METRICS_JSON  = RESULTS_DIR / "metrics.json"

# URL-источник
DATA_URL = (
    "https://raw.githubusercontent.com/..."
    "UCI_Machine_Learning_Repository_Breast_Cancer_Wisconsin_Diagnostic.csv"
)

# Облачные креды читаем из env
S3_BUCKET = os.getenv("S3_BUCKET", "")
GDRIVE_FOLDER_ID = os.getenv("GDRIVE_FOLDER_ID", "")
