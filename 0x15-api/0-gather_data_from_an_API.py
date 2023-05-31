#!/usr/bin/python3
'''
using REST API, for a given employee ID,
returns information about his/her TODO list progress
'''

import json
import sys
from urllib import parse, request


def get_name(id):
    """
    This function retrieves the name of a user
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    resp_name = request.urlopen(url)
    user_name = json.loads(resp_name.read().decode())
    return user_name.get("name")
    # return (user_name)


def get_todo(id):
    """
    gets the todo list of a user.
    """
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    response = request.urlopen(url)
    # read, decode and load the response as a json object
    json_data = json.loads(response.read().decode())
    return (json_data)


def run_all(id):
    """
    entry point into the program
    """
    name = get_name(id)
    todo_list = get_todo(id)
    done = 0
    total = 0
    completed = []

    for item in todo_list:
        total += 1
        if item.get("completed"):
            completed.append(item["title"])
            done += 1

    print("Employee {} is done with tasks({}/{}):" .format(name, done, total))
    print("\n".join("\t " + item for item in completed))


if __name__ == "__main__":
    """
    Executes the code if __name__ is __main__
    """
    run_all(sys.argv[1])
