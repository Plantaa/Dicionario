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
