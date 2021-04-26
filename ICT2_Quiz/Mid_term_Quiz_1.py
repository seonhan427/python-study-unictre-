#문제 1 2진수 10진수 변환


x = input("2진수를 입력하시오: ") # 1010

y = x[::-1]
a = 0
awnser = 0

for z in y:
    awnser += int(z)*2**a
    a += 1

print(awnser) # 10




