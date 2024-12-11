from functions import *
import os,time

while True:
    print('Algoritmo VENDAS\n')
    print('1 - Adicionar vendas de produtos')
    print('2 - Criar relatório de vendas')
    print('3 - Encerrar algoritmo\n')

    option = readInput('Escolha uma opção',1,1,['1','2','3'])

    if option != '3':
            
            if option == '1':
                products_list = list()

                while True:
                    products_list.append(inputProductInfos())
                    os.system("cls")
                    if(readInput("\nDeseja continuar a adicionar produtos? (s/n)",1,1,['s','n']) == 'n'):
                        insertProductIntoDB(products_list)
                        break

            if option == '2':
                generateReport(readSales())
                os.system("cls")
                print("Um arquivo com o relatório das vendas foi gerado em 'workspace/report.txt'")
                time.sleep(3)

    else:
        break
    os.system("cls")
    if readInput('Deseja continuar o programa? (s/n)',1,1,['s','n']) == 'n':
        break
