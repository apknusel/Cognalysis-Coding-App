file = open("input.txt","r")
fileLines = file.readlines()

# Prints out header for policies
print("{:15}{:15}{:15}".format("policyNumber","monthEarned","amountEarned"))
# Iterates through
for line in fileLines:
    line.replace("\n","")
    # Extracts information for each policy
    policyNum, startDate, endDate, premiumAmt = line.split(",")
    startMonth, startDay, startYear = startDate.split("/")
    endMonth, endDay, endYear = endDate.split("/")
    # Converts strings to ints
    startYear, startMonth, startDay = int(startYear), int(startMonth), int(startDay)
    endYear, endMonth, endDay = int(endYear), int(endMonth), int(endDay)
    premiumAmt = int(premiumAmt)
    # Calculates number of days in the given time span and the dailyEarnings
    numOfDays = (endYear-startYear)*365 + (endMonth-startMonth)*365/12 + (endDay-startDay)
    dailyEarning = premiumAmt/numOfDays
    # Algorithm to determine how many times to loop
    numLoops = (endYear-startYear)*12 + (endMonth-startMonth)
    # List of number of days in each month
    numOfDaysList = [31,28,31,30,31,30,31,31,30,31,30,31]

    # Loops through each month
    for i in range(startMonth,startMonth+numLoops+1):
        # Sets the correct monthly pay accounting for edge cases
        if i == startMonth:
            monthlyPay = (numOfDaysList[i-1]-startDay+1)*dailyEarning
        elif i == startMonth+numLoops:
            monthlyPay = endDay*dailyEarning
        else:
            monthlyPay = dailyEarning*numOfDaysList[i%12-1]
        # Makes string of the date
        date = str(startYear+((i-1)//12))+" "+str((i-1)%12+1)
        # Formats all of the data
        print("{:15}{:15}${:.2f}".format(policyNum,date,monthlyPay))
    print("")

file.close()