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
    filename = "{}.json".format(id)

    response = json.loads(request.urlopen(url).read())

    task = response.get('title')
    completed = response.get('completed')
    username = response.get('username')

    data = []

    data = {id: data}

    # with open(filename, 'w') as file:
    #     json.dump(file, response)


if __name__ == "__main__":
    """runs the program if name is main"""
    extract_to_json(argv[1])
