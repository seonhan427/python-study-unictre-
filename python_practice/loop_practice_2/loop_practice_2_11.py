# practice loop 2 문제11

x = input("입력하시오: ") 

y = x[::-1]
a = 0
awnser = 0

for z in y:
    awnser += int(z)*2**a
    a += 1

print(awnser)

