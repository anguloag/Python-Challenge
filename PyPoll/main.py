# Script must analyse election_data.csv and calculate the following:
#--- Total number of votes cast
#--- A complete list of the candidates who received votes
#--- Percentage of votes each candidate won
#--- Total number of votes each candidate won
#--- Winner of the election based on popular vote
# Script must also print the analysis to the terminal and export results as a text file
#------------------------------------------------------------------------------------------#

#----- INITIAL SET-UP -----

# Import os module to allow creation of file paths across operating systems
# Import csv module to allow use of csv files
import os
import csv

# Set variable for the path to the election_data.csv file 
#---election_data.csv is composed of 3 columns, 'Voter ID'(column[0]), 'County'(column[1]), and 'Candidate'(column[2])
csvfile = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Set variable to hold the total number of votes, define as null value
Tvotes = 0  
# Set list variable to hold each unique candidate name in the Candidate column, define as empty list
candidateList = []  
# Set truthy variable for whether the candidate name is new or not, default to true (needed for entering names in candidateList)
newName = True
# Set list variable to hold the vote count for each candidate, define as empty list
votecountList = []
# Set list variable to hold the percentage of votes for each candidate, define as empty list
percentList = []
# Set variable to hold the index number for the winner of the popular vote, define as null value
winnerVCIndex = 0
# Set variable to hold the name of the winning candidate, define as empty string
winnerName = ''

#----- CREATING THE MAIN LOOP -----

# Open csv data file as 'elecdata' to be use in the main loop
with open(csvfile) as elecdata:
    
    # Set variable that will allow elecdata to be read by the program through csv.reader 
    elecreader = csv.reader(elecdata, delimiter=',')
    
    # Find headers in first row and set them as variable (to ignore in following for loop)
    elecheader = next(elecreader)

    # Set up main for loop:
    # For each row in bgtreader after headers...
    for row in elecreader:
        # Add 1 to Tvotes value
        Tvotes = Tvotes + 1

        # For each name in candidateList...
        for name in candidateList:
            # If a name in matches the value in cell('row', Candidate)...
            if name == row[2]:
                # Then add 1 to the name's correseponding vote count in votecountList
                votecountList[candidateList.index(name)] = votecountList[candidateList.index(name)] + 1
                # And set newName to False so it doesn't add the name to candidateList again
                newName = False

        # If newName is still true (the value in cell('row', Candidate) is not included in candidateList)...
        if newName == True:
            # Then add the value in cell('row', Candidate) to candidateList
            candidateList.append(row[2])
            # And add a new value into the votecountList equal to 1 
            votecountList.append(1)
            #---doing these at the same time here will allow index numbers for candidate names and corresponding vote counts to match
        # Otherwise...
        else:
            # Make sure we are still in the default truthy condition for newName
            newName = True

#----- FINDING THE WINNING CANDIDATE -----

# For each value in the votecountList
for votecount in votecountList:
    # Calculate the percentage of votes, and add the resulting value to the percentList
    percentList.append((votecount / Tvotes)*100)
    # Set the value of winnerVCIndex as equal to the index number for the highest vote count in votecountList
    winnerVCIndex = votecountList.index(max(votecountList))
    # Set the value of winnerName as equal to the highest count's corresponding name in candidateList
    winnerName = candidateList[winnerVCIndex]
            
#----- PRINTING THE RESULTS -----

# Print the analysis results to the terminal:
#---have to create for loop to go through each name in candidateList and print out formatted results
print('Election Results')
print('---------------------------------------------------')
print(f'Total Votes: {Tvotes}')
print('---------------------------------------------------')
for name in candidateList:
    print(f'{name}: {round(percentList[candidateList.index(name)],3)}% ({votecountList[candidateList.index(name)]})')
print('---------------------------------------------------')
print(f'Winner: {winnerName}')
print('---------------------------------------------------')

# Export the analysis results as a text file:
# Set a variable for the path to where the text file should be exported to
txtfile = os.path.join('Analysis', 'ElectionResults_output.txt')

# Open the text file to be written in
with open(txtfile, 'w', newline='') as results:
    
    # Write out analysis results in the text file
    results.write('Election Results\n')
    results.write('---------------------------------------------------\n')
    results.write(f'Total Votes: {Tvotes}\n')
    results.write('---------------------------------------------------\n')
    for name in candidateList:
        results.write(f'{name}: {round(percentList[candidateList.index(name)],3)}% ({votecountList[candidateList.index(name)]})\n')
    results.write('---------------------------------------------------\n')
    results.write(f'Winner: {winnerName}\n')
    results.write('---------------------------------------------------\n')
    results.close()