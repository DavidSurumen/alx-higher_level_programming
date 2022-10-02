#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a
parameter."""

if __name__ == '__main__':
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    search = {'q': letter}
    r = requests.post(url, data=search)

    try:
        res = r.json()
        if len(res) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(res['id'], res['name']))
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
