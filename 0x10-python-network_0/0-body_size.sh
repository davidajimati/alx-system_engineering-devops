#!/usr/bin/env bash
#  takes in a URL, sends a request to that URL, and displays the size of the body of the response

response=$(curl -s -w "$1")
echo "$response"
