
import os
import csv

# Declare the required variables
total_votes_count = 0
kcount = 0
ccount = 0
lcount = 0
tcount = 0
winner_dict = {}


# Collects data from the election_data csv
election_data = os.path.join("Resources", "election_data.csv")

# Open and read election_data csv
with open(election_data, 'r') as csv_file:

    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Skip the header
    header = next(csv_reader)

    # Read through each row of data after the header
    for row in csv_reader:

        # Declare the required variables
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        # 1. total number of votes cast
        total_votes_count = total_votes_count + row.count(voter_id)

        # 2. complete list of candidates who received votes
        # 3. percentage of votes each candidate won
        # 4. total number of votes each candidate won
        # 5. winner of the election based on popular vote
        
        # conditional block will fetch the count for each candidate
        if candidate == "Khan":
            kcount = kcount + row.count(candidate)
        elif candidate == "Correy":
            ccount = ccount + row.count(candidate)
        elif candidate == "Li":
            lcount = lcount + row.count(candidate)
        elif candidate == "O'Tooley":
            tcount = tcount + row.count(candidate)


# print the required output as per below

print("Election Results") # print into console
print("Election Results", file=open('analysis/PyPoll_Results.txt', 'wt')) # write into file

# -----------------------------------------------------------------------------------

print("-------------------------") # print into console
print("-------------------------", file=open('analysis/PyPoll_Results.txt', 'at')) # append to file

# -----------------------------------------------------------------------------------

print("Total Votes:" + " " + str(total_votes_count)) # print into console
print("Total Votes:" + " " + str(total_votes_count), file=open('analysis/PyPoll_Results.txt', 'at')) # append to file

# -----------------------------------------------------------------------------------

print("-------------------------") # print into console
print("-------------------------", file=open('analysis/PyPoll_Results.txt', 'at')) # append to file

# -----------------------------------------------------------------------------------

# below will calculate % of votes for each candidate
k_win_percent = (kcount / total_votes_count) * 100
c_win_percent = (ccount / total_votes_count) * 100
l_win_percent = (lcount / total_votes_count) * 100
t_win_percent = (tcount / total_votes_count) * 100

# below will print % of votes and their respective counts for each candidate
print("Khan: " + str(format(k_win_percent,".3f")) + "% (" + str(kcount) + ")") # print into console
print("Khan: " + str(format(k_win_percent,".3f")) + "% (" + str(kcount) + ")", file=open('analysis/PyPoll_Results.txt', 'at')) # append to file

print("Correy: " + str(format(c_win_percent,".3f")) + "% (" + str(ccount) + ")") # print into console
print("Correy: " + str(format(c_win_percent,".3f")) + "% (" + str(ccount) + ")", file=open('analysis/PyPoll_Results.txt', 'at')) # append to file

print("Li: " + str(format(l_win_percent,".3f")) + "% (" + str(lcount) + ")") # print into console
print("Li: " + str(format(l_win_percent,".3f")) + "% (" + str(lcount) + ")", file=open('analysis/PyPoll_Results.txt', 'at')) # append to file

print("O'Tooley: " + str(format(t_win_percent,".3f")) + "% (" + str(tcount) + ")") # print into console
print("O'Tooley: " + str(format(t_win_percent,".3f")) + "% (" + str(tcount) + ")", file=open('analysis/PyPoll_Results.txt', 'at')) # append to file

# -----------------------------------------------------------------------------------

print("-------------------------") # print into console
print("-------------------------", file=open('analysis/PyPoll_Results.txt', 'at')) # append to file

# -----------------------------------------------------------------------------------

# creates dictionary to hold each candidate and their total vote count | for e.g Khan: '2218231'
winner_dict["Khan"] = kcount
winner_dict["Correy"] = ccount
winner_dict["Li"] = lcount
winner_dict["O'Tooley"] = tcount

# fetch the MAX value field from dictionary into variable
max_value = max(winner_dict.values())

# list out keys and values separately from dictionary
key_list = list(winner_dict.keys()) # Candidate
val_list = list(winner_dict.values()) # Total Votes

# find out the position of MAX value field from dictionary
max_position = val_list.index(max_value)

# get the winner candidate name from key list based on above max position
winner_candidate = str(key_list[max_position])

print("Winner: " + winner_candidate) # print into console
print("Winner: " + winner_candidate, file=open('analysis/PyPoll_Results.txt', 'at')) # append to file

# -----------------------------------------------------------------------------------

print("-------------------------") # print into console
print("-------------------------", file=open('analysis/PyPoll_Results.txt', 'at')) # append to file