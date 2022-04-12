# Import libraries
from os import *
from tkinter import *
import pandas as pd
import numpy as np

#Instantiate tkinter window
root = Tk()
root.title("To-Do List")

#Define Variables
fname = 'ToDoList.csv'
task_val = StringVar()
due_val = StringVar()
priority_val = StringVar()

# If there is an existing file, open it to dataframe. If not, create an empty dataframe to save to file later
try:
    data = pd.read_csv(fname, sep=',', index_col=0)
except:
    columns = ['Task','Due Date','Priority']
    data = pd.DataFrame(columns=columns)

#Define functions

def print_tasks():
    df=data.get()
    list_label = Label(root, text=df)
    list_label.grid(row=5, column=0, columnspan=2)

def add_task():
    task_val = taskE.get()
    due_val = dueDateE.get()
    priority_val = priorityE.get()
    df=data.get()
    newrow = {'Task' : [task_val],
            'Due Date' : [due_val],
            'Priority' : [priority_val]}
    df2 = pd.DataFrame(newrow)
    data = pd.concat([df, df2], axis=0).reset_index(drop=True)
    print(data)
    return data

def del_task():
    df=data.get()
    recordid = int(taskidE.get())
    data = df.drop(recordid).reset_index(drop=True)
    return data

def save(df):
    df.to_csv(fname, mode='w')

#Create field labels/titles
task = Label(root, text="Task Name: ")
task.grid(row=0,column=0)
due = Label(root, text="Due Date: ")
due.grid(row=1, column=0)
priority = Label(root, text="Priority")
priority.grid(row=2, column=0)
taskid = Label(root, text="Task ID")
taskid.grid(row=3, column=0)

#Create User Input Fields
taskE = Entry(root, width=35, border=5)
taskE.grid(row=0, column=1)
dueDateE = Entry(root, width=35, border=5)
dueDateE.grid(row=1, column=1)
priorityE = Entry(root, width=35, border=5)
priorityE.grid(row=2, column=1)
taskidE = Entry(root, width=35, border=5)
taskidE.grid(row=3, column=1)

# # # Note to self - stack the labels and the entry fields together into one code chunk

#Define buttons

printButton = Button(root, text="Print Tasks", padx=40, pady=20, command=print_tasks)
addButton = Button(root, text="Add Task", padx=40, pady=20, command=add_task())
deleteButton = Button(root, text="Delete Task", padx=40, pady=20, command=del_task)
saveButton = Button(root, text="Save List", padx=40, pady=20, command= save(data))
quitButton = Button(root, text="Quit", padx=40, pady=20, command=root.quit)


#Put buttons on the screen
printButton.grid(row=0, column=2)
addButton.grid(row=1, column=2)
deleteButton.grid(row=2, column=2)
saveButton.grid(row=3, column=2)
quitButton.grid(row=4, column=2)

root.mainloop()



""" # Run loop until Q is pressed

while flag != 'Q':
    option = input("Options: A to Add, D to Delete, P to Print Full Task List, Q to Quit \nAction: ")
    option = option.lower().upper()
    # Add an item to list
    if option == 'A':
        task = input("Enter task name: ")
        due = input("Enter due date (mm/dd/yyyy): ")
        priority = input("Enter priority: ")
        newrow = {'Task' : [task],
                'Due Date' : [due],
                'Priority' : [priority]}
        df2 = pd.DataFrame(newrow)
        df = pd.concat([df, df2], axis=0).reset_index(drop=True)
    # Delete an item from list
    elif option == 'D':
        row = int(input("Enter Task ID to delete: "))
        df = df.drop(row).reset_index(drop=True)
    # Print list for user
    elif option == 'P':
        print('Current Task List:\n', df)
    # Save df to file and quit program
    elif option == 'Q':
        flag = 'Q'
        print("Saving ToDo List...")
        df.to_csv(fname,mode='w')
        print("Closing.")
        exit
    else:
        print("Not a valid option. Please try again.") """