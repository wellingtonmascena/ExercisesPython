#Data: 30/03/2019
#Autor: Wellington Mascena
#Descrição: Ler largura e altura com input para formar um retângulo de #

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

#auxiliar para armazenar o valor da largura
aux = 0

while altura > 0:
    altura = altura - 1
    aux = largura
    while aux > 0:
        print("#",end='')
        aux = aux - 1

    print('')
