#Data: 04/04/2019
#Autor: Wellington Mascena
#Descrição: recebe como parâmetro um número inteiro positivo n n e devolva a
#soma de todos os inteiros entre 1 e n n que são comprimento da hipotenusa de
#algum triângulo retângulo com catetos inteiros.função n_primos que recebe como
#argumento um número inteiro maior ou igual a 2

#Função para verificar se o número pode ser medidad de hipotenusa
def é_hipotenusa(num):

    cateto1 = 1
    ehHipotenusa = False

    while cateto1 <= num:
        
        cateto2 = 1    
        while cateto2 <= num:
            quadradoCatetos = (cateto1**2) + (cateto2**2)
            #Testa se o quadrado do catetos é igual a soma quadrada da possível hipotenusa.
            if (num**2) == quadradoCatetos:
                ehHipotenusa = True
                break
            cateto2 = cateto2 + 1

        cateto1 = cateto1 + 1
        
    return ehHipotenusa

#Função que conta quantos primos existem até n.
def soma_hipotenusas(n):

    auxNumeros = 1
    somaHipotenusas = 0

    #Verificar quais números até n são primos    
    while auxNumeros <= n:
        
        if é_hipotenusa(auxNumeros) == True:
            somaHipotenusas = somaHipotenusas + auxNumeros

        auxNumeros = auxNumeros + 1
        
    return somaHipotenusas
