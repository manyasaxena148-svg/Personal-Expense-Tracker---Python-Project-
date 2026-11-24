# Personal Expense Tracker - Main Application
# Uses basic Python concepts: lists, dictionaries, functions, loops, and conditionals

import csv
import os
from datetime import datetime

# 1. Create required files
def create_files():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, "w") as file:
            file.write("0")





# 2. Read all expenses
def get_expenses():
    expenses = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append(row)

    return expenses


# 3. Add a new expense
def add_expense():
    try:
        date = input("Enter date (DD-MM-YYYY): ")
        datetime.strptime(date, "%d-%m-%Y")

        category = input("Enter category (Food/Travel/Shopping/Other): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])

        print("\nExpense added successfully!")

        check_budget()

    except ValueError:
        print("Invalid input! Please enter a valid date and amount.")


# 4. View all expenses
def view_expenses():
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n========== ALL EXPENSES ==========")

    for expense in expenses:
        print(
            f"Date: {expense['Date']} | "
            f"Category: {expense['Category']} | "
            f"Description: {expense['Description']} | "
            f"Amount: Rs. {float(expense['Amount']):.2f}"
        )


# 5. Calculate total expenses
def total_expenses():
    expenses = get_expenses()
    total = 0

    for expense in expenses:
        total += float(expense["Amount"])

    print(f"\nTotal Expenses: Rs. {total:.2f}")


# 6. Category-wise spending summary

def category_summary():

    categories = {}

    for expense in get_expenses():

        category = expense["Category"]
        amount = float(expense["Amount"])

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    if not categories:
        print(YELLOW + "\nNo expenses recorded yet." + RESET)
        return

    print(CYAN + "\n========== CATEGORY SUMMARY ==========" + RESET)

    for category, amount in categories.items():
        print(f"{category}: Rs. {amount:.2f}")


# 7. Search expenses by category
def search_expenses():
    category = input("Enter category to search: ").lower()
    found = False

    expenses = get_expenses()

    print("\n========== SEARCH RESULTS ==========")

    for expense in expenses:
        if expense["Category"].lower() == category:
            print(expense)
            found = True

    if not found:
        print("No expenses found in this category.")


# 8. Monthly expense summary
def monthly_summary():
    month = input("Enter month (MM-YYYY): ")

    try:
        datetime.strptime(month, "%m-%Y")
    except ValueError:
        print("Invalid month format!")
        return

    expenses = get_expenses()
    total = 0

    print("\n========== MONTHLY SUMMARY ==========")

    for expense in expenses:
        expense_month = expense["Date"][3:]

        if expense_month == month:
            amount = float(expense["Amount"])
            total += amount

            print(
                f"{expense['Date']} | "
                f"{expense['Category']} | "
                f"Rs. {amount:.2f}"
            )

    print(f"\nTotal for {month}: Rs. {total:.2f}")


# 9. Find highest expense
def highest_expense():
    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    highest = max(expenses, key=lambda x: float(x["Amount"]))

    print("\n========== HIGHEST EXPENSE ==========")
    print(f"Date: {highest['Date']}")
    print(f"Category: {highest['Category']}")
    print(f"Description: {highest['Description']}")
    print(f"Amount: Rs. {float(highest['Amount']):.2f}")


# 10. Set monthly budget
def set_budget():
    try:
        budget = float(input("Enter your monthly budget: "))

        if budget <= 0:
            print("Budget must be greater than zero.")
            return

        with open(BUDGET_FILE, "w") as file:
            file.write(str(budget))

        print(f"Monthly budget set to Rs. {budget:.2f}")

    except ValueError:
        print("Please enter a valid budget amount.")


# 11. Check budget status
def check_budget():
    with open(BUDGET_FILE, "r") as file:
        budget = float(file.read())

    if budget == 0:
        return

    current_month = datetime.now().strftime("%m-%Y")
    total = 0

    for expense in get_expenses():
        if expense["Date"][3:] == current_month:
            total += float(expense["Amount"])

    print(f"\nMonthly spending: Rs. {total:.2f}")
    print(f"Monthly budget: Rs. {budget:.2f}")

    if total > budget:
        print("WARNING! You have exceeded your monthly budget.")
    elif total == budget:
        print("You have reached your monthly budget.")
    else:
        print(f"Remaining budget: Rs. {budget - total:.2f}")


# 12. Main menu
def main():
    create_files()

    while True:
        print("\n========== PERSONAL EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Search Expenses by Category")
        print("5. Category-wise Spending Summary")
        print("6. Monthly Expense Summary")
        print("7. Find Highest Expense")
        print("8. Set Monthly Budget")
        print("9. Check Budget Status")
        print("10. Exit")

        choice = input("\nEnter your choice (1-10): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            search_expenses()
        elif choice == "5":
            category_summary()
        elif choice == "6":
            monthly_summary()
        elif choice == "7":
            highest_expense()
        elif choice == "8":
            set_budget()
        elif choice == "9":
            check_budget()
        elif choice == "10":
            print("\nThank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice! Please select between 1 and 10.")


if __name__ == "__main__":
    main()
#SAWAN CHOUDHARY

def search_by_category(expenses):

    print("--- Search by Category ---")

    search = input("Enter category: ")

    found = False

    for expense in expenses:

        if expense["category"].lower() == search.lower():

            print(expense)
            found = True

    if found == False:
        print("No expenses found")


def search_by_date(expenses):

    print("--- Search by Date ---")

    search_date = input("Enter date: ")

    found = False

    for expense in expenses:

        if expense["date"] == search_date:

            print(expense)
            found = True

    if found == False:
        print("No expenses found")


from csv_storage import save_expense

def add_expense(expenses):

    print("--- Add Expense ---")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Invalid amount")
            return

    except ValueError:
        print("Invalid amount")
        return

    category = input("Enter category: ")
    date = input("Enter date: ")

    expense = {
        "Amount": amount,
        "Category": category,
        "Date": date
    }

    expenses.append(expense)
    save_expense(expense)

    print("Expense added!")

#kavya's part
def total_expenses():

    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses available!")
        return

    total = 0

    for expense in expenses:
        amount = float(expense["Amount"])
        total += amount

    print("\n========== TOTAL EXPENSES ==========")
    print(f"Total Number of Expenses: {len(expenses)}")
    print(f"Total Amount Spent: ₹{total:.2f}")
    print("====================================")

# Manya's part 

import csv
import os

FILE_NAME = "expenses.csv"


def initialize_file():

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["amount", "category", "date"])


def save_expense(expense):

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            expense["amount"],
            expense["category"],
            expense["date"]
        ])


