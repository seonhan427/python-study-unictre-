# 2.2 if_statement_practice 문제 2

age = int(input("나이를 입력하시오: "))

if age < 8:
    print("450원입니다.")
elif age > 8 and age <= 19:
    print("720원입니다.")
elif age >= 20:
    print("1250원입니다.")