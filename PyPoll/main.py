import os
import csv

csvpath = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #to print data, could run print(csvreader)
    csv_header = next(csvreader) #to print data, could run print(f"CSV Header: {csv_header}")

    voter_list=[] #this variable and the one after create placeholder/empty lists that will be filled out in the later commands
    can_list=[]
    counter_list=[]
    candidatedict={}

    #find each candidate, then how many votes per person

    for row in csvreader:
        voter_list.append(row[0])
        candidatename=row[2]
        if candidatename not in candidatedict.keys():
            candidatedict[candidatename] = 1
        else:
            candidatedict[candidatename] += 1

    total_votes=len(voter_list)

    for key, value in candidatedict.items():
        print(f'{key}: ({(value/total_votes)*100})% ({value})')
    
    winner=max(candidatedict, key = candidatedict.get)
    print(f'Winner: {winner}')


