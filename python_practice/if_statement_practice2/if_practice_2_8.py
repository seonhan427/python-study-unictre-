# 2.2 if_statement_practice 문제 8

big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"

letter = input("입력하시오: ")

bigletter = letter.upper()
smallletter = letter.lower()

if letter in big:
    print(smallletter)
elif letter in small:
    print(bigletter)
else:
    print(letter)