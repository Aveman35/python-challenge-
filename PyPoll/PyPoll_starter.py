# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
names_and_vote_counts = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_vote_tracker = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        if row[0]:
            total_votes += 1

        # Get the candidate's name from the row
        names = row[2]
        
        # If the candidate is not already in the candidate list, add them
        # Add a vote to the candidate's count
        if names:
            if names in names_and_vote_counts:
                names_and_vote_counts[names] += 1
            else:
                names_and_vote_counts[names] = 1

candidates_vote_list = list(names_and_vote_counts.items())

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(total_votes)
    
    # Loop through the candidates to determine vote percentages and identify the winner
    candidate_results = []
    for candidate in candidates_vote_list:

        # Get the vote count and calculate the percentage
        results = f'''{candidate[0]}: {candidate[1] / total_votes * 100:.3f}% ({candidate[1]})'''

        # Print and save each candidate's vote count and percentage
        candidate_results.append(results)

        # Update the winning candidate if this one has more votes
        if candidate[1] > winning_vote_tracker:
            winning_vote_tracker = candidate[1]
            winning_candidate = candidate[0]

    # Generate and print the winning candidate summary
    winning_candidate_summary = f"""
    Election Results
    -------------------------
    Total Votes: {total_votes} 
    -------------------------
    {candidate_results[0]} 
    {candidate_results[1]} 
    {candidate_results[2]}
    -------------------------
    Winner: {winning_candidate}
    -------------------------"""
    print(winning_candidate_summary)
    # Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)