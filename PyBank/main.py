# Import modules
import os
import csv

# Creates a path to the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Declare Variables
totalmonths = 0
nettotal = 0
greatestincrease = 0
gimonth = ""
greatestdecrease = 0
gdmonth = ""
change = 0
changes_list = []

# Open the CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Reads the header row of the csv file
    csvheader = next(csvreader)

    for row in csvreader:
        
        # Adds one to the months for each row
        totalmonths = totalmonths + 1

        # Adds the monthly total to the profits/losses
        nettotal = nettotal + int(row[1])


        # Checks if the current month has the greatest increase in profits
        if (int(row[1]) > greatestincrease):
            
            # Sets the current monthly total to greatest increase
            greatestincrease = int(row[1])
            # Stores the current month
            gimonth = row[0]
        
        # Checks if the current month has the greatest decrease in profits
        if (int(row[1]) < greatestdecrease):
            
            # Sets the current monthly total to greatest decrease
            greatestdecrease = int(row[1])
            # Stores the current month
            gdmonth = row[0]

# Outputs the appropriate data formatted to the Terminal
print("Financial Analysis")
print("-----------------------------------------")
print("Total Months: " + str(totalmonths))
print("Total: " + str(nettotal))
print("Greatest Increase in Profits: " + gimonth + " ($" + str(greatestincrease) + ")")
print("Greatest Decrease in Profits: " + gdmonth + " ($" + str(greatestdecrease) + ")")

