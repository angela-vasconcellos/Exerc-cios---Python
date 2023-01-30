                
while True:

    print (''''
    [0]pedra
    [1]papel
    [2]tesoura
    Escolha uma jogada ...''')
    jogador1 = int(input())
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
    if jogador2 == 0 and jogador1 == 0:
        print ('Vocês empataram')
    elif jogador2 == 1 and jogador1 == 1:
         print ('Vocês empataram')            
    elif jogador2 == 2 and jogador1 == 2:
        print ('Vocês empataram')
       
        break
    
    resposta = ''
    while not (resposta.lower () == 'sair' or resposta.lower() == 's'):
            jogador1 = int(input())
            jogador2 = int(input())
            print ('Deseja continuar ou sair? (continuar/sair)')
            resposta = input ()
            if resposta.lower () == 'continuar' or resposta.lower() == 'c':
                continue
            elif resposta.lower () == 'sair' or resposta.lower() == 's':
                print ('Até a próxima')

           
