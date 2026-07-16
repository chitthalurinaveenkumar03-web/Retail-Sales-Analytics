import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

df = pd.read_csv("data/order_items.csv")

df.to_sql(
    "order_items",
    engine,
    if_exists="append",
    index=False
)

print(f"✅ Loaded {len(df)} order items into PostgreSQL")