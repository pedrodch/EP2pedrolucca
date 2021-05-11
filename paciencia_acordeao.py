# Jogo Paciência Acordeão

# Função que cria o baralho
def cria_baralho():
    import random
    e1 = 'A♠'
    c1 = 'A♥'
    o1 = 'A♦'
    p1 = 'A♣'
    e2 = '2♠'
    c2 = '2♥'
    o2 = '2♦'
    p2 = '2♣'
    e3 = '3♠'
    c3 = '3♥'
    o3 = '3♦'
    p3 = '3♣'
    e4 = '4♠'
    c4 = '4♥'
    o4 = '4♦'
    p4 = '4♣'
    e5 = '5♠'
    c5 = '5♥'
    o5 = '5♦'
    p5 = '5♣'
    e6 = '6♠'
    c6 = '6♥'
    o6 = '6♦'
    p6 = '6♣'
    e7 = '7♠'
    c7 = '7♥'
    o7 = '7♦'
    p7 = '7♣'
    e8 = '8♠'
    c8 = '8♥'
    o8 = '8♦'
    p8 = '8♣'
    e9 = '9♠'
    c9 = '9♥'
    o9 = '9♦'
    p9 = '9♣'
    e10 = '10♠'
    c10 = '10♥'
    o10 = '10♦'
    p10 = '10♣'
    e11 = 'J♠'
    c11 = 'J♥'
    o11 = 'J♦'
    p11 = 'J♣'
    e12 = 'Q♠'
    c12 = 'Q♥'
    o12 = 'Q♦'
    p12 = 'Q♣'
    e13 = 'K♠'
    c13 = 'K♥'
    o13 = 'K♦'
    p13 = 'K♣'
    baralho= [e1, c1, o1, p1, e2, c2, o2, p2, e3, c3, o3, p3, e4, c4, o4, p4, e5, c5, o5, p5, e6, c6, o6, p6, e7, c7, o7, p7, e8, c8, o8, p8, e9, c9, o9, p9, e10, c10, o10, p10, e11, c11, o11, p11, e12, c12, o12, p12, e13, c13, o13, p13]
    random.shuffle(baralho)
    return baralho

# Função que extrai o naipe da carta
def extrai_naipe(carta):
    return carta[-1]

# Função que extrai o valor da carta
def extrai_valor(carta):
    if len(carta) == 3:
        return '10'
    else:
        return carta[0]

# Função que mostra os movimentos possíveis
def lista_movimentos_possiveis(baralho, posicao):
    naipe = extrai_naipe(baralho[posicao])
    numero = extrai_valor(baralho[posicao])
    naipe_1 = extrai_naipe(baralho[posicao-1])
    numero_1 = extrai_valor(baralho[posicao-1])
    possibilidades = []
    if posicao == 0:
        return possibilidades
    elif posicao <= 2:
        if numero_1 == numero:
            possibilidades.append(1)
        if naipe_1 == naipe:
            possibilidades.append(1)
    else:
        naipe_3 = extrai_naipe(baralho[posicao-3])
        numero_3 = extrai_valor(baralho[posicao-3])
        if numero_1 == numero:
            possibilidades.append(1)
        if numero_3 == numero:
            possibilidades.append(3)
        if naipe_1 == naipe:
            possibilidades.append(1)
        if naipe_3 == naipe:
            possibilidades.append(3)
    return possibilidades

# Função que empilha baralhos
def empilha(baralho, origem, destino):
    baralho[destino] = baralho[origem]
    baralho.pop(origem)
    return baralho

# Função que mostra se tem movimentos possíveis
def possui_movimentos_possiveis(baralho):
    posicoes = 0
    for i in baralho:
        if lista_movimentos_possiveis(baralho, posicoes) != []:
            return True
        else:
            posicoes += 1
    return False

# Introdução ao jogo

print('Paciência Acordeão')
print('==================')

print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.')
print('Existem apenas dois movimentos possíveis: ')

print('1. Empilhar uma carta sobre a carta imediatamente anterior; ')
print('2. Empilhar uma carta sobre a terceira carta anterior.')

print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ')

print('1. As duas cartas possuem o mesmo valor ou ')
print('2. As duas cartas possuem o mesmo naipe. ')

print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. ')

input('Aperte [Enter] para iniciar o jogo... ')

print('Situação atual:')

i = 1
cartas = cria_baralho()
for carta in cartas:
    print('{}. {}'.format(i, carta))
    i += 1


posicao = input('Digite a posição da carta que deseja escolher: ')

x = lista_movimentos_possiveis(baralho, posicao)

i = True

while i:
    if x == []:
        posicao = ('Essa carta não pode ser movida. Escolha outra posição: ')
    elif x == [1]:
        print('O estado atual do baralho é: ', empilha(baralho, posicao, posicao-1))
    elif x == [3]:
        print('O estado atual do baralho é: ', empilha(baralho, posicao, posicao -3))
    else:
        print('Você tem duas opções: ')
        print('1.', baralho[posicao-1])
        print('2.', baralho[posicao-3])
        y = input('Sobre qual carta você deseja empilhar?: ')
        if y == 1:
            print('O estado atual do baralho é: ', empilha(baralho, posicao, posicao-1))
        elif y == 2:
            print(print('O estado atual do baralho é: ', empilha(baralho, posicao, posicao -3))
