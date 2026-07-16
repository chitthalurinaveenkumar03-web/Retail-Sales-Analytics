import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL, PRODUCTS_CSV, PRODUCTS_TABLE

engine = create_engine(DATABASE_URL)

df = pd.read_csv(PRODUCTS_CSV)

df.to_sql(
    PRODUCTS_TABLE,
    engine,
    if_exists="append",
    index=False
)

print(f"✅ Loaded {len(df)} products into PostgreSQL")