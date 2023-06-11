#!/usr/bin/python3
def no_c(my_string):
    str_cpy = ""
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            str_cpy += letter
    return (str_cpy) 
