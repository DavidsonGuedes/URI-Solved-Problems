#coding:utf-8

cont = 0
c1 = c2 = c3 = c4 = 0
while True:
        valor = int(input())
        if valor != 0:
                if valor >= 50:
                        c1 = valor//50
                        valor -= 50*c1
                if valor >= 10:
                        c2 = valor//10
                        valor -= 10*c2
                if valor >= 5:
                        c3 = valor//5
                        valor -= 5*c3
                if valor >= 1:
                        c4 = valor//1
                        valor -= 1*c4
                cont += 1
                print("Teste {}\n{} {} {} {}\n".format(cont, c1, c2, c3, c4))
                c1 = c2 = c3 = c4 = 0
        else:
                break
