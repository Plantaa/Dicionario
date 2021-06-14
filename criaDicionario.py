def main():
    cria_arquivo("Saida.txt", insercao(separa_palavras("Entrada.txt"), cria_vetor()))
    
def cria_vetor():
    v = ['']*1000
    return v

def separa_palavras(arquivo):
    texto = open(arquivo, 'r').read()
    palavra = ''
    palavras = ''
    for i in range(len(texto)):
        if texto[i].isalpha() == True:
            palavra += texto[i].lower()
        elif texto[i].isalpha() == False and palavra != '':
            palavras += palavra + ' '
            i += 1
            palavra = ''
    return palavras.split()
            
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

def cria_arquivo(arquivo, vetor):
    dicionario = open(arquivo, 'w')
    i = 0
    while vetor[i] != '':
        dicionario.write(vetor[i])
        dicionario.write('\n')
        i += 1
    dicionario.close()
    return dicionario

main()
