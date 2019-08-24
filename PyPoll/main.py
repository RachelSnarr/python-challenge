# THIS IS INCOMPLETE. 
# UNFORTUNATELY I DID NOT HAVE THE TIME TO FINISH THE HOMEWORK THIS WEEK
# I WILL BE FINISHING THIS ON MY OWN TIME
# IT JUST WON'T BE IN TIME TO BE GRADED ACCORDINGLY

# import
import os
import csv

# csv file pulling and reading
csvfile = os.path.join("..", "PyPoll", "election_data.csv")

with open(csvfile, 'r') as electionfile:

    election_reader = csv.reader(electionfile, delimiter=',')
    header = next(election_reader)

    totalvotes = 0 #starting value
    votes = [] #list of who was vote for
    candidates = []
    votespercandidate = []
    votepercentages = []
    winner = ""

    for row in election_reader:
        
        votes.append(row[2])
        totalvotes = len(votes) 

        if row[2] not in candidates:
            candidates.append(row[2])

print('Election Results' '\n' '----------')
print(f'Total votes: {totalvotes}' '\n' '----------')
print(f'{candidates[0]}')
print(f'{candidates[1]}')
print(f'{candidates[2]}')
print(f'{candidates[3]}' '\n' '----------' '\n')
print(f'Winner: {winner}' '\n' '----------')

with open('results.txt', 'w') as results:

    results.write('Election Results' '\n' '----------' '\n')
    
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.