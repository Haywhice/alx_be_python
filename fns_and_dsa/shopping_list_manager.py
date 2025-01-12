#A python script that implements a simple interface for managing a shopping list. This task focuses on using lists to store and manipulate data dynamically

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter an item: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter an item: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list")
            else:
                print(f"'{item}' is not in the shopping list")
            pass
        elif choice == '3':
            # Display the shopping list
            for i in shopping_list:
                print(i)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
