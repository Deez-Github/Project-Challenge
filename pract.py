#import json

expenses = []

def add():
    try:
        while True:
            item = input("What did you buy: ").strip().title()
            if item == "":
                print("Please add the item")
            else:
                break

        while True:
            category = input("What category is the item?: ").strip().title()
            if category == "":
                print("Invalid input")
            else:
                break
        while True:
            price = int(input("How much is it?: "))
            if price <= 0 :
                print("Invalid input")
            else:
                break

        while True:
            description = input("what for?: ").strip().title()
            if description == "":
                print("Invalid input")
            else:
                break

    except ValueError:
        print("invalid input")

    expense = {
        "item": item,
        "category": category,
        "price": price,
        "description": description,
    }

    expenses.append(expense)

add()

def view():
    if len(expenses) == 0 :
        print("No record")

    for index, expense in enumerate(expenses,start=1):
        print(f"{index}. {expense['item']} - {expense['category']} - #{expense['price']} - {expense['description']}")
view()


def total():
    total = 0

    for expense in expenses:
        total += expense["price"]
    return total
total = total()

print(total)


def cat_cal():
    caty = {}

    for expense in expenses:
        categories = expense['category']
        amount = expense['price']

        if categories in caty:
            caty['categories'] += amount
        else:
            caty['categories'] = amount
    return caty

caty_all = cat_cal()
print(caty_all)
    
