import math

x1= float (input ('Digite o valor de x:'))
y1= float(input ('Digite o valor de y:'))

x2= float (input ('Digite o valor de x1:'))
y2= float(input ('Digite o valor de y2:'))

distancia = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if distancia < 10:
    raiz1 =  math.sqrt((x1-x2)**2) + math.sqrt((y1-y2)**2)
    print ('perto')
else:
    print ('longe')
