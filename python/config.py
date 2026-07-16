DATABASE = {
    "HOST": "localhost",
    "PORT": 5432,
    "DATABASE": "retail_sales",
    "USER": "naveen"
}

DATABASE_URL = (
    f"postgresql+psycopg2://{DATABASE['USER']}"
    f"@{DATABASE['HOST']}:{DATABASE['PORT']}/{DATABASE['DATABASE']}"
)

CUSTOMERS_CSV = "data/customers.csv"
PRODUCTS_CSV = "data/products.csv"

CUSTOMERS_TABLE = "customers_import"
PRODUCTS_TABLE = "products"