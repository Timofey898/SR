import math
si =0
n  = int(input('введите начало'))
n1 = int(input('введите конец'))
for n in range (n,n1+1):
    si = si + math.sin(1/n)
s = (2/5 + si ) / 6 
print (s)
    

