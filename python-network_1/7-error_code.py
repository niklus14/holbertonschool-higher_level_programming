#!/usr/bin/python3
"""hellyea"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    a = req.status_code
    if a >= 400:
        print("Error code:", a)
    else:
        print(req.text)
