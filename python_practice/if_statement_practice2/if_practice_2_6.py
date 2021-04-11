# 2.2 if_statement_practice 문제 6

letter = input("알파벳을 입력하시오: ")

capletter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallletter = "abcdefghijklmnopqrstuvwxyz"

if letter in capletter :
    print("대문자입니다.")
elif letter in smallletter : 
    print("소문자입니다.")
else:
    print("error")    

