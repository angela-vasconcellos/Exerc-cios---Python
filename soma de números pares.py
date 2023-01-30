s = 0
for soma in range (0,6):
    num = int(input('Digite um número inteiro:'))
    if num //2 and num %2 ==0:
        s += num
print ('O somatório de todos os valores foi {}'. format (s))