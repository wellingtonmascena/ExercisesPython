#Data: 30/03/2019
#Autor: Wellington Mascena
#Descrição: Ler largura e altura com input para formar um retângulo vazio e bordas de #

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

#auxiliar para armazenar o valor da largura
auxColuna = 0
auxLinha = altura

while auxLinha > 0:
    
    auxColuna = largura
    while auxColuna > 0:
        
        if altura == auxLinha or auxLinha == 1:
            print("#",end='')
        else:
            if auxColuna == 1 or auxColuna == largura:
                print("#",end='')
            else:
                print(" ",end='')
                
        auxColuna = auxColuna - 1

    print('')
    auxLinha = auxLinha - 1
