# import
import os
import csv

# csv file pulling and reading
csvfile = os.path.join("..", "PyBank", "budget_data.csv")

with open(csvfile, 'r') as bankfile:

    bank_reader = csv.reader(bankfile, delimiter=',')
    bank_header = next(bank_reader)

    months = []
    monthlyprofitloss = []
    totalprofitloss = 0
    greatestprofit = 0
    greatestloss = 0
        
    for row in bank_reader:
       
        months.append(row[0])
        totalprofitloss += int(row[1])
        monthlyprofitloss.append(int(row[1]))
        greatestprofit = max(monthlyprofitloss)
        greatestloss = min(monthlyprofitloss)

        if int(row[1]) == greatestprofit:
            greatestprofitmonth = row[0]

        if int(row[1]) == greatestloss:
            greatestlossmonth = row[0]
 
    averagechange = round(totalprofitloss/len(months), 2)
    
    print(f'Number of months: {len(months)}')    
    print(f'Net total of Profit/Losses: $ {totalprofitloss}')
    print(f'Average change in Profit/Losses: $ {averagechange}')
    print(f'The greatest increase in profits: {greatestprofitmonth} $ {greatestprofit}')
    print(f'The greatest decrease in losses: {greatestlossmonth} $ {greatestloss}')
        
with open("summary.txt", 'w') as summary:

    summary.write("Financial Analysis" "\n" "---------------------------------------" "\n")
    summary.write(f'Number of months: {len(months)}''\n')
    summary.write(f'Net total of Profit/Losses: $ {totalprofitloss}''\n')
    summary.write(f'Average change in Profit/Losses: $ {averagechange}''\n')
    summary.write(f'The greatest increase in profits: {greatestprofitmonth} $ {greatestprofit}''\n')
    summary.write(f'The greatest decrease in losses: {greatestlossmonth} $ {greatestloss}''\n')
