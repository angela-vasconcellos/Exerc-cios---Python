#leia o tamanho da sequencia
n = int(input("Digite o tamanho da sequencia: "))

crescente = True
anterior = int(input("Digite um numero: "))

i = 1 # contador de numeros lidos
while i < n and crescente:
    atual = int(input("Digite um numero: "))
    if anterior >= atual:
        crescente = False
    anterior = atual
    i = i + 1

if crescente:
    print("Nao esta em ordem crescente.")
else:
    print("Esta em ordem crescente.")
