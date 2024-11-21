print("Counting up from 0 to 50:") #from 0 to 50, each number is counted up
for i in range(0, 51, 1):
    print(i)
print("\nCounting down from 50 to 0:") #from 50 to 0, each number is counted down
for i in range(50, -1, -1):
    print(i)
print("\nCounting up from 30 to 50:") #from 30 to 50, each number is counted up
for i in range(30, 51, 1):
    print(i)
print("\nCounting down from 50 to 10, skipping every other number:") #From 50 to 10, numbers are counted while skipping every other ones
for i in range(50, 9, -2):
    print(i)
print("\nCounting up from 100 to 200, adding 5 each time:") #from 100 to 200, each number is counted while adding 5 each time
for i in range(100, 201, 5):
    print(i)
