def extrai_valor(carta):
    if len(carta) == 3:
        return '10'
    else:
        return carta[0]