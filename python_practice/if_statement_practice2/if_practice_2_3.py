# 2.2 if_statement_practice 문제 3

sec = int(input("초를 입력하시오: "))

minute = sec//60
second = sec%60

print(minute,"분",second,"초", sep='')