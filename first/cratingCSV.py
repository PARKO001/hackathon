import csv
from datetime import datetime, timedelta
import random

# Define column names
columns = ["Earned/Spent On", "Expenses/Income", "Date"]

# Define possible values for Earned/Spent On
earned_spent_on = ["salary", "interests", "others", "grocery", "studies", "entertainment", "utilities"]

# Generate random data for 50 rows
data = []
current_date = datetime.now() - timedelta(days=50)  # Start date 50 days ago
total_income = 0
total_expense = 0
for _ in range(50):
    amount = random.randint(-100, 100)
    if amount > 0:
        total_income += amount
        spent_on = random.choice(earned_spent_on[:3])  # Choose from salary, interests, others
    else:
        total_expense += amount
        spent_on = random.choice(earned_spent_on[3:])  # Choose from grocery, studies, entertainment, utilities
    data.append([spent_on, amount, current_date.strftime("%Y-%m-%d")])
    current_date += timedelta(days=3)  # Increment date by 3 days

# Make sure total income is higher than total expense
if total_income < abs(total_expense):
    data[0][1] += abs(total_expense) - total_income

# Shuffle the data to make dates random
random.shuffle(data)

# Write data to CSV file
with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)
    writer.writerows(data)

print("CSV file 'data.csv' has been created successfully.")
