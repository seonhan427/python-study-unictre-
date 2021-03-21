#python print practice 문제 8

high, weight = map(int,input("민수의 키와 몸무게를 입력하시오 : ").split())
high1, weight1 = map(int,input("기영이의 키와 몸무게를 입력하시오 : ").split())

if high > high1 and weight > weight1:
    print("true")
else:
    print("false")
