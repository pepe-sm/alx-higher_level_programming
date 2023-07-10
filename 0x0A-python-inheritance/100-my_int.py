#!/usr/bin/python3
"""
    100-my_int module
"""


class MyInt(int):
    """ MyInt class """

    def __eq__(self, argument):
        return super().__ne__(argument)

    def __ne__(self, argument):
        return super().__eq__(argument)
