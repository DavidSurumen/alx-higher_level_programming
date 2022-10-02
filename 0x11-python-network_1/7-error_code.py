#!/usr/bin/python3
"""Takes in a URL, sends a request and displays response body.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    r = requests.get(url)
    code = r.status_code

    if code >= 400:
        print('Error code: ', code)
    else:
        print(r.content.decode('utf-8'))
