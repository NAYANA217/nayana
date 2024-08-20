# Expense Recording System

# Dictionary to store categories and their corresponding expenses
expenses = {}

def add_expense():
    """Function to add a new expense."""
    category = input("Enter the expense category (e.g., Food, Transport, Entertainment): ")
    amount = float(input("Enter the expense amount: "))
    
    if category in expenses:
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]
    
    print(f"Added {amount} to {category} category.")

def view_summary():
    """Function to view a summary of expenses."""
    print("\nExpense Summary:")
    total_expense = 0
    
    for category, amounts in expenses.items():
        category_total = sum(amounts)
        total_expense += category_total
        print(f"{category}: ${category_total:.2f}")
    
    print(f"\nTotal Expense: ${total_expense:.2f}\n")

def main():
    """Main function to run the Expense Recording System."""
    while True:
        print("Expense Recording System")
        print("1. Add a new expense")
        print("2. View summary of expenses")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    main()
