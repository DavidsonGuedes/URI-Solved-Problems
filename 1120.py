#coding:utf-8

while True:
	
	entrada = map(str, raw_input().split())
	if entrada == ["0","0"]:
		break
	num = entrada[1]
	dig = entrada[0]

	for i in range(len(dig)):
		num = num.replace(dig[i], "")

	if num == "":
		print "0"
	else:
		print int(num)

