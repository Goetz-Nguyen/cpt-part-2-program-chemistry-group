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

def identify_element_group(independent_element: str, second_compound: str, alkali_metal_list: list, alkaline_earth_metal_list: list, halogen_list: list, transition_metal_list: list) -> Element:
    individual_element, second_element_list = _decomposition(independent_element, second_compound)

# Converting classes for the independent element

    # Checks if the element is an alkali metal
    for element in alkali_metal_list:
        if individual_element in element:
            first_element = Alkali_Metal(element[0], element[1], element[2], element[3], element[4])
            break
        else:
            individual_element = individual_element

    # Checks if the element is an alkaline earth metal
    for element in alkaline_earth_metal_list:
        if individual_element in element:
            first_element = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3], element[4])
            break
        else:
            individual_element = individual_element

    # Checks if the element is a transition metal
    for element in transition_metal_list:
        if individual_element in element:
            first_element = Transition_Metal(element[0], element[1], element[2], element[3], element[4])
            break
        else:
            individual_element = individual_element


# Converting classes for the second compound

    # Checks if the element is an alkali metal
    for element in alkali_metal_list:
        if second_element_list[0] in element:
            second_element = Alkali_Metal(element[0], element[1], element[2], element[3], element[4])
            break
        else:
            second_element_list[0] = second_element_list[0]

    # Checks if the element is an alkaline earth metal
    for element in alkaline_earth_metal_list:
        if second_element_list[0] in element:
            second_element = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3], element[4])
            break
        else:
            second_element_list[0] = second_element_list[0]

    # Checks if the element is a transition metal
    for element in transition_metal_list:
        if second_element_list[0] in element:
            second_element = Transition_Metal(element[0], element[1], element[2], element[3], element[4])
            break
        else:
            second_element_list[0] = second_element_list[0]

    # Checks if the second element is a halogen
    for element in halogen_list:
        if second_element_list[1] in element:
            third_element = Halogen(element[0], element[1], element[2], element[3], element[4])
            break
        else:
            second_element_list[1] = second_element_list[1]

    return second_element_list, first_element, second_element
            
