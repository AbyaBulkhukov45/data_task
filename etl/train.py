import logging
logging.basicConfig(
    filename='logs/train.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    import joblib, pandas as pd
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from etl.config import CLEAN_CSV, MODEL_PKL, RESULTS_DIR
    
    def train() -> str:
        RESULTS_DIR.mkdir(exist_ok=True)
        df = pd.read_csv(CLEAN_CSV)
        X, y = df.drop(columns="target"), df["target"]
    
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, stratify=y, random_state=42
        )
    
        clf = LogisticRegression(max_iter=1000, n_jobs=-1)
        clf.fit(X_train, y_train)
    
        joblib.dump({"model": clf, "X_test": X_test, "y_test": y_test}, MODEL_PKL)
        return str(MODEL_PKL)
    logging.info("Обучение модели успешно выполнено.")
except Exception as e:
    logging.error("Обучение модели не выполнено: %s", e)
    raise
