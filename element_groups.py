
 
# Class system
class Element:
    """
    The Element Class: The skeleton characteristics of an element

    Attributes:

    name (str) - The name of the element
    atomic_number (int) - The number of protons in the element
    electronegativity (float) - An element's tendency to attract neighbooring electrons when bonded

    Examples:

    element = Element("Nothingium", 10, 1.20)

    print(element)
    
    Element Name: Nothingium
    Group: (Unknown)
    Atomic Number: 10
    Electronegativity: 1.20
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float) -> None:
        self.name = name
        self.atomic_number = atomic_number
        self.electronegativity = electronegativity

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: (Unknown)\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}"
   

# Alkali Metal Class
class Alkali_Metal(Element):
    """
    The Alkali Metal Class: The characteristics of an Alkali Metal

    Attributes:

    name - The name of the Alkali Metal
    atomic_number - The number of protons in the Alkali Metal
    electronegativity - The Alkali Metal's tendency to attract neighbooring electrons when bonded
    bonding_capacity (int) - The maximum number of bonds the Alkali Metal can make

    Examples:

    element = Alkali_Metal("Sodium", 11, 0.93, 1)

    print(element)
    
    Element Name: Sodium
    Group: Alkali Metal
    Atomic Number: 11
    Electronegativity: 0.93
    Bonding Capacity: 1
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, bonding_capacity: int, full_name: str) -> None:
        super().__init__(name, atomic_number, electronegativity)

        self.bonding_capacity = bonding_capacity
        self.full_name = full_name

    def declare_element(self):
        print(f"A shiny instance of elemental {self.name} is observed! Be careful around this one!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Alkali Metal\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}" \
               f"Bonding Capacity: {self.bonding_capacity}"
   
# Alkaline Earth Metal Class
class Alkaline_Earth_Metal(Element):
    """
    The Alkaline Earth Metal Class: The characteristics of an Alkaline Earth Metal

    Attributes:

    name - The name of the Alkaline Earth Metal
    atomic_number - The number of protons in the Alkaline Earth Metal
    electronegativity - The Alkaline Earth Metal's tendency to attract neighbooring electrons when bonded
    bonding_capacity (int) - The maximum number of bonds the Alkaline Earth Metal can make

    Examples:

    element = Alkaline_Earth_Metal("Magnesium", 12, 1.31, 2)

    print(element)
    
    Element Name: Magnesium
    Group: Alkaline Earth Metal
    Atomic Number: 12
    Electronegativity: 1.31
    Bonding Capacity: 2
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, bonding_capacity: int, full_name: str) -> None:
        super().__init__(name, atomic_number, electronegativity)

        self.bonding_capacity = bonding_capacity
        self.full_name = full_name

    def declare_element(self):
        print(f"An instance of elemental {self.name} is observed! Be careful, it's a fire hazard!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Alkaline Earth Metal\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}" \
               f"Bonding Capacity: {self.bonding_capacity}"
   
# Halogen Class
class Halogen(Element):
    """
    The Halogen Class: The characteristics of a Halogen

    Attributes:

    name - The name of the Halogen
    atomic_number - The number of protons in the Halogen
    electronegativity - The Halogen's tendency to attract neighbooring electrons when bonded
    bonding_capacity (int) - The maximum number of bonds the Halogen can make

    Examples:

    element = Halogen("Chlorine", 17, 3.16, 1)

    print(element)
    
    Element Name: Chlorine
    Group: Halogen
    Atomic Number: 17
    Electronegativity: 3.16
    Bonding Capacity: 1
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, bonding_capacity: int, full_name: str) -> None:
        super().__init__(name, atomic_number, electronegativity)

        self.bonding_capacity = bonding_capacity
        self.full_name = full_name

    def declare_element(self):
        print(f"An instance of elemental {self.name} is observed! It's eager to react!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Halogen\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}" \
               f"Bonding Capacity: {self.bonding_capacity}"
   
# Noble Gas Class
class Noble_Gas(Element):
    """
    The Noble Gas Class: The characteristics of a Noble Gas

    Attributes:

    name - The name of the Noble Gas
    atomic_number - The number of protons in the Noble Gas
    electronegativity - The Noble Gas' tendency to attract neighbooring electrons when bonded
    bonding_capacity (int) - The maximum number of bonds the Noble Gas can make

    Examples:

    element = Halogen("Argon", 18, 0.00, 0)

    print(element)
    
    Element Name: Argon
    Group: Noble Gas
    Atomic Number: 18
    Electronegativity: 0.00
    Bonding Capacity: 0
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, bonding_capacity: int, full_name: str) -> None:
        super().__init__(name, atomic_number, electronegativity)

        self.bonding_capacity = bonding_capacity
        self.full_name = full_name

    def declare_element(self):
        print(f"An instance of elemental {self.name} is observed! It's visibly dormant!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Noble Gas\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}" \
               f"Bonding Capacity: {self.bonding_capacity}"
    
# Transition Metals Class
class Transition_Metal(Element):
    """
    The Transition Metal Class: The characteristics of a Transition Metal

    Attributes:

    name - The name of the Transition Metal
    atomic_number - The number of protons in the Transition Metal
    electronegativity - The Transition Metal's tendency to attract neighbooring electrons when bonded
    possible_charges (int) - The number of possible charges a Transition Metal can have (Transition Metals are multi-valent)

    Examples:

    element = Transition_Metal("Iron", 26, 1.83, 3)

    print(element)
    
    Element Name: Iron
    Group: Transition Metal
    Atomic Number: 18
    Electronegativity: 1.83
    Possible Charges: 3
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, possible_charges: int, full_name: str) -> None:
        super().__init__(name, atomic_number, electronegativity)
        
        self.possible_charges = possible_charges
        self.full_name = full_name

    def declare_element(self):
        print(f"An instance of elemental {self.name} is observed! It's undecided on its ionic charge!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Transition Metal\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}" \
               f"Possible Charges: {self.possible_charges}"
    
    