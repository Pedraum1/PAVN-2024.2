from Classes.Square    import *
from Classes.Rectangle import *
from Classes.Circle    import *
from Functions.Inputs  import *
import os

#NOTA: o item 3 da primeira questão deveria conter 'abstração' ao invés de 'composição' para estar correto


while True:
    os.system('cls')
    print('\nFORMAS GEOMÉTRICAS')
    print('\nATENÇÃO: o programa está trabalhando com centímetros até 2 casas após a vírgula')

    while True:
        geometry = input('escolha a forma geométrica desejada: \n-Quadrado (1)\n-Retângulo (2)\n-Círculo (3)\n')
        
        if geometryWasPassed(geometry):
            os.system('cls')
            break
        else:
            os.system('cls')
            print('Erro: escolha uma opção válida\n')
    
    x_position = getPositionInAxis('X')
    os.system('cls')
    y_position = getPositionInAxis('Y')
    os.system('cls')

    if geometry == '1':
        side = getNumber('Insira o tamanho do lado do quadrado desejado: ','Erro: insira um número válido')
        geometry = Square(x_position, y_position, side)
        os.system('cls')

    if geometry == '2':
        width = getNumber('Insira a largura do retângulo desejado: ','Erro: insira um número válido')
        height = getNumber('Insira a altura do retângulo desejado: ','Erro: insira um número válido')
        geometry = Rectangle(x_position, y_position, width, height)
        os.system('cls')

    if geometry == '3':
        diameter = getNumber('Insira o diâmetro do círculo desejado: ','Erro: insira um número válido')
        geometry = Circle(x_position, y_position, diameter)
        os.system('cls')

    print(geometry)

    if input("Deseja encerrar o programa? (S/N)").lower() == 's':
        os.system('cls')
        break