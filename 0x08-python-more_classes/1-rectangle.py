#!/usr/bin/python3
""" define class Rectangle """


class Rectangle:
    """ define rectangle """

    def __init__(self, width=0, height=0):
        """Initialize rectangle
        Ars:
        width (int): widt
        height (int): height of rectangle
        """

        self.height = height
        self.width = width

    @property
    def height(self):
        """ Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets Height Rectangle """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
