#!/usr/bin/python3
"""send post to url with email as parameter"""
import urllib.request
import urllib.parse
from sys import argv


def myEmail(args, email):
    """encode email with ascii & request url with email as parameter"""
    value = {'email': email}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(args, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("{}".format(html.decode('utf-8')))

if __name__ == "__main__":
    myEmail(argv[1], argv[2])
