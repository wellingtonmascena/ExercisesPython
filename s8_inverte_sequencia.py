#Data: 09/04/2019
#Autor: Wellington Mascena
#Descrição: Imprime os números digitados pelo usuário na sequência contrária

num = int(input("Digite um número: "))
lista = []

#Lendo os números até digitar 0
while num != 0:
    lista.append(num)
    num = int(input("Digite um número: "))

#imprimindo na ordem inversa
for i in range(len(lista)):
    print(lista[len(lista)- i - 1])
