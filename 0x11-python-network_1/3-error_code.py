#!/usr/bin/python3
"""request url and if suceful print format else return error code"""
import urllib.request
import sys


def myError(url):
    """Error code"""
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print("{}".format(html.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))

if __name__ == "__main__":
    myError(sys.argv[1])
