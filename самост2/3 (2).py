import math
i = int(float(input('введите первое ограничение'))*10)
e = int(float(input('введите второе ограничение'))*10)
h = int(float(input('введите шаг '))*10)
p=' '
print ('x:',10*p,'y:')
for i in range (i,e+1,h):
    
    x = i/10
    
    y = (8.364 - 2.326 * 2**x )/(math.sqrt(1.364 * x**2 + 1.247))
    print (x,10*p,y)
