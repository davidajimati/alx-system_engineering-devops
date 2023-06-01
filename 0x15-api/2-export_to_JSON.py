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
    # name_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    response = json.loads(request.urlopen(url).read())
    data = {id: response}
    print(data)


if __name__ == "__main__":
    """runs the program if name is main"""
    extract_to_json(argv[1])
