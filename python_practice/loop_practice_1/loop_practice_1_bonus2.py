# practice loop 1 보너스 문제2

number = int(input("숫자를 입력하시오: "))


for a in range(number):
    print(" "*a,"*"*number)
    number -= 1
    a += 1 

