from dataclasses import dataclass

class Person:

    def __init__(self, name, age:int, number:int|str, street:str, neighborhood:str, city:str, state:str, country:str):
        
        self.name = name
        self.age = age
        self.address = Address(number, street, neighborhood, city, state, country)

class Employee(Person):

    def __init__(self,  name:str, age:int, number:int|str, street:str, neighborhood:str, city:str, state:str, country:str, salary:float):
        super().__init__(name, age, number, street, neighborhood, city, state, country)
        self.salary = salary

@dataclass
class Address:
    number:int|str
    street:str
    neighborhood:str
    city:str
    state:str
    country:str

    def __str__(self):
        return f"{self.street}, {self.number} - {self.neighborhood}, {self.city} - {self.state}/{self.country}"