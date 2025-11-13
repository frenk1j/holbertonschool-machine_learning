#!/usr/bin/env python3
"""
Module that retrieves and displays the first upcoming SpaceX launch.

Uses the SpaceX public API to fetch and format data about the next launch,
including its name, scheduled local time, rocket, and launch location.
"""

import requests


def get_first_launch():
    """
    Retrieve information about the nearest upcoming SpaceX launch.

    The function fetches all upcoming launches from the SpaceX API,
    sorts them by scheduled time, and returns details about the earliest one.

    Returns:
        str: A formatted string with the launch name, date (local time),
        rocket name, and launchpad information.
        Example output:
            "Galaxy 33 (15R) & 34 (12R) (2022-10-08T19:05:00-04:00)
             Falcon 9 - CCSFS SLC 40 (Cape Canaveral)"
    """
    launches_url = "https://api.spacexdata.com/v4/launches/upcoming"
    launches = requests.get(launches_url).json()

    # Sort launches by date_unix ascending
    launches.sort(key=lambda x: x.get("date_unix", float("inf")))

    first = launches[0]

    launch_name = first.get("name")
    date_local = first.get("date_local")
    rocket_id = first.get("rocket")
    launchpad_id = first.get("launchpad")

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
        f"{launch_name} ({date_local}) "
        f"{rocket_name} - {launchpad_name} ({locality})"
    )


if __name__ == "__main__":
    print(get_first_launch())
