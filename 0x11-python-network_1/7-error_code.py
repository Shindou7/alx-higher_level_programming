#!/usr/bin/python3
"""
Python script that sends a request to the URL
usage: ./7-error_code.py http://0.0.0.0:5000/status_401
"""

from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])

    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
