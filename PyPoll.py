#Add our dependencies.
import csv
import os
#assign a variable for the file to load and the path.
file_to_load = os.path.join("resources","election_results.csv")
#assign a variable for the file to load and the path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter.
total_votes = 0

#candidate Options
candidate_options =[]
#Candidate votes
candidate_votes={}
#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open (file_to_load) as election_data:
    file_reader = csv.reader(election_data)

     # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the toal vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]

        #add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #begin tracking candidates vote count.
            candidate_votes[candidate_name]= 0
        #add a vote to that candidate's count. 
        #has to be aligned with if to count
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_candidate = candidate_name
         winning_percentage = vote_percentage


    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)  
    # Determine winning vote count and candidate
    
    
    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    



