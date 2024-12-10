# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join('Resources', 'budget_data.csv')  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
monthscolumn = []
profitlosscolumn = []
# Add more variables to track other necessary financial data
net_change_list = []
net_change_across_months = []
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter = ",")
 # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to net_change_list    

       # Track the total and net change
    finaltotal = 0
    netchange = 0

    # Process each row of data
    #------ Creates a list of remaining data: 
    
    for row in reader:
        
        monthscolumn.append(row[0])
        profitlosscolumn.append(int(row[1]))
        
        # Track the total
       

    finaltotal = sum(profitlosscolumn)
      
    zip_month_profit = list(zip(monthscolumn, profitlosscolumn))
        # Track the net change
    for i in range(0, len(zip_month_profit)):
            date = zip_month_profit[i][0]
            change = zip_month_profit[i][1] - zip_month_profit[i - 1][1]
            net_change_list.append((date, change))
        
    
        # Calculate the greatest increase in profits (month and amount)
        # Learned the custom key function is used to return the date and the change value
        # Suggested by Xpert Learning Assistant
    max_change_date = max(net_change_list, key=lambda x: x[1])

        # Calculate the greatest decrease in losses (month and amount)
    min_change_date = min(net_change_list, key=lambda x: x[1])



# Calculate the average net change across the months
for i in range(1, len(profitlosscolumn)):
            netchange = profitlosscolumn[i] - profitlosscolumn[i - 1]
            net_change_across_months.append(netchange)
mean_net_change = sum(net_change_across_months) / len(net_change_across_months)

mean_net_change_rounded = "%.2f" % mean_net_change

# Generate the output summary
output_summary = f"""
Financial Analysis
-------------------------
Total Months: {len(monthscolumn)} 
Total: ${finaltotal} 
Average Change: ${mean_net_change_rounded} 
Greatest Increase in Profits: {max_change_date[0]} (${max_change_date[1]})
Greatest Decrease in Profits: {min_change_date[0]} (${min_change_date[1]}) """

print(output_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output_summary)