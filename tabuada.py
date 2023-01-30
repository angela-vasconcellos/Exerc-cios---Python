num = int(input('Digite um número para tabuada: '))
for n in range (1,11): #no caso, n tem que ser diferente do input, pois n é relativo ao range
    print ('-'*12)
    print ('{} x {} = {}'.format(num, n, num*n))
