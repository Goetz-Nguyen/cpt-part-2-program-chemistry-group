compound_list = {
        #   {COMPOUND NAME}: [({CHEMICAL FORMULA}), {NUMBER OF ATOMS}, {TYPE OF COMPOUND}, {ENTHALPY OF FORMATION}]
            "Methane": [("CH4"), 5, "Organic (Alkane)", -74.4],
            "Ethane": [("C2H6"), 8, "Organic (Alkane)", -84.68],
            "Benzene": [("C6H6"), 12, "Aromatic (Hydrocarbon)", +49.1],
            "Carbon Dioxide": [("CO2"), 3, "Covalent", -393.5],
            "Carbon Monoxide": [("CO"), 2, "Covalent", -110.53],
            "Ammonia": [("NH3"), 4, "Covalent", -45.9],
            "Hydrochloric Acid": [("HCl"), 3, "Molecular", -92.3],
            "Silver Bromide": [("AgBr"), 2, "Ionic", -100.37],
            "Silver Chloride": [("AgCl"), 2, "Ionic", -127.1],
            "Aluminum Chloride": [("AlCl3"), 4, "Covalent", -704],
            "Calcium Oxide": [("CaO"), 2, "Ionic", -635],
            "Sodium Chloride": [("NaCl"), 2, "Ionic", -411],
            "Water": [("H2O"), 3, "Covalent", -285.83],
            "Hydrogen Peroxide": [("H2O2"), 4, "Covalent", -187.8],
            "Sulfuric Acid": [("H2SO4"), 7, "Molecular", -814],
            "Nitric Acid": [("HNO3"), 5, "Molecular", -207],
            "Sodium Hydroxide": [("NaOH"), 3, "Ionic", -425.6],
            "Potassium Chloride": [("KCl"), 2, "Ionic", -436.7],
            "Calcium Carbonate": [("CaCO3"), 5, "Ionic", -1206.9],
            "Sodium Carbonate": [("Na2CO3"), 6, "Ionic", -1130.7],
            "Magnesium Oxide": [("MgO"), 2, "Ionic", -601.6],
            "Silicon Dioxide": [("SiO2"), 3, "Covalent Network", -910.9],
            "Ethanol": [("C2H5OH"), 9, "Organic (Alcohol)", -277.7],
            "Propane": [("C3H8"), 11, "Organic (Alkane)", -103.8],
            "Butane": [("C4H10"), 14, "Organic (Alkane)", -125.6],
            "Acetic Acid": [("CH3COOH"), 8, "Organic (Carboxylic Acid)", -484.5],
}

def main():
    list_of_choices = []
    list_of_compound_names = []
    i = 1
    continuous_loop = 0

    for key in compound_list:
        print(f"{i}. {key}")
        list_of_choices.append(i)
        list_of_compound_names.append(key)
        i += 1
        
    print("\n")
    
    while continuous_loop == 0:
        try:

            
            user_choice = int(input("Please press the number corresponding to the compound you would like to inspect: "))

            while user_choice not in list_of_choices:
                print("That is not a selectable option; please try again.")
                user_choice = int(input("Please press the number corresponding to the compound you would like to inspect: "))

            print("--------Compound Properties--------")
            property_counter = 0
            for item in compound_list[list_of_compound_names[user_choice - 1]]:
                if property_counter == 0:
                    print(f"Chemical Formula: {item}")
                elif property_counter == 1:
                    print(f"Total number of atoms: {item}")
                elif property_counter == 2:
                    print(f"Compound Type: {item}")
                elif property_counter == 3:
                    print(f"Enthalpy of Formation: {item}")
                property_counter += 1
            print("----------------")

        except ValueError:
            print("Invalid input; please try again.")
            

if __name__ == "__main__":
    main()