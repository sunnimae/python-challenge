import os
import csv

#locate path to file
pybank_csv = os.path.join("..","Resources","budget_data.csv")

#open and read file
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

#skip reading header
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

#intialize list
    profit = []
    change_profit = []
    data_month = []
   
   #start counting month
    month = 0
   
   #loop through month each row in data
    for row in csv_reader:
        #to count month
        month = month + 1
        #to create a list of profit
        profit.append(int(row[1]))
        #to create total
        total = sum(profit)
        #to create list of month
        data_month.append(row[0])

    #start creating a list of change profit:
    #loop through the profit data
    for i in range(len(profit) - 1):
       
        #find change of profit
        profit_1 = profit[i]
        profit_2 = profit[i + 1]
        change = profit_2 - profit_1
        
        #create a list of profit change
        change_profit.append(change)

        #find average in profit change
        total_change = sum(change_profit)
        average_change = round((total_change/(month-1)),2)
        
        #find highest change and the corresponding month
        maximum = max(change_profit)
        max_index = change_profit.index(maximum)
        best_month = data_month[max_index+1]

        #find the lowest change and the corresponding month
        minimum = min(change_profit)
        min_index = change_profit.index(minimum)
        worst_month = data_month[min_index+1]

      
print(f"\nFinancial Analysis")
print("-------------------------------------------------------------")
print(f"Total Months: {month}")
print(f"Net Profit: {total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {best_month} {maximum}")
print(f"Greatest Decrease in Profits: {worst_month} {minimum}")

   