def read_expenses():

    expenses = []

    if not os.path.exists(FILE_NAME):
        initialize_file()
        return expenses

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            expenses.append(row)

    return expenses
import csv
import os

FILE_NAME = "expenses.csv"


def get_expenses():

    expenses = []

    if not os.path.exists(FILE_NAME):
        return expenses

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if not row:
                continue

            date = (row.get("Date") or "").strip()
            category = (row.get("Category") or "").strip()
            amount = (row.get("Amount") or "").strip()

            if not date or not category or not amount:
                continue

            try:
                float(amount)
            except ValueError:
                continue

            expenses.append({
                "Date": date,
                "Category": category,
                "Amount": amount
            })

    return expenses


def category_summary():

    categories = {}

    expenses = get_expenses()

    for expense in expenses:

        category = expense.get("category")
        amount = expense.get("amount", 0)

        if category is None:
            continue

        try:
            amount = float(amount)
        except (ValueError, TypeError):
            print("Invalid expense amount:", amount)
            continue

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    if not categories:
        print(YELLOW + "\nNo expenses recorded yet." + RESET)
        return

    print(CYAN + "\n========== CATEGORY SUMMARY ==========" + RESET)

    for category, amount in categories.items():
        print(f"{category}: Rs. {amount:.2f}")


def view_expenses():

    expenses = get_expenses()

    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n========== ALL EXPENSES ==========")

    for expense in expenses:

        print(
            f"Date: {expense['Date']} | "
            f"Category: {expense['Category']} | "
            f"Amount: Rs. {float(expense['Amount']):.2f}"
        )


if __name__ == "__main__":
    view_expenses()

