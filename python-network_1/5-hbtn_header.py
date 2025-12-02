#!/usr/bin/python3
"""Dont worry"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)

    print(req.headers.get("X-Request-Id"))
