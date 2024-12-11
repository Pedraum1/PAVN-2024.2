import os
WORKSPACE_PATH = f"{os.path.dirname(__file__)}/workspace/"

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

def generateDB():
    '''
    Generates the sellers database. Unique use
    '''

    with open(f"{WORKSPACE_PATH}sales.txt",'w',encoding="UTF-8") as db:
        db.write(f'{"product":<21}{"category":^21}{"stock":^9}{"price":^9}{"sales":^9}\n')

def inputProductInfos()->dict:
    '''
    Reads inputs and process the informations to return the sales from the seller and his name along the year
    '''

    product = dict()
    product["product_name"] = readInput("NOME DO PRODUTO",21,1).replace(' ','_')
    product["category"]     = readInput("CATEGORIA",21,1).replace(' ','_')
    product["stock"]        = readInput("QUANTIDADE EM ESTOQUE",9,1).replace(',','.')
    product["price"]        = readInput("PREÇO",9,1).replace(',','.')
    product["sales"]        = readInput("VENDAS (em unidades vendidas)",9,1)


    return product

def insertProductIntoDB(products:list):
    '''
        Self-explanatory, insert the products from the parameter into the database
    '''
    with open(f"{WORKSPACE_PATH}sales.txt",'a',encoding="UTF-8") as db:
        for product in products:
            line = f"{product['product_name']:<21}{product['category']:^21}{product['stock']:^9}{product['price']:^9}{product['sales']:^9}\n"
            db.write(line)

def readSales()->list:
    '''
        Read the sales database and returns an list of the products with the total profit
    '''
    with open(f"{WORKSPACE_PATH}sales.txt",'r',encoding="UTF-8") as db:
        data = db.readlines()
        products_list = list()
        total_profit = 0

        for index,line in enumerate(data):
            if index > 0:
                product = dict()
                product_name,category,stock,price,sales = line.split()
                profit = float(price)*float(sales)

                product['product_name'] = product_name.capitalize().replace('_',' ')
                product['sales'] = sales
                product['profit'] = profit

                products_list.append(product)
                total_profit += profit

        products_list.append(total_profit)

    return products_list


def generateReport(products:list):
    '''
        creates the report of the products informations
    '''
    lines = list()

    for index,product in enumerate(products):

        if index < (len(products)-1):
            lines.append(f"{product['product_name']:<21}{product['sales']:^9}{product['profit']:^9}\n")

        else:
            lines.append(f'\nTotal de vendas: R$ {product}')

    with open(f"{WORKSPACE_PATH}report.txt",'w',encoding="UTF-8") as db:
        db.write(f'{"product":<21}{"sales":^9}{"profit":^9}\n')
        db.writelines(lines)

if __name__ == "__main__":
    #Run this file to generate the database
    generateDB()