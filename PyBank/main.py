import os
import csv

csvpath = os.path.join('Resources', 'PyBank_Resources_budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    datelist=[]
    net=[]
    change=[]
    for row in csvreader:
        datelist.append([row[0]])
        net.append(float(row[1]))
    print(datelist)
    print(net)
    print(len(datelist))
    print(sum(net))

    for x in range(1,len(net)): #or range(0,len(net)-1)
        change.append(net[x]-net[x-1]) 
        avchange=(sum(change)/len(change))#sum of hcnages divided by total number of changes
    print(avchange)

    #net=[]
    #for row in csvreader:
        #net.append(float(row[1]))
    #print(net)

    #print(row[1])
    #print(float(row[1])+100)

    #net=0
    #for row in csvreader:
        #net += (float(row[1]))
    #print(net)

    #dictionary, key=name; value=votes candidate name and number of votes
    #append everything in first for loop
    #create empty dictionary

    