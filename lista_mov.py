def lista_movimentos_possiveis (lista, i):

    if i == 0: 
        return []
    if i == 1: 
        if '♥' in lista [0] and '♥' in lista [1]:
            return [1]
        elif '♦' in lista [0] and '♦' in lista [1]:
            return [1]
        elif '♣' in lista [0] and '♣' in lista [1]:
            return [1]
        elif '♠' in lista [0] and '♠' in lista [1]:
            return [1]
        elif 'A' in lista [0] and 'A' in lista [1]:
            return [1]
        elif '2' in lista [0] and '2' in lista [1]:
            return [1]
        elif '3' in lista [0] and '3' in lista [1]:
            return [1]
        elif '4' in lista [0] and '4' in lista [1]:
            return [1]
        elif '5' in lista [0] and '5' in lista [1]:
            return [1]
        elif '6' in lista [0] and '6' in lista [1]:
            return [1]
        elif '7' in lista [0] and '7' in lista [1]:
            return [1]
        elif '8' in lista [0] and '8' in lista [1]:
            return [1]
        elif '9' in lista [0] and '9' in lista [1]:
            return [1]
        elif '10' in lista [0] and '10' in lista [1]:
            return [1]
        elif 'J' in lista [0] and 'J' in lista [1]:
            return [1]
        elif 'Q' in lista [0] and 'Q' in lista [1]:
            return [1]
        elif 'K' in lista [0] and 'K' in lista [1]:
            return [1]
        else: 
            return []
    if i == 2: 
        if '♥' in lista [1] and '♥' in lista [2]:
            return [2]
        elif '♦' in lista [1] and '♦' in lista [2]:
            return [2]
        elif '♣' in lista [1] and '♣' in lista [2]:
            return [2]
        elif '♠' in lista [1] and '♠' in lista [2]:
            return [2]
        elif 'A' in lista [1] and 'A' in lista [2]:
            return [2]
        elif '2' in lista [1] and '2' in lista [2]:
            return [2]
        elif '3' in lista [1] and '3' in lista [2]:
            return [2]
        elif '4' in lista [1] and '4' in lista [2]:
            return [2]
        elif '5' in lista [1] and '5' in lista [2]:
            return [2]
        elif '6' in lista [1] and '6' in lista [2]:
            return [2]
        elif '7' in lista [1] and '7' in lista [2]:
            return [2]
        elif '8' in lista [1] and '8' in lista [2]:
            return [2]
        elif '9' in lista [1] and '9' in lista [2]:
            return [2]
        elif '10' in lista [1] and '10' in lista [2]:
            return [2]
        elif 'J' in lista [1] and 'J' in lista [2]:
            return [2]
        elif 'Q' in lista [1] and 'Q' in lista [2]:
            return [2]
        elif 'K' in lista [1] and 'K' in lista [2]:
            return [2]
        else: 
            return []
    if i == 3: 
        #4 tem mesmo nipe que 1; 4 tem mesmo num que 3
        if '♥' in lista [0] and '♥' in lista [3] and 'A' in lista [2] and 'A' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and '2' in lista [2] and '2' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and '3' in lista [2] and '3' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and '4' in lista [2] and '4' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and '5' in lista [2] and '5' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and '6' in lista [2] and '6' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and '7' in lista [2] and '7' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and '8' in lista [2] and '8' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and '9' in lista [2] and '9' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and '10' in lista [2] and '10' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and 'J' in lista [2] and 'J' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and 'Q' in lista [2] and 'Q' in lista [3]:
            return [1][3]
        elif '♥' in lista [0] and '♥' in lista [3] and 'K' in lista [2] and 'K' in lista [3]:
            return [1][3]

        
        if '♦' in lista [0] and '♦' in lista [3] and 'A' in lista [2] and 'A' in lista [3]:
            return [1][3]
        elif '♦' in lista[0] and '♦' in lista [3] and '2' in lista [2] and '2' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and '3' in lista [2] and '3' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and '4' in lista [2] and '4' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and '5' in lista [2] and '5' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and '6' in lista [2] and '6' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and '7' in lista [2] and '7' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and '8' in lista [2] and '8' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and '9' in lista [2] and '9' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and '10' in lista [2] and '10' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and 'J' in lista [2] and 'J' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and 'Q' in lista [2] and 'Q' in lista [3]:
            return [1][3]
        elif '♦' in lista [0] and '♦' in lista [3] and 'K' in lista [2] and 'K' in lista [3]:
            return [1][3]

        if '♣' in lista [0] and '♣' in lista [3] and 'A' in lista [2] and 'A' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and '2' in lista [2] and '2' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and '3' in lista [2] and '3' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and '4' in lista [2] and '4' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and '5' in lista [2] and '5' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and '6' in lista [2] and '6' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and '7' in lista [2] and '7' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and '8' in lista [2] and '8' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and '9' in lista [2] and '9' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and '10' in lista [2] and '10' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and 'J' in lista [2] and 'J' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and 'Q' in lista [2] and 'Q' in lista [3]:
            return [1][3]
        elif '♣' in lista [0] and '♣' in lista [3] and 'K' in lista [2] and 'K' in lista [3]:
            return [1][3]
        
        if '♠' in lista [0] and '♠' in lista [3] and 'A' in lista [2] and 'A' in lista [3]:
            return [1][3]
        elif '♠' in lista[0] and '♠' in lista [3] and '2' in lista [2] and '2' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and '3' in lista [2] and '3' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and '4' in lista [2] and '4' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and '5' in lista [2] and '5' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and '6' in lista [2] and '6' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and '7' in lista [2] and '7' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and '8' in lista [2] and '8' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and '9' in lista [2] and '9' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and '10' in lista [2] and '10' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and 'J' in lista [2] and 'J' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and 'Q' in lista [2] and 'Q' in lista [3]:
            return [1][3]
        elif '♠' in lista [0] and '♠' in lista [3] and 'K' in lista [2] and 'K' in lista [3]:
            return [1][3]
        



        #4 tem mesmo nipe que 3; 4 tem mesmo num que 1
        if '♥' in lista [2] and '♥' in lista [3] and 'A' in lista [0] and 'A' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and '2' in lista [0] and '2' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and '3' in lista [0] and '3' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and '4' in lista [0] and '4' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and '5' in lista [0] and '5' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and '6' in lista [0] and '6' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and '7' in lista [0] and '7' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and '8' in lista [0] and '8' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and '9' in lista [0] and '9' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and '10' in lista [0] and '10' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and 'J' in lista [0] and 'J' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and 'Q' in lista [0] and 'Q' in lista [3]:
            return [1][3]
        elif '♥' in lista [2] and '♥' in lista [3] and 'K' in lista [0] and 'K' in lista [3]:
            return [1][3]

        
        if '♦' in lista [2] and '♦' in lista [3] and 'A' in lista [0] and 'A' in lista [3]:
            return [1][3]
        elif '♦' in lista[2] and '♦' in lista [3] and '2' in lista [0] and '2' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and '3' in lista [0] and '3' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and '4' in lista [0] and '4' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and '5' in lista [0] and '5' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and '6' in lista [0] and '6' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and '7' in lista [0] and '7' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and '8' in lista [0] and '8' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and '9' in lista [0] and '9' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and '10' in lista [0] and '10' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and 'J' in lista [0] and 'J' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and 'Q' in lista [0] and 'Q' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and 'K' in lista [0] and 'K' in lista [3]:
            return [1][3]

        if '♣' in lista [2] and '♣' in lista [3] and 'A' in lista [0] and 'A' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '2' in lista [0] and '2' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '3' in lista [0] and '3' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '4' in lista [0] and '4' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '5' in lista [0] and '5' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '6' in lista [0] and '6' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '7' in lista [0] and '7' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '8' in lista [0] and '8' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '9' in lista [0] and '9' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '10' in lista [0] and '10' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and 'J' in lista [0] and 'J' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and 'Q' in lista [0] and 'Q' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and 'K' in lista [0] and 'K' in lista [3]:
            return [1][3]
        
        if '♠' in lista [2] and '♠' in lista [3] and 'A' in lista [0] and 'A' in lista [3]:
            return [1][3]
        elif '♠' in lista[2] and '♠' in lista [3] and '2' in lista [0] and '2' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and '3' in lista [0] and '3' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and '4' in lista [0] and '4' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and '5' in lista [0] and '5' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and '6' in lista [0] and '6' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and '7' in lista [0] and '7' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and '8' in lista [0] and '8' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and '9' in lista [0] and '9' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and '10' in lista [0] and '10' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and 'J' in lista [0] and 'J' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and 'Q' in lista [0] and 'Q' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and 'K' in lista [0] and 'K' in lista [3]:
            return [1][3]

        #todos o mesmo num 
        if 'A' in lista [2] and 'A' in lista [3] and 'A' in lista [0] and 'A' in lista [3]:
            return [1][3]
        elif '2' in lista[2] and '2' in lista [3] and '2' in lista [0] and '2' in lista [3]:
            return [1][3]
        elif '3' in lista [2] and '3' in lista [3] and '3' in lista [0] and '3' in lista [3]:
            return [1][3]
        elif '4' in lista [2] and '4' in lista [3] and '4' in lista [0] and '4' in lista [3]:
            return [1][3]
        elif '5' in lista [2] and '5' in lista [3] and '5' in lista [0] and '5' in lista [3]:
            return [1][3]
        elif '6' in lista [2] and '6' in lista [3] and '6' in lista [0] and '6' in lista [3]:
            return [1][3]
        elif '7' in lista [2] and '7' in lista [3] and '7' in lista [0] and '7' in lista [3]:
            return [1][3]
        elif '8' in lista [2] and '8' in lista [3] and '8' in lista [0] and '8' in lista [3]:
            return [1][3]
        elif '9' in lista [2] and '9' in lista [3] and '9' in lista [0] and '9' in lista [3]:
            return [1][3]
        elif '10' in lista [2] and '10' in lista [3] and '10' in lista [0] and '10' in lista [3]:
            return [1][3]
        elif 'J' in lista [2] and 'J' in lista [3] and 'J' in lista [0] and 'J' in lista [3]:
            return [1][3]
        elif 'Q' in lista [2] and 'Q' in lista [3] and 'Q' in lista [0] and 'Q' in lista [3]:
            return [1][3]
        elif 'K' in lista [2] and 'K' in lista [3] and 'K' in lista [0] and 'K' in lista [3]:
            return [1][3]
        
        #todos tem o mesmo nipe
        if '♥' in lista [2] and '♥' in lista [3] and '♥' in lista [0] and '♥' in lista [3]:
            return [1][3]
        elif '♦' in lista [2] and '♦' in lista [3] and '♦' in lista [0] and '♦' in lista [3]:
            return [1][3]
        elif '♣' in lista [2] and '♣' in lista [3] and '♣' in lista [0] and '♣' in lista [3]:
            return [1][3]
        elif '♠' in lista [2] and '♠' in lista [3] and '♠' in lista [0] and '♠' in lista [3]:
            return [1][3]
        

        #1 e 4 mesmo num
        if 'A' in lista [0] and 'A' in lista [3]:
            return [1]
        elif '2' in lista [0] and '2' in lista [3]:
             return [1]
        elif '3' in lista [0] and '3' in lista [3]:
            return [1]
        elif '4' in lista [0] and '4' in lista [3]:
            return [1]
        elif '5' in lista [0] and '5' in lista [3]:
            return [1]
        elif '6' in lista [0] and '6' in lista [3]:
            return [1]
        elif '7' in lista [0] and '7' in lista [3]:
            return [1]
        elif '8' in lista [0] and '8' in lista [3]:
            return [1]
        elif '9' in lista [0] and '9' in lista [3]:
            return [1]
        elif '10' in lista [0] and '10' in lista [3]:
            return [1]
        elif 'J' in lista [0] and 'J' in lista [3]:
            return [1]
        elif 'Q' in lista [0] and 'Q' in lista [3]:
            return [1]
        elif 'K' in lista [0] and 'K' in lista [3]:
            return [1]

        #3 e 4 mesmo num
        if 'A' in lista [2] and 'A' in lista [3]:
            return [3]
        elif '2' in lista [2] and '2' in lista [3]:
             return [3]
        elif '3' in lista [2] and '3' in lista [3]:
            return [3]
        elif '4' in lista [2] and '4' in lista [3]:
            return [3]
        elif '5' in lista [2] and '5' in lista [3]:
            return [3]
        elif '6' in lista [2] and '6' in lista [3]:
            return [3]
        elif '7' in lista [2] and '7' in lista [3]:
            return [3]
        elif '8' in lista [2] and '8' in lista [3]:
            return [3]
        elif '9' in lista [2] and '9' in lista [3]:
            return [3]
        elif '10' in lista [2] and '10' in lista [3]:
            return [3]
        elif 'J' in lista [2] and 'J' in lista [3]:
            return [3]
        elif 'Q' in lista [2] and 'Q' in lista [3]:
            return [3]
        elif 'K' in lista [2] and 'K' in lista [3]:
            return [3]


        #1 e 4 mesmo nipe
        if '♥' in lista [0] and '♥' in lista [3]:
            return [1]
        elif '♦' in lista [0] and '♦' in lista [3]:
            return [1]
        elif '♣' in lista [0] and '♣' in lista [3]:
            return [1]
        elif '♠' in lista [0] and '♠' in lista [3]:
            return [1] 


        #3 e 4 mesmo nipe
        if '♥' in lista [2] and '♥' in lista [3]:
            return [3]
        elif '♦' in lista [2] and '♦' in lista [3]:
            return [3]
        elif '♣' in lista [2] and '♣' in lista [3]:
            return [3]
        elif '♠' in lista [2] and '♠' in lista [3]:
            return [3]
        else: 
            return []

lista = ['6♥', 'J♥', '9♣', '9♥']
i = 3
print(lista_movimentos_possiveis(lista, i))