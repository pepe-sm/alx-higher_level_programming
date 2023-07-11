#!/usr/bin/python3
"""
    11-student module
"""


class Student:
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ Initializes an instance of Student Class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        return self.__dict__.update(json)
