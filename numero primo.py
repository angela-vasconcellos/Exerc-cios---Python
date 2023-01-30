n = int (input('Digite um número: '))
total = 0
for num in range (1,n+1):
    if n%num==0:
        print ('\033[31m', end =' ')
        total +=1
    else:
        print ('\033[33m', end =' ')
    print ('{}'.format(num), end = ' ')

print('\033[35m', end=' ')
print ('-> O número {} foi dívisivel {} vezes'.format(num, total))

if total == 2:
    print('\033[35m', end=' ')
    print ('É número primo.')
else:
    print('\033[35m', end=' ')
    print ('Não é número primo.')
