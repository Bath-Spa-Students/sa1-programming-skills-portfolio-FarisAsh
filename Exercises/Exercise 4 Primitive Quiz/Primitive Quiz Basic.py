#Steps:
#1. Write a program that asks the user "What is the capital of France?" and waits for their response.
#2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
#3. If the answer is incorrect, the program should print a message saying the answer is wrong.
Capital = input("What is the Capital of France? ") #asking for an input for the capital
if Capital == "Paris":
    print("Answer is correct")
else:
    print("Answer is incorrect")