from .Shape import Shape

class Rectangle(Shape):

    def __init__(self,x_position, y_position, width_len, height_len):
        super().__init__(x_position, y_position)
        self.width = width_len
        self.height = height_len

    @property
    def perimeter(self):
        return 2*self.width + 2*self.height
    
    @property
    def area(self):
        return self.width*self.height
    
    def __str__(self):
        position = f"\nForma: Retângulo | Par ordenado do centro de massa no espaço = ({self.x_position}, {self.y_position})\n"
        size = f"Largura = {self.width:.2f} cm | Altura = {self.height:.2f} cm\n"
        dimensions = f"Area = {self.area:.2f} cm² | Perímetro = {self.perimeter:.2f} cm\n"
        return position + size + dimensions
    
if __name__ == "__main__":
    retangulo = Rectangle(3,4,5,7)
    print(retangulo)