# import the os module
# create file path for OS
import os

# Module touse in reading CSV files
import csv

csvpath = os.path.join('budget_data.csv')

month_year = []
profits = []
difference = []
average_changes2 = []

#Read the csv file

with open(csvpath, newline='') as csvfile:
     # CSV reader denoting delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
     # Read the header row first (skip this step if there is no header)
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
     # Read the header row first (skip this step if there is no header)

    for column in csvreader:
        month_year.append(column[0])
        profits.append(int(column[1]))

    print("Financial Analysis")
    print("____________________")   
    #Sum the Total amount of months
    Total_Months = (len(month_year))
    print(f"Total Months: {Total_Months}")
    #Sum Total amount of profits or losses
    Total_Profits = (sum(profits))
    print(f"Total profits = ${Total_Profits}")
    #Calculate the percentage change
    for column in range (0,len(profits)-1):
        difference.append(int(profits[column+1])-int(profits[column]))
        average_changes1 = sum(difference) / len(difference)
        
    print(f"Average Change: (${average_changes1})")
    # Determine greatest increase and greatest decrease in profits
    Greatest_positive_change = max(difference) 
    Greatest_negative_change = min(difference) 
     #Determine months with greatest increase and greatest decrease
    Greatest_increase_month = month_year[difference.index(Greatest_positive_change)+ 1]
    Greatest_decrease_month = month_year[difference.index(Greatest_negative_change)+ 1]
    print(f"Greatest Increase in Profits: {Greatest_increase_month} (${Greatest_positive_change})")
    print(f"Greatest Decrease in Profits: {Greatest_decrease_month} (${Greatest_negative_change})")

output_path = os.path.join("bank.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write(f"Total Months: {Total_Months}")
    txtfile.write(f"Total: ${Total_Profits}")
    txtfile.write(f"Average Change: ${average_changes1}")
    txtfile.write(f"Greatest Increase in Profits: {Greatest_increase_month} (${Greatest_positive_change})")
    txtfile.write(f"Greatest Decrease in Profits: {Greatest_decrease_month} (${Greatest_negative_change})")
    txtfile.close()

