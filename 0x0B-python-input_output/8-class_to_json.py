#!/usr/bin/python3
""" 8-class_to_json module """


def class_to_json(obj):
    """ Returns a JSON representation of a dictionary """
    return obj.__dict__
