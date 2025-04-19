# Expense Tracker

## Overview
This project is a command-line expense tracker application written in Python, designed to help users manage their expenses and budget. It uses a list of dictionaries (`entries`) to store expense records (amount, category, description, payment method, and date), with a `update_total_budget` function to track the total budget, and `datetime` to automatically record entry dates.

## Features
- **Add Records**: Users can add an expense record by entering the amount, category (e.g., food, transport), description, payment method (e.g., cash, card), and the date is automatically recorded using `datetime`.
- **Delete Records**: Users can delete records by selecting the record number, which updates the total budget by subtracting the deleted amount.
- **View Records**: Users can display all expense records, showing details like amount, category, description, payment method, and formatted date (YYYY-MM-DD).
- **Edit Records**: Users can edit existing records (amount, category, description, payment method) through a submenu with an exit confirmation (`Y/N`).
- **Track Budget**: Maintains a running total budget, updated when adding or deleting records.
- **Exit with Confirmation**: Users can exit the application with a confirmation prompt (`Y/N`).

## Setup
1. **Prerequisites**:
   - Python 3.6 or later (uses `datetime` module, which is built-in)
2. **Clone the Repository**:

## Usage
1. **Run the Program**:
- Execute the script in your terminal or command prompt:
  ```
  python expense_tracker.py
  ```
2. **Interact with the Expense Tracker**:
- The program displays: `Expense Tracker` and the current `Total Budget`.
- It prompts: `Insert '1' to add a record, '2' to delete a record, '3' to show records, '4' to edit records, '5' to exit application:`
- **Add a Record**: Select `1`, then enter the amount (e.g., `50.00`), category (e.g., `food`), description (e.g., `lunch`), and payment method (e.g., `card`). The date is automatically added (e.g., `2023-10-01`), and the budget updates.
- **Delete a Record**: Select `2`, view the numbered records, and enter the number of the record to delete (e.g., `1`). The budget updates by subtracting the deleted amount.
- **Show Records**: Select `3` to view all records with details (e.g., amount, category, date).
- **Edit a Record**: Select `4`, choose a record by number, then edit its amount, category, description, or payment method via a submenu (options `1` to `4`). Select `5` to exit the edit menu with a `Y/N` confirmation.
- **Exit**: Select `5`, then confirm by typing `Y` (or `y`) to quit, or `N` (or `n`) to continue.
3. **View Screenshots**:
- Screenshots of the program in action (e.g., adding a record, editing a record) are in the `screenshots/` folder.

## File Structure
- `expense_tracker.py`: Python script containing the expense tracker application.
- `README.md`: This file.

## Limitations
- **Command-Line Only**: The application runs in the terminal with no graphical user interface (GUI).
- **Non-Persistent Storage**: Records are stored in memory and lost when the program exits (no file or database storage).
- **Basic Error Handling**: Handles invalid numeric inputs (e.g., for menu selection, deletion), but does not validate empty inputs for record fields (e.g., category, description).
- **Recursive Edit Function**: The `edit_record` function calls `main_app` directly on exit, which may cause recursion issues if not handled carefully (e.g., stack overflow with repeated exits).

## Future Improvements
- Add persistent storage (e.g., using JSON or a database) to save records between sessions.
- Validate empty inputs for record fields to improve user experience.
- Refactor the `edit_record` function to avoid recursion by returning to the main loop instead of calling `main_app`.
- Add a feature to filter records by category or date for better expense analysis.
