#!/usr/bin/python3
"""Takes in a URL and sends a request to the URL and displays the
value of the X-Request -Id"""
import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as resp:
        info = resp.info()
        print(info['X-Request-Id'])
