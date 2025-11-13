#!/usr/bin/env python3
"""
Script that retrieves and displays the first upcoming SpaceX launch.
"""

import requests
from datetime import datetime, timezone


def get_first_launch():
    """
    Retrieve the nearest upcoming SpaceX launch using date_unix.
    Sorted ascending. Works with both mock and official API.

    Returns:
        str: Formatted string with required launch information.
    """
    launches_url = "https://api.spacexdata.com/v4/launches/upcoming"
    launches = requests.get(launches_url).json()

    # Sort by date_unix ascending
    launches.sort(key=lambda x: x.get("date_unix", float("inf")))

    first = launches[0]

    launch_name = first.get("name")
    date_unix = first.get("date_unix")
    rocket_id = first.get("rocket")
    launchpad_id = first.get("launchpad")

    # Convert date_unix to UTC ISO format with +00:00
    date_str = datetime.fromtimestamp(date_unix, tz=timezone.utc).isoformat()

    # Fetch rocket name
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
