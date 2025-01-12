from abc import ABC, abstractclassmethod

class Account(ABC):
    ''' Basic Account abstract class '''

    def __init__(self, name:str, money:float, income:float):
        self.owner_name = name
        self.money = money

    def __str__(self):
        return f"{self.owner_name} - Saldo: R$ {(self.money):.2f}"

    @abstractclassmethod
    def deposit(self, amount:float):
        pass

    @abstractclassmethod
    def withdraw(self, amount:float):
        pass

class Corrente(Account):

    def __init__(self, name:str, money:float, income:float):
        super().__init__(name, money, income)
        self.tax = 0.025

    def deposit(self, amount:float):
        if (self.money + amount - amount*self.tax) < self.tax:
            print("Erro, você não possuirá saldo suficiente para realizar a transação")
        else:
            self.money += amount - amount*self.tax
            print(f"Saldo atual: R$ {(self.money):.2f}")

    def withdraw(self, amount:float):
        if self.money < (amount+ amount*self.tax):
            print("Erro, você não possui saldo o suficiente")
        else:
            self.money -= amount + amount*self.tax
            print(f"Saldo atual: R$ {(self.money):.2f}")
    
class Poupanca(Account):

    def __init__(self, name:str, money:float, income:float):
        super().__init__(name, money, income)
        self.fees = 0.02

    def deposit(self, amount:float):
        self.money += amount
        print(f"Saldo atual: R$ {(self.money):.2f}")

    def withdraw(self, amount:float):
        self.money -= amount
        print(f"Saldo atual: R$ {(self.money):.2f}")

    def applyFees(self):
        self.money += self.fees * self.money