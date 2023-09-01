#!/usr/bin/python3
"""Sends a get request to Github API with BAsic authentication"""
from requests import get, auth
import sys


if __name__ == '__main__':
    usr = sys.argv[1]
    pwd = sys.argv[2]
    url = 'https://api.github.com/user'
    r = get(url, auth=auth.HTTPBasicAuth(usr, pwd))
    print(r.json().get('id'))
