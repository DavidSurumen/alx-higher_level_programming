#!/usr/bin/python3
"""Takes in a URL and an email addr, sends a POST request with
the email as a parameter, and displays reponse body."""

if __name__ == '__main__':
    import requests
    import sys

    # get url and email
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    r = requests.post(url, data=email)
    print(r.content.decode('utf-8'))
