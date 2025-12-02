#!/usr/bin/python3
"""Getting easy"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    rq = urllib.request.Request(url, headers={'cfclearance': 'true'})

    with urllib.request.urlopen(rq) as f:
        head = f.headers
        print(head.get("X-Request-Id"))
