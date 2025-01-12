from Functions.random_generation import generateList
from Functions.inputs import enterNumber,selectListItem
from Functions.list import binarySearch

size = enterNumber("Digite um tamanho válido para a lista desejada: ")

numbers_list = generateList(size)
print(f"Lista gerada:\n{numbers_list}\n")
number = selectListItem(numbers_list)

position = binarySearch(number,numbers_list)
print(f"Número {number} encontrado na posição {position} da lista")