#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, 
#Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)
#You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script 
# that analyzes the votes and calculates each of the following:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#As an example, your analysis should look similar to the one below:

#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
# -------------------------
#  Winner: Khan
# -------------------------

# Dependencies
import csv
import os

#File to load
election_data=os.path.join("..","pyPoll","election_data.csv")

#Define the variables and lists
total_votes=0
candidate_votes = {}
winner = ""
max_votes = 0
# Open and read csv
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    header= next(csvreader)
    
    # Loop through data
    for row in csvreader:
        #get the total votes
        total_votes = total_votes + 1
        #create the conditional for adding candidate and votes
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

#Print the output
print("Election Results")
print("----------------------------")
print("Total Votes: "+ str(total_votes))

print("----------------------------")

for candidate in candidate_votes:
    vote = candidate_votes[candidate]
    percentage = round((vote * 100)/float(total_votes),1)
    if vote > max_votes:
        max_votes = vote
        winner = candidate

    print(candidate + ": " + str(percentage)+ "% " + "(" + str(vote) + ")")
print("----------------------------")    
print("Winner: " + winner)
print("----------------------------")         

#set variable for output file
output_file = os.path.join("..","pyPoll","PyPollOutput.txt")

#open the output file
with open("PyPollOutput.txt", "w") as text_file:
        text_file.write("Election Results")
        text_file.write("----------------------------")
        text_file.write("Total Votes: "+ str(total_votes))
        text_file.write("----------------------------")
        text_file.write(candidate + ": " + str(percentage)+ "% " + "(" + str(vote) + ")")
        text_file.write("----------------------------")    
        text_file.write("Winner: " + winner)
        text_file.write("----------------------------")  