import os
import csv

#user_file= input('Enter the file (name.csv)')
Budget_data= os.path.join("raw_data","budget_data_1.csv")

with open(Budget_data,newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")

    next(reader)



    date_list=[]
    revenue_list=[]
    revenue_change_list=[]



    for row in reader:
        date_list.append(row[0])
        total_months= len(date_list)
        revenue_list.append(int(row[1]))
        total_revenue= sum(revenue_list)

        for x in range(1,len(revenue_list)):
            revenue_change_list.append(revenue_list[x]-revenue_list[x-1])
            greatest_increase= max(revenue_change_list)
            greatest_decrease= min(revenue_change_list)
            average_change= sum(revenue_change_list) / len(revenue_change_list)

        max_average_change_date = str(date_list[revenue_change_list.index(max(revenue_change_list))])
        min_average_change_date = str(date_list[revenue_change_list.index(min(revenue_change_list))])


    print("Total Months: ", total_months)
    print("Total Revenue: ","$", total_revenue)
    print("Average Revenue Change: ",max_average_change_date,"$",round(average_change))
    print("Greatest Increase in Revenue: ",min_average_change_date," $", greatest_increase)
    print("Greatest Decrease in Revenue: "," $", greatest_decrease)

    text_path = os.path.join("raw_data","Election_Data_1.txt")
    with open(text_path, "w") as text_file:
        text_file.write("Total Months: ", total_months)
        text_file.write("Total Revenue: ","$", total_revenue)
        text_file.write("Average Revenue Change: ",max_average_change_date,"$",round(average_change))
        text_file.write("Greatest Increase in Revenue: ",min_average_change_date," $", greatest_increase)
        text_file.write("Greatest Decrease in Revenue: "," $", greatest_decrease)
