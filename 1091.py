while True:
	jogadores_quadrados = raw_input().split(" ")
	jogadores,quadrados = [0] * int(jogadores_quadrados[0]), int(jogadores_quadrados[1])
	if len(jogadores) == 0:
		break
	condicao = [0] * len(jogadores)
	contador = -1
	x = 0
	armadilhas = raw_input().split(" ")
	armadilhas = [int(armadilhas[0]), int(armadilhas[1]), int(armadilhas[2])]
	rodadas = int(raw_input())
	while x < rodadas:
		contador += 1
		if contador == len(jogadores):
			contador = 0		
		if condicao[contador] == 1:
			condicao[contador] = 0
		else:		
			dados = raw_input().split(" ")
			dados = int(dados[0]) + int(dados[1])
			jogadores[contador] += dados
			x += 1
			if jogadores[contador] in armadilhas:
				condicao[contador] = 1	
	for i in xrange(len(jogadores)):
		if jogadores[i] == max(jogadores):
			print i + 1
			break		
		
