import os
import datetime
import csv
import sys

from task import Task # import Task class, so it is accessible here
from helpers import menu, welcome # import program text and flow messages

def clear():
    """Clears console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu(menu):
    """Displays worklog menu"""
    print(menu)
    

def get_new_task():
    """Allows user to enter a task name, time spent, and optional notes.

    Returns:
        [Task] -- [returns an instance of a Task class]
    """
    name = None
    date = None
    notes = None
    time = None

    # get Task name and time
    while not name or name.isspace():
        clear()
        # is none or white space (ENTER is a white space too)
        name = input('Enter task name or press (q) to quit.\n>>> ')
        if name.lower() == 'q':
            sys.exit(0)
    while not time:
        clear()
        try:
            time = int(input('Enter time spent on task (in min).\n>>> '))
        except ValueError:
            clear()
            print("Please only enter an integer.")
    clear()
    # get task notes
    notes = input(
        "Enter notes about the task (optional). Pres ENTER to skip.\n>>>")
    if notes == "":
        notes = None

    # set task entry date
    # format: '2018/12/31'
    date = datetime.datetime.now().strftime('%Y/%m/%d')

    new_task = Task(name=name,
                    date=date,
                    notes=notes,
                    time=time)
    return new_task


def save_to_file(task):
    """Saves task to a CSV file. Does not return anything.
    """

    # insert task into file
    with open("tasks.csv", "a+", newline="") as taskfile:
        fieldnames = ["name", "time", "notes", "date"]
        writer = csv.DictWriter(taskfile, fieldnames=fieldnames)
        
        # write headers for a new file
        if os.stat("tasks.csv").st_size == 0:
            writer.writeheader()
        # TODO: write header for an empty file

        # save current task as a row
        writer.writerow(task.as_dictionary())  
        # calls as_dictionary() to get task data in a dictionary format,
        # easy to save to a CSV file

def view_tasks(task):
    """Prints task to stdout. Does not return anything.
    """

    print(task)


# SEARCH SECTION
def search_by_date():
    """[summary]
    
    Returns:
        [type] -- [description]
    """


def search_by_time():
    """[summary]
    
    Returns:
        [type] -- [description]
    """


def search_by_pattern():
    """[summary]

    Returns:
        [type] -- [description]
    """


def search_by_exact():
    """[summary]
    
    Returns:
        [type] -- [description]
    """


def run_menu(menu):
    print(menu)
    
    choice = None
    
    while not choice:
        choice = input('>>> ')
        if choice.lower() == 'a': # enter new task
            task = get_new_task()
            clear()
            print("Your task was added. Here it is:")
            view_tasks(task)
            choice = input("Would you like to do something else? [Y/N]\n>>> ")
            if choice.lower() == "y":
                clear()
                print(menu)
                choice = None
            else:
                sys.exit(0)
        elif choice.lower() == 's': # search tasks
            pass
        elif choice.lower() == 'q':
            sys.exit(0)
        elif choice.lower() == 'm':
            clear()
            print(menu)
            choice = None
        else:
            clear()
            print("""This is not an option.
(A)dd a new task. (S)each task. (Q)uit. (M)enu.
""")
            choice = None









def main():
    clear() # clear terminal from all the stuff that was there
    run_menu(menu)

if __name__ == "__main__":
    main()
