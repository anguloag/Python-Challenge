# Script must analyse budget_data.csv and calculate the following:
#--- Total number of months in the data set
#--- Net total amount of Profit/Losses over entire period
#--- Change in Profit/Losses over entire period
#--- Average of changes in Profit/Losses 
#--- Greatest increase in profits for entire period (date and amount)
#--- Greatest decrease in profits for entire period (date and amount)
# Script must also print the analysis to the terminal and export results as a text file
#------------------------------------------------------------------------------------------#

#----- INITIAL SET-UP -----

# Import os module to allow creation of file paths across operating systems
# Import csv module to allow use of csv files
import os
import csv

# Set variable for the path to the budget_data.csv file 
#---budget_data.csv is composed of 2 columns, 'Date'(column[0]) and 'Profit/Losses'(column[1])
csvfile = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Set variable to hold the total number of months, define as null value
Tmths = 0
# Set list variable to hold each month under the Date column, define as empty list
mthList = []
# Set variable to hold the net total of Profit/loses, define as null value 
netTPL = 0.0
# Set list variable to hold each calculated monthly change in Profit/Losses, define as empty list 
chngPL = []
# Set variable to hold calculated average of monthly changes in Profit/Losses, define as null value
avgPL = 0.0
# Set variables for greatest inc. and greatest dec. in profits, define as null values
GIncP_value = 0.0
GDecP_value = 0.0
# Set variables for greatest inc. and greatest dec. dates, define as empty string values
GIncP_date = ''
GDecP_date = ''
# Set truthy variable for row1 (needed to set mth1 in first row)
row1 = True

#----- CREATING THE MAIN LOOP -----

# Open csv data file as 'bgtdata' to be use in the main loop
with open(csvfile) as bgtdata:
    
    # Set variable that will allow bgtdata to be read by the program through csv.reader 
    bgtreader = csv.reader(bgtdata, delimiter=',')
    
    # Find headers in first row and set them as variable (to ignore in following for loop)
    bgtheader = next(bgtreader)

    # Set up main for loop:
    # For each row in bgtreader after headers...
    for row in bgtreader:
        # Add the value in cell('row', Date) into mthList
        mthList.append(row[0])
        # Add 1 to Tmths value
        Tmths = Tmths + 1
        # Add the value in cell('row', Profit/Losses) to netTPL value
        #---need to force row[1] to be a float to match netTPL value type
        netTPL = netTPL + float(row[1])
        # Set value in cell('row', Profit/Losses) as mth2 - again as a float
        
        # If we are in the first row...
        if row1 == True:
            # Then set mth1 equal to the float value of cell('row', Profit/Losses)
            mth1 = float(row[1])
            # And reset truthy value of row1 to False so program knows we are not in row1 anymore
            row1 = False
        # In all other rows...
        else: 
            # Set mth2 qual to float valut of cell('row', Profit/Losses)
            mth2 = float(row[1])
            # Calculate change in Profit/Losses from mth1 to mth2, add value to chngPL list
            chngPL.append(mth2-mth1)
            # Reset value of mth1 to equal current mth2 in order to calculate next monthly change in P/Ls
            mth1 = mth2

#----- CALCULATING THE AVERAGE CHANGE IN PROFIT/LOSSES -----

# Calculate the average monthly change in Profit/Losses using sum() and len() of chngPL list 
avgPL = sum(chngPL) / len(chngPL)

#----- FINDING THE DATE AND VALUE FOR GREATEST INCREASE AND GREATEST DECREASE -----

# Find the values and dates for greatest increase and greatest decrease:
# For each value in the chngPL list...
for i in range(len(chngPL)):
    
    # If the value in the chngPL List is greater than the current GIncP_value...
    if chngPL[i] > GIncP_value:
        # Then set GIncP_value equal to the value in the chngPL List
        GIncP_value = chngPL[i]
        # And set GIncP_date as the corresponding date listed in mthList (i+1)
        GIncP_date = mthList[i+1]
    # If the value in the chngPL List is less than the current GDecP_value...   
    if chngPL[i] < GDecP_value:
        # Then set GDecP_value equal to the value in the chngPL List
        GDecP_value = chngPL[i]
        # And set GDecP_date as the corresponding date listed in mthList (i+1)
        GDecP_date = mthList[i+1]

#----- PRINTING THE RESULTS -----

# Print the analysis results to the terminal:
print('Financial Analysis')
print('---------------------------------------------------')
print(f'Total Months: {Tmths}')
print(f'Net Total Profit/Losses: ${round(netTPL,2)}')
print(f'Average Change: ${round(avgPL,2)}')
print(f'Greatest Increase: {GIncP_date} (${GIncP_value})')
print(f'Greatest Decrease: {GDecP_date} (${GDecP_value})')

# Export the analysis results as a text file:
# Set a variable for the path to where the text file should be exported to
txtfile = os.path.join('Analysis', 'FinancialAnalysis_results.txt')

# Open the text file to be written in
with open(txtfile, 'w', newline='') as results:
    
    # Write out analysis results in the text file
    results.write('Financial Analysis\n')
    results.write('---------------------------------------------------\n')
    results.write(f'Total Months: {Tmths}\n')
    results.write(f'Net Total Profit/Losses: ${round(netTPL,2)}\n')
    results.write(f'Average Change: ${round(avgPL,2)}\n')
    results.write(f'Greatest Increase: {GIncP_date} (${GIncP_value})\n')
    results.write(f'Greatest Decrease: {GDecP_date} (${GDecP_value})\n')
    results.close()
