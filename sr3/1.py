import math
a = float(input('граница1:'))
b = float(input('граница 2:'))
h = float(input('шаг'))
lil = []
while round (a) <= b :
    lil.append(((8.364 - 2.326 * 2**a) / (1.364 * a**2 + 1.247)**0.5))
    a = a + 1
print(lil)
