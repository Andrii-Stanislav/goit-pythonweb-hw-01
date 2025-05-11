from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")

class VehicleFactory(ABC):
    @classmethod
    @abstractmethod
    def create_car(cls, make):
        pass

    @classmethod
    @abstractmethod
    def create_motorcycle(cls, make):
        pass

class USVehicleFactory(VehicleFactory):
    @classmethod
    def create_car(cls, make):
        return Car(make, 'US Spec')

    @classmethod
    def create_motorcycle(cls, make):
        return Motorcycle(make, 'US Spec')

class EUVehicleFactory(VehicleFactory):
    @classmethod
    def create_car(cls, make):
        return Car(make, 'EU Spec')

    @classmethod
    def create_motorcycle(cls, make):
        return Motorcycle(make, 'EU Spec')

# # Використання

def get_vehicle_factory(country):
    if country == 'US':
        return USVehicleFactory()
    elif country == 'EU':
        return EUVehicleFactory()
    else:
        raise ValueError(f"Unsupported country: {country}")

def create_vehicle(factory, vehicle_type, make):
    if vehicle_type == 'car':
        return factory.create_car(make)
    elif vehicle_type == 'motorcycle':
        return factory.create_motorcycle(make)
    else:
        raise ValueError(f"Unsupported vehicle type: {vehicle_type}")


toyotaCar = create_vehicle(get_vehicle_factory('US'), 'car', 'Toyota')

print(toyotaCar)

toyotaMotorcycle = create_vehicle(get_vehicle_factory('US'), 'motorcycle', 'Toyota')

print(toyotaMotorcycle)


