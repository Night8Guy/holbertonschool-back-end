#!/usr/bin/python3
"""Python script that uses employee IDs,
along with this API, to return info 
on their TODO list progress."""

import json
import requests

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


def all_employees():
    data_dict = {}

    for employee_id in range(1, 11):
        tasks = get_employee_todos(employee_id)
        employeeName = get_employee_name(employee_id)

        employee_data = []
        for task in tasks:
            task_data = {
                "username": employeeName,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            employee_data.append(task_data)

        data_dict[str(employee_id)] = employee_data

    json_data = json.dumps(data_dict)
    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        jsonfile.write(json_data)


if __name__ == "__main__":
    all_employees()