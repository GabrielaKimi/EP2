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

def lista_movimentos_possiveis(baralho, indice):
    mp = []
    naipe = extrai_naipe(baralho[indice])
    valor = extrai_valor(baralho[indice])

    print(naipe)
    print(valor)

    if indice == 0:
        return mp

    naipe1 = extrai_naipe(baralho[indice - 1])
    valor1 = extrai_valor(baralho[indice - 1])
    if naipe1 == naipe:
        mp.append(1)
        print('entrouaq')
    elif valor1 == valor:
        mp.append(1)

    print(naipe1)
    print(valor1)
    print(mp)
    

    if indice - 3 >= 0:
        naipe3 = extrai_naipe(baralho[indice - 3])
        valor3 = extrai_valor(baralho[indice - 3])
        if naipe3 == naipe:
            mp.append(3)
        elif valor3 == valor:
            mp.append(3)

    return mp


print (lista_movimentos_possiveis(['6♥', 'J♥', '9♣', '9♥'],1))
