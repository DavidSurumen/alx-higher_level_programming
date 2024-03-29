#!/usr/bin/python3
"""Takes a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the
response."""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()

    print('{}'.format(body.decode("utf-8")))
