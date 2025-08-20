import csv
import random
import time
import os
from faker import Faker
from datetime import datetime

# Initialize Faker
fake = Faker()

# Ensure "input" directory exists
input_dir = "input"
os.makedirs(input_dir, exist_ok=True)

# Define headers
headers = ["name", "email", "product_name", "price", "product_date"]

print("🚀 CSV generator started... (Press CTRL+C to stop)")

try:
    while True:
        # Filename based on current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = os.path.join(input_dir, f"{timestamp}.csv")

        # Generate 10 records
        records = []
        for _ in range(10):
            name = fake.name()
            email = fake.email()
            product_name = fake.word().capitalize() + " " + fake.word().capitalize()
            price = random.randint(1000, 4000)  # price between 1,000 and 4,000
            product_date = fake.date_between(start_date="-1y", end_date="today").strftime("%Y-%m-%d")
            records.append([name, email, product_name, price, product_date])

        # Write to CSV
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)   # write header
            writer.writerows(records)  # write data

        print(f"✅ File '{filename}' created successfully!")

        # Wait 5 seconds before next file
        time.sleep(5)

except KeyboardInterrupt:
    print("\n🛑 Process interrupted by user. Stopping file generation...")
