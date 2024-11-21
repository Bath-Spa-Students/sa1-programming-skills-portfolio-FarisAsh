dictionary = {'Name' : 'Faris',#assigning keys and values to the dictionary
              'Roll No' : '1234',
              'Fathers Name' : 'Ashfaq Ahmed'}
print(dictionary.get("Name"))#Accessing a specific variable from the dictionary

def print_alert():#giving a definition to "print_alert"
    alert = "Warning, students have entered the building" #the alert is printed first
    print(alert)
    print_alert()