#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        r = resp.read()
        print('Body response:')
        print('\t-type: {}'.format(type(r)))
        print('\t-content: {}'.format(r))
        print('\t-utf8 content: {}'.format(r.decode('utf8')))
