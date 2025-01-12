from random import randint

def generateList(length: int)->list:
    number_list = list()
    for numbers in range(length):
        new_number = randint(0,100)
        number_list.append(new_number)
    return sorted(number_list)
    