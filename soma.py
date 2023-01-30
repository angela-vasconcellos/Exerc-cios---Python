soma=int(input("Digite o total de números a serem informados: "))
total=0
valor=1
while soma !=0:
    valor=int(input("Digite um número a ser somado: "))
    soma=soma - 1
    total=total + valor

print ("A soma dos valores digitados é: ", total)