import os
import datetime
import csv
import sys
import re

from task import Task  # import Task class, so it is accessible here
from helpers import main_menu, welcome  # import script text stuff

# TODO: remove from adding task and all others
# def quit_now(answer):
#     if answer.lower() == "q":
#         sys.exit()


def clear():
    """Clears console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu(menu):
    """Prints out the main menu to stdout"""
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


def view_results(list_of_ord_dict):
    """[summary]
    """
    idx = 0  # start index for results
    for odict in list_of_ord_dict:
        idx += 1
        print("Result {} of {}\n---------------".format(
            idx,
            len(list_of_ord_dict)
        ))

        for key, value in odict.items():
            print("{} - {} ".format(key, value))
        print("")


# SEARCH SECTION
def search_by_date():
    """[summary]

    Returns:
        [type] -- [description]
    """
    search_date = None
    search_results = []
    clear()
    print("Enter task date. Accepted date format: YYYY/MM/DD")

    while search_date is None:
        search_date = input(">>> ")
        try:
            datetime.datetime.strptime(search_date, '%Y/%m/%d')
        except ValueError:
            clear()
            print("Incorrect data format, should be YYYY/MM/DD")
            search_date = None

    with open("tasks.csv") as csvfile:
        task_reader = csv.DictReader(csvfile)
        for row in task_reader:
            if row["date"] == search_date:
                search_results.append(row)

    if len(search_results) == 0:
        clear()
        print("No tasks match that date")
        # try_again = input("")
    else:
        print(search_results)  # ordered Dict
        view_results(search_results)  # view results func4all types of results


def search_by_time():
    """[summary]

    Returns:
        [type] -- [description]
    """
    search_time = None
    search_results = []
    clear()
    print("Enter task time. Integers only.")
    while search_time is None:
        search_time = input(">>> ")
        # check if it is an integer, if not
        # complain
        # if it is, turn into string :) since
        # it comes as string from CSV :)
        try:
            search_time = int(search_time)
        except ValueError:
            clear()
            print("Only integers are allowed.")
            search_time = None
        else:
            search_time = str(search_time)

    with open("tasks.csv") as csvfile:
        task_reader = csv.DictReader(csvfile)
        for row in task_reader:
            if row["time"] == search_time:
                search_results.append(row)

    if len(search_results) == 0:
        clear()
        print("No tasks match that data")
        # try_again = input("")
    else:
        print(search_results)  # ordered Dict
        view_results(search_results)  # view results func4all types of results


def search_by_pattern():
    """[summary]

    Returns:
        [type] -- [description]
    """
    search_regex = None
    search_results = []
    clear()
    print("Enter your regex. Input the pattern part only: r\"pattern\".")
    # input() gets data as raw string and does not have to be r""-ed
    while search_regex is None:
        search_regex = input(">>> ")
        # check if it is an integer, if not
        # complain
        # if it is, turn into string :) since
        # it comes as string from CSV :)
        search_this = re.compile(search_regex)

    with open("tasks.csv") as csvfile:
        task_reader = csv.DictReader(csvfile)
        for row in task_reader:
            name = row["name"]
            time = row["time"]
            notes = row["notes"]
            date = row["date"]
            # do not join string
            # joining string would create edge cases that do not actually exist

            if search_this.findall(name) != []:
                search_results.append(row)
            elif search_this.findall(time) != []:
                search_results.append(row)
            elif search_this.findall(notes) != []:
                search_results.append(row)
            elif search_this.findall(date) != []:
                search_results.append(row)

    if len(search_results) == 0:
        clear()
        print("No tasks match that pattern")
        # return False to try_again = input("") ?
    else:
        # print(search_results)  # ordered Dict
        view_results(search_results)  # view results func4all types of results


def search_by_exact():
    """Searches for exact words in title or notes. No partial matches.
    Case insensitive. Does not search for phrases.
    search_by_pattern() can do that.

    example text: "This is example text"
    matches:
        * this
        * IS
        * TeXT
    does not match:
        * ex
        * pl
    """
    search_exact = None
    search_results = []
    clear()
    print("Enter search word.")
    while search_exact is None:
        search_exact = input(">>> ")

        if len(search_exact.split()) > 1:
            search_exact = None
            clear()
            print("You can search using only one word.")

    with open("tasks.csv") as csvfile:
        task_reader = csv.DictReader(csvfile)
        for row in task_reader:
            string = row["name"].lower().split()
            string += row["notes"].lower().split()
            # each word is separe in the list
            # they can be combined
            if search_exact.lower() in string:
                search_results.append(row)

    if len(search_results) == 0:
        clear()
        print("No tasks match that pattern")
        # return False to try_again = input("") ?
    else:
        # print(search_results)  # ordered Dict
        view_results(search_results)  # view results func4all types of results


def run_main_menu(menu_text):
    print(welcome)
    print(menu_text)

    choice = None

    while not choice:
        choice = input('>>> ')
        # enter new task (a) for ADD and (y) for yes in 2nd loop)
        if choice.lower() == 'a' or choice.lower() == "y":
            task = get_new_task()
            clear()
            save_to_file(task)
            print("Your task was added. Here it is:\n")
            view_tasks(task)
            print("Add something else?\nY/N Q(uit)/M(enu)]")
            choice = None
        elif choice.lower() == "q":
            sys.exit()
        elif choice.lower() == 's':
            pass
        elif choice.lower() == 'm' or choice.lower() == "n":
            clear()
            print(menu_text)
            choice = None
        else:
            clear()
            print("This is not an option.\n"
                  "(A)dd a new task. (S)each task. (Q)uit. (M)enu.")
            choice = None


def main():
    clear()  # clear terminal from all the stuff that was there
    run_main_menu(main_menu)


if __name__ == "__main__":
    main()
