# python basic practice 문제 7

letter1, letter2, number = input("문자 2개와 숫자를 입력하시오 : ").split()

number1 = int(number)

A = letter1[0:number1]
B = letter2[0:number1]
C = letter2.replace(B, A)

print(letter1+letter2)
print(C)