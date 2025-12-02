#!/usr/bin/python3
"""again but lil more"""


import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as f:
        print(f.read().decode("utf-8"))
