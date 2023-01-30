while True:
    print ('''
    Vamos Começar
    
    [0]pedra
    [1]papel
    [2]tesoura
    
    Jogador 1, Escolha uma jogada ...''')
    jogador1 = int(input())
    print ('''
    Jogador 2 - Escolha sua jogada: ''')
    jogador2 = int(input())
        #Considerando - Jogador1 vença
    if jogador1 == 0 and jogador2 == 2:
        print ('Jogador 1 venceu')
    elif jogador1 == 1 and jogador2 == 0:
        print ('Jogador 1 venceu')            
    elif jogador1 == 2 and jogador2 == 1:
        print ('Jogador 1 venceu')

            #Considerando - Jogador2 vença
    if jogador2 == 0 and jogador1 == 2:
        print ('Jogador 2 venceu')
    elif jogador2 == 1 and jogador1 == 0:
        print ('Jogador 2 venceu')            
    elif jogador2 == 2 and jogador1 == 1:
        print ('Jogador 2 venceu')

            #Considerando - Empate
    if jogador2 == jogador1:
        print ('Vocês empataram!')
    
    print ('Deseja continuar ou sair? (continuar/sair)')
    resposta = input ()
    if resposta.lower () == 'sair' or resposta.lower() == 's':
        print ('Até a próxima!')
        break