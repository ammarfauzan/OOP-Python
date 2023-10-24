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

#Instantiating object
ammar_home = Home(address="Mawar A 01", bedrooms=3, bathrooms=2, square_feet=200, has_garden=True)
print(ammar_home)
print("")
print(ammar_home.address) #access attribute address
ammar_home.add_resident("Ammar")
