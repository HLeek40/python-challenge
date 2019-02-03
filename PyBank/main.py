#Instructions
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#As an example, your analysis should look similar to the one below:
#Total Months: 86
#Total: $38382578
#Average Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Dependencies
import csv
import os

#File to load
budget_data=os.path.join("..","pyBank","budget_data.csv")

# Open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header
    header= next(csvreader)
    
    #Define the variables and lists
    line_count=0
    PandL_count= 0
    prevval = 0
    revchglist = []
    skiplist = []
    finalmax = 0
    finalmin = 9999999
# Loop through data
    for row in csvreader:
        #get the line count
        line_count = line_count + 1
        #get the total count
        PandL_count = (int(row[1])) + PandL_count
        #Calculate the revenue change between current and next month
        revchg = int(row[1]) - prevval
        prevval = int(row[1])
        #Conditional to find the max row and date
        if revchg > finalmax:
            finalmax = revchg
            finaldate = row[0]
        #Conditional to find the min row and data
        if revchg < finalmin:
            finalmin = revchg
            finaldate2 = row[0]
        #Hold the values of the change in the list
        revchglist.append(revchg)

#Calculate the average of the revenue change
newvar = revchglist[1:]
avglist = round(sum(newvar)/len(newvar), 2)

#Print the output
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(line_count))
print("Total: $" + str(PandL_count))
print("Average Change: $" + str(avglist))
print("Greatest Increase in Profits: " + (finaldate) + ", " + "($" + str(finalmax) + ")")
print("Greatest Decrease in Profits: " + (finaldate2) + ", " + "($" + str(finalmin) + ")")

#set variable for output file
output_file = os.path.join("..","pyBank","pybank_output.txt")
