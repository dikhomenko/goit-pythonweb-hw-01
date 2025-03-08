import logging
from .logging_config import configure_logging
from .Vehicle import Vehicle

configure_logging()


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model}: Двигун запущено")
