from common_functions import *

#Duplicate_example
area = calculate_area(5, 3)
perimeter = calculate_perimeter(5, 3)
volume = calculate_volume(5, 3, 2)
surface_area = calculate_surface_area(5, 3, 2)


# Duplicate code: calculate_area and calculate_perimeter functions have similar calculations.
area, perimeter = calculate_area_perimeter(5, 3)
