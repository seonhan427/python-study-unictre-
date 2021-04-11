# practice loop 1 문제3

num = 0

while num != -1:
    num = int(input("입력하시오: "))

    if num % 3 == 0:
        print(num//3)
    else: 
        continue