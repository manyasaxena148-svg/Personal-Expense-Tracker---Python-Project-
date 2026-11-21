# Personal Expense Tracker - Main Application
# Uses basic Python concepts: lists, dictionaries, functions, loops, and conditionals

import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# Add a new expense
def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Shopping/Other): ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])

        print("\nExpense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter a number.")


# View all expenses
def view_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        expenses = list(reader)

    if len(expenses) <= 1:
        print("\nNo expenses recorded yet.")
        return

    print("\n========== ALL EXPENSES ==========")

    for expense in expenses:
        print(
            f"Date: {expense[0]} | "
            f"Category: {expense[1]} | "
            f"Description: {expense[2]} | "
            f"Amount: Rs. {expense[3]}"
        )


# Calculate total expenses
def total_expenses():
    total = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expenses: Rs. {total:.2f}")


# Search expenses by category
def search_expenses():
    category = input("Enter category to search: ").lower()
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n========== SEARCH RESULTS ==========")

        for row in reader:
            if row["Category"].lower() == category:
                print(row)
                found = True

    if not found:
        print("No expenses found in this category.")


# Main menu
def main():
    create_file()

    while True:
        print("\n========== PERSONAL EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Search Expenses by Category")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            search_expenses()

        elif choice == "5":
            print("\nThank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select between 1 and 5.")


if __name__ == "__main__":
    main()
