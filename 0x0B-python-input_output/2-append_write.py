#!/usr/bin/python3
""" 2-append_write module """


def append_write(filename="", text=""):
    """ Appends text and returns number of chars """
    with open(filename, "a", encoding="utf-8") as file:
        amount_chars = file.write(text)
    return amount_chars
