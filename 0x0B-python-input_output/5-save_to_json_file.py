#!/usr/bin/python3
"""
Contains the "save_to_json_fiction
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, usingON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
