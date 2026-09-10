import json

expenses = []

def add_expense():
    print("==========================")
    print("ADD EXPENSE")
    print("==========================")
    print()

    try:
        while True:
            category = input("what Category: ").strip().title()
            if category == "":
                print("Invalid input")
            else:
                break
        while True:
            amount = int(input("How much: "))

            if amount > 0:
                break
            else:
                print("input a valid number")

        while True:
            description = input("what for: ").strip().title()
            if description == "":
                print("Invalid input")
            else:
                break

    except ValueError:
        print("Invalid input")
        return


    expense = {
        "category": category,
        "amount": amount,
        "description": description
    }


    expenses.append(expense)
    save_expenses()


    print("\nExpense added successfully!\n")



def view_expenses():
    if len(expenses) == 0:
        print("\nNO EXPENSES RECORDED YET")
        return
    
    print("\n==========================")
    print(" ALL EXPENSES")
    print("==========================")

    for index, expense in enumerate(expenses, start=1):
        print(
        f"{index}. {expense['category']} - "
        f"#{expense['amount']} - "
        f"{expense['description']}"
    )



def calculate_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total





def calculate_by_category():
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals







def delete_expense():
    if len(expenses) == 0:
        print("NO EXPENSES TO DELETE")
        return
    
    view_expenses()
    try: 
        delete = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Invalid input")
        return

    if delete < 1 or delete > len(expenses):
        print("Invalid expense number")
        return
    
    index = delete - 1
    expenses.pop(index)
    save_expenses()

    print("Expense deleted successfully!")   


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file,indent=2)



def load_expenses():
    try: 
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError :
        return []
    except json.JSONDecodeError:
        return[]
    
expenses = load_expenses()
#print(expenses)

def show_menu():
    print("\n==========================")
    print("EXPENSE TRACKER")
    print("==========================")

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Spending by Category")
    print("5. Delete Expense")
    print("6. exit")

while True:
    show_menu()
    
    choice = input("Enter your Choice: ").strip()

    if choice == "1":
        print("Add Expense")
        add_expense()

    elif choice == "2":
        print("View Expense")
        view_expenses()

    elif choice == "3":
        print("view Total Spending")
        total = calculate_total()
        print(f"Total spending: #{total}")

    elif choice == "4":
        print("Spending by category")
        category_totals = calculate_by_category()

        for category, total in category_totals.items():
            print(f"{category}: #{total}")

        
    elif choice == "5":
        print("Delete Expense")
        delete_expense()

    elif choice == "6":
        save_expenses()
        print("Goodbye")
        break

    else:
        print("Invalid Choice")
