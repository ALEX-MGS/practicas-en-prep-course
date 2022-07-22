def extrae_primos_de_lista(lista):
    lista_primos = []
    for elemento in lista:
        if verifica_primo(int(elemento)):
            lista_primos.append(elemento)
    return lista_primos

def verifica_primo(nro):
    es_primo = True
    for i in range(2, nro):
        if nro % i == 0:
            es_primo = False
            break
    return es_primo
    
def extrae_primos_de_lista(lista):
    lista_primos = []
    for elemento in lista:
        if (int(es_primo)):
            es_primo = True
            for i in range(2, nro):
                if nro % i == 0:
                    es_primo = False
                    break
        lista_primos.append(elemento)
    return lista_primos

def listconcat(lst):
    for elem in lst:
        if type(elem) in (tuple, list):
            for i in listconcat (elem):
                yield i
        else:
            yield elem

    