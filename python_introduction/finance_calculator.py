#a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

monthly_income =  float(input("Enter your monthly income: "))
Expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - Expenses

print(f"Your monthly savings are ${monthly_savings:.2f}")
#Interest_rate = int(0.05)
#time = 1 year = 12 months

annual_savings = monthly_savings * 12
Projected_savings = float(annual_savings + (annual_savings * 0.05))
print(f"Projected savings after one year, with interest, is: ${Projected_savings:.2f}.")

