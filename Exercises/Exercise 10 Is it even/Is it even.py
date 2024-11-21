def check_even_odd(number): #checking if the number is odd   
    if number % 2 == 0: #detected by whether the value is divisible by 2
        return f"{number} is even."
    else:
        #else, value is odd
        return f"{number} is odd."
def main(): #checking if the number is even or odd   
    try: #prompting user for a number
        user_number = int(input("Enter a number: "))       
        result_message = check_even_odd(user_number) #Calling the "check_even_odd" function and getting the output        
        print(result_message) #output the result
    except ValueError: #in case of a non-integer value, display an erorr message
        print("Invalid input. Only integers are allowed.")
if __name__ == "__main__": #run the main function if the script is ran directly from there
    main()