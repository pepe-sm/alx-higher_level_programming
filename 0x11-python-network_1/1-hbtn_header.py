#!/usr/bin/python3
"""what's my status"""
import urllib.request
import sys


def resHeader(arg):
    """what's my status"""
    with urllib.request.urlopen(arg) as response:
        html = response.info()
        print("{}".format(html['X-Request-Id']))

if __name__ == "__main__":
    resHeader(sys.argv[1])
