#This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

size = int(input("Enter the size of the pattern: "))

while size > 0:
    for i in range(size):
        print("*", end="")
    print()
    #if i == size:
    break;

