# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle 
# and demonstrate changing the owner.


class Vehicle: 
    def __init__(self, reg_num, type, owner): 
        self.registration_number = reg_num 
        self.type = type 
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner update to {new_owner} for vehicle with registration number {self.registration_number}")

# Demonstration

if __name__ == "__main__":
    Vehicle1 = Vehicle("ABC123", "Car", "John Doe")
    Vehicle2 = Vehicle("XYZ789", "Truck", "Jane Smith")

# Display origional owners

    print(f"Vehicle 1: {Vehicle1.registration_number}, Type: {Vehicle1.type}, Owner: {Vehicle1.owner}")
    print(f"vehicle 2: {Vehicle2.registration_number}, Type: {Vehicle2.type}, Owner: {Vehicle2.owner}")

# New owners

Vehicle1.update_owner("Alice Johnson" )
Vehicle2.update_owner("Bob Brown" )

# Updated new owners

print(f"Vehicle 1: {Vehicle1.registration_number}, Type: {Vehicle1.type}, Owner: {Vehicle1.owner}") 
print(f"Vehicle 2: {Vehicle2.registration_number}, Type: {Vehicle2.type}, Owner: {Vehicle2.owner}")