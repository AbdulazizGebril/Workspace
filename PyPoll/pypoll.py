import os
import csv

poll_data= os.path.join("raw_data","election_data_2.csv")

#def candidate_count(candidate_name, candidate, count=0):
    #if candidate in candidate_name:
        #count = count + 1
        #candidate_name.remove(candidate)
    #return candidate_count(candidate_name, candidate, count)




with open(poll_data,newline="") as csvfile:
    reader=csv.reader(csvfile, delimiter=",")

    next(reader)

    voter_id=[]
    candidate_name=[]
    candidate_1=[]
    candidate_2=[]
    candidate_3=[]
    candidate_4=[]





    for row in reader:
        voter_id.append(row[0])
        candidate_name.append(row[2])

    for candidate in candidate_name:
        if candidate == "Khan":
            candidate_1.append(candidate)

        elif candidate == "Li":
            candidate_2.append(candidate)

        elif candidate == "Correy":
            candidate_3.append(candidate)

        elif candidate == "O'Tooley":
            candidate_4.append(candidate)

    candidate_1_percent = (len(candidate_1)/len(voter_id))*100
    candidate_2_percent = (len(candidate_2)/len(voter_id))*100
    candidate_3_percent = (len(candidate_3)/len(voter_id))*100
    candidate_4_percent = (len(candidate_4)/len(voter_id))*100

    Winner={"Khan":len(candidate_1),"Li":len(candidate_2),"Correy":len(candidate_3),"O'Tooley":len(candidate_4)}



    print("Election Results")
    print("---------------------------------")
    print("Total Votes: ", len(voter_id))
    print("---------------------------------")
    print("Khan: ", candidate_1_percent,"% ","(", len(candidate_1),")")
    print("Li: ",candidate_2_percent,"% ","(", len(candidate_2),")")
    print("Correy: ",candidate_3_percent,"% ","(", len(candidate_3),")")
    print("O'Tooley: ",candidate_4_percent,"% ","(", len(candidate_4),")")
    print("---------------------------------")
    print("Winner: ", max(Winner))

    
