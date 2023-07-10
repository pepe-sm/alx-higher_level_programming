#!/usr/bin/python3
"""  4-inherits_from """

def inherits_from(obj, a_class):
    """ if inherited directly or indirectly return else false """
    return isinstance(obj, a_class) and type (obj) is not a_class
