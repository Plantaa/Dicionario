def insercao(origem, destino):
    indice_destino = 1
    destino[0] = origem[0]
    for i in range(len(origem)):
        if origem[i] > destino[indice_destino-1]:
            destino[indice_destino] = origem[i]
            indice_destino += 1
        elif origem[i] == destino[indice_destino-1]:
            i += 1
        elif origem[i] < destino[indice_destino-1] and busca_binaria(destino, origem[i], 0, indice_destino-1) == 0:
            passos = indice_destino
            while origem[i] < destino[passos-1]:
                destino[passos] = destino[passos-1]
                passos -= 1
            destino[passos] = origem[i]
            indice_destino += 1
    return destino
