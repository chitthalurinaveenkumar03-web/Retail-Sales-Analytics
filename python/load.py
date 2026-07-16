from database import engine
from config import TABLE_NAME

def load_data(df):
    df.to_sql(
        TABLE_NAME,
        engine,
        if_exists="append",
        index=False
    )

    print(f"✅ Loaded {len(df)} records into PostgreSQL")