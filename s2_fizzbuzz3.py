#Data: 17/05/18
#Autor: Wellington Mascena
#Descrição: Recebe um inteiro na entrada e imprimi FizzBuzz se for divisível por três e cinco.
# Caso contrário, imprima o número que foi dado na entrada.

#Recebendo um número na entrada
numero = int(input('Digite um número:'))

#Verificando se o número é divisível por três e cinco
#Todo número divisível por três e cinco deixa resto zero na divisão por 3 e por 5
if(numero%3==0 and numero%5==0):
    print('FizzBuzz')
else:
    print(numero) 