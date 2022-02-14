# Import libraries
from os import *
import pandas as pd
import numpy as np

fname = 'ToDoList.csv'
flag = None

# If there is an existing file, open it to dataframe. If not, create an empty dataframe to save to file later
try:
    df = pd.read_csv(fname, sep=',', index_col=0)
except:
    columns = ['Task','Due Date','Priority']
    df = pd.DataFrame(columns=columns)

# Print out the current task List
print('Current Task List:\n', df)

# Run loop until Q is pressed

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
        print("Not a valid option. Please try again.")