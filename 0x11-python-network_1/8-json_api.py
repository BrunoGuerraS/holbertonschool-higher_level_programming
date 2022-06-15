#!/usr/bin/python3
"""
script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with
the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    data = {
        "q": "" if len(argv) < 2 else argv[1]
    }

    response = requests.post(url, data=data)
    try:
        response = response.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except Exception:
        print("Not a valid JSON")
