#함수 속에 값이 하나인경우 call by value 값 변화 x

#함수 속에 값이 2개 이상인경우 call by reference 값을 변화 가능

#global -> 전역 변수를 함수 안에서 사용시
sum = lambda x,y : x+y;

print("정수의 합 : ",sum(10,20))

add = (lambda x,y : x+y) (10,20)

print(add)