#!/usr/bin/python3
"""Takes 2 arguments and retrives the 10 latest commit of a repo"""
from requests import get
import sys


if __name__ == '__main__':
    try:
        owner = sys.argv[2]
        repo = sys.argv[1]
        url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
        r = get(url)

        for i in range(10):
            sha = r.json()[i].get('sha')
            author_name = r.json()[i].get('commit').get('author').get('name')
            print('{}: {}'.format(sha, author_name))
    except Exception:
        pass
