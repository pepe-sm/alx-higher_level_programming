#!/usr/bin/python3
"""X-Request-Id"""
import requests
import sys


def myReq(arg):
    """what's te response id"""
    x = requests.get(arg)
    print("{}".format(x.headers.get('X-Request-Id')))

if __name__ == "__main__":
    myReq(sys.argv[1])
