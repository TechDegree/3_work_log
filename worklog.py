import os
import datetime
import csv

from task import Task # import Task class, so it is accessible here


def clear():
    """Clears console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """Displays worklog menu"""
    pass
    

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
        # is none or white space (ENTER is a white space too)
        name = input('Enter task name or press (q) to quit.\n>>>')
        if name.lower() == 'q':
            sys.exit(0)
    while not time:
        try:
            time = int(input('Enter time spent on task (in min).\n>>>'))
        except ValueError:
            print("Please only enter an integer.")

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

def view_tasks():
    """[summary]

    Returns:
        [type] -- [description]
    """
    pass

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












def main():

    task = get_new_task()
    save_to_file(task)
    print(task.as_dictionary())

if __name__ == "__main__":
    main()
