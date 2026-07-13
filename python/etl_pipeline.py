from extract import extract_data
from transform import transform_data
from load import load_data
from logger import logger

def run_etl():
    try:
        logger.info("========== ETL Started ==========")

        df = extract_data()
        logger.info(f"Extracted {len(df)} records.")

        df = transform_data(df)
        logger.info(f"Cleaned data. {len(df)} records remaining.")

        load_data(df)
        logger.info("Data loaded successfully.")

        print("✅ ETL Completed Successfully!")

    except Exception as e:
        logger.exception(f"ETL Failed: {e}")
        print("❌ ETL Failed. Check logs/etl.log")

if __name__ == "__main__":
    run_etl()