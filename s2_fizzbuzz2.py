#Data: 17/05/18
#Autor: Wellington Mascena
#Descrição: Recebe um inteiro na entrada e imprimi Buzz se for divisível por cinco.
# Caso contrário, imprima o número que foi dado na entrada.
#Recebendo um número na entrada
numero = int(input('Digite um número:'))

#Verificando se o número é divisível por cinco
#Todo número divisível por cinco deixa resto zero na divisão por 5
if(numero%5==0):
    print('Buzz')
else:
    print(numero) 