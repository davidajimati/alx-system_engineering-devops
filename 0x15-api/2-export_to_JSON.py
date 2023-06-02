#!/usr/bin/python3
"""
exports user data defined in script 0 to a json file
"""

import json
from sys import argv
from urllib import request


def extract_to_json(id):
    """
    Extracts user information and exports it to json
    """
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    name_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    filename = "{}.json".format(id)
    response = json.loads(request.urlopen(url).read())
    username = json.loads(request.urlopen(name_url).read()).get('username')

    data = []
    for item in response:
        task = item.get('title')
        completed = item.get('completed')
        line = {"task": task, "completed": completed, "username": username}
        data.append(line)

    result = {id: data}

    with open(filename, 'w') as file:
        json.dump(response, file)


if __name__ == "__main__":
    """runs the program if name is main"""
    extract_to_json(argv[1])
