import random

comnumber = random.randint(1,100)

count = 0

while True:
    usernumber = int(input("숫자입력>"))
    count += 1
    if usernumber == comnumber:
        print("정답입니다!!, ",count,"번 만에 맞추셨습니다.",sep='')
        break
    elif comnumber > usernumber:
        print("틀렸습니다, 제가 고른 숫자는 더 큰수 입니다.")
        continue
    elif comnumber < usernumber:
        print("틀렸습니다, 제가 고른 숫자는 더 작은 수 입니다.")
        continue
    