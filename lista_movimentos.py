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

def extrai_naipe(carta):
    return carta[-1]

def extrai_valor(carta):
    if len(carta) == 3:
        return '10'
    else:
        return carta[0]

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
