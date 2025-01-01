#This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        
        if time == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        
        else:
            print(f"Reminder: '{task}' is a high priority task, but does not require immediate attention today!")
    
    case "medium":
        if time == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
             print(f"Reminder: '{task}' is a medium priority task, but does not require immediate attention today!")
    case "low":
        if time == "yes":
            print(f"Reminder: '{task}' is a low priority task, that requires immediate attention today!")
        else:
            print(f"Note:'{task}'is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"'{task}' has unspecified priority")
