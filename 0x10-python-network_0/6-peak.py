#!/usr/bin/python3
"""function returns maximum integer"""


def find_peak(list_of_integers):
    """find peak"""
    if len(list_of_integers) == 0:
        return
    list_of_integers.sort()
    return list_of_integers[-1]
