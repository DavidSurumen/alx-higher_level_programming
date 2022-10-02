#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using
requests module."""

if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    res = r.content.decode('utf-8')

    print('Body response:')
    print('\t- type: {}'.format(type(res)))
    print('\t- content: {}'.format(res))
