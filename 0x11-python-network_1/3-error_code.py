#!/usr/bin/python3
"""Send a URL request and displays the body response
and Error code"""
from urllib import request, error
import sys


if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as resp:
            r = resp.read()
            print(r.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
