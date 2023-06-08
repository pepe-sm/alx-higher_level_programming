#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    arg_size = len(args) - 1

    msg = "arguments"

    if arg_size > 1:
        print("{} {}:".format(arg_size, msg))
        for j in range(1, arg_size + 1):
            print("{}: {}".format(j, args[j]))


    elif arg_size == 0:
        print("{} {}.".format(arg_size, msg))

    else:
        print("{} {}:".format(arg_size, msg[:8]))
        print("{}: {}".format(arg_size, args[1]))

