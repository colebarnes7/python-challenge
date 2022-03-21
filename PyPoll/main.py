# Import modules
import os
import csv

# Creates a path to the csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# Declare variables
totalvotes = 0
winner = ""

# Sets up a dictionary to hold all the necessary data
candidates = {
    "name": ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"],
    "vote percentage": [0, 0, 0],
    "votes": [0, 0, 0]
}

# Open the CSV
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Reads the header row of the csv file
    csvheader = next(csvreader)

     # Loop to go through each row in csv file
    for row in csvreader:

        # Adds a vote for each row in csv file
        totalvotes += 1

        # Set of conditionals to check the name of the candidate, adds vote to that candidate
        if (row[2] == candidates["name"][0]):
            candidates["votes"][0] += 1
        
        elif (row[2] == candidates["name"][1]):
            candidates["votes"][1] += 1
        
        else:
            candidates["votes"][2] += 1


# Calculates the vote percentage for each candidate and rounds to 3 decimals
candidates["vote percentage"][0] = round((candidates["votes"][0]/totalvotes) * 100, 3)
candidates["vote percentage"][1] = round((candidates["votes"][1]/totalvotes) * 100, 3)
candidates["vote percentage"][2] = round((candidates["votes"][2]/totalvotes) * 100, 3)

# Conditionals to determine the winner of the election
if (candidates["votes"][0] > candidates["votes"][1] and candidates["votes"][0] > candidates["votes"][2]):
    winner = candidates["name"][0]

elif (candidates["votes"][1] > candidates["votes"][0] and candidates["votes"][1] > candidates["votes"][2]):
    winner = candidates["name"][1]

else:
    winner = candidates["name"][2]


# Outputs the data to the terminal in correct format
print("Election Results")
print("------------------------------")
print("Total Votes: " + str(totalvotes))
print("------------------------------")
print(f'{candidates["name"][0]}: {candidates["vote percentage"][0]}% ({candidates["votes"][0]})')
print(f'{candidates["name"][1]}: {candidates["vote percentage"][1]}% ({candidates["votes"][1]})')
print(f'{candidates["name"][2]}: {candidates["vote percentage"][2]}% ({candidates["votes"][2]})')
print("------------------------------")
print("Winner: " + winner)
print("------------------------------")

# Sets up the analysis file
output_file = os.path.join("Analysis", "census_results.csv")

# Opens the file to write into
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Outputs the appropriate data formatted to the text file
    writer.writerow(["Election Results"])
    writer.writerow(["------------------------------"])
    writer.writerow(["Total Votes: " + str(totalvotes)])
    writer.writerow(["------------------------------"])
    writer.writerow([f'{candidates["name"][0]}: {candidates["vote percentage"][0]}% ({candidates["votes"][0]})'])
    writer.writerow([f'{candidates["name"][1]}: {candidates["vote percentage"][1]}% ({candidates["votes"][1]})'])
    writer.writerow([f'{candidates["name"][2]}: {candidates["vote percentage"][2]}% ({candidates["votes"][2]})'])
    writer.writerow(["------------------------------"])
    writer.writerow(["Winner: " + winner])
    writer.writerow(["------------------------------"])
