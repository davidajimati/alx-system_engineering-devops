#!/usr/bin/python3
'''
This module gets the name and todo details of
    users and stores the output in a csv file
'''

import csv
import json
from sys import argv
from urllib import request


def get_details(id):
    """
    gets the details of users and
    writes into a csv file
    """
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    name_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)

    userName = json.loads(request.urlopen(
        name_url).read().decode()).get("username")
    todo_list = json.loads(request.urlopen(todo_url).read().decode())

    filename = "{}.csv".format(id)

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for record in todo_list:
            writer.writerow([id, userName, record.get(
                "completed"), record.get("title")])


if __name__ == "__main__":
    """
    runs the program if module is not imported
    """
    get_details(argv[1])
