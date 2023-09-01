#!/usr/bin/python3
"""Sends a POST request with an email passed as parameter"""
import requests
import sys


if __name__ == '__main__':
    try:
        r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
        print(r.text)
    except Exception:
        pass
