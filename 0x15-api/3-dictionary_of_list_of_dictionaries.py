#!/usr/bin/python3
"""
Extend Python script 0 to export data in the JSON format
"""

import json
from sys import argv
from urllib import request


def list_dict():
    """
    Carries out the program
    """
    filename = "todo_all_employees.json"
    data = {}

    # initialize and empty list for each user
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = json.loads(request.urlopen(users_url).read())
    idx = 0
    for user in users:
        user_id = users[idx].get('id')
        username = users[idx].get('username')
        data[user_id] = []

        # get detail of each user
        todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
            .format(
                user_id)
        response = json.loads(request.urlopen(todo_url).read())

        # loop through response to fill in the details
        for item in response:
            task = item.get('title')
            completed = item.get('completed')

            line = {"username": username, "task": task, "completed": completed}
            data[user_id].append(line)
        idx += 1

    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    """
    If name is main
    """
    list_dict()
