# practice loop 2 문제1

number = int(input("입력하시오: "))

y = 1
x = 0
for y in range(1,11):
    x = number*y
    y +=1
    print(x,end=' ')
    if x >100:
        break

# 값이 100을 넘었을때 넘은 수까지는 출력됨
#왜?????