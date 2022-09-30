#!/usr/bin/python3
"""Takes a URL, sends a request to the URL, displays the response body
and handles HTTPError."""

if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print('Error code: ', e.code)
