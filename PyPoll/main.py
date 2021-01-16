import os
import csv

csvpath = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #to print data, could run print(csvreader)
    csv_header = next(csvreader) #to print data, could run print(f"CSV Header: {csv_header}")

    voter_list=[] #this variable creates a placeholder/empty list that will be filled out in the later commands
    candidatedict={} #this creates a dictionary to hold the candidates and the number of votes they have

    #this for loop will read each row in the csv file (minus the header)
    #and the for loop will append the voter ID to the voter_list
    #and the for loop will create a dictionary with the candidate name as the key
    #and the counts of the candidate as the value in the key:value pair
    for row in csvreader:
        voter_list.append(row[0])
        candidatename=row[2]
        if candidatename not in candidatedict.keys():
            candidatedict[candidatename] = 1
        else:
            candidatedict[candidatename] += 1
    
    #the codes below will print the results to the terminal
    print("Election Results")
    print("--------------------------------")
    total_votes=len(voter_list)#this counts the total number of votes, which is the total number of voters
    print(f'Total Votes: {total_votes}')
    print("--------------------------------")
    for key, value in candidatedict.items():
        print(f'{key}: {"{:.3f}".format((value/total_votes)*100)}% ({value})')
    print("--------------------------------")
    winner=max(candidatedict, key = candidatedict.get)#this will calculate the max votes of the dictionary
    print(f'Winner: {winner}')
    print("--------------------------------")

    #the codes below will save the terminal output to a txt file
    #obtained this code from https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
    import sys 
    original_stdout = sys.stdout
    with open('Analysis/pypolloutput.txt', 'w') as f:
        sys.stdout = f 

        print("Election Results")
        print("--------------------------------")
        total_votes=len(voter_list)
        print(f'Total Votes: {total_votes}')
        print("--------------------------------")
        for key, value in candidatedict.items():
            print(f'{key}: {"{:.3f}".format((value/total_votes)*100)}% ({value})')
        print("--------------------------------")
        winner=max(candidatedict, key = candidatedict.get)
        print(f'Winner: {winner}')
        print("--------------------------------")

        sys.stdout = original_stdout