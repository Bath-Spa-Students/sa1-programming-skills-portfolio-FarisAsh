names = ["Faris", "Cyrus", "Steven", "Fardeen", "Omer", "Alaa"] #defined list of names
search = input("Enter the name of who you're looking for: ").strip() #asking user to search for a name, .strip() for removing blank spaces
if search.lower() in [name.lower() for name in names]: #Checking for the name in the list, ignoring case sensitive requirements
    print(f"Success. '{search}' is in the list.") #if name is found, output a message for success
else:   
    print(f" The name, '{search}' does not exist in the list.") #if name is not found, output a message for failure
