#coding:utf-8

cont = 0
while True:
        N = int(input())
        if N != 0:
                seq = input().split()
                for i in range(len(seq)):
                        if int(seq[i]) == int(i+1):
                                cont += 1
                                print("Teste {}\n{}\n".format(cont, seq[i]))
        else:
                break
        
                
