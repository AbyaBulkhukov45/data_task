import logging
logging.basicConfig(
    filename='logs/preprocess.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # etl/preprocess.py
    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    from etl.config import RAW_CSV, CLEAN_CSV, DATA_PROCESSED
    
    def preprocess() -> str:
        DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
        df = pd.read_csv(RAW_CSV)
    
        if "id" in df.columns:
            df = df.drop(columns="id")
    
        df = df.rename(columns={"diagnosis": "target"})
        y = df["target"].map({"M": 1, "B": 0})
        X = df.drop(columns="target")
    
        X_scaled = pd.DataFrame(StandardScaler().fit_transform(X), columns=X.columns)
        pd.concat([y, X_scaled], axis=1).to_csv(CLEAN_CSV, index=False)
        return str(CLEAN_CSV)
    logging.info("Предобработка данных успешно выполнено.")
except Exception as e:
    logging.error("Предобработка данных не выполнено: %s", e)
    raise
