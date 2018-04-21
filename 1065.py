#coding:utf-8

cont = 0
lista = []
while True:
        n = input()
        lista.append(n)
        if len(lista) == 5:
                break
for i in range(len(lista)):
        if int(lista[i]) % 2 == 0:
                cont+=1
print("{} valores pares".format(cont))
        
