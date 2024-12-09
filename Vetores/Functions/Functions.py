def readInput(message: str = "", max_input_len: int = 99, min_input_len: int = 0, options: list = []) -> str:
    '''
    Receives inputs and sets conditions to grant stability in code
    '''
    while True:
        entry = input(f"{message}\n").lower()

        if len(entry) < min_input_len:
            print(f"ERRO: Entrada deve ter no mínimo {min_input_len} caracteres")

        elif len(entry) > max_input_len:
            print(f"ERRO: Entrada deve ter no máximo {max_input_len} caracteres")

        else:
            if(len(options)>0):

                if entry not in options:
                    print(f"ERRO: Entrada deve ser uma das opções listadas acima")
                else:
                    return entry
            else:
                return entry
            
def optionsInputs(options:list,message:str = ''):
    '''
    Similar to above function, but it lists the options of the user and uses numbers as main input type
    '''
    options_indexes = list()

    for index in enumerate(options):
        options_indexes.append(str(index[0]+1))

    print(message)
    for index,option in enumerate(options):
        print(f"{index+1} - {option}")

    return int(readInput('',1,1,options_indexes))-1

def inputOnlyNumber(message:str)->float:
    '''
    Forces the user's input to be an float
    '''
    print(message)
    while True:
        entry = input()
    
        try:
            entry = float(entry)
            return entry
        except ValueError:
            print("Você deve inserir um número, tente novamente:")