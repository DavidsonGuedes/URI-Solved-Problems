#coding:utf-8

while True:
  try:
        while True:
                grau = input()
                if int(grau) % 6 == 0:
                        print("Y")
                else:
                        print("N")
  except EOFError:
    break


