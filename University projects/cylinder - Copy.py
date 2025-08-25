# A program to give us a surface area of the cylinder
# Luyanda Ntombela
# 17 April 2025

from math import pi, pow

def surface_area (diameter,height) : # function to calculate surface Area
        surface_area = 2*pi*pow((0.5*diameter),2) + pi*diameter*height #formula for surface area
        return surface_area

def main():
        height = float(input("Enter the height of the cylinder:\n")) # height of the cylinder
        diameter = float(input("Enter the diameter of the base:\n")) # diameter of the cyinder
        if diameter <= 0 or height <= 0:
                print("The height and diameter must be greater than zero.") # The is no negative Surface Area
        else:
                print("The surface area is",round(surface_area (diameter,height),2),end='.')
    
if __name__ == '__main__':
        main()
