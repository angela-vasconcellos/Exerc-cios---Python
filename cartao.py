meuCartao= int(input("Digite o número do seu cartão de crédito: "))

cartaoLido=1
encontreiMeuCartao=False

while cartaoLido != 0 and not encontreiMeuCartao:
    cartaoLido=int(input("Digite o próximo número de cartão: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartao = True

if encontreiMeuCartao:
    print ("Eba, Cartão encontrado!")
else:
    print ("Que pena, Cartão não encontrado!")