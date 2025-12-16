"""
author: Aidan Lone
date: December 14, 2025
purpose: Scrapwork for computer science culminating performance task
"""

# Hydrogen single bonds
hydrogen_hydrogen_bond = 432
hydrogen_fluorine_bond = 565
hydrogen_chlorine_bond = 427
hydrogen_bromine_bond = 363
hydrogen_iodine_bond = 295

# Carbon single bonds
carbon_hydrogen_bond = 413
carbon_carbon_bond = 347
carbon_nitrogen_bond = 305
carbon_oxygen_bond = 358
carbon_fluorine_bond = 485
carbon_chlorine_bond = 339
carbon_bromine_bond = 276
carbon_iodine_bond = 240
carbon_sulfur_bond = 259

# Nitrogen single bonds
nitrogen_hydrogen_bond = 391
nitrogen_nitrogen_bond = 160
nitrogen_fluorine_bond = 272
nitrogen_chlorine_bond = 200
nitrogen_bromine_bond = 243
nitrogen_oxygen_bond = 201

# Oxygen single bonds
oxygen_hydrogen_bond = 467
oxygen_oxygen_bond = 146
oxygen_fluorine_bond = 190
oxygen_chlorine_bond = 203
oxygen_iodine_bond = 234

# Fluorine single bonds
fluorine_fluorine_bond = 154
fluorine_chlorine_bond = 253
fluorine_bromine_bond = 237

# Chlorine single bonds
chlorine_chlorine_bond = 239
chlorine_bromine_bond = 218

# Bromine single bonds
bromine_bromine_bond = 193

# Iodine single bonds
iodine_iodine_bond = 149
iodine_chlorine_bond = 208
iodine_bromine_bond = 175

# Sulfur single bonds
sulfur_hydrogen_bond = 347
sulfur_fluorine_bond = 327
sulfur_chlorine_bond = 253
sulfur_bromine_bond = 218
sulfur_sulfur_bond = 266

# Silicon single bonds
silicon_silicon_bond = 340
silicon_hydrogen_bond = 393
silicon_carbon_bond = 360
silicon_oxygen_bond = 452

# Double bonds
carbon_carbon_double_bond = 614
oxygen_oxygen_double_bond = 495
carbon_oxygen_double_bond_1 = 745 # When not in carbon dioxide
carbon_oxygen_double_bond_2 = 799 # When in carbon dioxide
nitrogen_oxygen_double_bond = 607
nitrogen_nitrogen_double_bond = 418
carbon_nitrogen_double_bond = 615

# Triple bonds
carbon_carbon_triple_bond = 839
carbon_oxygen_triple_bond = 1072
nitrogen_nitrogen_triple_bond = 941
carbon_nitrogen_triple_bond = 891

# Alkali Metal Database
lithium = ("Li", 3, 1.0, 1)
sodium = ("Na", 11, 0.9, 1)
potassium = ("K", 19, 0.8, 1)
rubidium = ("Rb", 37, 0.8, 1)
cesium = ("Cs", 55, 0.7, 1)
francium = ("Fr", 87, 0.7, 1)

# Alkaline Earth Metal Database
beryllium = ("Be", 4, 1.5, 2)
magnesium = ("Mg", 12, 1.2, 2)
calcium = ("Ca", 20, 1.0, 2)
strontium = ("Sr", 38, 1.0, 2)
barium = ("Ba", 56, 0.9, 2)
radium = ("Ra", 88, 0.9, 2)

# Halogen Data Base
fluorine = ("F", 9, 4.0, 1)
chlorine = ("Cl", 17, 3.0, 1)
bromine = ("Br", 35, 2.8, 1)
iodine = ("I", 53, 2.5, 1)
astatine = ("At", 85, 2.2, 1)

# Alkali Metal List
alkali_metal_list = [lithium, sodium, potassium, rubidium, cesium, francium]

# Alkaline Earth Metal List
alkaline_earth_metal_list = [beryllium, magnesium, calcium, strontium, barium, radium]

# Halogen List
halogen_list = [fluorine, chlorine, bromine, iodine, astatine]

