#!/usr/bin/python3
"""
Python script that sends a request to the URL
usage: ./5-hbtn_header https://intranet.hbtn.io
"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
