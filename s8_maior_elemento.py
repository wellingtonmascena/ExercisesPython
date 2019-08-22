#Data: 09/04/2019
#Autor: Wellington Mascena
#Descrição: Função que retorna o maior elemento de uma lista de inteiros

def maior_elemento(lista):
    
    lista.sort()

    return lista[-1]
