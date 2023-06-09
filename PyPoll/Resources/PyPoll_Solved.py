# import the os module
# create file path for OS
import os

# Module touse in reading CSV files
import csv

csvpath = os.path.join('election_data.csv')

print("Election Results")
print("__________________")
votes = []
candidates = []
BallotID = []
Winner = []
percentage =[]

# Reading using CSV module

with open(csvpath,newline='') as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    
  # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
     
    for column in csvreader:
         votes.append(column[0])
         candidates.append(column[2])
    
                            
Total_Votes = (len(votes))
print(f"Total Votes: {Total_Votes}")
    
    #Count each number of candidates in the candidates list
CharlesCasperStockham = int(candidates.count("Charles Casper Stockham"))
DianaDeGette = int(candidates.count("Diana DeGette"))
RaymonAnthonyDoane = int(candidates.count("Raymon Anthony Doane"))
       #Get a percentage of each candidates vote total
CharlesCasperStockham_percentage = round((CharlesCasperStockham/Total_Votes) * 100, 1)
DianaDeGette_percentage = round((DianaDeGette/Total_Votes) * 100, 1)
RaymonAnthonyDoane_percentage = round((RaymonAnthonyDoane/Total_Votes) * 100, 1)
    
    #Print each candidate's name, vote percentage, and raw number of votes
print(f"CharlesCasperStockham: {CharlesCasperStockham_percentage}% ({CharlesCasperStockham})") 
print(f"DianaDeGette: {DianaDeGette_percentage}% ({DianaDeGette})") 
print(f"RaymonAnthonyDoane: {RaymonAnthonyDoane_percentage}% ({RaymonAnthonyDoane})")
    
    #Compare Votes and pick winner with the most votes
if CharlesCasperStockham > DianaDeGette > RaymonAnthonyDoane:
    Winner = "Charles Casper Stockham"
elif DianaDeGette>CharlesCasperStockham>RaymonAnthonyDoane:
    Winner = "Diana DeGette"    
elif RaymonAnthonyDoane > CharlesCasperStockham > DianaDeGette:
    Winner = "Raymon Anthony Doane" 

print(f"Winner: {Winner}")   

output_path = os.path.join("election.txt")
with open(output_path, 'w', newline='') as txtfile:
    txtfile.write(f"Total Votes: {Total_Votes}")
    txtfile.write(f"CharlesCasperStockham: {CharlesCasperStockham_percentage}% ({CharlesCasperStockham})")
    txtfile.write(f"DianaDeGette: {DianaDeGette_percentage}% ({DianaDeGette})")
    txtfile.write(f"RaymonAnthonyDoane: {RaymonAnthonyDoane_percentage}% ({RaymonAnthonyDoane})")
    txtfile.write(f"Winner: {Winner}")
    txtfile.close()
