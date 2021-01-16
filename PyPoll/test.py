for row in csvreader:
        voter.append(row[0])
        candidatedict["name"]=(row[2])
        if candidatedict["name"] not in candidatedict:
            candidatedict["votes"]=1
        else:
            candidatedict["votes"]+=1

    print(row)
    print(candidatedict)
    print(len(voter))