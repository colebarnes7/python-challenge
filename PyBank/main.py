# Import modules
import os
import csv

# Creates a path to the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Declare Variables
totalmonths = 0
nettotal = 0
currentvalue = 0
profit_loss = []
month = []
currentchange = 0
totalchange = 0
averagechange = 0
greatestincrease = 0
gimonth = ""
greatestdecrease = 0
gdmonth = ""


# Open the CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Reads the header row of the csv file
    csvheader = next(csvreader)

    # Loop to go through each row in csv file
    for row in csvreader:
        
        # Adds one to the months for each row
        totalmonths += 1

        # Pulls the current monthly total
        currentvalue = int(row[1])

        # Adds the monthly total to the profits/losses
        nettotal = nettotal + currentvalue

        # Adds monthly total to a list
        profit_loss.append(currentvalue)

        # Adds month to a list
        month.append(row[0])

# Loop to go through all the monthly profit/loss values
for i in range(len(profit_loss)):
    
    # Conditional to keep the values in range
    if (i < len(profit_loss)-1):

        # Calculates the difference between this month and previous
        currentchange = profit_loss[i+1] - profit_loss[i]
    
        # Calculates the total change for the length of the data
        totalchange = totalchange + currentchange
    
    # Conditionals to determine the greatest increase and decrease in profits/losses
    # Assigns the appropriate month as well
    if (currentchange > greatestincrease):
        greatestincrease = currentchange
        gimonth = month[i]

    if (currentchange < greatestdecrease):
        greatestdecrease = currentchange
        gdmonth = month[i]

# Calculates the average change over the course of the data
averagechange = round(totalchange/(totalmonths-1), 2)

# Outputs the appropriate data formatted to the Terminal
print("Financial Analysis")
print("-----------------------------------------")
print("Total Months: " + str(totalmonths))
print("Total: " + str(nettotal))
print("Average Change: $" + str(averagechange))
print(f'Greatest Increase in Profits: {gimonth} (${greatestincrease})')
print(f'Greatest Decrease in Profits: {gdmonth} (${greatestdecrease})')

# Sets up the analysis file
output_file = os.path.join("Analysis", "budget_analysis.csv")

# Opens the file to write into
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Outputs the appropriate data formatted to the text file
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------------------------"])
    writer.writerow(["Total Months: " + str(totalmonths)])
    writer.writerow(["Total: " + str(nettotal)])
    writer.writerow(["Average Change: $" + str(averagechange)])
    writer.writerow([f'Greatest Increase in Profits: {gimonth} (${greatestincrease})'])
    writer.writerow([f'Greatest Decrease in Profits: {gdmonth} (${greatestdecrease})'])