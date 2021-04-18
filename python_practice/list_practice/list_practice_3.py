#list practice 문제3
number = []

while True :
    number.append(int(input("문자를 입력하시오: ")))
    if 0 in number:
        number.pop() # 마지막 값을 지우기 위해 사용
        break
print(number)