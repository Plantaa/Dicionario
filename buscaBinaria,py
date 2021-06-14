def busca_binaria(vetor, elemento, inicio, fim):
    if inicio > fim:
        return 0
    m = (inicio + fim)//2
    if elemento == vetor[m]:
        return -1
    elif elemento < vetor[m]:
        return busca_binaria(vetor, elemento, inicio, m-1)
    elif elemento > vetor[m]:
        return busca_binaria(vetor, elemento, m+1, fim)
