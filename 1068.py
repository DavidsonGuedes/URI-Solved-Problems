#coding:utf-8

while True:
        try:
                linha = input()

                lista = []
                p1 = 0
                p2 = 0
                for i in linha:
                        if i == "(":
                                p1 += 1
                                lista.append(i)
                        if i == ")":
                                p2 += 1
                                lista.append(i)

                if len(lista)%2 != 0:
                        print("incorrect")
                else:
                        if lista[0] == ")" or lista[len(lista)-1] == "(":
                                print("incorrect")
                        else:
                                if p1 != p2:
                                        print("incorrect")
                                else:
                                        print("correct")
        except EOFError:
                break
