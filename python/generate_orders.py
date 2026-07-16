import pandas as pd
from faker import Faker
import random

fake = Faker()

orders = []

payment_methods = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Cash",
    "PayPal"
]

order_status = [
    "Delivered",
    "Shipped",
    "Processing",
    "Cancelled"
]

for order_id in range(1, 50001):

    orders.append({
        "order_id": order_id,
        "customer_id": random.randint(1, 10000),
        "order_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "total_amount": round(random.uniform(20, 3000), 2),
        "payment_method": random.choice(payment_methods),
        "order_status": random.choice(order_status)
    })

df = pd.DataFrame(orders)

print(df.head())

df.to_csv("data/orders.csv", index=False)

print(f"\n✅ {len(df)} Orders Generated Successfully!")