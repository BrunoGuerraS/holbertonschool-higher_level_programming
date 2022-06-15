#!/usr/bin/python3
"""
The Holberton School staff evaluates candidates
applying for a back-end position with multiple
technical challenges
"""
import requests
from sys import argv


def api_github(path="", params=""):
    """ Request to api of github """
    api_github = "https://api.github.com"
    url = api_github + "/" + path + params
    response = requests.get(url)
    return response


def trigger():
    [repo, owner] = argv[1:]

    commits = api_github("repos/{}/{}/commits?per_page=10".format(owner, repo))
    commits = commits.json()
    for commit in commits:
        print("{}: {}".format(
            commit.get("sha"),
            commit.get("commit").get("author").get("name")
        ))


if __name__ == "__main__":
    trigger()
