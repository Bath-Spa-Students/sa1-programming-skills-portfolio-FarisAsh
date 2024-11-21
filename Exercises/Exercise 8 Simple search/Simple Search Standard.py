names = ["Faris", "Cyrus", "Steven", "Fardeen", "Omer", "Alaa"] #Defined names in a list
search = input("Please enter the name you want to search for: ").strip() #asking user to search for a name, .strip() for removing blank spaces
found = False #a flag for checking if the name exists in the list
for name in names: #loop command so that it goes through the list until the name is found    
    if name.lower() == search.lower(): #for removing any case sensitivity        
        found = True #if a name is found, found = true and inform the user with success
        print(f"Success, the name, '{search}' does exist in the list.")
        break  #break loop and end interaction
if not found: 
    print(f"Invalid entry, '{search}' does not exist in the list.")
#if loop completes and name is still not found, inform user with an error