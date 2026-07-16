import pandas as pd
from faker import Faker
import random

fake = Faker()

order_items = []

NUMBER_OF_ROWS = 200000

for i in range(1, NUMBER_OF_ROWS + 1):

    quantity = random.randint(1, 5)

    unit_price = round(random.uniform(10, 2000), 2)

    discount = random.choice([0, 5, 10, 15, 20])

    line_total = round(
        quantity * unit_price * (1 - discount / 100),
        2
    )

    order_items.append({

        "order_id": random.randint(1, 50000),

        "product_id": random.randint(1, 2000),

        "quantity": quantity,

        "unit_price": unit_price,

        "discount": discount,

        "line_total": line_total

    })

df = pd.DataFrame(order_items)

print(df.head())

df.to_csv(
    "data/order_items.csv",
    index=False
)

print(f"\n✅ {len(df)} Order Items Generated Successfully!")