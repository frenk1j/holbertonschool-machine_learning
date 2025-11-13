#!/usr/bin/env python3
"""
Module that provides the availableShips function.

This function queries the SWAPI (Star Wars API) to retrieve all starships
that can hold at least a given number of passengers. It handles pagination
and returns a list of ship names that satisfy the requirement.

Functions:
    availableShips(passengerCount): Returns list of ship names that can
    accommodate the given passenger count.
"""

import requests


def availableShips(passengerCount):
    """
    Retrieve starships that can hold at least passengerCount passengers.

    Args:
        passengerCount (int): Minimum number of passengers required.

    Returns:
        list: List of starship names that satisfy the requirement.
              Returns an empty list if none are found.
    """
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data.get("results", []):
            passengers = ship.get("passengers", "0")

            # Remove commas and verify it's numeric
            passengers = passengers.replace(",", "")
            if passengers.isdigit():
                if int(passengers) >= passengerCount:
                    ships.append(ship.get("name"))

        # Go to next page
        url = data.get("next")

    return ships
