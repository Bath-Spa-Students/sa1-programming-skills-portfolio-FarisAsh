# Instructions:
#1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#2. Input Handling: Ask the user to input the month number.
#3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
days_in_month = {
    1: 31,   #January
    2: 28,   #February, leap ver
    3: 31,   #March
    4: 30,   #April
    5: 31,   #May
    6: 30,   #June
    7: 31,   #July
    8: 31,   #August
    9: 30,   #September
    10: 31,  #October
    11: 30,  #November
    12: 31   #December
}
try: #inserting a value that represents a month, with a strip command for empty spaces
    month_days = int(input("Please enter a month number (1-12): ").strip())
    if month_days in days_in_month: #confirming the input is valid
        #output the number of days in the inserted month value
        print(f"The number of days in {month_days} is {days_in_month[month_days]}.")
    else:
        #output an error for a range higher than 1-12
        print("Invalid input, it is not a valid month number, it must be a value between 1-12.")

except ValueError:
    #output an error message for the wrong input
    print("Invalid input, it must be a numberical value between 1-12")