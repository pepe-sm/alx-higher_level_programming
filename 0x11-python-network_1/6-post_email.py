#!/usr/bin/python3
"""request url wit post email"""
import requests
import sys


def reqEmail(args, email):
    """what's my status"""
    data = {'email': email}
    x = requests.post(args, data=data)
    print("{}".format(x.text))

if __name__ == "__main__":
    reqEmail(sys.argv[1], sys.argv[2])
