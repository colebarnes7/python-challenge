# Import modules
import os
import csv

# Creates a path to the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Declare Variables
totalmonths = 0
nettotal = 0
currentchange = 0
totalchange = 0
currentmonth = 0
previousmonth = 0
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

    for row in csvreader:
        
        # Adds one to the months for each row
        totalmonths += 1

        # Pulls the current monthly total
        currentmonth = int(row[1])

        # Adds the monthly total to the profits/losses
        nettotal = nettotal + currentmonth

        # Grabs the change from this month to last month
        currentchange = currentmonth - previousmonth
        
        # Calculates the total change from month to month
        totalchange = totalchange + currentchange

        # Checks if this month's increase is the largest
        if (currentchange > greatestincrease):
            greatestincrease = currentchange
            gimonth = row[0]
        
        # Checks if this month's decrease is the largest
        if (currentchange < greatestdecrease):
            greatestdecrease = currentchange
            gdmonth = row[0]

        # Holds the previous month for next iteration
        previousmonth = int(row[1])

averagechange = round(totalchange/totalmonths, 2)

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