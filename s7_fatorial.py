#Data: 24/03/2018
#Autor: Wellington Mascena
#Descrição: Para cada número digitado pelo usuário retornar o fatorial.
n = 1
while n >= 0:
    n = int(input("Digite um número inteiro: "))
    fatorial = 1
    while n > 1:
        fatorial = fatorial*n
        n = n - 1
    print("O valor do fatorial ", n,"é ",fatorial,"!")

