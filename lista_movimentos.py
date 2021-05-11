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
