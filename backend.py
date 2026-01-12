"""
author: Aidan Lone, Husnain Sidhu, Muhammad Ali, Malaz Nakaweh, Dabeer Awan
date: January 12, 2026
purpose: Backend programming for computer science culminating performance task
"""
import os
from datetime import datetime as dt
from elements import *
from element_groups import *
from compounds import *

# Decomposition Function
def _decomposition(second_compound: str) -> list:
    """
    Breaks down a compound into its individual elements
    
    Arguments:
        - second_compound (str): The compound that will be broken down

    Returns:
        - broken_down_elements (list): A list containing the two chemical symbols
                                       that made up the original compound.

    Example:

    >>> compound = "Ag-Cl"
    >>> _decomposition(compound)
    ["Ag", "Cl"]
    """

    # The list containing the individual elements are created
    broken_down_elements = second_compound.split("-")

    return broken_down_elements


# Identifying the element groups that each element in the reaction belong to
def identify_element_group(individual_element: str, second_compound: str, 
                           alkali_metal_list: list, alkaline_earth_metal_list: list, halogen_list: list, 
                           transition_metal_list: list) -> Element:
    """
    Takes the decomposed elements and associates them with an appropriate group
    
    Arguments:

        - individual_element (str): The chemical symbol of the isolated element
        - second_compound (str): The chemical formula of the second compound
        - alkali_metal_list (list): A list containing all possible alkali metals
        - alkaline_earth_metal_list (list): A list containinfg all possible alkaline earth metals
        - halogen_list (list): A list containing all possible halogens
        - transition_metal_list (list): A list containing all possible transition metals

    Returns:

        Element - Individual elements, this time associated with a class

    Example:

    >>> compound = "Ag-Cl"
    >>> individual_element = "Be"
    >>> identify_element_group(individual_element, compound)

    Alkaline_Earth_Metal("Be", 4, 1.5, 2, "Beryllium")
    Transition_Metal("Ag", 47, 1.9, 1, "Silver")
    Halogen("Cl", 17, 3.0, 1, "Chlorine")
    """
    
    second_element_list = _decomposition(second_compound)

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

    # Checks if the first element is an alkali metal
    for element in alkali_metal_list:
        if second_element_list[0] in element:
            second_element = Alkali_Metal(element[0], element[1], element[2], element[3], element[4])
            break
        else:
            second_element_list[0] = second_element_list[0]

    # Checks if the first element is an alkaline earth metal
    for element in alkaline_earth_metal_list:
        if second_element_list[0] in element:
            second_element = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3], element[4])
            break
        else:
            second_element_list[0] = second_element_list[0]

    # Checks if the first element is a transition metal
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

    return second_element_list, first_element, second_element, third_element



