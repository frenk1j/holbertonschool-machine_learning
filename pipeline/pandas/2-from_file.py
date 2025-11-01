#!/usr/bin/env python3
"""Module that loads data from a file as a pandas DataFrame."""

import pandas as pd


def from_file(filename, delimiter):
    """
    Loads data from a file as a pandas DataFrame.

    Args:
        filename (str): The path to the file to load.
        delimiter (str): The column separator used in the file.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    df = pd.read_csv(filename, delimiter=delimiter)
    return df
