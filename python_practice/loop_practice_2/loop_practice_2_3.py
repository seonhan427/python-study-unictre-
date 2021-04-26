# practice loop 2 문제3

number = int(input("입력하시오 :"))
z = 0
for x in range(number):
    for y in range(x):
        print(' ', end='')
    for y in range(number-x):
        z +=1
        print(z,end='')
    print()

