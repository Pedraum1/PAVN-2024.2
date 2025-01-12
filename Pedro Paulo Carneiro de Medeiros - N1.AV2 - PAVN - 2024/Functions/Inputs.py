def geometryWasPassed(geometry: str)->bool:
    if geometry == '1' or geometry == '2' or geometry == '3':
        return True
    return False

def getPositionInAxis(axis:str)->float:
    while True:
        position = input(f'Insira a posição da forma no eixo {axis}: ').replace(',','.')

        if isFloat(position):
            return float(position)
        print(f'Insira um NÚMERO para assumir a posição da forma geométrica no eixo {axis}: ')

def getNumber(text:str, error_text:str)->float:
    while True:
        number = input(text).replace(',','.')

        if isFloat(number):
            return float(number)
        print(error_text)

def isFloat(number:str)->bool:
    try:
        float(number)
        return True
    except ValueError:
        return False
    
if __name__ == "__main__":
    print(isFloat('1'))
        