frase = str(input('Digite uma palavra ou frase: ')).strip().upper() #strip - tira os espaços e upper - deixas as letras maiusculas
palavras = frase.split() #split separa a frase em palavras, tipo lista.
junto = ''.join(palavras) #join - retira os espaços entre as palavras
inverso = '' #é possível substituir as linhas 4, 5, 6 - por inverso = [::-1] - : começo e fim, -1. Isso se chama fatiamento
for letra in range (len(junto) -1, -1, -1): #len - comprimento
    inverso += junto[letra]
print ('O inferso de {} é {}'.format (junto, inverso))
if inverso == junto:
    print ('Temos um palíndromo!')
else:
    print ('A frase não é um palíndromo!')

