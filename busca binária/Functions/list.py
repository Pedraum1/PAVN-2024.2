def binarySearch(number: int, original_list:list)->int:

    list_of_numbers = original_list
    position = 0

    while True:
        if(len(list_of_numbers) > 1):
            (right_side, left_side) = getHalfsList(list_of_numbers)
            midpoint = getHalfIndex(list_of_numbers)
            if max(right_side) >= number:
                list_of_numbers = right_side
            else:
                list_of_numbers = left_side                
                position += midpoint
                
        else:
            return position

def getHalfIndex(list_numbers: list)->int:
    return round(len(list_numbers)/2)

def getHalfsList(list_numbers: list)->list:
    half = getHalfIndex(list_numbers)
    return [list_numbers[:half],list_numbers[half:]]

if __name__ == "__main__":
    lista = [1,2,3,4,5,123,124,567]
    numero = 567
    posicao = binarySearch(numero,lista)
    print(f"Número {numero} encontrado na posição {posicao} da lista")