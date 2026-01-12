"""
author: Aidan Lone, Husnain Sidhu, Muhammad Ali, Malaz Nakaweh, Dabeer Awan
date: January 12, 2026
purpose: Element Class System
"""

class Element:
    """
    The Element Class: The skeleton characteristics of an element

    Attributes:

    name (str) - The chemical symbol of the element
    atomic_number (int) - The number of protons in the element
    electronegativity (float) - An element's tendency to attract neighbooring electrons when bonded
    full_name (str) - The element's full name

    Invariants:
    - name cannot be empty; should default to "???"
    - atomic_number cannot be less than 1 or greater than 118 
      (there are currently only 118 discovered elements); should default to 1
    - electronegativity cannot be lower than 0.0 or greater than 4.0; should default to 0.0
    - full_name cannot be empty; should default to "Unknown Element"

    Example:

    >>> element = Element("No", 10, 1.2, "Nothingium")
    >>> print(element)
    Chemical Symbol: No
    Group: (Unknown)
    Atomic Number: 10
    Electronegativity: 1.2
    Full Name: Nothingium
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, full_name: str) -> None:
        """Initializes the Element's attributes"""
        self.name = name
        self.atomic_number = atomic_number
        self.electronegativity = electronegativity
        self.full_name = full_name

    def __str__(self) -> str:
        """
        Returns a user-friendly message, showing the element's core properties

        Arguments:
            (None)
        
        Returns:
            str - A user-friendly message, showing the element's core properties

        Example:

        >>> element = Element("No", 10, 1.2, "Nothingium")
        >>> print(element)
        Chemical Symbol: No
        Group: (Unknown)
        Atomic Number: 10
        Electronegativity: 1.2
        Full Name: Nothingium
        """
        return f"Chemical Symbol: {self.name}\n" \
               f"Group: (Unknown)\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}\n" \
               f"Full Name: {self.full_name}"
   

# Alkali Metal Class
class Alkali_Metal(Element):
    """
    The Alkali Metal Super Class: The characteristics of an Alkali Metal

    Attributes:

    name - The chemical symbol of the Alkali Metal
    atomic_number - The number of protons in the Alkali Metal
    electronegativity - The Alkali Metal's tendency to attract neighbooring electrons when bonded
    full_name - The Alkali Metal's full name
    bonding_capacity (int) - The maximum number of bonds the Alkali Metal can make
    
    Invariants:
    - name cannot be empty; should default to "???"
    - atomic_number cannot be less than 1 or greater than 118 
      (there are currently only 118 discovered elements); should default to 1
    - electronegativity cannot be lower than 0.0 or greater than 4.0; should default to 0.0
    - bonding_capacity cannot be less than 0 or greater than  4; 
      should default to 1 if it does (the usual bonding capacity of an Alkali Metal)
    - full_name cannot be empty; should default to "Unknown Alkali Metal"

    Examples:

    >>> element = Alkali_Metal("Na", 11, 0.9, 1, "Sodium")
    >>> print(element)
    Chemical Symbol: Na
    Group: Alkali Metal
    Atomic Number: 11
    Electronegativity: 0.9
    Bonding Capacity: 1
    Full Name: Sodium
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, 
                 bonding_capacity: int, full_name: str) -> None:
        """Initializes the Alkali Metal's attributes"""
        super().__init__(name, atomic_number, electronegativity, full_name)

        self.bonding_capacity = bonding_capacity

    def __str__(self) -> str:
        """
        Returns a user-friendly message, showing the Alkali Metal's core properties

        Arguments:
            (None)
        
        Returns:
            str - A user-friendly message, showing the Alkali Metal's core properties

        Example:

        >>> element = Alkali_Metal("Na", 11, 0.9, 1, "Sodium")
        >>> print(element)
        Chemical Symbol: Na
        Group: Alkali Metal
        Atomic Number: 11
        Electronegativity: 0.9
        Bonding Capacity: 1
        Full Name: Sodium
        """
        return f"Chemical Symbol: {self.name}\n" \
               f"Group: Alkali Metal\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}\n" \
               f"Bonding Capacity: {self.bonding_capacity}\n" \
               f"Full Name: {self.full_name}"
   
# Alkaline Earth Metal Class
class Alkaline_Earth_Metal(Element):
    """
    The Alkaline Earth Metal Super Class: The characteristics of an Alkaline Earth Metal

    Attributes:

    name - The chemical symbol of the Alkaline Earth Metal
    atomic_number - The number of protons in the Alkaline Earth Metal
    electronegativity - The Alkaline Earth Metal's tendency to attract neighbooring electrons when bonded
    full_name - The Alkaline Earth Metal's full name
    bonding_capacity (int) - The maximum number of bonds the Alkaline Earth Metal can make
    

    Invariants:
    - name cannot be empty; should default to "???"
    - atomic_number cannot be less than 1 or greater than 118 
      (there are currently only 118 discovered elements); should default to 1
    - electronegativity cannot be lower than 0.0 or greater than 4.0; should default to 0.0
    - bonding_capacity cannot be less than 0 or greater than 4; 
      should default to 2 if it does (the usual bonding capacity of an Alkaline Earth Metal)
    - full_name cannot be empty; should default to "Unknown Alkaline Earth Metal"

    Examples:

    >>> element = Alkaline_Earth_Metal("Mg", 12, 1.2, 2, "Magnesium")
    >>> print(element)
    Chemical Symbol: Mg
    Group: Alkaline Earth Metal
    Atomic Number: 12
    Electronegativity: 1.2
    Bonding Capacity: 2
    Full Name: Magnesium
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, 
                 bonding_capacity: int, full_name: str) -> None:
        """Initializes the Alkaline Earth Metal's attributes"""
        super().__init__(name, atomic_number, electronegativity, full_name)

        self.bonding_capacity = bonding_capacity

    def __str__(self) -> str:
        """
        Returns a user-friendly message, showing the Alkaline Earth Metal's core properties

        Arguments:
            (None)
        
        Returns:
            str - A user-friendly message, showing the Alkaline Earth Metal's core properties

        Example:

        >>> element = Alkaline_Earth_Metal("Mg", 12, 1.2, 2, "Magnesium")
        >>> print(element)
        Chemical Symbol: Mg
        Group: Alkaline Earth Metal
        Atomic Number: 12
        Electronegativity: 1.2
        Bonding Capacity: 2
        Full Name: Magnesium
        """
        return f"Chemical Symbol: {self.name}\n" \
               f"Group: Alkaline Earth Metal\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}\n" \
               f"Bonding Capacity: {self.bonding_capacity}\n" \
               f"Full Name: {self.full_name}"
   
