#!/usr/bin/python3
for first_int in range(0, 10):
    for second_int in range(first_int + 1, 10):
        if first_int != 8:
            print("{}{}".format(first_int, second_int), end=", ")
        else:
            print("{}{}".format(first_int, second_int))
