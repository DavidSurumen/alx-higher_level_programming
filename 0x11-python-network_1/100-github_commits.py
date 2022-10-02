#!/usr/bin/python3
"""Takes Github credentials and uses Github API to display user
id."""

if __name__ == '__main__':
    import requests
    import sys

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    r = requests.get(url)
    commits = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(commits[i]['sha'],
                  commits[i]['commit']['author']['name']
                ))
    except IndexError:
        pass
