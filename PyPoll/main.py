import os
import csv

csvpath = os.path.join('Resources', 'PyPoll_Resources_election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    voter=[]
    candidate=[]
    candict={}
    candict={
            "candidate":candidate,
            "votes":voter}
    for row in csvreader:
        voter.append(row[0])
        candidate.append(row[2])
            if candidate[ in candidate:
                break
        
        


    #voter=[]
    #candidatedict={}
    #for row in csvreader:
        #voter.append(row[0])
        #candidatename=(row[2])
        #if candidatename not in candidatedict:
            #candidatedict[candidatename]=1
        #else:
            #candidatedict[candidatename] += 1
    #print(len(voter))
    #print(candidatedict)


