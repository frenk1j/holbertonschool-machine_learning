#!/usr/bin/env python3
"""
Script that prints the location of a GitHub user
or the rate limit reset time.
"""

import sys
import requests
import time


def get_location(url):
    """
    Return a user's location or a rate-limit message.

    Args:
        url (str): GitHub API URL.

    Returns:
        str: location, "Not found", or "Rate limit Xmin".
    """
    response = requests.get(url)

    # User not found
    if response.status_code == 404:
        return "Not found"

    # Rate limit hit
    if response.status_code == 403:
        reset = int(response.headers.get("X-RateLimit-Reset", 0))
        now = int(time.time())
        minutes = int((reset - now) / 60)
        if minutes < 0:
            minutes = 0
        return f"Rate limit {minutes}min"

    # Normal response
    data = response.json()
    location = data.get("location")

    return location


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    result = get_location(sys.argv[1])
    if result is not None:
        print(result)
