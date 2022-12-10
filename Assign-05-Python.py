#!/usr/bin/env python3

# Created By: Nathan
# Date: Dec. 8, 2022
# This program calculates the surface area of a cylinder,
# the circumference and area of the circles on the top
# and bottom it then displays it

import math

# Function to calculate the area of the circles
def area_circle_calculate(radius):
    # Area of a circle formula
    area = math.pi * radius**2
    # Round the area to 2 digits
    area_round = round(area, 2)
    # Return area_round to main()
    return area_round


# Function to calculate the circumference of the circles
def circumference_calculate(radius):
    # Circumference of a circle formula
    circumference = 2 * math.pi * radius
    # Round the circumference to 2 digits
    circumference_round = round(circumference, 2)
    # return circumference_round to main()
    return circumference_round


# Function to calculate the surface area of the cylinder
def surface_area_calculate(radius, height):
    # surface_area of a circle formula
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius**2
    # Round the surface_area to 2 digits
    surface_area_round = round(surface_area, 2)
    # return surface_area_round to main()
    return surface_area_round


def main():
    # While true statement for the user to be able to restart the program
    while True:
        # Gets user_radius_str from the user
        user_radius_str = input("Enter the radius of the cylinder: ")
        # Gets user_height_str from the user
        user_height_str = input("Enter the height of the cylinder: ")
        # Gets user_units from the user
        user_units = input("Enter the type of units you want to use: ")
        # A try catch to to catch any invalid inputs
        try:
            user_radius = float(user_radius_str)
            user_height = float(user_height_str)
        except:
            # If they entered a invalid input then display this
            print("You must enter a valid number.")
        else:
            # If they entered a number less than 0
            if user_radius > 0 and user_height > 0:
                # Call circumference_calculate(user_radius)
                circumference = circumference_calculate(user_radius)
                # Call surface_area_calculate(user_radius, user_height)
                surface_area = surface_area_calculate(user_radius, user_height)
                # Call area_circle_calculate(user_radius)
                area_circle = area_circle_calculate(user_radius)
                # Display the the surface area, area and circumference
                print(
                    f"The surface area of the cylinder is {surface_area} {user_units}²."
                    f"The circumference of the circle is {circumference} {user_units}."
                    f"The area of the circles of the is {area_circle} {user_units}²."
                )
            else:
                print("Enter a number greater than 0")
            # Asks the user if they want to enter two new numbers
            play_again = input("Do you want to enter two new numbers?(y or n): ")
            # If they don't respond with either Y or YES then loop back, otherwise end the program
            if play_again.upper() != "Y" and play_again.upper() != "YES":
                break


if __name__ == "__main__":
    main()