# Halogen Class
class Halogen(Element):
    """
    The Halogen Super Class: The characteristics of a Halogen

    Attributes:

    name - The chemical symbol of the Halogen
    atomic_number - The number of protons in the Halogen
    electronegativity - The Halogen's tendency to attract neighbooring electrons when bonded
    full_name - The Halogen's full name
    bonding_capacity (int) - The maximum number of bonds the Halogen can make
    

    Invariants:
    - name cannot be empty; should default to "???"
    - atomic_number cannot be less than 1 or greater than 118 
      (there are currently only 118 discovered elements); should default to 1
    - electronegativity cannot be lower than 0.0 or greater than 4.0; should default to 0.0
    - bonding_capacity cannot be less than 0 or greater than 4; 
      should default to 1 if it does (the usual bonding capacity of a Halogen)
    - full_name cannot be empty; should default to "Unknown Halogen"

    Examples:

    >>> element = Halogen("Cl", 17, 3.0, 1, "Chlorine")
    >>> print(element)
    Chemical Symbol: Cl
    Group: Halogen
    Atomic Number: 17
    Electronegativity: 3.0
    Bonding Capacity: 1
    Full Name: Chlorine
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, 
                 bonding_capacity: int, full_name: str) -> None:
        """Initializes the Halogen's attributes"""
        super().__init__(name, atomic_number, electronegativity, full_name)

        self.bonding_capacity = bonding_capacity

    def __str__(self) -> str:
        """
        Returns a user-friendly message, showing the Halogen's core properties

        Arguments:
            (None)
        
        Returns:
            str - A user-friendly message, showing the Halogen's core properties

        Example:

        >>> element = Halogen("Cl", 17, 3.0, 1, "Chlorine")
        >>> print(element)
        Chemical Symbol: Cl
        Group: Halogen
        Atomic Number: 17
        Electronegativity: 3.0
        Bonding Capacity: 1
        Full Name: Chlorine
        """
        return f"Chemical Symbol: {self.name}\n" \
               f"Group: Halogen\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}\n" \
               f"Bonding Capacity: {self.bonding_capacity}\n" \
               f"Full Name: {self.full_name}"
    
# Transition Metals Class
class Transition_Metal(Element):
    """
    The Transition Metal Super Class: The characteristics of a Transition Metal

    Attributes:

    name - The chemical symbol of the Transition Metal
    atomic_number - The number of protons in the Transition Metal
    electronegativity - The Transition Metal's tendency to attract neighbooring electrons when bonded
    full_name - The Transition Metal's full name
    possible_charges (int) - The number of possible charges a Transition Metal can have (Transition Metals are multi-valent)
    

    Invariants:
    - name cannot be empty; should default to "???"
    - atomic_number cannot be less than 1 or greater than 118 
      (there are currently only 118 discovered elements); should default to 1
    - electronegativity cannot be lower than 0.0 or greater than 4.0; should default to 0.0
    - possible_charges cannot be less than 0 or greater than 5; 
      should default to 1
    - full_name cannot be empty; should default to "Unknown Transition Metal"

    Examples:

    >>> element = Transition_Metal("Fe", 26, 1.8, 2, "Iron")
    >>> print(element)
    Chemical Symbol: Fe
    Group: Transition Metal
    Atomic Number: 26
    Electronegativity: 1.8
    Possible Charges: 2
    Full Name: Iron
    """

    def __init__(self, name: str, atomic_number: int, electronegativity: float, 
                 possible_charges: int, full_name: str) -> None:
        """Initializes the Transition Metal's attributes"""
        super().__init__(name, atomic_number, electronegativity, full_name)
        
        self.possible_charges = possible_charges

    def __str__(self) -> str:
        """
        Returns a user-friendly message, showing the Transition Metal's core properties

        Arguments:
            (None)
        
        Returns:
            str - A user-friendly message, showing the Transition Metal's core properties

        Example:

        >>> element = Transition_Metal("Fe", 26, 1.8, 2, "Iron")
        >>> print(element)
        Chemical Symbol: Fe
        Group: Transition Metal
        Atomic Number: 26
        Electronegativity: 1.8
        Possible Charges: 2
        Full Name: Iron
        """
        return f"Chemical Symbol: {self.name}\n" \
               f"Group: Transition Metal\n" \
               f"Atomic Number: {self.atomic_number}\n" \
               f"Electronegativity: {self.electronegativity}\n" \
               f"Possible Charges: {self.possible_charges}\n" \
               f"Full Name: {self.full_name}"
       