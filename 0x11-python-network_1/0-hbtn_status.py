#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """

import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(
                'https://alx-intranet.hbtn.io/status'
        ) as response:
            html = response.read()
            print('Body response:')
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
            print("\t- utf8 content: {}".format(html.decode('utf-8')))
    except HTTPError as e:
        print("Error: {}".format(e))
