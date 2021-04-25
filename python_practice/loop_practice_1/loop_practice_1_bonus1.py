# practice loop 1 보너스 문제1

number = int(input("숫자를 입력하시오: "))

a = 0
b = number 
for a in range(number+1):
    print(" "*b,"*"*a)
    b -= 1
    a += 1 