#Data: 10/05/2018
#Autor: Wellington Mascena
#Semana 2: Exercício opcional 
#Descrição: Escreva o programa para imprimir a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos.
#A saída deve estar no formato: a dias, b horas, c minutos e d segundos.
#Seja cuidadoso com o formato!
#Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

#Recebendo a entrada de segundos para converter
segundosTotal = int(input('Por favor, entre com o número de segundos que deseja converter:'))

dias = segundosTotal//86400
horas = (segundosTotal%86400)//3600
minutos =(segundosTotal%3600)//60
segundos =(segundosTotal%360)

print(dias,'dias,', horas,'horas', minutos,'minutos e', segundos,'segundos')
