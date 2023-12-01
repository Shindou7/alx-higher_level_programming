#!/usr/bin/python3
"""
Python script that sends a POST request to the URL
http://0.0.0.0:5000/search_user
usage: ./8-json_api.py [letter only]
"""

from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    try:
        url = 'http://0.0.0.0:5000/search_user'
        payload = {'q': q}
        r = requests.post(url, payload).json()

        if {'id', 'name'} <= r.keys():
            print('[{id}] {name}'.format(id=r.get('id'), name=r.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
