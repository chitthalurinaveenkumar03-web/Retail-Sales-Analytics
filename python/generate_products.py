from faker import Faker
import pandas as pd
import random

fake = Faker()

categories = {
    1: "Electronics",
    2: "Footwear",
    3: "Clothing",
    4: "Furniture",
    5: "Sports",
    6: "Books",
    7: "Beauty",
    8: "Groceries"
}

products = []

for product_id in range(1, 2001):

    category_id = random.randint(1, 8)

    products.append({
        "product_id": product_id,
        "product_name": fake.word().title() + " " + fake.word().title(),
        "category_id": category_id,
        "brand": fake.company(),
        "unit_price": round(random.uniform(5, 2000), 2),
        "stock_quantity": random.randint(10, 500),
        "created_date": fake.date_this_year()
    })

df = pd.DataFrame(products)

print(df.head())

df.to_csv("data/products.csv", index=False)

print("\n✅ 2000 Products Generated Successfully!")