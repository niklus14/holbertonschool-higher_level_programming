#!/usr/bin/python3
"""kefhrf"""


import json


def save_to_json_file(my_obj, filename):
    """kdnfn"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
