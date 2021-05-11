def empilha(baralho, origem, destino):
    baralho[destino] = baralho[origem]
    baralho.pop(origem)
    return baralho