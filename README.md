# Personal-Expense-Tracker---Python-Project-
💰 Personal Expense Tracker

A lightweight, beginner-friendly command-line application built with pure Python to help individuals track, organize, and analyze personal expenses across different months.

Built with clean, modular programming principles (DRY), this project provides a solid foundation for beginners learning Python and a ready-to-fork base for open-source GitHub contributors.

🎯 Key Objectives
Record Expenses with Full Details: Capture essential expense data including amount, category/item, and date.
Calculate and Display Total Expenses: Automatically compute total expenditures to give immediate visibility into overall spending.
Categorise Spending: Group and summarize expenses so users clearly understand where their money is being spent.
Simple & Organized Tracking: Provide an intuitive, distraction-free command-line interface for day-to-day use.
Improve Financial Awareness: Help users actively monitor cash outflow and develop better budgeting habits.
Beginner-Friendly Foundation: Showcase core Python building blocks—lists, functions, loops, conditional statements, and file I/O—in an accessible, clean codebase.
🏗️ Architectural Approach

The application is structured around a predictable, step-by-step workflow:

User Input: The user selects a target month and enters the expense item and amount.
Input Validation: Validates the month format, positive numeric values for amounts, and valid menu choices to minimize entry errors.
Data Processing: Checks whether an entered item already exists for the selected period and updates its values accordingly.
Persistent Storage: Uses CSV files to persist records so data is safely retained even after closing the program.
Expense Retrieval: Allows users to select and review recorded expenses from any previously saved month.
Automatic Analysis: Automatically aggregates and displays monthly totals and breakdown summaries.
Modular Design (DRY Principle): Core operations are isolated into reusable functions like load_data() and save_data(), keeping the codebase organized and easy to maintain.
