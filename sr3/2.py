def func (x):
    a = 0
    b = 0
    c = 0
    my = []
    p=len(x.split())
    for i in range (len (x)):
        if x [i].isalpha():
            a = 1 + a
        elif x[i].isdigit():
            b = 1 + b
        elif x[i] in string.punctuation:
            c = 1 + c
    my.append(len(x))
    my.append(p)
    my.append(a)
    my.append(b)
    my.append(c)
    print(my)
func(input ())
