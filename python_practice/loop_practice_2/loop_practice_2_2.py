# practice loop 2 문제2

number = int(input("입력하시오: "))
numbers = []
space = number-1
for x in range(1,number+1):
    numbers.append(x)
    print(" "*space,numbers,sep='')
    space -= 1
#해결 ㄴㄴㄴ
num =1

for raw in range(3):
    for col in range(3):
        if col >= 3-1:
            print(num)
            num += 1
    #num+=1 다음문제