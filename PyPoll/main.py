# Filename:  main.py
# Used to analyze election_data.csv (PyPoll)
# Eric Staveley   MWSa
# 
# You will be give a set of poll data called election_data.csv. 
# The dataset is composed of three columns: Voter ID, County, and Candidate. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os   # import the os module...to create file paths across operating systems
import csv  # Module for reading CSV files

candidates = {}    #init a dictionary called candidates, 
                    #candidates will have a key: candidate name , value: votes

#csv file will be in Resources dir at our script level
csvfile = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvfile, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)
    # The dataset is composed of three columns: VoterID, County, Candidate
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    tot_votes = 0           # running variable used for each vote count

    for row in csvreader:
        #print(row)
        tot_votes = tot_votes + 1       #running TOTAL of ALL votes (REQUESTED)
        if row[2] in candidates:        # check if candidate is already in our dict
            candidates[row[2]] += 1     #they are, so add 1 to the votecount
        else:
            candidates[row[2]] = 1      #theyre not there yet so make it 1

# REQUESTED print to the terminal
print("Election Results\n")     
print("-----------------------\n") 
print("Total Votes: " + str(tot_votes) + "\n")
print("-----------------------\n") 
# find the %s now, by looping thru the dictionary
for key, value in candidates.items():
    print(key + ": " + str(round((value/tot_votes * 100),2)) + "% (" + str(value) + ")")    # REQUESTED
print("-----------------------\n") 
print("Winner: " + max(candidates, key=candidates.get) + "\n")          #  REQUESTED
print("-----------------------") 

foutname = "election_data_analysis.txt"
print("Printing this financial analysis to: " + str(os.getcwd()) + "/" + foutname)

#write the Election Analysis to a file, a text file, not a csv file     # REQUESTED OUTPUT TO A FILE
with open(foutname, 'w') as file_object:
    file_object.write("Election Results\n")
with open(foutname, 'a') as file_object:
    file_object.write("-----------------------\n")
    file_object.write("Total Votes: " + str(tot_votes) + "\n")
    file_object.write("-----------------------\n")
    # find the %s now, by looping thru the dictionary
    for key, value in candidates.items():
        file_object.write(key + ": " + str(round((value/tot_votes * 100),2)) + "% (" + str(value) + ")\n")
    file_object.write("-----------------------\n") 
    file_object.write("Winner: " + max(candidates, key=candidates.get) + "\n")
    file_object.write("-----------------------") 
    
print("\nFinished!")