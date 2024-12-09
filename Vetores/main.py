from Classes.Vetor import Vector
from Functions.Functions import *

print("Algoritmo: Vetores")

while True:
  vector_infos = list()
  
  print("Insira as informações do vetor 1")
  for component in ['i','j','k']:
    vector_infos.append(float(inputOnlyNumber(f"Insira a componente {component}:")))

  vector_1 = Vector(vector_infos[0], vector_infos[1], vector_infos[2])

  vector_infos = list()
  
  print("Insira as informações do vetor 2")
  for component in ['i','j','k']:
    vector_infos.append(float(inputOnlyNumber(f"Insira a componente {component}:")))

  vector_2 = Vector(vector_infos[0], vector_infos[1], vector_infos[2])

  option = optionsInputs(['somar vetores','subtrair vetores','produto escalar dos vetores','multiplicar por constante','mostrar vetores','pular etapa'],"Escolha uma opção:")
  match option:
    case 0:
      print(f"Soma dos vetores; {vector_1+vector_2}")

    case 1:
      print(f"Subtração dos vetores; {vector_1-vector_2}")

    case 2:
      print(f"Produto escalar dos vetores: {vector_1*vector_2}")

    case 3:
      constant = inputOnlyNumber("Insira o valor da constante:")
      vector = optionsInputs([f'Vetor 1: {vector_1}',f'Vetor 2: {vector_2}'], "Escolha o vetor a ser multiplicado")
      
      match vector:
        case 0:
          print(f"Multiplicação do vetor por constante; {vector_1*constant}")
        case 1:
          print(f"Multiplicação do vetor por constante; {vector_2*constant}")

    case 4:
      pass

  if optionsInputs(['sim','não'],"Deseja continuar o algoritmo?") == 1:
    break