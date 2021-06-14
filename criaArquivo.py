def cria_arquivo(arquivo, vetor):
    dicionario = open(arquivo, 'w')
    i = 0
    while vetor[i] != '':
        dicionario.write(vetor[i])
        dicionario.write('\n')
        i += 1
    dicionario.close()
    return dicionario
