import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
DATABASE_URL = "postgresql+psycopg2://naveen@localhost:5432/retail_sales"

engine = create_engine(DATABASE_URL)

# Read CSV
df = pd.read_csv("data/customers.csv")

# Load into PostgreSQL
df.to_sql(
    "customers_import",
    engine,
    if_exists="append",
    index=False
)

print("✅ Data loaded successfully!")