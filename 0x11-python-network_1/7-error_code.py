#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""
import requests
from sys import argv


def fetch_url_content(url):
    """
    Function that fetches URL content and handles HTTP errors
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.text
    except requests.exceptions.HTTPError as err:
        return f"Error code: {err.response.status_code}"


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <URL>")
    else:
        url = argv[1]
        content = fetch_url_content(url)
        print(content)
