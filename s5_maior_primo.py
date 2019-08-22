#Data: 04/06/2018
#Autor: Wellington Mascena
#Descrição Semana05 - ex02: Função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro
#e devolve o maior número primo menor ou igual ao número passado à função

def ehPrimo(n):
    
    #Variável auxiliar para verificar se n é primo
    aux = n - 1

    #Variável boleana se é primo ou não
    ehPrimo = True

    #Testar a divisão de todos os números por n, exceto 1 e ele mesmo.
    while(aux > 1):

        if((n%aux)==0):
            ehPrimo = False
            
        #Decrementa em uma unidade para executar a divisão
        aux = aux - 1
        

    #Retorna se é primo ou não
    return ehPrimo

#Verificar quem é o maior primo menor ou igual a n
def maior_primo(p):

    maior = 1

    aux = 1

    while(aux <= p):
        if(ehPrimo(aux)):
            maior = aux
        aux = aux + 1

    return maior
