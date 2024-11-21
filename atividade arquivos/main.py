from functions import functions as f

print('***ALGORITMO VENDEDORES***')
print('Bem-vindo, qual ação deseja realizar?')
options = ['adicionar vendedor','gerar lista de vendedores']

entry = f.optionsInputs(options)
if entry == 0:

    loop = True
    loop_options = [True,False]
    while loop:
        f.addEmployeeData(f.readEmployeeInfos())
        loop = loop_options[f.optionsInputs(loop_options,'Deseja continuar?')]
    
if entry == 1:
    print(f"Uma lista de vendedores foi gerada em {f.WORKSPACE_PATH}bestSellers.txt\n")
    sellers = f.readSellerFile()
    sellers = sorted(sellers,key=lambda x: x["sales"], reverse=True)

    lines = list()
    for index, seller in enumerate(sellers):
        lines.append(f"{seller['first_name'].capitalize():<17}{seller['last_name'].capitalize():^17}{seller['sales']:^12.2f}\n")
        print(f"{index} - {f"{seller['first_name'].capitalize()} {seller['last_name'].capitalize()}":<32} - R$ {seller['sales']:>12.2f}")
    f.generateList(lines)