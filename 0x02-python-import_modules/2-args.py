#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    size = len(sys.argv) - 1

    msg = "arguments"

    if size == 1:
        print("{} {}:".format(size, msg[:8]))

    else:
        print("{} {}{}".format(size, msg,
              "." if size == 0 else ":"))

    for ac, name in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(ac, name))
