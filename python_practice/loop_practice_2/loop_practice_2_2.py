# practice loop 2 문제2

number = int(input("입력하시오 : "))
rangenum = number+1

for x in range(1,rangenum):
    for y in range(1,rangenum):
        if y > rangenum - (x+1):
            print(y-(rangenum-(x+1)),end='')
        else:
            print(' ',end='')
    print()