from compounds import *
from datetime import datetime as dt
import os

def inspect_compound():
    list_of_choices = []
    list_of_compound_names = []
    characteristic_list = []
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

            property_counter = 0
            for item in compound_list[list_of_compound_names[user_choice - 1]]:
                if property_counter == 0:
                    characteristic_list.append(f"Chemical Formula: {item}")
                elif property_counter == 1:
                    characteristic_list.append(f"Total number of atoms: {item}")
                elif property_counter == 2:
                    characteristic_list.append(f"Compound Type: {item}")
                elif property_counter == 3:
                    characteristic_list.append(f"Enthalpy of Formation: {item}")
                property_counter += 1
            
            now = dt.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            if os.path.isfile("history.txt"):
                with open("history.txt", "a") as f:
                    f.write(f"User inspected {list_of_compound_names[user_choice - 1]} - {dt_string}\n")
            else:
                with open("history.txt", "w") as f:
                    f.write(f"User inspected {list_of_compound_names[user_choice - 1]} - {dt_string}\n")
            return "\n".join(characteristic_list)

        except ValueError:
            print("Invalid input; please try again.")


if __name__ == "__main__":
    print(inspect_compound())