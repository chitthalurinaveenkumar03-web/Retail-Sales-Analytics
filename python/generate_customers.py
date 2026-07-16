from faker import Faker
import pandas as pd
import random

fake = Faker()

customers = []

for i in range(1, 10001):
    customers.append({
        "customer_id": i,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 70),
        "city": fake.city(),
        "state": fake.state(),
        "signup_date": fake.date_between(
            start_date="-3y",
            end_date="today"
        )
    })

df = pd.DataFrame(customers)

print(df.head())

df.to_csv("data/customers.csv", index=False)

print("\n✅ 10,000 customers generated successfully!")