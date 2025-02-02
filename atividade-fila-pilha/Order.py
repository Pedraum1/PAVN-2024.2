from dataclasses import dataclass

@dataclass
class Order():
    name: str
    price: float

    def __str__(self):
        return f"{self.name} - R$ {self.price:,.2f}"