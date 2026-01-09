def main():


    prefix_dictionary = {1: "Meth", 2: "Eth", 3: "Prop", 4: "But", 5: "Pent", 6: "Hex", 7: "Hept", 8: "Oct", 9 : "Non", 10: "Dec"}


    print("Welcome to the Organic Compound Generator!\n")
    print("Organic compounds are chemical compounds composed primarily of carbon and hydrogen.")
    print("The relationship between the two elements is what we will be exploring here!")
   
    continuous_loop = 0


    while continuous_loop == 0:
        try:
            print("----\n")
            print("1. Alkane (Contains only single-bonded carbon-carbon chains)")
            print("2. Alkene (Contains an instance of a double-bonded carbon-carbon chain)")
            print("3. Alkyne (Contains an instance of a triple-bonded carbon-carbon chain)")
            print("----\n")
            organic_compound_type = int(input("Please enter the number corresponding to the organic compound type you would like to produce: "))


            while (organic_compound_type < 1) or (organic_compound_type > 3):
                print("That is not an available option; please try again.")
                organic_compound_type = int(input("Please enter the number corresponding to the organic compound type you would like to produce: "))


            carbon_chain_length = int(input("How many carbons would you like in your organic compound? (1-10): "))


            while (carbon_chain_length < 1) or (carbon_chain_length > 10):
                print("That is not an available option; please try again.")
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


            print(f"Chemical Formula: {chemical_formula}")
            print(f"Chemical Formula: {chemical_name}")


               
        except ValueError:
            print("Invalid input; please try again.")


if __name__ == "__main__":
    main()
