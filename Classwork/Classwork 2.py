salary=int(input("Enter your salary: "))
if salary>=30000:#connected to the last else condition
    years_on_job=float(input("Enter the years of job: "))
    if years_on_job>=2:
        print("You qualify for the job ")
    else:
        print("experience is less than 2")
else:print("You need to earn atleast 30k to qualify")#connected to the first if condition
#second example with different integers and conditions
salary=int(input("Enter your salary: "))
if salary>=40000:
    years_on_job=float(input("Enter the years of job: "))
    if years_on_job>=3:
        print("You qualify for the job ")
    else:
        print("experience is less than 3")
else:print("You need to earn atleast 40k to qualify")