#Data: 17/05/18
#Autor: Wellington Mascena
#Descrição: Recebe um inteiro na entrada e imprimi Fizz se for divisível por três.
# Caso contrário, imprima o número que foi dado na entrada.
#Recebendo um número na entrada
numero = int(input('Digite um número:'))

#Verificando se o número é divisível por três
#Todo número divisível por três deixa resto zero na divisão por 3
if(numero%3==0):
    print('Fizz')
else:
    print(numero) 