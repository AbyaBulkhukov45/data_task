import logging
logging.basicConfig(
    filename='logs/metrics.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    import json, joblib
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    from etl.config import MODEL_PKL, METRICS_JSON
    
    def compute_metrics() -> str:
        bundle = joblib.load(MODEL_PKL)
        clf, X_test, y_test = bundle["model"], bundle["X_test"], bundle["y_test"]
    
        preds = clf.predict(X_test)
        metrics = {
            "accuracy":  accuracy_score(y_test, preds),
            "precision": precision_score(y_test, preds),
            "recall":    recall_score(y_test, preds),
            "f1":        f1_score(y_test, preds),
        }
    
        METRICS_JSON.write_text(json.dumps(metrics, indent=2))
        return str(METRICS_JSON)
    logging.info("Вычисление метрик успешно выполнено.")
except Exception as e:
    logging.error("Вычисление метрик не выполнено: %s", e)
    raise
