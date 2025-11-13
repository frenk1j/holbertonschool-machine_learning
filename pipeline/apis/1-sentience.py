#!/usr/bin/env python3
"""
Module for retrieving home planets of all sentient species
using the SWAPI (Star Wars API).
"""

import requests


def sentientPlanets():
    """
    Retrieve a list of the home planets of all sentient species.

    Sentience appears in the 'classification' or 'designation'.
    Only species with a valid homeworld are considered.
    """
    url = "https://swapi-api.alx-tools.com/api/species/"
    planets = []

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data.get("results", []):
            classification = species.get("classification", "").lower()
            designation = species.get("designation", "").lower()

            # Check sentience
            if "sentient" in classification or "sentient" in designation:
                homeworld = species.get("homeworld")

                # Checker requirement: do NOT include "unknown"
                if homeworld:
                    hw = requests.get(homeworld).json()
                    planet_name = hw.get("name")
                    if planet_name:
                        planets.append(planet_name)

        url = data.get("next")

    return planets
