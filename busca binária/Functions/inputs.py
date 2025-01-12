def enterNumber(sentence: str)->int:
    while True:
        inputed_sentence = input(sentence)
        try:            
            return int(inputed_sentence)
        except ValueError:
            print(f"ERROR: '{inputed_sentence}' não é um número válido")

def selectListItem(number_list:list)->int:
    while True:
        selected_item = enterNumber("Selecione um número da lista gerada: ")
        if selected_item in number_list:
            return selected_item
        print(f"Error: {selected_item} não está na lista")
    
