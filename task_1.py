from abc import ABC, abstractmethod
from logger import get_logger

logger = get_logger()


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @classmethod
    @abstractmethod
    def create_car(cls, make: str) -> Car:
        pass

    @classmethod
    @abstractmethod
    def create_motorcycle(cls, make: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    @classmethod
    def create_car(cls, make: str) -> Car:
        return Car(make, "US Spec")

    @classmethod
    def create_motorcycle(cls, make: str) -> Motorcycle:
        return Motorcycle(make, "US Spec")


class EUVehicleFactory(VehicleFactory):
    @classmethod
    def create_car(cls, make: str) -> Car:
        return Car(make, "EU Spec")

    @classmethod
    def create_motorcycle(cls, make: str) -> Motorcycle:
        return Motorcycle(make, "EU Spec")


# # Використання


def get_vehicle_factory(country: str) -> VehicleFactory:
    if country == "US":
        return USVehicleFactory()
    elif country == "EU":
        return EUVehicleFactory()
    else:
        raise ValueError(f"Unsupported country: {country}")


def create_vehicle(factory: VehicleFactory, vehicle_type: str, make: str) -> Vehicle:
    if vehicle_type == "car":
        return factory.create_car(make)
    elif vehicle_type == "motorcycle":
        return factory.create_motorcycle(make)
    else:
        raise ValueError(f"Unsupported vehicle type: {vehicle_type}")


toyotaCar = create_vehicle(get_vehicle_factory("US"), "car", "Toyota")

logger.info(toyotaCar)

toyotaMotorcycle = create_vehicle(get_vehicle_factory("US"), "motorcycle", "Toyota")

logger.info(toyotaMotorcycle)
