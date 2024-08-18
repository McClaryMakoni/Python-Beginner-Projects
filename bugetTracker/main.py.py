import json  # Import the JSON module to handle JSON file operations


# Function to add an expense to the expenses list
def add_expense(expenses: list, description: str, amount: float) -> None:
    """
    Adds an expense to the expenses list.

    Parameters:
    expenses (list): The list of current expenses.
    description (str): The description of the expense.
    amount (float): The amount of the expense.
    """
    expenses.append({"description": description, "amount": amount})  # Add a new expense to the list
    print(f"Added expense: {description}, Amount: {amount}")  # Print a confirmation message


# Function to get the total of all expenses
def get_total_expenses(expenses: list) -> float:
    """
    Calculates the total amount of all expenses.

    Parameters:
    expenses (list): The list of current expenses.

    Returns:
    float: The total amount of expenses.
    """
    return sum(expense['amount'] for expense in expenses)  # Sum up all the amounts in the expenses list


# Function to get the remaining budget after expenses
def get_balance(budget: float, expenses: list) -> float:
    """
    Calculates the remaining budget after subtracting expenses.

    Parameters:
    budget (float): The initial budget.
    expenses (list): The list of current expenses.

    Returns:
    float: The remaining budget.
    """
    return budget - get_total_expenses(expenses)  # Subtract total expenses from the budget


# Function to display the budget details
def show_budget_details(budget: float, expenses: list) -> None:
    """
    Prints the details of the budget, including expenses and remaining budget.

    Parameters:
    budget (float): The initial budget.
    expenses (list): The list of current expenses.
    """
    print(f"Total Budget: {budget}")  # Print the initial budget
    print("Expenses:")  # Print a header for the expenses list
    for expense in expenses:
        print(f"- {expense['description']}: {expense['amount']}")  # Print each expense description and amount
    print(f"Total Spent: {get_total_expenses(expenses)}")  # Print the total amount spent
    print(f"Remaining Budget: {get_balance(budget, expenses)}")  # Print the remaining budget


# Function to load budget data from a JSON file
def load_budget_data(filepath: str) -> tuple:
    """
    Loads budget data from a JSON file.

    Parameters:
    filepath (str): The path to the JSON file.

    Returns:
    tuple: A tuple containing the initial budget and the expenses list.
    """
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)  # Load the JSON data from the file
            return data['initial_budget'], data['expenses']  # Return the initial budget and expenses list
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  # Return default values if the file doesn't exist or is empty/corrupted


# Function to save budget data to a JSON file
def save_budget_data(filepath: str, initial_budget: float, expenses: list) -> None:
    """
    Saves budget data to a JSON file.

    Parameters:
    filepath (str): The path to the JSON file.
    initial_budget (float): The initial budget.
    expenses (list): The list of current expenses.
    """
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)  # Save the data to the file in JSON format


# Main function to run the budget app
def main() -> None:
    """
    Main function to run the budget application.
    """
    print("Welcome to the Budget App")  # Print a welcome message
    #initial_budget = float(input("Please enter your initial budget: "))  # Prompt the user to enter the initial budget
    filepath = r'C:\Users\User\Documents\budget\budget_data.json'  # Define the path to your JSON file
    initial_budget, expenses = load_budget_data(filepath)
    budget = initial_budget  # Set the initial budget
    #expenses = []  # Initialize an empty list to store expenses

    while True:
        print("\nWhat would you like to do?")  # Print a prompt for the user's next action
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")  # Get the user's choice

        if choice == "1":
            description = input("Enter expense description: ")  # Prompt the user to enter the expense description
            amount = float(input("Enter expense amount: "))  # Prompt the user to enter the expense amount
            add_expense(expenses, description, amount)  # Add the expense to the list
        elif choice == "2":
            show_budget_details(budget, expenses)  # Show the budget details
        elif choice == "3":
            print("Exiting Budget App. Goodbye!")  # Print a goodbye message
            save_budget_data(filepath=filepath, initial_budget=budget, expenses=expenses)
            break  # Exit the loop and end the program
        else:
            print("Invalid choice, please choose again.")  # Print an error message for invalid choices


# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()  # Run the main function
