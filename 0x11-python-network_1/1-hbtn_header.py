#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL, and displays
the values of the X-Request-Id header variable."""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print('{}'.format(response.getheader('X-Request-Id')))
