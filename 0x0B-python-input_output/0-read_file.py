#!/usr/bin/python3
""" 0-read_file module """


def read_file(filename=""):
    """ this function reads a file """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
