#curso udemy
#Data: 17/04/2019
#Autor: Wellington Mascena
#Descrição: Resolve equação do segundo grau

print("Vamos montar a equação do segundo grau ax^2+bx+c=0:")

a = float(input("Digite o valor do coeficiente a: "))
b = float(input("Digite o valor do coeficiente b: "))
c = float(input("Digite o valor do coeficiente c: "))

if a == 0:
      print("Erro:O coeficente de ax^2 deve ser diferente de zero!")
else:
    raiz1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    print(raiz1)
        
    raiz2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    print(raiz2)
        
