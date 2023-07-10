#!/usr/bin/python3
""" 7-base_geometry """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """Raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Function that validates a value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
