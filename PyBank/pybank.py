import os
import csv

#user_file= input('Enter the file (name.csv)')
Budget_data= os.path.join("raw_data","budget_data_2.csv")

with open(Budget_data,newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")

    next(reader)



    date_list=[]
    revenue_list=[]
    revenue_change_list=[]
    max_month = ""
    min_month = ""


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
            if(revenue_list[x]-revenue_list[x-1] == greatest_increase):
                max_month = date_list[x-1]
            if(revenue_list[x]-revenue_list[x-1] == greatest_decrease):
                min_month = date_list[x-1]





    print("Total Months: ", total_months)
    print("Total Revenue: ","$", total_revenue)
    print("Average Revenue Change: ","$",round(average_change))
    print("Greatest Increase in Revenue: ",max_month," $", greatest_increase)
    print("Greatest Decrease in Revenue: ",min_month," $", greatest_decrease)

    text_path = os.path.join('.','budget_data_2.txt')
with open(text_path, "w") as text_file:
   text_file.write("Financial Analysis")
   text_file.write("---------------------------------")
   text_file.write("Total Months: " + str(total_months))
   text_file.write("Total Revenue: $" + str(total_revenue))
   text_file.write("Average Revenue Change: +""$" + str(round(average_change)))
   text_file.write("Greatest Increase in Revenue: " + str(max_month)+" $" + str(max_month))
   text_file.write("Greatest Decrease in Revenue: " + str(min_month)+" $" + str(min_month))
