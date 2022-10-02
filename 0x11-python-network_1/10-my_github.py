#!/usr/bin/python3
"""Takes Github credentials and uses Github API to display user
id."""

if __name__ == '__main__':
    import requests
    import sys

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]

    r = requests.get(url, auth=(username, token))

    print(r.json().get('id'))
