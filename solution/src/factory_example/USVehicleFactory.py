import logging
from src.logging_config import configure_logging
from .VehicleFactory import VehicleFactory
from .Car import Car
from .Motorcycle import Motorcycle

configure_logging()


class USVehicleFactory(VehicleFactory):
    def __init__(self, spec: str) -> None:
        self.spec: str = spec

    def create_car(self, make: str, model: str) -> Car:
        car = Car(make, model)
        car.start_engine = lambda: logging.info(
            f"{car.make} {car.model}: Двигун запущено ({self.spec})"
        )
        return car

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        motorcycle = Motorcycle(make, model)
        motorcycle.start_engine = lambda: logging.info(
            f"{motorcycle.make} {motorcycle.model}: Двигун запущено ({self.spec})"
        )
        return motorcycle
