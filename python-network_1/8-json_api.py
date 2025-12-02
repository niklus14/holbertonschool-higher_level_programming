#!/usr/bin/python3
"""No comment"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data=payload)

    try:
        json_response = response.json()

        if json_response:
            print("[{}] {}".format(json_response.get('id'),
                                   json_response.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
