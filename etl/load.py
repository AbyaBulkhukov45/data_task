import logging
logging.basicConfig(
    filename='logs/load.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # etl/load.py
    import requests
    from etl.config import DATA_URL, RAW_CSV, DATA_RAW
    
    def download() -> str:
        DATA_RAW.mkdir(parents=True, exist_ok=True)
        r = requests.get(DATA_URL, timeout=30)
        r.raise_for_status()
        RAW_CSV.write_bytes(r.content)
        return str(RAW_CSV)
    logging.info("Загрузка данных успешно выполнено.")
except Exception as e:
    logging.error("Загрузка данных не выполнено: %s", e)
    raise
