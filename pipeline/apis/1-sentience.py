#!/usr/bin/env python3
"""
Module for retrieving home planets of all sentient species
using the SWAPI (Star Wars API).

A sentient species is identified when the word 'sentient'
appears either in the 'classification' or in the 'designation'.
"""

import requests


def sentientPlanets():
    """
    Retrieve a list of the home planets of all sentient species.

    Sentience is defined by the presence of the word 'sentient'
    in the classification or designation attributes.

    Returns:
        list: List of planet names (strings) for all sentient species.
              Includes "unknown" when the API returns None.
    """
    url = "https://swapi-api.alx-tools.com/api/species/"
    planets = []

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data.get("results", []):
            classification = species.get("classification", "").lower()
            designation = species.get("designation", "").lower()

            # Check if species is sentient
            if "sentient" in classification or "sentient" in designation:
                homeworld_url = species.get("homeworld")

                if homeworld_url:
                    hw_response = requests.get(homeworld_url).json()
                    planets.append(hw_response.get("name", "unknown"))
                else:
                    planets.append("unknown")

        # Continue to next page
        url = data.get("next")

    return planets
