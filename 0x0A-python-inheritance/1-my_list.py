#!/usr/bin/python3
""" 1-my_list function """


class MyList(list):
    """ MyList class inherits from list """

    def print_sorted(self):
        """ Prints sorted list """
        print(sorted(self))
