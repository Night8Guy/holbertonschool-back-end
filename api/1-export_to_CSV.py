#!/usr/bin/python3
"""exporting API data to CSV file"""

import csv
import requests
import sys


url = "https://jsonplaceholder.typicode.com"


def get_employee_todos(employee_id):
    """gets the employye tasks"""
    url_todos = f"{url}/users/{employee_id}/todos"
    todos = requests.get(url_todos)
    return todos.json()


def get_employee_name(employee_id):
    """gets the employee name"""
    url_name = f"{url}/users/{employee_id}"
    user_data = requests.get(url_name).json()
    employee_name = user_data.get("username")
    return employee_name


def get_completed_tasks(tasks):
    """gets the completed tasks of the employee"""
    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed_tasks.append(task)
    return completed_tasks


def print_employee_tasks(employeeName, completedTasks, totalTasks):
    """prints employee tasks"""
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(completedTasks), totalTasks))
    for task in completedTasks:
        print("\t {}".format(task.get("title")))

    with open(f"{employee_id}.csv", "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([employee_id, employeeName,
                             task.get("completed"), task.get("title")])


if __name__ == "__main__":
    employee_id = sys.argv[1]
    tasks = get_employee_todos(employee_id)
    employeeName = get_employee_name(employee_id)
    completedTasks = get_completed_tasks(tasks)
    print_employee_tasks(employeeName, completedTasks, len(tasks))