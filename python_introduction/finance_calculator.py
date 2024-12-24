#a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

monthly_income = int(input("Enter your monthly income: "))
Expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = (monthly_income - Expenses)
print("Your monthly savings are $", monthly_savings)
#Interest_rate = int(0.05)
#time = 1 year = 12 months
Projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print("Projected savings after one year, with interest, is: $", Projected_savings)

