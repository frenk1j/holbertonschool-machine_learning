#!/usr/bin/env python3
"""
Test file for get_location()
"""

get_location = __import__('2-user_location').get_location

if __name__ == "__main__":
    print(get_location("https://api.github.com/users/Holbertonschoolml"))
