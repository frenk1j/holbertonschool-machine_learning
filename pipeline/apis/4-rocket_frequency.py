#!/usr/bin/env python3
"""
Uses the (unofficial) SpaceX API to count the number of launches per rocket.
"""

import requests


if __name__ == "__main__":
    launches_url = "https://api.spacexdata.com/v4/launches"
    rockets_url = "https://api.spacexdata.com/v4/rockets"

    launches = requests.get(launches_url).json()
    rockets = requests.get(rockets_url).json()

    # Map rocket IDs to names
    rocket_names = {r["id"]: r["name"] for r in rockets}

    rocket_dict = {}
    for launch in launches:
        rocket_id = launch.get("rocket")
        rocket_name = rocket_names.get(rocket_id)
        if rocket_name:
            rocket_dict[rocket_name] = rocket_dict.get(rocket_name, 0) + 1

    # Sort alphabetically, then by count descending
    rocket_list = sorted(rocket_dict.items(), key=lambda kv: (-kv[1], kv[0]))
    for rocket, count in rocket_list:
        print(f"{rocket}: {count}")
