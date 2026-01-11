from datetime import datetime as dt
import os

def organic_compound_generator():


    prefix_dictionary = {1: "Meth", 2: "Eth", 3: "Prop", 4: "But", 5: "Pent", 6: "Hex", 7: "Hept", 8: "Oct", 9 : "Non", 10: "Dec"}
   
    organic_compound_type = int(input("Please enter the number corresponding to the organic compound type you would like to produce: "))

    carbon_chain_length = int(input("How many carbons would you like in your organic compound? (1-10): "))

    if organic_compound_type == 1:
        chemical_formula = f"C{carbon_chain_length}H{(2 * carbon_chain_length) + 2}"
        chemical_name = f"{prefix_dictionary[carbon_chain_length]}ane"
    elif organic_compound_type == 2:
        chemical_formula = f"C{carbon_chain_length}H{(2 * carbon_chain_length)}"
        chemical_name = f"{prefix_dictionary[carbon_chain_length]}ene"
    elif organic_compound_type == 3:
        chemical_formula = f"C{carbon_chain_length}H{(2 * carbon_chain_length) - 2}"
        chemical_name = f"{prefix_dictionary[carbon_chain_length]}yne"

    now = dt.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    if os.path.isfile("history.txt"):
        with open("history.txt", "a") as f:
            f.write(f"User created {chemical_name} ({chemical_formula}) - {dt_string}\n")
    else:
        with open("history.txt", "w") as f:
            f.write(f"User created {chemical_name} ({chemical_formula}) - {dt_string}\n")

    return chemical_formula, chemical_name

if __name__ == "__main__":
    organic_compound_generator()
