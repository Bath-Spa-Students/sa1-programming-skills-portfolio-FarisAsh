password = "password" #Assigning a correct value
max_attempts = 3 #maximum allowed attempts
attempts = 0 #Counter for attempts made by the user
while attempts < max_attempts: #a loop is made for until the correct value is entered or too many attempts are made    
    user_password = input("Password: ").strip() #prompt the user for password
    masked_password = '*' * len(user_password)   #masking the entered values for privacy   
    attempts += 1 #attempt counter increases after incorrect values are entered by the user
    if user_password == password: #matching the entered value with the correct one        
        print("Access granted. Welcome") #if it matches, the user is allowed to enter, break loop to end interaction
        break
    else:
        print(f"Incorrect password: {masked_password}") #incorrect value is unmasked and displayed along with an error message       
        if attempts == max_attempts - 1: #hint for the password if user has reached certain attempts
            print("Hint: The password is a word that passes.")            
        if attempts == max_attempts: #upon too many incorrect values entered, lock out the user
            print("Access Denied. Too many incorrect attempts")