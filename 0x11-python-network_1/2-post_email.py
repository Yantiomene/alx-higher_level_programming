#!/usr/bin/python3
"""Sends a post request and display the body response"""
from urllib import request, parse
import sys


if __name__ == '__main__':
    values = {
        'email': sys.argv[2]
    }
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as resp:
        r = resp.read()
        print(r.decode('utf-8'))
