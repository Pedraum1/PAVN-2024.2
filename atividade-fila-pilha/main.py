from functions import *
from my_data_struct import Queue

orders = Queue()
total_revenue = 0

clearPrompt()
print("RESTAURANT MANAGER")
waitUserType()

while True:
    clearPrompt()
    option = menu()

    if option == 1:
        showOrders(orders)


    elif option == 2:
        addOrder(orders)

    elif option == 3:
        total_revenue += removeOrder(orders)
    elif option == 4:
        showRevenue(total_revenue)
    else:
        break
    
    delay(0.25)

delay(0.5)
clearPrompt()
