# practice loop 2 문제2

number = int(input("입력하시오: "))
numbers = []
space = number-1
for x in range(1,number+1):
    numbers.append(x)
    print(" "*space,numbers,sep='')
    space -= 1
#해결 ㄴㄴㄴ