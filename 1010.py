# -*- coding: utf-8 -*-

linha1 = raw_input().split(" ")
linha2 = raw_input().split(" ")

cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print("VALOR A PAGAR: R$ %0.2f" %total)
