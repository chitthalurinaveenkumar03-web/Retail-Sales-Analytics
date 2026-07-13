from faker import Faker
import pandas as pd
import random

fake = Faker()

customers = []

for _ in range(10000):
    customers.append({
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 70),
        "city": fake.city(),
        "state": fake.state(),
        "signup_date": fake.date_between(start_date="-2y", end_date="today")
    })

df = pd.DataFrame(customers)

df.to_csv("data/customers_large.csv", index=False)

print("✅ Generated 10,000 customers.")