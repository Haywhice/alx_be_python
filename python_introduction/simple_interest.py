#Basic Python arithmetic operations and variable assignments to calculate the simple interest on a given principal amount, rate of interest, and time.

principal = int(1000) #$1000
rate = float(0.05) #5% annual interest rate
time = int(3) #3 years

#(I = P * R * T)
interest = float(principal * rate * time)
print("The simple interest is: ", interest)
