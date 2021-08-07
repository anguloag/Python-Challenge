# Script must analyse election_data.csv and calculate the following:
#--- Total number of votes cast
#--- A complete list of the candidates who received votes
#--- Percentage of votes each candidate won
#--- Total number of votes each candidate won
#--- Winner of the election based on popular vote
# Script must also print the analysis to the terminal and export results as a text file
#------------------------------------------------------------------------------------------#

#----- Initial Set-Up -----

# Import os module to allow creation of file paths across operating systems
# Import csv module to allow use of csv files
import os
import csv

#from collections import Counter

# Set variable for the path to the election_data.csv file 
#---election_data.csv is composed of 3 columns, 'Voter ID'(column[0]), 'County'(column[1]), and 'Candidate'(column[2])
csvfile = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Set variable to hold the total number of votes, define as null value
Tvotes = 0  
# Set list variable to hold each unique candidate name in the Candidate column, define as empty list
candidateList = []  
# Set truthy variable for whether the candidate name is new or not (needed for entering names in candidateList)
newName = True

votecountList = []

percentList = []

winnerVCIndex = 0

winnerName = ''

#----- Creating Main Loop -----

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

        # Compare each name in candidateList to value in cell('row', Candidate)
        for name in candidateList:
            # If one of the names in candidateList matches the value in cell('row', Candidate)...
            if name == row[2]:
                # Then add 1 to number of votes for that candidate in votecountList
                votecountList[candidateList.index(name)] = votecountList[candidateList.index(name)] + 1
                # Set newName to False so we don't add the name to candidateList 
                newName = False

        if newName == True:
            # Then add the value in cell('row', Candidate) to candidateList
            candidateList.append(row[2])
            votecountList.append(1)
        else:
            newName = True

for votecount in votecountList:
    percentList.append((votecount / Tvotes)*100)

    winnerVCIndex = votecountList.index(max(votecountList))

    winnerName = candidateList[winnerVCIndex]

#print(Tvotes)
#print(candidateList)
#print(votecountList)
#print(percentList)
#print(f'{winnerVCIndex}')
#print(winnerName)
            
#----- Printing the Results -----

# Print the analysis results to the terminal:
print('Election Results')
print('---------------------------------------------------')
print(f'Total Votes: {Tvotes}')
print('---------------------------------------------------')
for name in candidateList:
    print(f'{name}: {round(percentList[candidateList.index(name)],3)}% ({votecountList[candidateList.index(name)]})')
#print(f'{NAME}: {PERCENT}% ({VOTES})')
#print(f'{NAME}: {PERCENT}% ({VOTES})')
#print(f'{NAME}: {PERCENT}% ({VOTES})')
#print(f'{NAME}: {PERCENT}% ({VOTES})')
print('---------------------------------------------------')
print(f'Winner: {winnerName}')
print('---------------------------------------------------')

# Export the analysis results as a text file:
# Set a variable for the path to where the text file should be exported to
#txtfile = os.path.join('Analysis', 'ElectionResults_output.txt')

# Open the text file to be written in
#with open(txtfile, 'w', newline='') as results:
    
    # Write out analysis results in the text file
    #results.write('Election Results\n')
    #results.write('---------------------------------------------------\n')
    #results.write(f'\n')
    #results.write('---------------------------------------------------\n')
    #results.write(f'\n')
    #results.write(f'\n')
    #results.write(f'\n')
    #results.write(f'\n')
    #results.write('---------------------------------------------------\n')
    #results.write(f'\n')
    #results.write('---------------------------------------------------\n')