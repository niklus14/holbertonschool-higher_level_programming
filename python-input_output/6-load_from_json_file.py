#!/usr/bin/python3
"""kldnfknr"""


import json


def load_from_json_file(filename):
    """klenfn"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
