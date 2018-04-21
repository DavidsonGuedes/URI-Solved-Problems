#coding:utf-8

while True:
    h, c = map(int, raw_input().split())
    if h == 0 and c == 0:
        break
    else:
        cortes = map(int, raw_input().split())
        laser = h - cortes[0]
        for i in range(1, len(cortes)):
            if cortes[i-1] > cortes[i]:
                laser += cortes[i-1] - cortes[i]
	print laser
