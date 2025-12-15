def show_menu(welcome_text, menu):
    print(welcome_text)
    print()
    print("Menu:")
    for number, item in enumerate(menu, 1):
        print(f"{number}. {item}")


def get_int_choice(prompt="Enter your choice (1-5): "):
    while True:
        user_input = input(prompt)
        try:
            choice = int(user_input)
            return choice
        except ValueError:
            print("Please enter a whole number (e.g., 1, 2, 3, 4, 5).")


def get_float_amount(prompt="Enter expense amount: "):
    while True:
        user_input = input(prompt)
        try:
            amount = float(user_input)
            return amount
        except ValueError:
            print("Please enter a number (e.g., 100 or 46.2).")


def add_expense(expenses):
    amount = get_float_amount("Enter expense amount: ")
    expenses.append(amount)
    print("Expense added successfully!")


def show_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
    else:
        print("Your expenses:")
        for number, value in enumerate(expenses, 1):
            print(f"{number}. {value}")


def average_expense(expenses):
    if len(expenses) == 0:
        print("No expenses recorded yet.")
    else:
        total = sum(expenses)
        average = total / len(expenses)
        print(f"Total expense: {total}")
        print(f"Average expense: {average}")


menu = [
    "Add a new expense",
    "View all expenses",
    "Calculate total and average expense",
    "Clear all expenses",
    "Exit"
]

show_menu("Welcome to the Daily Expense Tracker!", menu)

expenses = []

while True:
    choice = get_int_choice("Enter your choice (1-5): ")

    if choice == 1:
        add_expense(expenses)
    elif choice == 2:
        show_expenses(expenses)
    elif choice == 3:
        average_expense(expenses)
    elif choice == 4:
        expenses.clear()
        print("All expenses cleared.")
    elif choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