# Reacting two compounds together
def react(independent_element: str, second_compound: str) -> str:
    """
    Reacts an independent element with a compound, provided its conditions are set.
    This function will make heavy use of the activity series of metals in 
    elements.py to find the index of the metals reacting. The index of the lone
    metal must be higher than the index of the metal in the compound for a
    reaction to be successful.

    Arguments:

        - independent_element (str): The chemical symbol of the independent element
        - second_compound (str): The chemical formula of the compound

    Returns:
        str - A statement stating if the reaction took place or not, with a unique
              message tailored to the specific reaction.

    Example:

    >>> react("Hg", "Na-Cl")
    Reaction cannot occur; Hg (Mercury) is lower on the activity series of metals, 
    compared to Na. NaCl (Sodium Chloride) remains as is.
    >>> react("K", "Au-Cl")
    A vigorous reaction between K (Potassium) (an Alkali Metal) and AuCl 
    (Gold Chloride) occurred, producing Au (Gold) (a Transition Metal) 
    and KCl (Potassium Chloride). The air around it starts to heat up!
    >>> react("K", "K-Br")
    Reaction cannot occur; K (Potassium) cannot react with itself! 
    KBr (Potassium Bromide) remains as is.
    """
    now = dt.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    
    second_element_list, first_element, second_element, third_element = identify_element_group(
                                                                                independent_element,
                                                                                second_compound,
                                                                                alkali_metal_list, 
                                                                                alkaline_earth_metal_list, 
                                                                                halogen_list, transition_metal_list
                                                                                        )
    
    # Storing the chemical symbol of the compound pre-reaction (without the "-") into a separate variable
    initial_compound = f"{second_element_list[:][0]}{second_element_list[:][1]}"

    # Storing the chemical symbol of the individual element pre-reaction into a separate variable
    initial_individual_element = first_element.name

    # Checks the activity series of metals to see if the reaction can occur 
    # (Individual element must have a higher index on the activity series compared to
    # the first element in the compound for it to occur)
    if activity_series.index(first_element.name) > activity_series.index(second_element.name):

        # The chemical symbols are swapped, as per the process of a single-displacement reaction
        first_element.name, second_element_list[0] = second_element_list[0], first_element.name

        # Stores the name of the individual element post-reaction into another variable
        final_individual_element = first_element.name

        # Stores the name of the compound post-reaction into another variable
        final_compound = f"{second_element_list[0]}{second_element_list[1]}"


        # Checks if the newly-isolated element is an alkali metal
        for element in alkali_metal_list:
            if final_individual_element in element:
                element_attributes = Alkali_Metal(element[0], element[1], element[2], element[3], element[4])
                break
            else:
                final_individual_element = final_individual_element

        # Checks if the newly-isolated element is an alkaline earth metal
        for element in alkaline_earth_metal_list:
            if final_individual_element in element:
                element_attributes = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3], element[4])
                break
            else:
                final_individual_element = final_individual_element

        # Checks if the newly-isolated element is a transition metal
        for element in transition_metal_list:
            if final_individual_element in element:
                element_attributes = Transition_Metal(element[0], element[1], element[2], element[3], element[4])
                break
            else:
                final_individual_element = final_individual_element

        # Checks the element groups of each isolated element to print a unique message catered to the energy changes that would occur
        if isinstance(first_element, Alkali_Metal) and isinstance(second_element, Alkali_Metal) and isinstance(third_element, Halogen) and isinstance(element_attributes, Alkali_Metal):

            # Writes this reaction into history.txt
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound} - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound} - {dt_string}\n")

            # Returns a string describing the reaction in-question
            return f"A vigorous reaction between {initial_individual_element} ({first_element.full_name}) (an Alkali Metal) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) (an Alkali Metal) and {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}). Loads of energy are produced!"
        
        elif isinstance(first_element, Alkali_Metal) and isinstance(second_element, Alkaline_Earth_Metal) and isinstance(third_element, Halogen) and isinstance(element_attributes, Alkaline_Earth_Metal):

            # Writes this reaction into history.txt
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound} - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound} - {dt_string}\n")

            # Returns a string describing the reaction in-question
            return f"A vigorous reaction between {initial_individual_element} ({first_element.full_name}) (an Alkali Metal) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) (an Alkaline Earth Metal) and {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}). Don't stand too close!"
    
        elif isinstance(first_element, Alkali_Metal) and isinstance(second_element, Transition_Metal) and isinstance(third_element, Halogen) and isinstance(element_attributes, Transition_Metal):

            # Writes this reaction into history.txt
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound} - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound} - {dt_string}\n")

            # Returns a string describing the reaction in-question
            return f"A vigorous reaction between {initial_individual_element} ({first_element.full_name}) (an Alkali Metal) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) (a Transition Metal) and {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}). The air around it starts to heat up!"

        elif isinstance(first_element, Alkaline_Earth_Metal) and isinstance(second_element, Alkali_Metal) and isinstance(third_element, Halogen) and isinstance(element_attributes, Alkali_Metal):

            # Writes this reaction into history.txt
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}2 - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}2 - {dt_string}\n")

            # Returns a string describing the reaction in-question
            return f"A not-as-vigorous reaction between {initial_individual_element} ({first_element.full_name}) (an Alkaline Earth Metal) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) (an Alkali Metal) and {final_compound}2 ({chemical_name_list[chemical_formula_list.index(final_compound)]}). Some bright flames are observed!"
        
        elif isinstance(first_element, Alkaline_Earth_Metal) and isinstance(second_element, Alkaline_Earth_Metal) and isinstance(third_element, Halogen) and isinstance(element_attributes, Alkaline_Earth_Metal):

            # Writes this reaction into history.txt
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}2 - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}2 - {dt_string}\n")

            # Returns a string describing the reaction in-question
            return f"A not-as-vigorous reaction between {initial_individual_element} ({first_element.full_name}) (an Alkaline Earth Metal) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) (an Alkaline Earth Metal) and {final_compound}2 ({chemical_name_list[chemical_formula_list.index(final_compound)]}). The resulting flames are scorching hot!"
    
        elif isinstance(first_element, Alkaline_Earth_Metal) and isinstance(second_element, Transition_Metal) and isinstance(third_element, Halogen) and isinstance(element_attributes, Transition_Metal):

            # Writes this reaction into history.txt
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}2 - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}2 - {dt_string}\n")

            # Returns a string describing the reaction in-question
            return f"A not-as-vigorous reaction between {initial_individual_element} ({first_element.full_name}) (an Alkaline Earth Metal) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) (a Transition Metal) and {final_compound}2 ({chemical_name_list[chemical_formula_list.index(final_compound)]}). Ultraviolet lights spirals out of the reaction site!"
        
        elif isinstance(first_element, Transition_Metal) and isinstance(second_element, Alkali_Metal) and isinstance(third_element, Halogen) and isinstance(element_attributes, Alkali_Metal):

            # Writes this reaction into history.txt
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}3 - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}3 - {dt_string}\n")

            # Returns a string describing the reaction in-question
            return f"An unpredictable reaction between {initial_individual_element} ({first_element.full_name}) (a Transition Metal) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) (an Alkali Metal) and {final_compound}3 ({chemical_name_list[chemical_formula_list.index(final_compound)]}). The erupting sparks start to tickle!"
        
        elif isinstance(first_element, Transition_Metal) and isinstance(second_element, Alkaline_Earth_Metal) and isinstance(third_element, Halogen) and isinstance(element_attributes, Alkaline_Earth_Metal):

            # Writes this reaction into history.txt
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}3 - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}3 - {dt_string}\n")

            # Returns a string describing the reaction in-question
            return f"An unpredictable reaction between {initial_individual_element} ({first_element.full_name}) (a Transition Metal) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) (an Alkaline Earth Metal) and {final_compound}3 ({chemical_name_list[chemical_formula_list.index(final_compound)]}). The site brims with possibilities!"
    
        elif isinstance(first_element, Transition_Metal) and isinstance(second_element, Transition_Metal) and isinstance(third_element, Halogen) and isinstance(element_attributes, Transition_Metal):

            # Writes this reaction into history.txt
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}3 - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User prompted a reaction between {initial_individual_element} and {first_element.full_name}, producing {final_individual_element} and {final_compound}3 - {dt_string}\n")

            # Returns a string describing the reaction in-question
            return f"A unpredictable reaction between {initial_individual_element} ({first_element.full_name}) (a Transition Metal) and {initial_compound} ({chemical_name_list[chemical_formula_list.index(initial_compound)]}) occurred, producing {final_individual_element} ({element_attributes.full_name}) (a Transition Metal) and {final_compound}3 ({chemical_name_list[chemical_formula_list.index(final_compound)]}). The material starts to feel lukewarm..."
    
    
    elif activity_series.index(first_element.name) == activity_series.index(second_element.name):

        # The reaction is unable to occur; as such, the "final" variables will be the
        # same as the "initial" ones
        final_individual_element = first_element.name
        final_compound = f"{second_element_list[0]}{second_element_list[1]}"

        # Writes this non-reaction into history.txt
        if os.path.isfile("history.txt"):
            with open("history.txt", "a") as f:
                f.write(f"User prompted an impossible reaction between {final_individual_element} and {final_compound} - {dt_string}\n")
        else:
            with open("history.txt", "w") as f:
                f.write(f"User prompted an impossible reaction between {final_individual_element} and {final_compound} - {dt_string}\n")

        # Returns a string, stating that the reaction could not occur
        return f"Reaction cannot occur; {first_element.name} ({first_element.full_name}) cannot react with itself! {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}) remains as is."
        
    else:

        # The reaction is unable to occur; as such, the "final" variables will be the
        # same as the "initial" ones
        final_individual_element = first_element.name
        final_compound = f"{second_element_list[0]}{second_element_list[1]}"

        # Writes this non-reaction into history.txt
        if os.path.isfile("history.txt"):
            with open("history.txt", "a") as f:
                f.write(f"User prompted an impossible reaction between {final_individual_element} and {final_compound} - {dt_string}\n")
        else:
            with open("history.txt", "w") as f:
                f.write(f"User prompted an impossible reaction between {final_individual_element} and {final_compound} - {dt_string}\n")

        # Returns a string, stating that the reaction could not occur
        return f"Reaction cannot occur; {first_element.name} ({first_element.full_name}) is lower on the activity series of metals, compared to {second_element.name}. {final_compound} ({chemical_name_list[chemical_formula_list.index(final_compound)]}) remains as is."
        