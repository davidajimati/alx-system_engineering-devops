#!/usr/bin/python3
'''
using REST API, for a given employee ID,
returns information about his/her TODO list progress
'''
import sys
import json
from urllib import parse, request


def get_name(id):
    """
    This function retrieves the name of a user
    """
    data = {"id": id}
    values = parse.urlencode(data).encode('utf-8')
    url = 'https://jsonplaceholder.typicode.com/users'

    req1 = request.Request(url, data=values, method="GET")
    resp_name = request.urlopen(req1)
    user_name = json.loads(resp_name.read().decode())
    return (user_name[0]["name"])


def get_todo(id):
    """
    gets the todo list of a user.
    """
    params = {"userId": id}
    query = parse.urlencode(params).encode(
        'utf-8')     # encodes the parameters to bytes
    url = "https://jsonplaceholder.typicode.com/todos"

    # form standard url that can be accepted by the target API
    req = request.Request(url, data=query, method="GET")
    # query the API by opening the link
    response = request.urlopen(req)
    # read, decode and load the response as a json object
    json_data = json.loads(response.read().decode())
    return (json_data)


def run_all(id):
    name = get_name(id)
    # todo = get_todo(id)

    print(name)

if __name__ == "__main__":
    """
    Executes the code if __name__ is __main__
    """
    run_all(sys.argv[1])
