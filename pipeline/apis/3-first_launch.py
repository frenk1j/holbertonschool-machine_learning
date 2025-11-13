#!/usr/bin/env python3
"""
Script that retrieves and displays the very first SpaceX launch
with the following information:

<launch name> (<date>) <rocket name> - <launchpad name> (<locality>)
"""

import requests
from datetime import datetime
import pytz


def get_first_launch():
    """
    Retrieve the first recorded SpaceX launch using date_unix.

    Returns:
        str: Formatted string with the required launch information.
    """
    launches_url = "https://api.spacexdata.com/v4/launches"

    launches = requests.get(launches_url).json()

    # Sort by date_unix (ascending)
    launches.sort(key=lambda x: x.get("date_unix", float("inf")))

    first = launches[0]

    launch_name = first.get("name")
    date_unix = first.get("date_unix")
    rocket_id = first.get("rocket")
    launchpad_id = first.get("launchpad")

    # Convert date_unix to local time ISO format
    local_dt = datetime.fromtimestamp(date_unix).astimezone()
    date_str = local_dt.isoformat()

    # Fetch rocket name
    rocket = requests.get(
        f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    ).json()
    rocket_name = rocket.get("name")

    # Fetch launchpad name + locality
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
