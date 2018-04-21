#coding:utf-8

while True:
	h1, m1, h2, m2 = map(int,  raw_input().split())
	if h1 == 0 and h2 == 0 and m1 == 0 and m2 == 0:
		break
	total1 = (h1*60 + m1)
	total2 = (h2*60 + m2)
	if total1 <= total2:
		minutos = abs(total1 - total2)
	else:		
		minutos = abs(total1 - (total2+24*60))  
	print minutos
