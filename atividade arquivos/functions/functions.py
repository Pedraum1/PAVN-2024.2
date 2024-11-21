import os
WORKSPACE_PATH = f"{os.path.dirname(__file__)}/../workspace/"

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

def generateDB():
    '''
    Generates the sellers database. Unique use
    '''
    months = f"{"JAN":^9}{"FEV":^9}{"MAR":^9}{"ABR":^9}{"MAI":^9}{"JUN":^9}{"JUL":^9}{"AGO":^9}{"SET":^9}{"OUT":^9}\n"

    with open(f"{WORKSPACE_PATH}seller.txt",'w',encoding="UTF-8") as db:
        db.write(f"{"first_name":<17}{"last_name":^17}{months}")

def readEmployeeInfos()->dict:
    '''
    Reads inputs and process the informations to return the sales from the seller and his name along the year
    '''
    months = ['JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT']

    employee = {}
    employee["first_name"] = readInput("NOME",15,2)
    employee["last_name"]  = readInput("SOBRENOME",15,2)
    employee["sales"]      = list()

    for month in months:
        sales = readInput(f"Vendas em {month}",9).replace(',','.')

        if sales == '':
            sales = 0

        employee["sales"].append(sales)

    return employee

def addEmployeeData(data:dict):
    '''
    Self explanatory, adds a new employee/seller to database
    '''
    sales = ""
    for sale in data['sales']:
        sales = f"{sales}{sale:^9}"
    with open(f"{WORKSPACE_PATH}seller.txt",'a',encoding='UTF-8') as file:
        file.write(f"{data['first_name']:<17}{data['last_name']:^17}{sales}\n")

def readSellerFile()->list:
    '''
    Reads sellers database and process the informations to return the total of sales per employee along the year
    '''
    with open(f"{WORKSPACE_PATH}seller.txt",'r',encoding='utf-8') as file:
        data = file.readlines()
        infos_list = list()

        for index,infos in enumerate(data):

            if index > 0:
                info = dict()
                columns = infos.split()

                info['first_name'] = columns[0]
                info['last_name']  = columns[1]
                info['sales'] = 0
                for index,column in enumerate(columns):
                    if index > 1:
                        info['sales'] += float(column)

                
                infos_list.append(info)
    
    return infos_list

def generateList(data:list):
    '''
    Generates the ordered list of employees/sellers, ranked by total of sales
    '''
    with open(f"{WORKSPACE_PATH}bestSellers.txt",'w',encoding='utf-8') as file:
        file.write(f"{'first_name':<17}{'last_name':^17}{'Sales':^12}\n")
        file.writelines(data)