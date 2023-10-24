class Home:
    # Initialize the attribute for the Home
    def __init__(self, address, bedrooms, bathrooms, square_feet, has_garden=False):
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_feet = square_feet
        self.has_garden = has_garden
        self.residents = []

    def add_resident(self, resident_name):
        self.residents.append(resident_name)
        print(f"{resident_name} has been added as a resident of {self.address}.")

    def describe_home(self):
        print(f"\nHome Information:")
        print(f"Address: {self.address}")
        print(f"Bedrooms: {self.bedrooms}")
        print(f"Bathrooms: {self.bathrooms}")
        print(f"Square Feet: {self.square_feet}")
        print(f"Has Garden: {'Yes' if self.has_garden else 'No'}")
        if self.residents:
            print(f"Residents: {', '.join(self.residents)}")
        else:
            print("No residents yet.")

class Apartment(Home):
    def __init__(self, address, bedrooms, bathrooms, square_feet, has_garden=False, floor_level=None, has_doorman=False):
        # Call the constructor of the parent class (Home)
        super().__init__(address, bedrooms, bathrooms, square_feet, has_garden)
        
        # Additional attributes for Apartment
        self.floor_level = floor_level
        self.has_doorman = has_doorman

    def describe_apartment(self):
        # Call the describe_home method of the parent class
        self.describe_home()
        
        # Describe additional attributes for Apartment
        print(f"Floor Level: {self.floor_level}")
        print(f"Has Doorman: {'Yes' if self.has_doorman else 'No'}")

#Instantiating object
#Inheritance
oak_apartment = Apartment(address="Jl.Patimura 57", bedrooms=2, bathrooms=1, square_feet=43, floor_level=18, has_doorman=True)
oak_apartment.add_resident("Umar")
print(oak_apartment.describe_apartment())

# print(help(oak_apartment))
