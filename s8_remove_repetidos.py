#Data: 09/04/2019
#Autor: Wellington Mascena
#Descrição: Função remove_repetido recebe como parametro uma lista de inteiros e
#retorna uma lista ordenada sem elementos repetidos.

def remove_repetidos(lista):

    lista.sort()
    lista_sem_repetidos = []

    for num in lista:

        if not(num in lista_sem_repetidos):
            lista_sem_repetidos.append(num)
            
    return lista_sem_repetidos
