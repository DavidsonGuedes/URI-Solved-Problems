#coding:utf-8

cont = 0
aux = 0
soma = 0
while True:
        nota = float(input())
        if 10 >= nota >= 0:
                soma += nota
                cont += 1
                if cont == 2:
                        break
        else:
                aux += 1
                
for i in range(aux):
        print("nota invalida")
        
print("media = {:.2f}".format(soma/2))
