#Data: 16/06/2018
#Autor: Wellington Mascena
#Descrição: Programa completo - Jogo do NIM - Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro.
#Dois jogadores jogam alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

#Função computador_escolhe_jogada que recebe, como parâmetros,
#os números n e m descritos acima e devolve um inteiro
#correspondente à próxima jogada do computador de acordo com a
#estratégia vencedora.
def computador_escolhe_jogada(n, m):
    #Peças para retirar
    pc_jogada = m
    while pc_jogada>1:
        
        if(((n - pc_jogada)%(m+1))==0):
            return pc_jogada
        else:
            pc_jogada = pc_jogada -1
    return pc_jogada
            
    
#Função usuario_escolhe_jogada que recebe os mesmos parâmetros,
#solicita que o jogador informe sua jogada e verifica se o valor
#informado é válido. Se o valor informado for válido, a função
#deve devolvê-lo; caso contrário, deve solicitar novamente
#ao usuário que informe uma jogada válida.
            
def usuario_escolhe_jogada(n, m):
    #Jogada do jogador
    jogada = int(input('\nQuantas peças você vai tirar?'))
    
    while (int(jogada) > int(m) or jogada == 0):
        print('Oops! Jogada inválida! Tente de novo.')
        jogada = input('\nQuantas peças você vai tirar?')

    return jogada
            
#Uma função partida que não recebe nenhum parâmetro,
#solicita ao usuário que informe os valores de n e m
#e inicia o jogo, alternando entre jogadas do computador
# e do usuário (ou seja, chamadas às duas funções anteriores).
#A escolha da jogada inicial deve ser feita em função da
#estratégia vencedora, como dito anteriormente. A cada jogada,
#deve ser impresso na tela o estado atual do jogo, ou seja,
#quantas peças foram removidas na última jogada quantas
#restam na mesa. Quando a última peça é removida,
#essa função imprime na tela a mensagem "O computador ganhou!"
#ou "Você ganhou!" conforme o caso.
def partida():
    n = int(input('\nQuantas peças?'))
    m = int(input('Limite de peças por jogadas?'))

    #Define quem inicia a partida
    if (n%(m+1))==0:
        print('\nVocê começa!')
        vez_usuario = True
    else:
        print('\nComputador começa!')
        vez_usuario = False
        
    #Executa enquanto o jogo não termina
    while(n):
        if(vez_usuario):

            jogada_usuario = int(usuario_escolhe_jogada(n, m))
            print('\nVocê tirou ',jogada_usuario, 'peças.')
            n = n - jogada_usuario
            #Verificar se é fim de jogo
            if(n==0):
                print('Você ganhou!')
                break
            else:
                print('Agora resta apenas', n ,'peças no tabuleiro')
                #Passa a vez para o computador
                vez_usuario = False
        else:
            
            pc_jogada = int(computador_escolhe_jogada(n, m))
            print('\nO computador retiro', pc_jogada, 'peças!')
            n = n - pc_jogada

            #Verificar se o computador ganhou o jogo.
            if(n==0):
                print('Fim do jogo! O computador ganhou!')
                break
            else:
                print('Agora resta', n,'peças no tabuleiro.')
                #passa a vez para o usuário
                vez_usuario = True
    return vez_usuario
            
    
#função deve realizar três partidas seguidas do jogo e, ao final,
#mostrar o placar dessas três partidas e indicar o vencedor do campeonato.
def campeonato():
    print('\nVocê escolheu jogar campeonato!')
    contador = 0
    placar_usuario = 0
    placar_computador = 0
    
    while( contador < 3):
        contador = contador + 1
        print('\n**** Rodada ',contador, '****')
        if(partida()):
            placar_usuario = placar_usuario + 1
        else:
            placar_computador = placar_computador + 1
        
    print('\n**** Final do campeonato! ****')
    print('\nPlacar: Você ',placar_usuario,'x',placar_computador,' Computador')

    
#Iniciando o jogo.
print('Bem-vindo ao jogo do NIM! Escolha:\n')

#Menu de opções de partidas.
menu = int(input('1 - para jogar uma partida isolada \n2 - para jogar um campeonato '))

if menu == 1:
    print('\nVocê escolheu jogar partida isolada!')
    partida()
    
elif menu == 2:
    campeonato()
    
