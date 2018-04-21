#coding:utf-8

while True:
    l_c = input().split()
    x1 = int(l_c[0])
    y1 = int(l_c[1])
    x2 = int(l_c[2])
    y2 = int(l_c[3])
    if x1+x2+y1+y2 == 0:
        break
    else:
        if (x1 == x2 and y1 == y2):
                print(0)
        elif ((x2-x1) == -(y2-y1) or -(x2-x1) == -(y2-y1)): 
                print(1)
        elif -(x2-x1) == (y2-y1) or (x2-x1) == (y2-y1):
                print(1)
        elif (x1 == x2 or y1 == y2):
                print(1)
        else:
                print(2)
