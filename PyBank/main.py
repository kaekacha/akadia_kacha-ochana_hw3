import os
import csv

csvpath = os.path.join('Resources', 'PyBank_Resources_budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    datelist=[]
    profloss=[]
    change=[]
    for row in csvreader:
        datelist.append(row[0])
        profloss.append(int(row[1]))
    #print(datelist)
    #print(profloss)
    #print(len(datelist))
    #print(sum(profloss))

    for x in range(1,len(profloss)): #or range(0,len(net)-1)
        change.append(profloss[x]-profloss[x-1]) 
        avchange="{:.2f}".format((sum(change)/len(change)))#sum of hcnages divided by total number of changes

    maxprof_index=change.index(max(change))
    maxprof=max(change)
    maxprof_month=datelist[maxprof_index+1]
   
    minprof_index=change.index(min(change))
    minprof=min(change)
    minprof_month=datelist[minprof_index+1]

    print("Financial Analysis")
    print("--------------------------")
    print(f'Total Months: {len(datelist)}')
    print(f'Total: ${sum(profloss)}')
    print(f'Average Change: ${avchange}')
    print(f'Greatest Increase in Profits: {maxprof_month} (${maxprof})')
    print(f'Greatest Decrease in Profits: {minprof_month} (${minprof})')