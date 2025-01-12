from .Shape import Shape
from math import pi,sqrt

class Circle(Shape):

    def __init__(self,x_position:float, y_position:float, diameter_len:float):
        super().__init__(x_position, y_position)
        self.diameter = diameter_len
        self.radius = diameter_len/2

    @property
    def perimeter(self):
        return pi*self.diameter
    
    @property
    def area(self):
        return pi*((self.diameter**2)/4)
    
    def __str__(self):
        position = f"\nForma: Círculo | Par ordenado do centro de massa no espaço = ({self.x_position}, {self.y_position})\n"
        size = f"Diâmetro = {self.diameter:.2f} cm | Raio = {self.radius:.2f} cm\n"
        dimensions = f"Area = {self.area:.2f} cm²  | Perímetro = {self.perimeter:.2f} cm\n"
        return position + size + dimensions
    
if __name__ == "__main__":
    circulo = Circle(32,44,56)
    print(circulo)