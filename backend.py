"""
author: Aidan Lone
date: December 14, 2025
purpose: Backend programming for computer science culminating performance task
"""
from elements import *
from element_groups import *

# Decomposition Function
def _decomposition(independent_element: str, second_compound: str) -> list:

    secondary_individual_elements = second_compound.split("-")

    return independent_element, secondary_individual_elements

def identify_element_group(independent_element: str, second_compound: str, alkali_metal_list: list, alkaline_earth_metal_list: list, halogen_list: list) -> Element:
    individual_element, second_element_list = _decomposition(independent_element, second_compound)

# Converting classes for the independent element

    # Checks if the element is an alkali metal
    for element in alkali_metal_list:
        if individual_element in element:
            first_element = Alkali_Metal(element[0], element[1], element[2], element[3])
            break
        else:
            individual_element = individual_element

    # Checks if the element is an alkaline earth metal
    for element in alkaline_earth_metal_list:
        if individual_element in element:
            first_element = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3])
            break
        else:
            individual_element = individual_element


# Converting classes for the second compound

    # Checks if the element is an alkali metal
    for element in alkali_metal_list:
        if second_element_list[0] in element:
            second_element = Alkali_Metal(element[0], element[1], element[2], element[3])
            break
        else:
            second_element_list[0] = second_element_list[0]

    # Checks if the element is an alkaline earth metal
    for element in alkaline_earth_metal_list:
        if second_element_list[0] in element:
            second_element = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3])
            break
        else:
            second_element_list[0] = second_element_list[0]

    # Checks if the element is a halogen
    for element in halogen_list:
        if second_element_list[1] in element:
            third_element = Halogen(element[0], element[1], element[2], element[3])
            break
        else:
            second_element_list[1] = second_element_list[1]

    return second_element_list, first_element, second_element, third_element
            
# Reacting two compounds together
def react(independent_element: str, second_compound: str) -> str:
    
    second_element_list, first_element, second_element, third_element = identify_element_group(
                                                                                independent_element,
                                                                                second_compound,
                                                                                alkali_metal_list, 
                                                                                alkaline_earth_metal_list, 
                                                                                halogen_list
                                                                                        )
    
    if isinstance(first_element, Element) and isinstance(second_element, Element):
        if activity_series.index(first_element.name) > activity_series.index(second_element.name):
            first_element.name, second_element_list[0] = second_element_list[0], first_element.name
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"
        else:
            print(f"Reaction cannot occur; {first_element.name} is lower on the activity series of" \
                  f" metals, compared to {second_element.name}.")

    return final_individual_element, final_compound
            

                                                                            

