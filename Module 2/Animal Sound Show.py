from abc import ABC, abstractmethod


# ── ABSTRACT BASE CLASS (Parent) ──────────────────────────────────────────────
# Vehicle inherits from ABC — this makes it an abstract class
class Vehicle(ABC):

    # Parent constructor
    def __init__(self, brand, fuel_type):
        self.brand = brand
        self.fuel_type = fuel_type

    # Concrete method
    def display(self):
        print(f"Brand: {self.brand}  |  Fuel Type: {self.fuel_type}")

    # Abstract method
    @abstractmethod
    def start(self):
        pass


# ── CHILD CLASS 1 ─────────────────────────────────────────────────────────────
class Car(Vehicle):

    def __init__(self, brand, fuel_type, model):
        super().__init__(brand, fuel_type)
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} starts with a smooth engine sound.")


# ── CHILD CLASS 2 ─────────────────────────────────────────────────────────────
class Motorcycle(Vehicle):

    def __init__(self, brand, fuel_type, style):
        super().__init__(brand, fuel_type)
        self.style = style

    def start(self):
        print(f"{self.brand} ({self.style}) starts with a loud revving sound.")


# ── CHILD CLASS 3 ─────────────────────────────────────────────────────────────
class Truck(Vehicle):

    def __init__(self, brand, fuel_type, capacity):
        super().__init__(brand, fuel_type)
        self.capacity = capacity

    def start(self):
        print(f"{self.brand} Truck ({self.capacity} tons) starts with a powerful roar.")


# ── CREATE OBJECTS & RUN THE SHOW ─────────────────────────────────────────────
car = Car("Toyota", "Petrol", "Corolla")
bike = Motorcycle("Yamaha", "Petrol", "Sport")
truck = Truck("Volvo", "Diesel", 12)

print("=== Vehicle Demonstration ===\n")

for vehicle in [car, bike, truck]:
    vehicle.display()
    vehicle.start()
    print()