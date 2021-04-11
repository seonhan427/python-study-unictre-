# if_statement_practice 문제 2

heigt, weigt = map(int,input("키와 몸무게를 입력하시오: ").split())

# 미리 계산 변수를 만들어놓았습니다

obe = (weigt+100)- heigt

if obe > 0 :
    print(obe)
    print("Obesity")
else :
    print("you are not Obesity")
