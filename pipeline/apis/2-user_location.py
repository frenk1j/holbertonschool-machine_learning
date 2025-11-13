#!/usr/bin/env python3
"""
Script that retrieves and prints the location of a GitHub user
using the GitHub API.

Usage:
    ./2-user_location.py <full_api_url>
"""

import sys
import requests
import time


def get_location(url):
    """
    Retrieve the location of a GitHub user from the provided API URL.

    Args:
        url (str): Full GitHub API URL for a user.

    Returns:
        str: Location string, "Not found", or rate-limit message.
    """
    response = requests.get(url)

    if response.status_code == 404:
        return "Not found"

    if response.status_code == 403:
        reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
        current_time = int(time.time())
        minutes = int((reset_time - current_time) / 60)
        if minutes < 0:
            minutes = 0
        return f"Reset in {minutes} min"

    data = response.json()
    return data.get("location")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    api_url = sys.argv[1]
    result = get_location(api_url)

    if result:
        print(result)
