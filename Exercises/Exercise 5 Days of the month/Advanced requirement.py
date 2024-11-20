#A dictionary that links each month number (1-12) to the number of days in that month for a non-leap year
days_in_month = { 
    1: 31,   #giving january (1) the value of 31 because it has 31 days
    2: 28,   #giving february (2) the value of 31 because it has 28 days, in a non-leap year
    3: 31,   #giving march (3) the value of 31 because it has 31 days
    4: 30,   #giving april (4) the value of 31 because it has 30 days
    5: 31,   #giving may (5) the value of 31 because it has 31 days
    6: 30,   #giving june (6) the value of 31 because it has 30 days
    7: 31,   #giving july (7) the value of 31 because it has 31 days
    8: 31,   #giving august (8) the value of 31 because it has 31 days
    9: 30,   #giving september (9) the value of 31 because it has 30 days
    10: 31,  #giving october (10) the value of 31 because it has 31 days
    11: 30,  #giving november (11) the value of 31 because it has 30 days
    12: 31   #giving december (12) the value of 31 because it has 31 days
}
try: #User inputs any month from 1-12
    month_number = int(input("Please enter the month number (1-12): ").strip())  #.strip() is sued to remove spaces
    
    if 1 <= month_number <= 12: #used to check if the input matches one of the 12 months
        if month_number == 2:
            leap = input("Is it a leap year (yes or no)?: ").strip().lower()#Input from user, clarifying if its a lep year so that the value of february is changed
            days = 29 if leap == "yes" else 28#changing february to have a different day count
        else:            
            days = days_in_month[month_number]                
        print(f"Number of days in {month_number} is {days}.")#The output for the day count of the specified month is shown
    else:
        print("Invalid value, use months in their number format only (1-12)")#Show an error for the user not typing in the correct value
except ValueError:
    print("Invalid entry, any number indicating a month from 1-12 should be used")#An error code is displayed if a value that isnt a number is inputted by the user
