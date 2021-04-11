# if_statement_practice 문제 3

age = int(input("나이를 입력하시오: "))

if age >= 20:
    print("adult")
else:
    #변수를 따로 담아놓았습니다
    A = 20 - age
    print(A,"years later")