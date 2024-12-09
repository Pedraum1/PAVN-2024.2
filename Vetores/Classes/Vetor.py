from math import sqrt

class Vector:

  def __init__(self, i_component, j_component, k_component):
    self.i = float(i_component)
    self.j = float(j_component)
    self.k = float(k_component)

  def modulus(self):
    return sqrt(self.i**2 + self.j**2 + self.k**2)
  
  def __add__(self, other):
    return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
  
  def __sub__(self, other):
    return Vector(self.i - other.i, self.j - other.j, self.k - other.k)
  
  def __mul__(self,other):
    
    if isinstance(other, (float, int)):
      return Vector(self.i*other, self.j*other, self.k*other)
    
    return self.i * other.i + self.j * other.j + self.k * other.k
  
  def __rmul__(self, other):
    return self.__mul__(other)

  
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"


if __name__ == "__main__":
  i = input("insira a componente i:")
  j = input("insira a componente j:")
  k = input("insira a componente k:")

  vetor1 = Vector(i,j,k)
  vetor2 = 4

  print(vetor1*4)