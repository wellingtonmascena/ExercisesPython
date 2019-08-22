#Data: 31/03/2019
#Autor: Wellington Mascena
#Descrição: função n_primos que recebe como argumento um número inteiro maior ou igual a 2
#como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

def ehprimo(num):
    auxPrimo = 2
    ehprimo = True
    while auxPrimo <= (num//2):
        
        if(num%auxPrimo) == 0:
            ehprimo = False
            break
        auxPrimo = auxPrimo + 1
   
    return ehprimo        

#Função que conta quantos primos existem até n.
def n_primos(n):

    auxNumeros = 2
    totalPrimos = 0

    #Verificar quais números até n são primos    
    while auxNumeros <= n:
        
        if ehprimo(auxNumeros)==True:
            totalPrimos = totalPrimos + 1

        auxNumeros = auxNumeros + 1
        
    return totalPrimos
