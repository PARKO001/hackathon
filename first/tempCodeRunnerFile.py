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