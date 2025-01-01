#This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

size = int(input("Enter the size of the pattern: "))
# Initialize row counter for the while loop
row = 0
while row < size:
    for i in range(size):
        print("*", end="")
    print() 
    row += 1

