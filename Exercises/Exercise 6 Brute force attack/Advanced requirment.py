password = "password"#assigning the correct value
max_attempts = 5 #maxmimum allowed attempts is 5
attempts = 0 #attempt counter for number of inputted values
while attempts < max_attempts: #A loop is made until the correct value is entered
    user_password = input("Password: ").strip()#The displayed message asking for a password
    attempts += 1 #Attempts are added by 1 
    if user_password == password: #Comparing the input and correct value to determine if it is the correct value
        print("Welcome back, user") #a valid input will output this message
        break
    else:
        remaining_attempts = max_attempts - attempts #max attempts subtracted by each wrong attempt, to warn the user
        print(f"Incorrect passcode. You have {remaining_attempts} attempt(s) remaining.") #Warn the user that in the case of too many invalid inputs, a final warning will be issued
        if attempts == max_attempts: #In case user inputs an invalid code upon the threshold of attempts, a final warning is issued
            print("Too many invalid attempts, notifiying security. Please remain where you are.")