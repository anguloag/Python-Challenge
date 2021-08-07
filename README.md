# PyBank Challenge
### Objective
Develop a Python code that analyzes a company's financial records and creates a summary output of the results.

### Description of the Data: budget_data
The company's financial records are contained in a csv file called "budget_data". The dataset is organized in two columns: 
- Date - the month and year for each entry
- Profit/Losses - the total profit or losses from that month

### What the Code Should Do
The Python code should loop through all of the entries and create a summary table containing the following information:
- The total number of months included in the dataset
- The net total amount of Profit/Losses over the whole period (from the first entry to the last), formatted in dollars
- The average change in Profit/Losses (the sum of each change in Profit/Losses from one month to the next / the total number of months), formatted in dollars
- The date and value (in $) of the greatest increase in profits over the whole period
- The date and value (in $) of the greatest decrease in profits over the whole period

In addition to printing the anaylsis results into the terminal, the code should export the results into a text file.

# PyPoll Challenge
### Objective
Develop a Python code that analyzes the votes from a town's election data and creates a summary output of the results.

### Description of the Data: election_data
The votes from the town's election are contained in a csv file called "election_data". The dataset is organized in three columns:
- Voter ID - The voter identification number for each citizen
- County - The county that the citizen is from
- Candidate - The candidate that the citizen voted for

### What the Code Should Do
The Python code should loop through all of the votes and create a summary table containing the following information:
- The total number of votes cast during the election
- A list of the candidates the town citizens voted for
- The percentage of votes each candidate won
- The number of votes each candidate won
- The name of the candidate who won the town's popular vote

In addition to printing the anaylsis results into the terminal, the code should export the results into a text file.
