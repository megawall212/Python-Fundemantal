from pakuri import Pakuri

class Pakudex:
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuri_list = []

    def get_size(self):
        return len(self.pakuri_list)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if not self.pakuri_list:
            return None
        return [pakuri.get_species() for pakuri in self.pakuri_list]

    def get_stats(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species().lower() == species.lower():  # Case insensitive check
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    def sort_pakuri(self):
        self.pakuri_list.sort(key=lambda pakuri: pakuri.get_species())  # Case insensitive sorting
        

    def add_pakuri(self, species):
        # Check if Pakudex is full
        if self.get_size() >= self.capacity:
            return False  # Return False instead of printing error

        # Check for duplicate species
        for pakuri in self.pakuri_list:
            if pakuri.get_species().lower() == species.lower():  # Case insensitive check
                return False  # Return False if species already exists

        # If no duplicates, add the new species
        new_pakuri = Pakuri(species)
        self.pakuri_list.append(new_pakuri)
        return True

    def evolve_species(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species().lower() == species.lower():  # Case insensitive check
                pakuri.evolve()
                return True
        return False  # Species not found; return False instead of printing error

