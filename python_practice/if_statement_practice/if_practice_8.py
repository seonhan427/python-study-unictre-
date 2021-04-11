# if_statement_practice 문제 8

year = int(input("년도를 입력하시오: "))

if year % 400 == 0:
    print("leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("leap year")
else : 
    print("common year")