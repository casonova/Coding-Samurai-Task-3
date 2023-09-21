
# CLI Based Expense Tracker Application

expenses=[]

# Add Expense
class Expense:
    def __init__(self, date, amount, category, description):
        self.date=date
        self.amount = amount
        self.category = category
        self.description = description
def add_Expense():
    date=input("Enter date (YYYY-MM-DD): ")
    amount=float(input("Enter expense amount: "))
    category=input("Enter expense category: ")
    description = input("Enter a brief description: ")
    expenses.append(Expense(date, amount, category, description))
    print("Expense added")


# List Expenses

def list_expense():
    for expense in expenses:
        print(f"Date: {expense.date}, Amount: ${expense.amount:.2f}, Category: {expense.category}, Description: {expense.description}")        

# Expense Categorie

def total_expense():
    total=sum(expense.amount for expense in expenses)
    return total

def list_category():
    categories=set(expense.category for expense in expenses)   
    for category in categories:
        print(f"Category: {category}")  
    return categories       

def total_expense_category(category):
    total = sum(expense.amount for expense in expenses if expense.category == category)
    return total


# Monthly Report

def monthly_report(month,year):
    print(f"Monthly Report for {month} {year}: ")
    for category in list_category():
        total=total_expense_category(category)
        print(f"Category: {category}, Total Expenses: ${total:.2f}")

# Save Data

def save_data(filename):
    with open(filename,'w') as file:
        for expense in expenses:
            file.write(f"C{expense.date},{expense.amount},{expense.category},{expense.description}\n")  
    print("Data Saved")

# Load Data


def load_data(filename):
    expenses.clear()
    try:
        with open(filename,'r') as file:
            for line in file:
                date, amount, category, description = line.strip().split(',')
                expenses.append(Expense(date, float(amount), category, description))
        print("Data loaded.")
    except FileNotFoundError:
        print("No save data found")


filename = "expenses.txt"
load_data(filename)

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. List Categories")
    print("4. Calculate Total Expenses")
    print("5. Generate Monthly Report")
    print("6. Save Data")
    print("7. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_Expense()
    elif choice == '2':
        list_expense()
    elif choice == '3':
        list_category()
    elif choice == '4':
        total = total_expense()
        print(f"Total Expenses: ${total:.2f}")
    elif choice == '5':
        month = input("Enter the month (e.g., January): ")
        year = input("Enter the year (e.g., 2023): ")
        monthly_report(month, year)
    elif choice == '6':
        save_data(filename)
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")    