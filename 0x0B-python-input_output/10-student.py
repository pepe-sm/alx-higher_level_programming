#!/usr/bin/python3
""" 10-student module """


class Student:
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ Initializes an instance of Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns JSON format """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
