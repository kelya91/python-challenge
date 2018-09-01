
# coding: utf-8

# In[47]:


# Dependencies
import csv


file_to_load = "budget_data.csv"
file_to_output = "budget_analysis_.txt"

# Track various revenue parameters
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)


# In[51]:


import os

# Module for reading CSV files
import csv
filename = "budget_data.csv"
Months =[]
Profit_Loss =[]
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


with open(filename, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)


# In[50]:


# Read the csv and convert it into a list of dictionaries
with open (file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        # Find the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # Find the revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")


print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

