from pakudex import Pakudex
from pakuri import Pakuri


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    # Get user input for max capacity
    while True:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid size.")

    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.\n")

    # Main menu loop
    while True:
        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")

        choice = input("\nWhat would you like to do? ")

        if choice == '1':  # List Pakuri
            species_list = pakudex.get_species_array()
            if species_list:
                print("Pakuri In Pakudex:")
                for i, species in enumerate(species_list, 1):
                    print(f"{i}. {species}")
            else:
                print("No Pakuri in Pakudex yet!")

        elif choice == '2':  # Show Pakuri
            species = input("Enter the name of the species to display: ").strip()
            stats = pakudex.get_stats(species)
            if stats:
                print(f"\nSpecies: {species}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")
            else:
                print("Error: No such Pakuri!")
                continue


        elif choice == '3':  # Add Pakuri

            if pakudex.get_size() >= pakudex.get_capacity():

                print("Error: Pakudex is full!")

            else:

                species = input("Enter the name of the species to add: ").strip()

                if pakudex.add_pakuri(species):
                    print(f"Pakuri species {species} successfully added!")



        elif choice == '4':  # Evolve Pakuri

            species = input("Enter the name of the species to evolve: ").strip()

            if not pakudex.evolve_species(species):  # Call the evolve method

                print("Error: No such Pakuri!")
            else:
                print(f"{species} has evolved!")


        elif choice == '5':  # Sort Pakuri
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == '6':  # Exit
            print("Thanks for using Pakudex! Bye!")
            break

        else:
            print("Unrecognized menu selection!")

        print()  # Print a new line


if __name__ == '__main__':
    main()
