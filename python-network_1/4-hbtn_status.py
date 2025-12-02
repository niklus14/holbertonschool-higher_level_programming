#!/usr/bin/python3
"""Hmmm"""

import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"

    req = requests.get(url, headers={'cfclearance': 'true'})

    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
