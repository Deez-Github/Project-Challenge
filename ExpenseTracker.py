import json

import subprocess
import platform

expenses = []
def clear_terminal():
    if platform.system()== "Windows":
        command = "cls"
    else:
        command = "clear"

    subprocess.run(command, shell=True)

def add_expense():
    print("==========================")
    print("ADD EXPENSE")
    print("==========================")
    print()

    try:
        while True:
            item = input("What did you buy: ").strip().title()
            if item == "":
                print("Please add the item")
            else:
                break
        while True:
            category = input("what Category: ").strip().title()
            if category == "":
                print("Invalid input")
            else:
                break
        while True:
            amount = float(input("How much: "))

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
        "item" : item,
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
        f"{index}. {expense['item']} - "
        f"{expense['category']} - "
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
    deleted_expenses = expenses.pop(index)
    save_expenses()

    print(
        f"The following expense {deleted_expenses["category"]} "
        f"for {deleted_expenses["description"]} was deleted successfully!"
    )   



def edit_expense():
    print("\n==========================")
    print(" EDIT EXPENSES")
    print("==========================")

    if len(expenses) == 0:
            print("NO EXPENSES TO DELETE")
            return
        
    view_expenses()
    try: 
        edit = int(input("Enter expense number to edit: "))

        if edit < 1 or edit > len(expenses):
            print("Invalid expense number")
            return
        index = edit - 1
        expense = expenses[index]

        print("1. Item")
        print("2. Category")
        print("3. Amount")
        print("4. Description")

        edit_value = int(input("What do you want to edit?: "))

        if edit_value== 1:
            while True:
                new_item = input("Enter New item: ").strip().title()
                if new_item == "" :
                    print("Invalid input ")
                else:
                    break
                    
            expense['item'] = new_item

        elif edit_value == 2:
            while True:
                new_category = input("Enter New Category: ").strip().title()
                if new_category == "" :
                    print("Invalid input ")
                else:
                    break
            expense['category'] = new_category

        elif edit_value == 3:
            while True:
                try:
                    new_amount = float(input("Enter New Amount: ").strip())

                    if new_amount <= 0:
                        print("Amount must be greater than 0")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number")

            expense['amount'] = new_amount
                
        elif edit_value == 4:
            while True:
                new_description = input("Enter New Description: ").strip().title()
                if new_description == "" :
                    print("Invalid input ")
                else:
                    break
            expense['description'] = new_description
        else:
            print("Invalid number")
            return
        
    except ValueError:
        print("Invalid Input")
        return

    print("Expense updated successfully!")
    save_expenses()



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
        return []
    
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
    print("6. Edit Expense")
    print("7. exit")

while True:

    show_menu()
    
    choice = input("Enter your Choice: ").strip()

    if choice == "1":
        clear_terminal()
        print("Add Expense")
        add_expense()

    elif choice == "2":
        clear_terminal()
        print("View Expense")
        view_expenses()

    elif choice == "3":
        clear_terminal()
        print("view Total Spending")
        total = calculate_total()
        print(f"Total spending: #{total}")

    elif choice == "4":
        clear_terminal()
        print("Spending by category")
        category_totals = calculate_by_category()

        for category, total in category_totals.items():
            print(f"{category}: #{total}")

        
    elif choice == "5":
        clear_terminal()
        print("Delete Expense")
        delete_expense()

    elif choice == "6":
        clear_terminal()
        print("Edit Expense")
        edit_expense()


    elif choice == "7":
        clear_terminal()
        save_expenses()
        print("Goodbye")
        break

    else:
        print("Invalid Choice")
