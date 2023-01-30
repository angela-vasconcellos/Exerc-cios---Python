n1 = int(input('Digite o termo inicial da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = n1 + (10 - 1) * r #fórmula matemática de PA
for PA in range (n1,decimo + r, r): #inicio - n1, temrino decimo + r, intervalo: razão
    print ('{} '.format(PA), end = ' -> ')
print ('ACABOU')
