import json
from datetime import datetime

priority_list = ["High", "Medium", "Low"]

def add_task():
    global next_task_id
    while True:
        title = input("What do you want to do? : ").strip().title()
        if title == "" :
            print("Please provide a title")

        else:
            break
    while True:
        priority =  input("Enter priority (High, Medium, Low): ").strip().title()
        if priority in priority_list:
            break
        else:
            print("Enter priority (High, Medium, Low)")
    while True:
        try:
            due_date = datetime.strptime(input("Enter due date (YYYY-MM-DD): "), "%Y-%m-%d").strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Enter date in this format (YYYY-MM-DD)")


    task = {
        "id" : next_task_id,
        "title" : title,
        "completed" : False,
        "priority" :  priority,
        "due_date" : due_date
    }

    next_task_id += 1
    tasks.append(task)




def view_task():
    if len(tasks) == 0:
        print("No Task Available")
        return

    print("\n========== YOUR TASKS ==========")


    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "DONE"
        else:
            status = "PENDING"

        print(
            f"{index}. ID: {task['id']}  [{status}] {task['title']}"
            f"| Priority: {task['priority']}"
            f"| Due Date: {task['due_date']}"
        )

def  complete_task():
    if len(tasks) == 0:
        print("No tasks available to complete")
        return
    view_task()

    while True:
        try: 
            task_id = int(input("Enter the ID of the task to complete: "))
            break
        except ValueError:
            print("Please enter a valid number")
        while True:
            for task in tasks:
                if task_id in task['id']:
                    break
                else:
                    print("invalid Task ID")


    found = False

    for task in tasks:
        if task['id'] == task_id:
            if task['completed']:
                print("This task is already completed")
            else:
                print(f"Are you Sure task{task_id} is completed ")
                complete_ans = input("Answer Yes or No: ").strip().title()
                if complete_ans == "Yes":
                 task['completed'] = True
                else:
                    print("Go and complete your task")

    
            found = True
            break
    if not found:
        print("Task ID not found")


def delete_task():
    if len(tasks) == 0:
            print("No tasks available to Delete")
            return
    view_task()
    while True:
        try: 
            delete_id = int(input("Enter the ID of the task to Delete: "))
            break
        except ValueError:
            print("Please enter a valid number")
        while True:
            for task in tasks:
                if delete_id in task['id']:
                    break
                else:
                    print("invalid Task ID")

            
    found = False

    for index, task in enumerate(tasks):
        if task['id'] == delete_id:
            deleted_task = tasks.pop(index)

            found = True
            break

    print(f"This was deleted{deleted_task}")

    if not found:
        print("Task ID not found")

    


def edit_task():
    if len(tasks) == 0:
        print("No tasks available to complete")
        return
    view_task()
    
    try: 
        task_id = int(input("Enter the ID of the task to Edit: "))
    except ValueError:
        print("Please enter a valid number")
        return

    found = False
    for task in tasks:
        if task['id'] == task_id:
            task_item = (input("Do you want to edit the Title or Priority: ")).strip().title()
            
            if task_item == "Title":
                change_title = (input("New Title name : ")).strip().title()
                task['title'] = change_title
            elif task_item == "Priority":
                change_priority = (input("New Priority name : ")).strip().title()
                task['priority'] = change_priority
            else:
                print("Please choose Title or Priority")

            found = True
            break
    if not found:
        print("Task ID not found")
        

def filter_task():

    if len(tasks) == 0:
        print("No tasks available to filter")
        return
    view_task()

    filter_by = input("what View Option ").strip().title()
    found = False
    complete_list = ["Pending", "Done"]
    

    if filter_by not in complete_list and filter_by not in priority_list:
        print("Invalid filter option")
        return

    for task in tasks:
        if filter_by in complete_list:
            if filter_by == "Pending":
                if not task['completed']:
                    print(task)
                    found = True
                    
            elif filter_by == "Done":
                if task['completed']:
                    print(task)
                    found = True
            
        elif filter_by in priority_list:
            if task['priority'] == filter_by:
                print(task)
                found = True
    
            
    if not found:
        print("No matching task Found")

def task_summary():

    if len(tasks) == 0:
        print("No tasks available")
        return

    total_task = len(tasks)
    completed_task = 0
    pending_task = 0
    high_priority = 0
    medium_priority = 0
    low_priority = 0

    for task in tasks:
        if not task['completed']:
            pending_task += 1
        else:
            completed_task += 1

        if task['priority'] == "High":
            high_priority += 1
        elif task['priority'] == "Medium":
            medium_priority += 1
        else:
            low_priority +=1
    

    print("========== TASK SUMMARY ==========\n")
    print(f"Total tasks: {total_task}")
    print(f"Completed tasks: {completed_task}")
    print(f"Pending tasks: {pending_task}")

    print(" ")
    print("Priority Breakdown:")
    print(f"High Priority: {high_priority}")
    print(f"Medium Priority: {medium_priority}")
    print(f"Low Priority: {low_priority}")




def save_task():
    with open("task.json", "w") as file:
        json.dump(tasks, file,indent=2)



def load_task():
    try: 
        with open("task.json", "r") as file:
            return json.load(file)
    except FileNotFoundError :
        return []
    except json.JSONDecodeError:
        return []

tasks = load_task()  

next_task_id = max([task["id"] for task in tasks], default=0) + 1



while True:

    print("========== TO-DO MANAGER ==========")

    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Edit Task")
    print("6. Filter Task")
    print("7. Task Summary")
    print("8. Exit")

    choice = input("Select a Choice: ")

    if choice == "1":
        add_task()
        save_task()
    elif choice   == "2":
        view_task()
    elif choice == "3":
        complete_task()
        save_task()

    elif choice == "4":
        delete_task()
        save_task()
    elif choice == "5":
        edit_task()
        save_task()

    elif choice == "6":
        filter_task()

    elif choice == "7":
        task_summary()

    elif choice == "8":
        print("Good Bye")
        break
    else:
        print("invalide Choice")