#python print practice 문제 5

num1, num2, num3 = map(int,input("정수 3개를 입력하시오 : ").split())

if num1 > num2 and num1 > num3:
    print("true")
else:
    print("false")
if num1 == num2 == num3:
    print("true")
else:
    print("false")