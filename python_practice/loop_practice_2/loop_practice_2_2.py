# practice loop 2 문제2

number = int(input("입력하시오 : "))

for x in range(number):
    for y in range(number-x-1): 
        print(' ',end=' ')
    for y in range(x+1):
        print(y+1,end=' ')
    print()