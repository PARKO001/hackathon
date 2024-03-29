import pandas as pd

def import_csv(file_path):
    try:
        # Read CSV file into a DataFrame
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print("Error occurred while importing CSV:", e)
        return None

# Example usage:
file_path = "data.csv"
bank_data = import_csv(file_path)
if bank_data is not None:
    print("Data imported successfully!")
    print(bank_data.head())  

def calculate_expenditure_and_transactions(data, category_keyword):
    total_expenditure = 0
    transaction_count = 0
    for index, row in data.iterrows():
        if category_keyword.lower() in row['Earned/Spent On'].lower():
            total_expenditure += row['Expenses/Income']
            transaction_count += 1
    return total_expenditure, transaction_count

# Calculate total expenditure and number of transactions for specific categories
studies_expenditure, studies_transactions = calculate_expenditure_and_transactions(bank_data, "studies")
groceries_expenditure, groceries_transactions = calculate_expenditure_and_transactions(bank_data, "grocery")
entertainment_expenditure, entertainment_transactions = calculate_expenditure_and_transactions(bank_data, "entertainment")
utilities_expenditure, utilities_transactions = calculate_expenditure_and_transactions(bank_data, "utilities")

# Print the results
print("Total Expenditure and Number of Transactions:")
print(f"Studies: Expenditure: ${studies_expenditure:.2f}, Transactions: {studies_transactions}")
print(f"Groceries: Expenditure: ${groceries_expenditure:.2f}, Transactions: {groceries_transactions}")
print(f"Entertainment: Expenditure: ${entertainment_expenditure:.2f}, Transactions: {entertainment_transactions}")
print(f"Utilities: Expenditure: ${utilities_expenditure:.2f}, Transactions: {utilities_transactions}")

def calculate_category_totals(data, categories):
    category_totals = {}
    for category in categories:
        expenditure, transactions = calculate_expenditure_and_transactions(data, category)
        category_totals[category] = {'Expenditure': expenditure, 'Transactions': transactions}
    return category_totals

# Calculate totals for salary, interest, and others
category_totals = calculate_category_totals(bank_data, ['salary', 'interest', 'others'])
print("\nCategory Totals:")
for category, totals in category_totals.items():
    print(f"{category.capitalize()}: Expenditure: ${totals['Expenditure']:.2f}, Transactions: {totals['Transactions']}")

def calculate_expected_dates(data):
    expected_dates = {}
    for value in data['Earned/Spent On'].unique():
        value_dates = pd.to_datetime(data[data['Earned/Spent On'] == value]['Date'])
        if len(value_dates) > 0:
            expected_dates[value] = value_dates.mean().strftime("%Y-%m-%d")
        else:
            expected_dates[value] = "N/A"
    return expected_dates

# Calculate expected dates for values in the first column
expected_dates = calculate_expected_dates(bank_data)
print("\nExpected Dates:")
for value, date in expected_dates.items():
    print(f"{value.capitalize()}: Expected Date: {date}")

# =============================================================
def get_expenditure_by_category_in_all_months(data):
    categories = ['salary', 'interest', 'grocery', 'entertainment', 'utilities', 'others']
    expenditures_by_month_and_category = {}
    for month in range(1, 13):  # Iterate over all months
        expenditures_by_category = {}
        for category in categories:
            expenditure, _ = calculate_expenditure_and_transactions(data, category, month)
            expenditures_by_category[category] = expenditure
        expenditures_by_month_and_category[month] = expenditures_by_category
    return expenditures_by_month_and_category

# Example usage of the function
expenditures_by_month = get_expenditure_by_category_in_all_months(bank_data)
for month, expenditures_by_category in expenditures_by_month.items():
    print(f"Month {month}:")
    for category, expenditure in expenditures_by_category.items():
        print(f"{category.capitalize()}: ${expenditure:.2f}")
    print()  # Add a blank line for readability


