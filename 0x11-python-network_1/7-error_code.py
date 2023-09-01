#!/usr/bin/python3
"""Sends a request and display the body of the response"""
import requests
import sys


if __name__ == '__main__':
    try:
        r = requests(sys.argv[1])
        if (r.status_code >= 400):
            print("Error code: {}".format(r.status_code))
        else:
            print(r.text)
    except Exception:
        pass