# Activity Series of Metals
activity_series = ['Pt', 'Au', 'Ag', 'Hg', 'Cu', 'Bi', 'Sb', 'H', 'Pb', 'Sn', 'Ni', 'Co', 'Cd', 'Fe', 'Cr', 'Zn', 'Mn', 'Al', 'Mg', 'Ca', 'Sr', 'Ba', 'Li', 'Na', 'K']

# Compound database
methane = {"Compound Name": "methane", "Number of Atoms": 5, "Type of Compound": "Organic (Alkane)", "Enthalpy of Formation": -74.4}
carbon_dioxide = {"Compound Name": "carbon dioxide", "Number of Atoms": 3, "Type of Compound": "Covalent", "Enthalpy of Formation": -393.5}
ammonia = {"Compound Name": "ammonia", "Number of Atoms": 4, "Type of Compound": "Covalent", "Enthalpy of Formation": -45.9}

# Class system
class Element:

    def __init__(self, name: str, atomic_number: int, electronegativity: float, bonding_capacity: int) -> None:
        self.name = name
        self.atomic_number = atomic_number
        self.electronegativity = electronegativity
        self.bonding_capacity = bonding_capacity

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: (Unknown)\n" \
               f"Atomic Number {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}"
   

# Alkali Metal Class
class Alkali_Metal(Element):

    def __init__(self, name: str, atomic_number: int, electronegativity: float, bonding_capacity: int) -> None:
        super().__init__(name, atomic_number, electronegativity, bonding_capacity)

    def declare_element(self):
        print(f"A shiny instance of elemental {self.name} is observed! Be careful around this one!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Alkali Metal\n" \
               f"Atomic Number {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}"
   
# Alkaline Earth Metal Class
class Alkaline_Earth_Metal(Element):

    def __init__(self, name: str, atomic_number: int, electronegativity: float, bonding_capacity: int) -> None:
        super().__init__(name, atomic_number, electronegativity, bonding_capacity)

    def declare_element(self):
        print(f"An instance of elemental {self.name} is observed! Be careful, it's a fire hazard!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Alkaline Earth Metal\n" \
               f"Atomic Number {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}"
   
# Halogen Class
class Halogen(Element):

    def __init__(self, name: str, atomic_number: int, electronegativity: float, bonding_capacity: int) -> None:
        super().__init__(name, atomic_number, electronegativity, bonding_capacity)

    def declare_element(self):
        print(f"An instance of elemental {self.name} is observed! It's eager to react!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Halogen\n" \
               f"Atomic Number {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}"
   
# Noble Gas Class
class Noble_Gas(Element):

    def __init__(self, name: str, atomic_number: int, electronegativity: float, bonding_capacity: int) -> None:
        super().__init__(name, atomic_number, electronegativity, bonding_capacity)

    def declare_element(self):
        print(f"An instance of elemental {self.name} is observed! It's visibly dormant!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Noble Gas\n" \
               f"Atomic Number {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}"

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
        else:
            element_list[0] = element_list[0]

    for element in alkaline_earth_metal_list:
        if element_list[0] in element:
            first_element = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3])
        else:
            element_list[0] = element_list[0]

    for element in halogen_list:
        if element_list[1] in element:
            second_element = Halogen(element[0], element[1], element[2], element[3])
        else:
            element_list[1] = element[1]

# Converting classes for the second compound
    for element in alkali_metal_list:
        if second_element_list[0] in element:
            third_element = Alkali_Metal(element[0], element[1], element[2], element[3])
        else:
            second_element_list[0] = second_element_list[0]

    for element in alkaline_earth_metal_list:
        if second_element_list[0] in element:
            third_element = Alkaline_Earth_Metal(element[0], element[1], element[2], element[3])
        else:
            second_element_list[0] = second_element_list[0]

    for element in halogen_list:
        if second_element_list[1] in element:
            fourth_element = Halogen(element[0], element[1], element[2], element[3])
        else:
            second_element_list[1] = second_element_list[1]

    if isinstance(second_element_list, Halogen) and isinstance(third_element, Alkali_Metal):
        return True
    else:
        return False

    

    

print(react("C-Cl", "Na-Cl", alkali_metal_list, alkaline_earth_metal_list, halogen_list))

