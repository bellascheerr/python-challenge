import os
import csv

# Define variables used throughout the script
candidates = {}
total_votes = 0
winner_name = ""
winner_total_votes = 0

# Define function to format as percentage to two decimal places
def as_percentage(amount):
    return '{:,.3f}%'.format(amount)

# Path to acquire data from the Resources folder
election_csv = os.path.join('.', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Iterate through the rows to obtain the vote counts
    for row in csvreader:
        candidate = row[2]

        # Check if the candidate name has not been listed and add it and set the vote total to zero
        if candidate not in candidates.keys():
            candidates[candidate] = 0

        # Tally the votes per candidate
        candidates[candidate] += 1

        total_votes += 1

# Print the vote tally analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Go through the dictionary and get the candidate names and total votes
for candidate_name, candidate_total_votes in candidates.items():
    percentage_votes = (candidate_total_votes / total_votes) * 100
    print(f"{candidate_name}: {as_percentage(percentage_votes)} ({candidate_total_votes})")

    # Find the name of the candidate with the most votes and the total votes for that candidate
    if candidate_total_votes > winner_total_votes:
        winner_total_votes = candidate_total_votes
        winner_name = candidate_name

print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

# Output the analysis to a text file in the 'analysis' folder
analysis_results = os.path.join('.', 'analysis', 'election_results.txt')
with open(analysis_results, 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")

    for candidate_name, candidate_total_votes in candidates.items():
        percentage_votes = (candidate_total_votes / total_votes) * 100
        f.write(f"{candidate_name}: {as_percentage(percentage_votes)} ({candidate_total_votes})\n")

    f.write("-------------------------\n")
    f.write(f"Winner: {winner_name}\n")
    f.write("-------------------------\n")
