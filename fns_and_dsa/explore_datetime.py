#This script performs specified operations with date and time using the datetime module

from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time""" 
    current_date = datetime.now()
    print("Current date and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))
display_current_datetime()
    

def calculate_future_date ():
    """Calcuates the future date with the user's input"""
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    print("Future date: ", future_date.strftime("%Y-%m-%d"))
calculate_future_date ()


