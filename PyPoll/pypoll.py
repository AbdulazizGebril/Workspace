import os
import csv

poll_data= os.path.join("raw_data","election_data_1.csv")

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
        if candidate == "Vestal":
            candidate_1.append(candidate)

        elif candidate == "Torres":
            candidate_2.append(candidate)

        elif candidate == "Seth":
            candidate_3.append(candidate)

        elif candidate == "Cordin":
            candidate_4.append(candidate)

    candidate_1_percent = (len(candidate_1)/len(voter_id))*100
    candidate_2_percent = (len(candidate_2)/len(voter_id))*100
    candidate_3_percent = (len(candidate_3)/len(voter_id))*100
    candidate_4_percent = (len(candidate_4)/len(voter_id))*100

    Winner={"Vestal":len(candidate_1),"Torres":len(candidate_2),"Seth":len(candidate_3),"Cordin":len(candidate_4)}



    print("Election Results")
    print("---------------------------------")
    print("Total Votes: ", len(voter_id))
    print("---------------------------------")
    print("Vestal: ", candidate_1_percent,"% ","(", len(candidate_1),")")
    print("Torres: ",candidate_2_percent,"% ","(", len(candidate_2),")")
    print("Seth: ",candidate_3_percent,"% ","(", len(candidate_3),")")
    print("Cordin: ",candidate_4_percent,"% ","(", len(candidate_4),")")
    print("---------------------------------")
    print("Winner: ", max(Winner))


    text_path = os.path.join("raw_data","Election_Data_1.txt")
    with open(text_path, "w") as text_file:
        text_file.write("Election Results")
        text_file.write("---------------------------------")
        text_file.write("Total Votes: ", len(voter_id))
        text_file.write("---------------------------------")
        text_file.write("Vestal: ", candidate_1_percent,"% ","(", len(candidate_1),")")
        text_file.write("Torres: ",candidate_2_percent,"% ","(", len(candidate_2),")")
        text_file.write("Seth: ",candidate_3_percent,"% ","(", len(candidate_3),")")
        tex_file.write("Cordin: ",candidate_4_percent,"% ","(", len(candidate_4),")")
        text_file.write("---------------------------------")
        text_file.wriet("Winner: ", max(Winner))
