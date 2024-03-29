# import pandas as pd

# df = pd.read_csv('data.csv')
# print(df.head())

# def calculate_expenditure(data, category_keyword):
#     total_expenditure = 0
#     for index, row in data.iterrows():
#         if category_keyword.lower() in row['earned/spend on'].lower():
#             total_expenditure += row['expenses/income']
#     return total_expenditure

# # Calculate total expenditure on specific categories
# salary_expenditure = calculate_expenditure(df, "salary")
# groceries_expenditure = calculate_expenditure(df, "groceries")
# entertainment_expenditure = calculate_expenditure(df, "entertainment")
# utilities_expenditure = calculate_expenditure(df, "utilities")

# # Print the results
# print("Total Expenditure:")
# print(f"Salary: ${salary_expenditure:.2f}")
# print(f"Groceries: ${groceries_expenditure:.2f}")
# print(f"Entertainment: ${entertainment_expenditure:.2f}")
# print(f"Utilities: ${utilities_expenditure:.2f}")
