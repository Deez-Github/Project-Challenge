orders = [
    {"order_id" :"001",
    "product":"Laptop",
    "quantity":5,
    "unit_price":450.00,
    "discount": 0.05
    },
    {"order_id" :"002",
    "product":"Mouse",
    "quantity":3,
    "unit_price":150.00,
    "discount": 0.05
    },
    {"order_id" :"003",
    "product":"Keyboard",
    "quantity":2,
    "unit_price":2000.00,
    "discount": 0.05
    },
]

grand_total = 0.0
for order in orders:
   net_revenue =  order['quantity'] * order['unit_price'] * (1 - order['discount'])
   grand_total += net_revenue
   print(f"Order {order['order_id']} | {order['product']} x {order['quantity']} = ${order['unit_price']:.2f} | Net Reveneue : ${net_revenue:.2f}")

print(f"Grand Total : {grand_total:.2f}")



# Step 1: Make a list of 4 students.

students = [
    {"name": "Alice", "scores": [88, 92, 95]},
    {"name": "Bob", "scores": [75, 68, 80]},
    {"name": "Charlie", "scores": [62, 58, 65]},
    {"name": "Diana", "scores": [45, 52, 50]},
]

def calculate_average(scores):
    total = sum(scores)
    count = len(scores)
    return total / count


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


print("----- GRADE BOOK REPORT -----")

for student in students:
    name = student["name"]
    scores = student["scores"]

    average = calculate_average(scores)
    grade = assign_grade(average)

    # :.2f means "show 2 numbers after the decimal point"
    print(f"{name}: average = {average:.2f}, grade = {grade}")
   

