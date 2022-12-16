def bob(x):
     with open('newvegas.txt',mode='r') as myfile  :
        file_contents  = myfile.read().splitlines()
     print(file_contents.pop(x))
bob(x=int(input('Введите номер строки из текста>>>')))
