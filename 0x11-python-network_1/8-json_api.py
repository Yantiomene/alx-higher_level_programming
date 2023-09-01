#!/usr/bin/python3
"""Sends a post request to http://0.0.0.0:5000/search_user"""
import requests
import sys


if __name__ == '__main__':
    data = {'q': ""}
    try:
        data['q'] = sys.argv[1]
    except Exception:
        pass

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data)
        try:
            obj = r.json()
            if not obj:
                print("No result")
            else:
                print("[{}] {}".format(obj['id'], obj['name']))
        except Exception:
            print("Not a valid JSON")
    except Exception:
        pass
