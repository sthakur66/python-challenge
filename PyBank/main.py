
import os
import csv

# Declare the required variables
month_count = 0
total = 0
hold_profit_loss = 0.0
avg_change = 0.0
sum_avg_change = 0.0
grand_avg_change = 0.0
max_profit_loss = 0
min_profit_loss = 0
profit_dict = {}

# Collects data from the budget_data csv
budget_data = os.path.join("Resources", "budget_data.csv")

# Open and read budget_data csv
with open(budget_data, 'r') as csv_file:

    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Skip the header
    header = next(csv_reader)

    # Read through each row of data after the header in reversed direction
    for row in reversed(list(csv_reader)):

        # Declare the required variables
        date = row[0]
        profit_loss = int(row[1])

        # 1. total number of months included in the dataset
        month_count = month_count + row.count(date)

        # 2. net total amount of "Profit/Losses" over the entire period
        total = total + profit_loss

        # 3. average of the changes in "Profit/Losses" over the entire period
        # 4. greatest increase in profits (date and amount) over the entire period
        # do not run below conditional statement when we have last record from profit/loss field
        # dont forget we are traversing csv in reverse order
        if hold_profit_loss != 0.0:
            avg_change = hold_profit_loss - float(profit_loss) # takes difference between the previous and current row
            profit_dict[avg_change] = hold_date # creates dictionary to hold date for each avg change key | for e.g 532869.0: 'Feb-2017'

        temp_profit_loss = profit_loss
        hold_profit_loss = temp_profit_loss # holds the previous row with profit loss value
        temp_date = date
        hold_date = temp_date # holds the previous row with date value

        # get the sum of all profit/loss changes
        sum_avg_change = sum_avg_change + avg_change


# print the required output as per below
print("Financial Analysis") # print into console
print("Financial Analysis", file=open('analysis/PyBank_Results.txt', 'wt')) # write into file

# -----------------------------------------------------------------------------------

print("----------------------------") # print into console
print("----------------------------", file=open('analysis/PyBank_Results.txt', 'at')) # write into file

# -----------------------------------------------------------------------------------

print("Total Months:" + " " + str(month_count)) # print into console
print("Total Months:" + " " + str(month_count), file=open('analysis/PyBank_Results.txt', 'at')) # write into file

# -----------------------------------------------------------------------------------

print("Total:" + " " + "$" + str(total)) # print into console
print("Total:" + " " + "$" + str(total), file=open('analysis/PyBank_Results.txt', 'at')) # write into file

# -----------------------------------------------------------------------------------

grand_avg_change = round(sum_avg_change / float(month_count - 1),2) # get the average of all profit/loss changes
print("Average  Change:" + " " + "$" + str(grand_avg_change)) # print into console
print("Average  Change:" + " " + "$" + str(grand_avg_change), file=open('analysis/PyBank_Results.txt', 'at')) # write into file

# -----------------------------------------------------------------------------------

# Greatest Increase/Decrease in Profits starts here
# fetch the MAX/MIN key field from dictionary
max_profit_loss = max(profit_dict.keys())
min_profit_loss = min(profit_dict.keys())

# list out keys and values separately from dictionary
key_list = list(profit_dict.keys()) # profit loss
val_list = list(profit_dict.values()) # dates

# find out the position of MAX key field from dictionary
max_position = key_list.index(max_profit_loss)
min_position = key_list.index(min_profit_loss)

v_max_profit_loss = str(round(key_list[max_position]))
v_max_date = val_list[max_position]
v_min_profit_loss = str(round(key_list[min_position]))
v_min_date = val_list[min_position]

print("Greatest Increase in Profits: " + v_max_date + " ($" + v_max_profit_loss + ") ") # print into console
print("Greatest Increase in Profits: " + v_max_date + " ($" + v_max_profit_loss + ") ", file=open('analysis/PyBank_Results.txt', 'at')) # write into file

print("Greatest Decrease in Profits: " + v_min_date + " ($" + v_min_profit_loss + ") ") # print into console
print("Greatest Decrease in Profits: " + v_min_date + " ($" + v_min_profit_loss + ") ", file=open('analysis/PyBank_Results.txt', 'at')) # write into file

# -----------------------------------------------------------------------------------
