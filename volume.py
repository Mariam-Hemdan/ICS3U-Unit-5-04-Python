#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : November 2019
# This function calculate volume of cylinder

import math


def calculate_volume(radius, height):
    # calculate volume of cylinder

    # process
    volume = math.pi*pow(radius, 2)*height
    return volume


def main():
    # this function gets the radius and the height

    # input
    radius = (input("Enter the radius:"))
    height = (input("Enter the height:"))
    print("")

    # process
    try:
        radius_as_int = int(radius)
        height_as_int = int(height)
        solution = calculate_volume(height=height_as_int, radius=radius_as_int)
        print("The solutions is {0}".format(solution))
    except Exception:
        print("Theses are not integers")


if __name__ == "__main__":
    main()
