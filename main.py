# Personal Expense Tracker - Main Application
# Uses basic Python concepts: lists, dictionaries, functions, loops, and conditionals

expenses = []


def add_expense():
    """Record a new expense with amount, category, and date."""
    print("\n--- Add New Expense ---")
    try:
        amount = float(input("Enter amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    category = input("Enter category (Food, Travel, Bills, Shopping, Other): ").strip().title()
    if not category:
        category = "Other"

    date = input("Enter date (DD-MM-YYYY): ").strip()
    if not date:
        date = "Not Specified"

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }
    expenses.append(expense)
    print(f"Success! Recorded ₹{amount:.2f} under '{category}' on {date}.")


def view_expenses():
    """Teammate 1: Display all recorded expenses in a clean format."""
    print("\n[Pending] View All Expenses feature will be added by Teammate 1.")


def calculate_total():
    """Teammate 2: Calculate and display total expenses."""
    print("\n[Pending] Total Expense Calculation will be added by Teammate 2.")


def category_summary():
    """Teammate 3: Categorise spending and show total per category."""
    print("\n[Pending] Category-wise Spending Summary will be added by Teammate 3.")


def main_menu():
    """Main application loop."""
    while True:
        print("\n====================================")
        print("     PERSONAL EXPENSE TRACKER")
        print("====================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Category-wise Spending Summary")
        print("5. Exit")
        print("====================================")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("\nThank you for using Personal Expense Tracker. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main_menu()
