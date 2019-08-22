#Data: 09/05/2018
#Autor: Wellington Mascena
#Descrição: Programa que pede como entrada o tamanho do lado do quadrado e retorna como saída o perímetro e a área do quadrado.

#Entrada do lado do quadrado
ladoQuadrado = int(input ('Digite o valor correspondente ao lado de um quadrado:'))

#Calcula o perímetro e armazena na variável perímetroQuadrado
perimetroQuadrado = 4*ladoQuadrado

#Calcula a área do quadrado e armazena na variável areaQuadrado
areaQuadrado = ladoQuadrado**2

#Imprimir a saída de acordo com o padrão pedido
print('perímetro:',perimetroQuadrado,'- área:',areaQuadrado)
