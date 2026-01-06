
 
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
    
# Transition Metals Class
class Transition_Metal(Element):

    def __init__(self, name: str, atomic_number: int, electronegativity: float, possible_charges: int) -> None:
        super().__init__(name, atomic_number, electronegativity)
        self.possible_charges = possible_charges

    def declare_element(self):
        print(f"An instance of elemental {self.name} is observed! It's undecided on its ionic charge!")

    def __str__(self):
        return f"Element Name: {self.name}\n" \
               f"Group: Transition Metal\n" \
               f"Atomic Number {self.atomic_number}\n" \
               f"Possible Charges: {self.possible_charges}"
    
    