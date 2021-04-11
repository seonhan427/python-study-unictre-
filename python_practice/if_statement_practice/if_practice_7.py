# if_statement_practice 문제 7

num1, num2, num3 = map(int,input("입력하시오 : ").split())

if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num1 and num2 < num3:
    print(num2)
else : 
    print(num3)
