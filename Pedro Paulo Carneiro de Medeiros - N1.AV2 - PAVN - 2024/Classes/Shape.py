from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Shape(ABC):
    x_position: float
    y_position: float

    @abstractmethod
    def perimeter():
        pass

    @abstractmethod
    def area():
        pass
