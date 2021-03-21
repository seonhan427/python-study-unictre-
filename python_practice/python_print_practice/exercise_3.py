#python print practice 문제 3

number1, number2 = map(int,input("숫자를 입력하시오 : ").split(' '))
# number1 = 4 / number2 = 5

if number1 < number2:
    print(number1,">",number2,"---","0")
    print(number1,"<",number2,"---","1")
    print(number1,">=",number2,"---","0")
    print(number1,"<=",number2,"---","1")
else :
    print(number1,">",number2,"---","1")
    print(number1,"<",number2,"---","0")
    print(number1,">=",number2,"---","1")
    print(number1,"<=",number2,"---","0")    

    