# A function that performs basic arithmetic operations.

def perform_operation(num1, num2, operation):
    """Executes additon, subtraction, multiplication and division operation"""

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 != 0:
             return num1 / num2
        else:
            return "ZeroDivisionError"

