#!/usr/bin/python3
"""
    9-rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Initializes the Rectangle class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area """
        return self.__width * self.__height

    def __str__(self):
        """ description of a rectangle """
        return f"[Rectangle] {self.__width}/{self.__height}"
