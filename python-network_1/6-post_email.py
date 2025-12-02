#!/usr/bin/python3
"""alright"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    s = requests.post(url, data=data)
    print(s.text)
