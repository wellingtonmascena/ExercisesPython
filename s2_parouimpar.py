#Data: 17/05/18
#Autor: Wellington Mascena
#Descrição: Retorna se o número digitado é par ou ímpar.

#Entrada do número a ser testado
numero = int(input ('Digite um número:'))

# Testar se o número é par:
# Todo número par tem resto zero na divisão por dois
if (numero%2 == 0):
    print('par')
else:
    print('impar')