# Reacting two compounds together
def react(independent_element: str, second_compound: str) -> str:
    
    second_element_list, first_element, second_element = identify_element_group(
                                                                                independent_element,
                                                                                second_compound,
                                                                                alkali_metal_list, 
                                                                                alkaline_earth_metal_list, 
                                                                                halogen_list, transition_metal_list
                                                                                        )
    
    if isinstance(first_element, Alkali_Metal) and (isinstance(second_element, Alkali_Metal) or isinstance(second_element, Alkaline_Earth_Metal) or isinstance(second_element, Transition_Metal)):
        initial_compound = f"{second_element_list[:][0]}{second_element_list[:][1]}"
        initial_individual_element = first_element.name

        if activity_series.index(first_element.name) > activity_series.index(second_element.name):
            first_element.name, second_element_list[0] = second_element_list[0], first_element.name
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"


            # Checks if the element is an alkali metal
            for element in alkali_metal_list:
                if final_individual_element in element:
                    element_attributes = Alkali_Metal(element[0], element[1], element[2], element[3], element[4])
                    break
            else:
                final_individual_element = final_individual_element

            # Checks if the element is an alkaline earth metal
            for element in alkaline_earth_metal_list:
                if final_individual_element in element:
                    element_attributes = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3], element[4])
                    break
                else:
                    final_individual_element = final_individual_element

            # Checks if the element is a transition metal
            for element in transition_metal_list:
                if final_individual_element in element:
                    element_attributes = Transition_Metal(element[0], element[1], element[2], element[3], element[4])
                    break
                else:
                    final_individual_element = final_individual_element


            return f"A vigorous reaction between {initial_individual_element} ({first_element.full_name}) (an {str(type(first_element)).split('\'')[1].split('.')[1].replace("_", " ")}) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) and {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}). Loads of energy are produced!."
        
        elif activity_series.index(first_element.name) == activity_series.index(second_element.name):
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"

            return f"Reaction cannot occur; {first_element.name} ({first_element.full_name}) cannot react with itself! {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}) remains as is."
        
        else:
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"

            return f"Reaction cannot occur; {first_element.name} ({first_element.full_name}) is lower on the activity series of metals, compared to {second_element.name}. {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}) remains as is."
        
    elif isinstance(first_element, Alkaline_Earth_Metal) and (isinstance(second_element, Alkali_Metal) or isinstance(second_element, Alkaline_Earth_Metal) or isinstance(second_element, Transition_Metal)):
        initial_compound = f"{second_element_list[:][0]}{second_element_list[:][1]}"
        initial_individual_element = first_element.name
        
        if activity_series.index(first_element.name) > activity_series.index(second_element.name):
            first_element.name, second_element_list[0] = second_element_list[0], first_element.name
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"


            # Checks if the element is an alkali metal
            for element in alkali_metal_list:
                if final_individual_element in element:
                    element_attributes = Alkali_Metal(element[0], element[1], element[2], element[3], element[4])
                    break
            else:
                final_individual_element = final_individual_element

            # Checks if the element is an alkaline earth metal
            for element in alkaline_earth_metal_list:
                if final_individual_element in element:
                    element_attributes = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3], element[4])
                    break
                else:
                    final_individual_element = final_individual_element

            # Checks if the element is a transition metal
            for element in transition_metal_list:
                if final_individual_element in element:
                    element_attributes = Transition_Metal(element[0], element[1], element[2], element[3], element[4])
                    break
                else:
                    final_individual_element = final_individual_element


            return f"A not-as-vigorous reaction between {initial_individual_element} ({first_element.full_name}) (an {str(type(first_element)).split('\'')[1].split('.')[1].replace("_", " ")}) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) and {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}). Some bright flames are observed!"
        
        elif activity_series.index(first_element.name) == activity_series.index(second_element.name):
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"

            return f"Reaction cannot occur; {first_element.name} ({first_element.full_name}) cannot react with itself! {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}) remains as is."
        
        else:
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"

            return f"Reaction cannot occur; {first_element.name} ({first_element.full_name}) is lower on the activity series of metals, compared to {second_element.name}. {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}) remains as is."
        
    elif isinstance(first_element, Transition_Metal) and (isinstance(second_element, Alkali_Metal) or isinstance(second_element, Alkaline_Earth_Metal) or isinstance(second_element, Transition_Metal)):
        initial_compound = f"{second_element_list[:][0]}{second_element_list[:][1]}"
        initial_individual_element = first_element.name
        
        if activity_series.index(first_element.name) > activity_series.index(second_element.name):
            first_element.name, second_element_list[0] = second_element_list[0], first_element.name
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"


            # Checks if the element is an alkali metal
            for element in alkali_metal_list:
                if final_individual_element in element:
                    element_attributes = Alkali_Metal(element[0], element[1], element[2], element[3], element[4])
                    break
            else:
                final_individual_element = final_individual_element

            # Checks if the element is an alkaline earth metal
            for element in alkaline_earth_metal_list:
                if final_individual_element in element:
                    element_attributes = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3], element[4])
                    break
                else:
                    final_individual_element = final_individual_element

            # Checks if the element is a transition metal
            for element in transition_metal_list:
                if final_individual_element in element:
                    element_attributes = Transition_Metal(element[0], element[1], element[2], element[3], element[4])
                    break
                else:
                    final_individual_element = final_individual_element


            return f"A variable reaction between {initial_individual_element} ({first_element.full_name}) (an {str(type(first_element)).split('\'')[1].split('.')[1].replace("_", " ")}) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) and {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}). It's brimming with possibilities!"
        
        elif activity_series.index(first_element.name) == activity_series.index(second_element.name):
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"

            return f"Reaction cannot occur; {first_element.name} ({first_element.full_name}) cannot react with itself! {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}) remains as is."
        
        else:
            final_individual_element = first_element.name
            final_compound = f"{second_element_list[0]}{second_element_list[1]}"

            return f"Reaction cannot occur; {first_element.name} ({first_element.full_name}) is lower on the activity series of metals, compared to {second_element.name}. {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}) remains as is."

    
            

                                                                            

print(react("Ca", "Mg-Cl"))