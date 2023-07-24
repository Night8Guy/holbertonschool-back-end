#!/usr/bin/python3
"""Script that gets info about the user 
from an API"""

import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com"


def get_employee_todos(employee_id):
    """gets employye tasks"""
    url_todos = f"{url}/users/{employee_id}/todos"
    todos = requests.get(url_todos)
    return todos.json()


def get_employee_name(employee_id):
    """gets  employee name"""
    url_name = f"{url}/users/{employee_id}"
    user_data = requests.get(url_name).json()
    employee_name = user_data.get("username")
    return employee_name


def print_employee_tasks(employeeName, completedTasks, totalTasks):
    """prints employee tasks"""
    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, len(completedTasks), totalTasks))
    for task in completedTasks:
        print("\t {}".format(task.get("title")))


def export_to_json(employeeId, employeeName, completedTasks):
    data_dict = {str(employeeId): []}

    for task in completedTasks:
        task_dict = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": employeeName}
        data_dict[str(employeeId)].append(task_dict)

    json_data = json.dumps(data_dict)

    filename = "{}.json".format(employeeId)
    with open(filename, "w") as jsonfile:
        jsonfile.write(json_data)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    tasks = get_employee_todos(employee_id)
    employeeName = get_employee_name(employee_id)
    export_to_json(employee_id, employeeName, tasks)
