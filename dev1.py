def cria_baralho():
    listacartas = ['K♠', 'Q♠', 'J♠', '10♠', '9♠', '8♠', '7♠', '6♠', '5♠', '4♠', '3♠', '2♠', 'A♠', 'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥','7♥','6♥','5♥','4♥', '3♥', '2♥', 'A♥', 'K♦', 'Q♦', 'J♦', '10♦', '9♦', '8♦', '7♦', '6♦', '5♦', '4♦', '3♦', '2♦', 'A♦', 'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣', 'A♣']
    return listacartas

def extrai_naipe (naipe):
    if '♦' in naipe:
        return '♦'
    if '♥' in naipe:
        return '♥'
    if '♣' in naipe:
        return '♣'
    if '♠' in naipe:
        return '♠'

def extrai_valor (valor):
    if 'A' in valor:
        return 'A'
    if '10' in valor:
        return '10'
    if '1' in valor:
        return '1'
    if '2' in valor:
        return '2'
    if '3' in valor:
        return '3'
    if '4' in valor:
        return '4'
    if '5' in valor:
        return '5'
    if '6' in valor:
        return '6'
    if '7' in valor:
        return '7'
    if '8' in valor:
        return '8'
    if '9' in valor:
        return '9'
    if 'J' in valor:
        return 'J'
    if 'Q' in valor:
        return 'Q'
    if 'K' in valor:
        return 'K'

def empilha (lista, o, d):
    lista[d] = lista[o]
    del lista[o]
    return lista

def lista_movimentos_possiveis (baralho, indice):
    mp =[]
    if indice == 0:
        return mp 
    elif indice == 1:
        if extrai_valor(baralho[0]) == extrai_valor(baralho[1]) or extrai_naipe(baralho[0]) == extrai_naipe(baralho[1]):
            mp = [1]
            return mp
        else:
            return mp
    elif indice == 2:
        if extrai_valor(baralho[0]) == extrai_valor(baralho[2]) or extrai_naipe(baralho[0]) == extrai_naipe(baralho[2]):
            a = True
        else:
            a = False 
        if extrai_valor(baralho[1]) == extrai_valor(baralho[2]) or extrai_naipe(baralho[1]) == extrai_naipe(baralho[2]):                      
            b = True
        else:
            b = False
        if a == True and b == True:
            mp = [1,2]
            return mp
        elif a == True and b == False:
            mp = [1]
            return mp
        elif b == True and a == False:
            mp = [2]
            return mp
    
    elif indice == 3:
        if extrai_valor(baralho[0]) == extrai_valor(baralho[3]) or extrai_naipe(baralho[0]) == extrai_naipe(baralho[3]):
            a = True
        else:
            a = False
        if extrai_valor(baralho[1]) == extrai_valor(baralho[3]) or extrai_naipe(baralho[1]) == extrai_naipe(baralho[3]):
            b = True
        else:
            b = False 
        if extrai_valor(baralho[2]) == extrai_valor(baralho[3]) or extrai_naipe(baralho[2]) == extrai_naipe(baralho[3]):
            c = True
        else:
            c = False
        if a == True and b == True and c == True:
            mp = [1, 2, 3]
            return mp
        elif a == True and b == True and c == False:
            mp = [1, 2]
            return mp
        elif a == True and c == True and b == False:
            mp = [1, 3]
            return mp
        elif b == True and c == True and a == False:
            mp = [2, 3]
            return mp
        elif a == True and b == False and c == False:
            mp = [1]
            return mp
        elif b == True and a == False and c == False:
            mp = [2]
            return mp
        elif c == True and a == False and b == False:
            mp = [3]
            return mp