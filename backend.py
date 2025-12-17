"""
author: Aidan Lone
date: December 14, 2025
purpose: Scrapwork for computer science culminating performance task
"""
from elements import *
from element_groups import *


# Decomposition Function
def decomposition(first_compound: str, second_compound: str) -> str:

    individual_elements = first_compound.split("-")
    secondary_individual_elements = second_compound.split("-")

    return individual_elements, secondary_individual_elements


def react(first_compound: str, second_compound: str, alkali_metal_list: list, alkaline_earth_metal_list: list, halogen_list: list) -> str:
    element_list, second_element_list = decomposition(first_compound, second_compound)

# Converting classes for the first compound
    for element in alkali_metal_list:
        if element_list[0] in element:
            first_element = Alkali_Metal(element[0], element[1], element[2], element[3])
            break
        else:
            element_list[0] = element_list[0]

    for element in alkaline_earth_metal_list:
        if element_list[0] in element:
            first_element = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3])
            break
        else:
            element_list[0] = element_list[0]

    for element in halogen_list:
        if element_list[1] in element:
            second_element = Halogen(element[0], element[1], element[2], element[3])
            break
        else:
            element_list[1] = element_list[1]

# Converting classes for the second compound
    for element in alkali_metal_list:
        if second_element_list[0] in element:
            third_element = Alkali_Metal(element[0], element[1], element[2], element[3])
            break
        else:
            second_element_list[0] = second_element_list[0]

    for element in alkaline_earth_metal_list:
        if second_element_list[0] in element:
            third_element = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3])
            break
        else:
            second_element_list[0] = second_element_list[0]

    for element in halogen_list:
        if second_element_list[1] in element:
            fourth_element = Halogen(element[0], element[1], element[2], element[3])
            break
        else:
            second_element_list[1] = second_element_list[1]

    if isinstance(first_element, Alkali_Metal) and isinstance(third_element, Alkaline_Earth_Metal):
        return True
    else:
        return False

    

    

print(react("Na-F", "Mg-Cl", alkali_metal_list, alkaline_earth_metal_list, halogen_list))

