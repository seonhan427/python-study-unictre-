#python print practice 문제 6

num1, num2 = map(int,input("정수 2개를 입력하시오 : ").split())

quotient = num1 // num2
remainder = num1 % num2

print(num1,"/",num2,"=",quotient,"...",remainder)