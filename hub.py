from CASIC.CASIC import *

def add_new_task():
        clear()
        task2 = input("Enter your next task: ")
        clear()
        id2 = input("Enter a name/id for the next task: ")
        clear()
        print("Your Tasks:")
        print(id1 + " - " + task1)
        print(id2 + " - " + task2)
        wait(5)
        clear()
    
used()
wait(2)
clear()
print("Welcome to hub - a simple FOSS to-do list manager.")
wait(1)
print("note this is in alpha and is very minimal and janky. really just a demo program.")
wait(2)
clear()
task1 = input("Enter your first task: ")
clear()
id1 = input("Enter a name/id for the first task: ")

def task_list():
    clear()
    print("Your Tasks:")
    print(id1 + " - " + task1)
    wait(5)
    clear()
    add_task = input("Would you like to add another task? (yes/no): ")
    if add_task == "yes":
        add_new_task()
    else:
        clear()
        print("Thank you for using hub!")
        wait(2)
        clear()

task_list()

          

