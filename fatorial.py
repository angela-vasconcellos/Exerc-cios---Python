#quando um número for informado, mostrar se possuem 2 números adjacentes iguais
n= int(input("Digite um número inteiro: "))
n=1
while n > 0:
    fatorial = 1
    while n>1:
        fatorial= fatorial *n
        n=n-1
    print (fatorial)
    n= int(input("Digite um número inteiro: "))