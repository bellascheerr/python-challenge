import os
import pandas as pd

# Define function to format as currency to two decimal places
def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

# Path to acquire data from the Resources folder
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Read in the CSV file using Pandas
data = pd.read_csv(budget_csv)

# Calculate the total number of months
total_months = data['Date'].count()

# Calculate the net total amount of "Profit/Losses"
total_profit = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
data['Change'] = data['Profit/Losses'].diff()

# Calculate the average of those changes
average_profit_change = data['Change'].mean()

# Find the greatest increase in profits (date and amount)
greatest_profit_increase_row = data.loc[data['Change'] == data['Change'].max(), ['Date', 'Change']].iloc[0]

# Find the greatest decrease in profits (date and amount)
greatest_profit_decrease_row = data.loc[data['Change'] == data['Change'].min(), ['Date', 'Change']].iloc[0]

# Print the financial analysis results
print("\nFinancial Analysis\n----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: {as_currency(total_profit)}\n")
print(f"Average Change: {as_currency(average_profit_change)}\n")
print(f"Greatest Increase in Profits: {greatest_profit_increase_row['Date']} ({as_currency(greatest_profit_increase_row['Change'])})\n")
print(f"Greatest Decrease in Profits: {greatest_profit_decrease_row['Date']} ({as_currency(greatest_profit_decrease_row['Change'])})")

# Output the analysis to a text file in the 'analysis' folder
analysis_results = os.path.join('.', 'analysis', 'analysis_results.txt')
with open(analysis_results, 'w') as f:
    f.write("\nFinancial Analysis\n\n----------------------------\n")
    f.write(f"\nTotal Months: {total_months}\n")
    f.write(f"\nTotal: {as_currency(total_profit)}\n")
    f.write(f"\nAverage Change: {as_currency(average_profit_change)}\n")
    f.write(f"\nGreatest Increase in Profits: {greatest_profit_increase_row['Date']} ({as_currency(greatest_profit_increase_row['Change'])})\n")
    f.write(f"\nGreatest Decrease in Profits: {greatest_profit_decrease_row['Date']} ({as_currency(greatest_profit_decrease_row['Change'])})")
