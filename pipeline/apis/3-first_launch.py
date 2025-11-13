#!/usr/bin/env python3
"""
Script that retrieves and displays the very first SpaceX launch.
"""

import requests
from datetime import datetime, timezone


def get_first_launch():
    """
    Retrieve the first recorded SpaceX launch using date_unix.

    Returns:
        str: Formatted launch information.
    """
    launches_url = "https://api.spacexdata.com/v4/launches"

    launches = requests.get(launches_url).json()

    # Sort launches by date_unix ascending
    launches.sort(key=lambda x: x.get("date_unix", float("inf")))

    first = launches[0]

    # Extract information
    launch_name = first.get("name")
    date_unix = first.get("date_unix")
    rocket_id = first.get("rocket")
    launchpad_id = first.get("launchpad")

    # Convert unix timestamp to UTC ISO8601 formatted date
    date_str = datetime.fromtimestamp(date_unix, tz=timezone.utc).isoformat()

    # Fetch rocket info
    rocket = requests.get(
        f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    ).json()
    rocket_name = rocket.get("name")

    # Fetch launchpad info
    launchpad = requests.get(
        f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    ).json()
    launchpad_name = launchpad.get("name")
    locality = launchpad.get("locality")

    return (
        f"{launch_name} ({date_str}) "
        f"{rocket_name} - {launchpad_name} ({locality})"
    )


if __name__ == "__main__":
    print(get_first_launch())
