from .Shape import Shape

class Square(Shape):

    def __init__(self,x_position, y_position, side_len):
        super().__init__(x_position, y_position)
        self.side = side_len
    
    @property
    def perimeter(self):
        return 4*self.side
    
    @property
    def area(self):
        return self.side**2
    
    def __str__(self):
        position = f"\nForma: Quadrado | Par ordenado do centro de massa no espaço = ({self.x_position}, {self.y_position})\n"
        size = f"Largura = {self.side:.2f} cm | Altura = {self.side:.2f} cm\n"
        dimensions = f"Area = {self.area:.2f} cm² | Perímetro = {self.perimeter:.2f} cm\n"
        return position + size + dimensions
    
if __name__ == "__main__":
    quadrado = Square(34,72,52)
    print(quadrado)