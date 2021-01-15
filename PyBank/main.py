import os
import csv

csvpath = os.path.join('Resources', 'PyBank_Resources_budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #to print data, could run print(csvreader)
    csv_header = next(csvreader) #to print data, could run print(f"CSV Header: {csv_header}")

    datelist=[] #this variable and the two after create placeholder/empty lists for the variables
    profloss=[]
    change=[]
    for row in csvreader: 
        datelist.append(row[0]) #in this for loop, the dates list is appended with the data in column A (index 0) 
        profloss.append(int(row[1])) #within the same for loop, the profloss list is appended with the data in column B (index 1)

    for x in range(1,len(profloss)): #or range(0,len(profloss)-1)
        change.append(profloss[x]-profloss[x-1]) #or change.append(profless[x+1]-profless[x])
        avchange="{:.2f}".format((sum(change)/len(change))) #sum of changes divided by total number of changes, adding format for 2 decimal places

    #finding max of the change (which is a list decreased by one to length 85),
        #Use the index+1 to pull the max month from the date list (to accomodate date list length of 86)
    maxprof_index=change.index(max(change))
    maxprof=max(change)
    maxprof_month=datelist[maxprof_index+1]
   
    #finding min of the change similar to above
    minprof_index=change.index(min(change))
    minprof=min(change)
    minprof_month=datelist[minprof_index+1]

    #print in terminal the findings
    print("Financial Analysis")
    print("--------------------------")
    print(f'Total Months: {len(datelist)}')
    print(f'Total: ${sum(profloss)}')
    print(f'Average Change: ${avchange}')
    print(f'Greatest Increase in Profits: {maxprof_month} (${maxprof})')
    print(f'Greatest Decrease in Profits: {minprof_month} (${minprof})')

    #create a variable to print findingsto a txt file
    mystring=f"""
    Financial Analysis
    ----------------------------------
    Total Months: {len(datelist)}
    Total: ${sum(profloss)}
    Average Change: ${avchange}
    Greatest Increase in Profits: {maxprof_month} (${maxprof})
    Greatest Decrease in Profits: {minprof_month} (${minprof})
    """

    #Printing txt file to Analysis folder
    txtoutput = open("Analysis/pybankoutput.txt", "w")
    txtoutput.write(mystring)
    output_path = os.path.join("Analysis", "pybankoutput.txt")