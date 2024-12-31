# This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using a Match Case statement and display the result.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").lower()

match operation:
    case "+":
        addition = num1 + num2
        print("The result is ", addition)
    case "-":
        subtraction = num1 - num2
        print("The result is ", subtraction)
    case "*":
        multiplication = num1 * num2
        print("The result is ", multiplication)
    case "/":
        Division = num1 / num2
        print("The result is ", Division)
    case _:
        #result = num1 / num2
        if num2 <= 0:
            print("Cannot divide by zero")
