# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
monthscolumn = []
profitlosscolumn = []
# Add more variables to track other necessary financial data


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter = ",")

    # Skip the header row
    header = next(reader)
    
    # Extract first row to avoid appending to net_change_list    

       # Track the total and net change
    total = 0
    netchange = 0

    # Process each row of data
    #------ Creates a list of remaining data: 
    data = [row for row in reader]
    for row in data:
        
        monthscolumn.append(row[0])
        profitlosscolumn.append(int(row[1]))
        
        # Track the total
        # total += int(row[1])
        total = sum(profitlosscolumn)
      

        # Track the net change
        netchange = total / len(profitlosscolumn)
    print (netchange)
        # Calculate the greatest increase in profits (month and amount)
    
        # Calculate the greatest decrease in losses (month and amount)



# Calculate the average net change across the months


# Generate the output summary


# Print the output


# Write the results to a text file
#with open(file_to_output, "w") as txt_file:
#----txt_file.write(output)