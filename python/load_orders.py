import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

df = pd.read_csv("data/orders.csv")

df.to_sql(
    "orders",
    engine,
    if_exists="append",
    index=False
)

print(f"✅ Loaded {len(df)} orders into PostgreSQL")