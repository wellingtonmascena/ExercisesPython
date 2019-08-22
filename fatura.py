#Data: 10/05/2018
#Autor: Wellington Mascena
#Semana 2: Exercício1 opcional 
#Descrição: Programa que recebe o nome do cliente, o dia de vencimento, o mês de vencimento e o valor
#   da fatura e imprima a mensagem com os dados recebidos. O programa imprime a saída em duas linhas diferentes.
#    Note também que, como não é preciso realizar cálculos, o valor não precisa ser convertido para número, pode ser tratado como texto.

#Criando as variáveis e recebendo os dados de entrada
nomeCliente = input('Digite o nome do Cliente: ')
diaVencimento = input('Digite o dia de vencimento: ')
mesVencimento = input('Digite o mês de vencimento: ')
valorFatura = input('Digite o valor da fatura: ')

#Tratando a saída dos dados
print('Olá,',nomeCliente,'\n','A sua fatura com vencimento em',diaVencimento,'de',mesVencimento,'no valor de R$',valorFatura,'está fechada.')
