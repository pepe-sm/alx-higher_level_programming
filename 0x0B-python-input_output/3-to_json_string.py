#!/usr/bin/python3
""" 3-to_json_string module """

import json


def to_json_string(my_obj):
    """ Return JSON rep of an object """
    return json.dumps(my_obj)
