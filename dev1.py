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


def lista_movimentos_possiveis(baralho, indice):
    mp = []
    naipe = extrai_naipe(baralho[indice])
    valor = extrai_valor(baralho[indice])

    if indice == 0:
        return mp

    naipe1 = extrai_naipe(baralho[indice - 1])
    valor1 = extrai_valor(baralho[indice - 1])
    if naipe1 == naipe:
        mp.append(1)
    elif valor1 == valor:
        mp.append(1)


    if indice - 3 >= 0:
        naipe3 = extrai_naipe(baralho[indice - 3])
        valor3 = extrai_valor(baralho[indice - 3])
        if naipe3 == naipe:
            mp.append(3)
        elif valor3 == valor:
            mp.append(3)

    return mp

def possui_movimentos_possiveis (baralho): 
    indice = 1
    mp = []
    naipe = extrai_naipe(baralho[indice])
    valor = extrai_valor(baralho[indice])
    while indice <len(baralho): 
        if indice == 0:
            indice += 1 
            return False
        naipe1 = extrai_naipe(baralho[indice - 1])
        valor1 = extrai_valor(baralho[indice - 1])
        if naipe1 == naipe:
            indice += 1 
            return True 
        indice += 1 
        if valor1 == valor:
            indice += 1 
            return True 
        indice += 1 
        if indice - 3 >= 0:
            naipe3 = extrai_naipe(baralho[indice - 3])
            valor3 = extrai_valor(baralho[indice - 3])
            if naipe3 == naipe:
                indice += 1 
                return True 
            elif valor3 == valor:
                indice += 1 
                return True 
        else:
            return False 
    return False 


import random 

def shuffle (bara): 
    shuffle = random.shuffle(bara)
    return shuffle 

def posicao_baralho(baralho):
    i = 0
    print("Status atual do baralho:")
    while i < len(baralho):
        naipe = extrai_naipe(baralho[i])
        print("{0} -{1}".format(i + 1,baralho[i]))
        i += 1
    return ''
    
print ('Paciência Acordeão')
print ('==================') 

print ('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.') 

print ('Existem apenas dois movimentos possíveis:') 

print ('1. Empilhar uma carta sobre a carta imediatamente anterior;') 
print ('2. Empilhar uma carta sobre a terceira carta anterior.') 

print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:') 

print('1. As duas cartas possuem o mesmo valor ou') 
print('2. As duas cartas possuem o mesmo naipe.') 

print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.')

a = input('Digite "ir" para iniciar o jogo: ')
bara = cria_baralho()

if a == 'ir':
    shuffle(bara)

print (posicao_baralho(bara))

while possui_movimentos_possiveis(bara) != False:
    print(bara)
    escolha = int(input('escolha uma carta de 1 - 52: '))
    if lista_movimentos_possiveis(bara, escolha) == []:
        print ('A carta {escolha} não pode ser movida. Por favor, digite um número entre 1 e 52): '.format)

