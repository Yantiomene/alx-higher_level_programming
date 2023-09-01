#!/usr/bin/python3
"""Send a request to the URL and display the value the
variable X-request-ID"""
import requests
import sys


if __name__ == '__main__':
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except Exception:
        pass
