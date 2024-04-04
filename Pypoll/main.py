import os
import csv

#Path to file
pypoll_csv = os.path.join("..", "resources", "election_data.csv")

#Reading file
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Print and skip counting the header
    csv_header = next(csv_reader)

#initialize count
    total_votes = 0
    charles_count = 0
    diana_count = 0
    raymon_count = 0

#loop through row to find total votes and candidate votes
    for row in csv_reader:
        total_votes += 1

        if row[2] == "Charles Casper Stockham":
            charles_count += 1

        if row[2] == "Diana DeGette":
            diana_count += 1

        if row[2] == "Raymon Anthony Doane":
            raymon_count += 1

# Calculate percentages only if there are votes for each candidate
    if total_votes != 0:
        charles_percent = round((charles_count / total_votes) * 100, 3)
        diana_percent = round((diana_count / total_votes) * 100, 3)
        raymon_percent = round((raymon_count / total_votes) * 100, 3)

# create dictionary to summarize result
candidate_dict = {"Charles Casper Stockham": charles_percent, "Diana DeGette": diana_percent, "Raymon Athony Doana": raymon_percent}

#find winner
winner = max(candidate_dict, key=candidate_dict.get)


print("\nElection Results")
print("---------------------------------------------")
print(f"Total Votes = {total_votes}" )
print("---------------------------------------------")
print(f"Charles Casper Stockham: {charles_percent} % {charles_count}")
print(f"Diana DeGette: {diana_percent}% {diana_count}")
print(f"Raymon Anthony Doane: {raymon_percent}% {(raymon_count)}")
print(f"\nWinner: {winner}")
print("\n--------------------------------------------")