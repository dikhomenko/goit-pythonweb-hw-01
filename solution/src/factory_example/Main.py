import sys
import os

# Add solution to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.factory_example.EUVehicleFactory import EUVehicleFactory
from src.factory_example.USVehicleFactory import USVehicleFactory


class Main:
    def run(self) -> None:
        us_factory = USVehicleFactory("US Spec")
        eu_factory = EUVehicleFactory("EU Spec")

        us_car = us_factory.create_car("Ford", "Mustang")
        us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
        eu_car = eu_factory.create_car("BMW", "3 Series")
        eu_motorcycle = eu_factory.create_motorcycle("Ducati", "Monster")

        us_car.start_engine()
        us_motorcycle.start_engine()
        eu_car.start_engine()
        eu_motorcycle.start_engine()


if __name__ == "__main__":
    main = Main()
    main.run()
