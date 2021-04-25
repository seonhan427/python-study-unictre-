# practice loop 1 문제9

number1, number2 = map(int,input("입력하시오 :").split())
range(10,1,-1)
if number1 > number2:
    for x in range(1,10):
        for y in range(number1,number2-1,-1):
            print(y,"*",x,"=",y*x,end='   ')
elif number1 < number2:
    for x in range(1,10):
        for y in range(number1,number2+1):
            print(y,"*",x,"=",y*x,end='   ')
elif number1 == number2:
    for x in range(1,10):
        print(number1,"*",x,"=",number1*x,end='   ')
        
    