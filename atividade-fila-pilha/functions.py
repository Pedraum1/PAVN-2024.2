from os import system
from time import sleep
from Order import Order

def waitUserType() -> None:
    print("\n\nPressione qualquer tecla para continuar")
    while True:
        if  input() != None:
            return

def clearPrompt() -> None:
    system("cls")

def delay(time:float) -> None:
    sleep(time)

def isFloat(value:str) -> bool:
    try:
        float(value)
        return True
    except:
        return False

def menu() -> int:
    
    while True:
        print("MENU | ESCOLHA O NÚMERO CORRESPONDENTE À OPÇÃO")
        print("1 - Listar pedidos")
        print("2 - Adicionar pedidos")
        print("3 - Remover pedido")
        print("4 - Mostrar valor total")
        print("\n5 - *Sair do gerenciador*")

        choice = input().strip()

        if choice in ['1','2','3','4','5']:
            return int(choice)
        
        print("ENTRADA NÃO COMPUTADA, ESCOLHA UMA OPÇÃO VÁLIDA")
        delay(1)
        clearPrompt()

def showOrders(orders) -> None:

    if not len(orders) > 0:
        print("Não há pedidos ainda para serem apresentados")
        waitUserType()
        return
    
    print(orders)
    waitUserType()
    
def addOrder(orders_queue) -> None:
    name = input("Escreva o pedido a ser adicionado: ")
    while True:
        price = input("Insira o preço do pedido: ").replace(",",".")
        if isFloat(price):
            price = float(price)
            break
        print("Insira um valor válido")
        delay(1)
        clearPrompt()

    new_order = Order(name, price)
    
    orders_queue.push(new_order)
    print(f"Pedido: \"{new_order}\" adicionado com sucesso")
    waitUserType()

def removeOrder(orders_queue) -> float:
    if len(orders_queue) > 0:
        order = orders_queue.pop()
        print(f"Pedido: \"{order}\" removido com sucesso")
        waitUserType()

        return order.price
    
    print("Não há pedidos a serem removidos")
    waitUserType()

    return 0

def showRevenue(price:float) -> None:
    print(f"O valor total pago foi de: R$ {price:,.2f}")
    waitUserType()