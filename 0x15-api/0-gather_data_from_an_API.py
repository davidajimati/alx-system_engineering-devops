#!/usr/bin/python3
'''
using REST API, for a given employee ID,
returns information about his/her TODO list progress
'''
import sys
import json
from urllib import parse, request


def get_todo(id):
    """
    gets the todo list of a user.
    """

    params = {"userId": id}
    query = parse.urlencode(params)

    url = "https://jsonplaceholder.typicode.com/todos" + "?" + query

    response = request.urlopen(url)     #opens url
    html = response.read()              # converts the response to human readable format
    jsonFormat = json.load(html)        # Json format
    print(jsonFormat)

    # print("Employee {} is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):")


if __name__ == "__main__":
    """
    Executes the code if __name__ is __main__
    """
    get_todo(sys.argv[1])
